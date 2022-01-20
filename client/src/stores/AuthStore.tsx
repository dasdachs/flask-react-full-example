import { createContext } from "react";
import { AuthState } from "../interfaces/Auth";

export const initAuthState: AuthState = {
  token: "",
};

export const AuthContext = createContext<AuthState>(initAuthState);
