import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

import Header from './components/Header';
import Menu from './components/Menu';
import Footer from './components/Footer';
import SerieComponent from './components/SerieComponent';
import DescripcionComponent from './components/DescripcionComponent';

import Home from './pages/Home';
import Series from './pages/Series';
import Contacto from './pages/Contacto';

function App() {
  const series = [
    {cod:1, nom:"Friends", cat:"Comedia", img:"Friends"},
    {cod:2, nom:"Law & Order", cat:"Drama", img:"Law+%26+Order"},
    {cod:3, nom:"The Big Bang Theory", cat:"Comedia", img:"The+Big+Bang+Theory"},
    {cod:4, nom:"Stranger Things", cat:"Terror", img:"Stranger+Things"},
    {cod:5, nom:"Dr. House", cat:"Drama", img:"Dr.+House"},
    {cod:6, nom:"The X-Files", cat:"Drama", img:"The+X-Files"}
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

          <Route path="/listado" element={
            <div>
              <h1 className="border-bottom pb-3 mb-3">Series</h1>
              <div className="row">
                {series.map((serie) => (
                  <div key={serie.cod} className="col-md-4 mb-3">
                    <SerieComponent
                      codigo={serie.cod}
                      nombre={serie.nom}
                      genero={serie.cat}
                      imagen={serie.img}
                    />
                  </div>
                ))}
              </div>
            </div>
          } />

          <Route path="/descripcion/:nombre/:genero" element={<DescripcionComponent />} />
        </Routes>
      </div>
      <Footer />
    </Router>
  );
}

export default App;
