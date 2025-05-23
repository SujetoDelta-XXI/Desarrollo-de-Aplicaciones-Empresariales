import { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomPage';
import CategoryPage from './pages/CategoryPage';
import CategoryFormPage from './pages/CategoryFormPage';
import SeriePage from './pages/SeriePage';
import SerieFormPage from './pages/SerieFormPage';

function App() {
  const [series, setSeries] = useState([
    { cod: 1, nom: "Friends", cat: "Comedy", img: "friends.png" },
    { cod: 2, nom: "Law & Order", cat: "Drama", img: "law-and-order.png" },
    { cod: 3, nom: "The Big Bang Theory", cat: "Comedy", img: "the-big-bang.png" },
    { cod: 4, nom: "Stranger Things", cat: "Horror", img: "stranger-things.png" },
    { cod: 5, nom: "Dr. House", cat: "Drama", img: "dr-house.png" },
    { cod: 6, nom: "The X-Files", cat: "Drama", img: "the-x-files.png" },
  ]);

  const [categories, setCategories] = useState([
    { cod: 1, nom: "Horror" },
    { cod: 2, nom: "Comedy" },
    { cod: 3, nom: "Action" },
    { cod: 4, nom: "Drama" },
  ]);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/categories" element={<CategoryPage categories={categories} setCategories={setCategories} />} />
        <Route path="/categories/edit/:idcategory" element={<CategoryFormPage categories={categories} setCategories={setCategories} />} />
        <Route path="/series" element={<SeriePage series={series} setSeries={setSeries} />} />
        <Route path="/series/edit/:idserie" element={
          <SerieFormPage
            series={series}
            setSeries={setSeries}
            categories={categories}       // <-- PASAR CATEGORÍAS AQUÍ
          />
        } />
      </Routes>
    </Router>
  );
}

export default App;