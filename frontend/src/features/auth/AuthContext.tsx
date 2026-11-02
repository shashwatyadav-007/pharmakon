import React, { createContext, useContext, useState } from "react";
import type { UserSummary } from "../../types/api";
import { api } from "../../lib/api/client";

interface AuthContextType {
  user: UserSummary | null;
  token: string | null;
  isAuthenticated: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  isLoading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [token, setToken] = useState<string | null>(() => localStorage.getItem("pharmakon_token"));
  const [user, setUser] = useState<UserSummary | null>(() => {
    const savedToken = localStorage.getItem("pharmakon_token");
    const savedUser = localStorage.getItem("pharmakon_user");
    if (savedToken && savedUser) {
      try {
        return JSON.parse(savedUser);
      } catch {
        localStorage.removeItem("pharmakon_token");
        localStorage.removeItem("pharmakon_user");
        return null;
      }
    }
    return null;
  });
  const [isLoading] = useState(false);

  const login = async (username: string, password: string) => {
    const data = await api.auth.login(username, password);
    setToken(data.access_token);
    setUser(data.user);
    localStorage.setItem("pharmakon_token", data.access_token);
    localStorage.setItem("pharmakon_user", JSON.stringify(data.user));
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem("pharmakon_token");
    localStorage.removeItem("pharmakon_user");
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        isAuthenticated: !!token,
        login,
        logout,
        isLoading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export function useAuth(): AuthContextType {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
