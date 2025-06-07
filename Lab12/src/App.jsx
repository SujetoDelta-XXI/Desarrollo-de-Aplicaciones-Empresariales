import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import HomePage from "./pages/HomePage";

import CategoryPage from "./pages/CategoryPage";
import CategoryFormPage from "./pages/category/CategoryFormPage";
import CategoryEditFormPage from "./pages/category/CategoryEditFormPage";

import SeriePage from "./pages/SeriePage";
import SerieFormPage from "./pages/SerieFormPage";

import PrivateRoute from "./components/PrivateRoute";

function App() {
  const [categories, setCategories] = useState([]);
  const [series, setSeries] = useState([]);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={<LoginPage setIsAuthenticated={setIsAuthenticated} />}
        />

        <Route
          path="/home"
          element={
            <PrivateRoute isAuthenticated={isAuthenticated}>
              <HomePage />
            </PrivateRoute>
          }
        />

        <Route
          path="/categories"
          element={
            <PrivateRoute isAuthenticated={isAuthenticated}>
              <CategoryPage categories={categories} setCategories={setCategories} />
            </PrivateRoute>
          }
        />
        <Route
          path="/categories/new"
          element={
            <PrivateRoute isAuthenticated={isAuthenticated}>
              <CategoryFormPage />
            </PrivateRoute>
          }
        />
        <Route
          path="/categories/edit/:id"
          element={
            <PrivateRoute isAuthenticated={isAuthenticated}>
              <CategoryEditFormPage />
            </PrivateRoute>
          }
        />

        <Route
          path="/series"
          element={
            <PrivateRoute isAuthenticated={isAuthenticated}>
              <SeriePage series={series} setSeries={setSeries} />
            </PrivateRoute>
          }
        />
        <Route
          path="/series/edit/:idserie"
          element={
            <PrivateRoute isAuthenticated={isAuthenticated}>
              <SerieFormPage
                series={series}
                setSeries={setSeries}
                categories={categories}
              />
            </PrivateRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
