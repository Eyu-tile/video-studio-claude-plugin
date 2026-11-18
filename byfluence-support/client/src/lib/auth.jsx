import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react';
import { api, setAuthHandlers } from './api.js';

const AuthCtx = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(undefined); // undefined = loading, null = signed out
  const [settings, setSettings] = useState(null);

  const loadSettings = useCallback(async () => {
    try { setSettings(await api('/settings')); } catch { /* ignore */ }
  }, []);

  const refresh = useCallback(async () => {
    try {
      const { user: u } = await api('/auth/me');
      setUser(u);
      loadSettings();
    } catch { setUser(null); }
  }, [loadSettings]);

  useEffect(() => {
    setAuthHandlers(() => setUser(null), () => setUser((u) => (u ? { ...u, must_change_password: true } : u)));
    refresh();
  }, [refresh]);

  const login = async (email, password) => {
    const { user: u } = await api('/auth/login', { method: 'POST', body: { email, password } });
    setUser(u);
    loadSettings();
    return u;
  };
  const logout = async () => {
    try { await api('/auth/logout', { method: 'POST' }); } catch { /* ignore */ }
    setUser(null);
  };

  const value = useMemo(() => ({
    user, setUser, settings, loadSettings, refresh, login, logout,
    can: (perm) => !!user?.permissions?.includes(perm),
  }), [user, settings, refresh, loadSettings]);
  return <AuthCtx.Provider value={value}>{children}</AuthCtx.Provider>;
}

export const useAuth = () => useContext(AuthCtx);
