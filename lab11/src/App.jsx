import { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import HomePage from "./pages/HomPage";
import CategoryPage from "./pages/CategoryPage";
import CategoryFormPage from "./pages/CategoryFormPage";
import SeriePage from "./pages/SeriePage";
import SerieFormPage from "./pages/SerieFormPage";
import PrivateRoute from "./components/PrivateRoute";


function App() {

  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // 1. Leer series desde localStorage o usar valores iniciales
  const storedSeries = JSON.parse(localStorage.getItem("series")) || [
    { cod: 1, nom: "Friends", cat: "Comedy", img: "friends.png" },
    { cod: 2, nom: "Law & Order", cat: "Drama", img: "law-and-order.png" },
    {
      cod: 3,
      nom: "The Big Bang Theory",
      cat: "Comedy",
      img: "the-big-bang.png",
    },
    {
      cod: 4,
      nom: "Stranger Things",
      cat: "Horror",
      img: "stranger-things.png",
    },
    { cod: 5, nom: "Dr. House", cat: "Drama", img: "dr-house.png" },
    { cod: 6, nom: "The X-Files", cat: "Drama", img: "the-x-files.png" },
  ];

  const [series, setSeries] = useState(storedSeries);

  // 2. Guardar series en localStorage cada vez que cambien
  useEffect(() => {
    localStorage.setItem("series", JSON.stringify(series));
  }, [series]);

  // 3. Leer categorías desde localStorage o usar valores iniciales
  const storedCategories = JSON.parse(localStorage.getItem("categories")) || [
    { cod: 1, nom: "Horror" },
    { cod: 2, nom: "Comedy" },
    { cod: 3, nom: "Action" },
    { cod: 4, nom: "Drama" },
  ];

  const [categories, setCategories] = useState(storedCategories);

  // 4. Guardar categorías en localStorage cada vez que cambien
  useEffect(() => {
    localStorage.setItem("categories", JSON.stringify(categories));
  }, [categories]);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage setIsAuthenticated={setIsAuthenticated} />} />

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
              <CategoryPage
                categories={categories}
                setCategories={setCategories}
              />
            </PrivateRoute>
          }
        />
        <Route
          path="/categories/edit/:idcategory"
          element={
            <PrivateRoute isAuthenticated={isAuthenticated}>
              <CategoryFormPage
                categories={categories}
                setCategories={setCategories}
              />
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
    </Router>
  );
}

export default App;
