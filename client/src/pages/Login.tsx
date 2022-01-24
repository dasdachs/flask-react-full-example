import { useContext, useState } from "react";
import { Token } from "../interfaces/Api";
import { AuthContext } from "../stores/AuthStore";

export function Login() {
  const { token, addToken } = useContext(AuthContext);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleClick = async () => {
    fetch("/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    })
      .then((data) => data.json())
      .then((auth) => {
        const { access_token } = auth as Token;

        if (access_token) {
          sessionStorage.setItem("token", access_token);
          addToken!(access_token);
        }
      })
      .catch((e) => {
        setError(e);
      });
  };

  console.log(token);

  return (
    <form>
      <div className="mb-3">
        {error && <div>{error}</div>}
        <label htmlFor="email" className="form-label">
          Email address
        </label>
        <input
          type="email"
          className="form-control"
          id="email"
          aria-describedby="emailHelp"
          value={username}
          onChange={(e) => setUsername(e.currentTarget.value)}
        />
        <div id="emailHelp" className="form-text">
          We'll never share your email with anyone else.
        </div>
      </div>
      <div className="mb-3">
        <label htmlFor="password" className="form-label">
          Password
        </label>
        <input
          type="password"
          className="form-control"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.currentTarget.value)}
        />
      </div>

      <button type="button" className="btn btn-primary" onClick={handleClick}>
        Submit
      </button>
    </form>
  );
}
