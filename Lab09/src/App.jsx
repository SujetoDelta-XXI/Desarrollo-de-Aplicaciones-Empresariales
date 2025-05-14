import { BrowserRouter, Routes, Route } from "react-router-dom";
import SerieComponent from './components/SerieComponent';
import Header from './components/Header';
import DescripcionComponent from './components/DescripcionComponent';
import Footer from './components/Footer';

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
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={
          <div className="container mt-3">
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
      <Footer /> {/* El Footer va aquí, fuera de <Routes> */}
    </BrowserRouter>
  );
}

export default App;