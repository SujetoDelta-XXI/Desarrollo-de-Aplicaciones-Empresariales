import { useEffect, useState } from "react";
import axios from "axios";
import HeaderComponent from "../components/HeaderComponent";
import SerieComponent from "../components/SerieComponent";
import { useNavigate } from "react-router-dom";

function SeriePage({ series, setSeries }) {
  const [categories, setCategories] = useState([]);
  const navigate = useNavigate();

  // Cargar series
  useEffect(() => {
    const loadData = async () => {
      try {
        const resp = await axios.get("http://localhost:8000/api/series/");
        setSeries(resp.data);
      } catch (error) {
        console.error("Error cargando series:", error);
      }
    };
    loadData();
  }, [setSeries]);

  // Cargar categorías
  useEffect(() => {
    axios.get("http://localhost:8000/api/categorias/")
      .then(resp => setCategories(resp.data));
  }, []);

  // Función para obtener el nombre de la categoría
  const getCategoriaNombre = (catId) => {
    const cat = categories.find(c => c.id === catId);
    return cat ? cat.nombre : "";
  };

  const handleDelete = async (id) => {
    if (window.confirm("¿Está seguro de eliminar esta serie?")) {
      await axios.delete(`http://localhost:8000/api/series/${id}/`);
      setSeries(series.filter((serie) => serie.id !== id));
    }
  };

  const handleEdit = (id) => {
    navigate(`/series/edit/${id}`);
  };

  const handleNew = () => {
    navigate("/series/edit/new");
  };

  return (
    <>
      <HeaderComponent />
      <div className="container mt-3">
        <div className="d-flex justify-content-between border-bottom pb-3 mb-3">
          <h3>Series</h3>
          <div>
            <button className="btn btn-primary" onClick={handleNew}>
              Nuevo
            </button>
          </div>
        </div>
        <div className="row">
          {series.map((serie) => (
            <div key={serie.id} className="col-md-3 mb-3">
              <SerieComponent
                codigo={serie.id}
                nombre={serie.nombre}
                categoria={getCategoriaNombre(serie.categoria)}
                imagen={serie.imagen_url || "https://dummyimage.com/400x250/000/fff&text=No+Image"}
                onDelete={handleDelete}
                onEdit={handleEdit}
              />
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default SeriePage;