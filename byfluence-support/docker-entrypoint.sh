#!/bin/sh
set -e
DATA_DIR="${DATA_DIR:-/app/data}"
mkdir -p "$DATA_DIR"

# Hosting platforms often mount volumes owned by root. Fix ownership, then drop to the unprivileged "node" user.
if [ "$(id -u)" = "0" ]; then
  chown -R node:node "$DATA_DIR"
  exec setpriv --reuid=node --regid=node --init-groups "$0" "$@"
fi

# First start: create the database (admin account + documentation; no demo data unless SEED_ARGS=--with-demo)
USERS=$(node --no-warnings=ExperimentalWarning -e "import('./server/db.js').then(m=>console.log(m.get('SELECT COUNT(*) n FROM users').n))")
if [ "$USERS" = "0" ]; then
  echo "First start: initializing database in $DATA_DIR"
  node --no-warnings=ExperimentalWarning server/seed/seed.js ${SEED_ARGS:---no-demo}
fi
exec node --no-warnings=ExperimentalWarning server/index.js
