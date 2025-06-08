import HeaderComponent from "../components/HeaderComponent";
import SerieComponent from "../components/SerieComponent";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import axios from "axios";
import { API_BASE_URL } from "../config";

function SeriePage({ series, setSeries }) {
  const navigate = useNavigate();
  const urlApi = `${API_BASE_URL}series/`;

  const handleDelete = async (cod) => {
    if (window.confirm("¿Está seguro de eliminar esta serie?")) {
      await axios.delete(`${urlApi}${cod}/`);
      setSeries(series.filter((serie) => serie.id !== cod));
    }
  };

  const handleEdit = (cod) => {
    navigate(`/series/edit/${cod}`);
  };

  const handleNew = () => {
    navigate("/series/edit/new");
  };

  useEffect(() => {
    axios.get(urlApi).then((resp) => setSeries(resp.data));
  }, []);

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
                categoria={serie.categoria}
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
