import { useLayoutEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import { Navbar } from "./components/Navbar";
import { Login } from "./pages/Login";
import { PublicLists } from "./pages/PublicLists";
import { AuthContext } from "./stores/AuthStore";

function App() {
  const [token, setToken] = useState("");

  const addToken = (token: string) => {
    setToken(token);
  };

  useLayoutEffect(() => {
    const storedToken = localStorage.getItem("token");

    if (storedToken) {
      setToken(storedToken);
    }
  }, [setToken]);

  return (
    <>
      <Navbar />
      <main className="container">
        <AuthContext.Provider value={{ token, addToken }}>
          <Routes>
            <Route path="login" element={<Login />} />
            <Route index element={<PublicLists />} />
          </Routes>
        </AuthContext.Provider>
      </main>
    </>
  );
}

export default App;
