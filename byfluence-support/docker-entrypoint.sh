#!/bin/sh
set -e
# First start: create the database (admin account + documentation, no demo data)
if [ ! -f "$DATA_DIR/byfluence-support.db" ] || [ "$(node --no-warnings=ExperimentalWarning -e "import('./server/db.js').then(m=>console.log(m.get('SELECT COUNT(*) n FROM users').n))")" = "0" ]; then
  node --no-warnings=ExperimentalWarning server/seed/seed.js ${SEED_ARGS:---no-demo}
fi
exec node --no-warnings=ExperimentalWarning server/index.js
