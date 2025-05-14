import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import Header from './components/Header'
import Menu from './components/Menu'
import SerieComponent from './components/SerieComponent'
import Home from './pages/Home'
import Series from './pages/Series'
import Contacto from './pages/Contacto'

function App() {
  const series = [
    {cod:1, nom:"Friends", cat:"Comedy", img:"friends.png"},
    {cod:2, nom:"Law & Order", cat:"Drama", img:"law-and-order.png"},
    {cod:3, nom:"The Big Bang Theory", cat:"Comedy", img:"the-big-bang-theory.png"},
    {cod:4, nom:"Stranger Things", cat:"Terror", img:"stranger-things.png"},
    {cod:5, nom:"Dr. House", cat:"Drama", img:"dr-house.png"},
    {cod:6, nom:"The X-Files", cat:"Drama", img:"the-x-files.png"}
  ];

  return (
    <Router>
      <Header />
      <Menu />
      <div className="container mt-3">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/series" element={<Series series={series} />} />
          <Route path="/contacto" element={<Contacto />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;