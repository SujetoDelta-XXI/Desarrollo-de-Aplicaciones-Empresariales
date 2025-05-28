import { Navigate } from "react-router-dom";

function PrivateRoute({ isAuthenticated, children }) {
  return isAuthenticated ? children : <Navigate to="/" />;
}

export default PrivateRoute;
