import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomPage';
import CategoryPage from './pages/CategoryPage';
import SeriePage from './pages/SeriePage';
import SerieFormPage from './pages/SerieFormPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/categories" element={<CategoryPage />} />
        <Route path="/series" element={<SeriePage />} />
        <Route path="/series/edit/:idserie" element={<SerieFormPage />} />
      </Routes>
    </Router>
  );
}

export default App
