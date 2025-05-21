import HeaderComponent from "../components/HeaderComponent";
import SerieComponent from "../components/SerieComponent";
import { useNavigate } from "react-router-dom";

function SeriePage({ series, setSeries }) {
  const navigate = useNavigate();

  const handleDelete = (cod) => {
    if (window.confirm("¿Está seguro de eliminar esta serie?")) {
      setSeries(series.filter((serie) => serie.cod !== cod));
      // También eliminar imagen de LocalStorage
      localStorage.removeItem(`serie-img-${cod}`);
    }
  };
  
  const handleEdit = (cod) => {
    navigate(`/series/edit/${cod}`);
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
          {series.map((serie) => {
            // Leer imagen Base64 de LocalStorage
            const imgBase64 = localStorage.getItem(`serie-img-${serie.cod}`);
            return (
              <div key={serie.cod} className="col-md-3 mb-3">
                <SerieComponent
                  codigo={serie.cod}
                  nombre={serie.nom}
                  categoria={serie.cat}
                  imagen={imgBase64 || "https://dummyimage.com/400x250/000/fff&text=No+Image"}
                  onDelete={handleDelete}
                  onEdit={handleEdit}
                />
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
}

export default SeriePage;
