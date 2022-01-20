export interface AuthState {
  token: string;
  addToken?: (token: string) => void;
}
