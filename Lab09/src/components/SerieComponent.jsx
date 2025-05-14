import { useNavigate } from "react-router-dom";

function SerieComponent(props) {
  const navigate = useNavigate();

  const handleDescripcion = () => {
    // Navega a la ruta de descripción con los datos de la serie
    navigate(`/descripcion/${encodeURIComponent(props.nombre)}/${encodeURIComponent(props.genero)}`);
  };

  return (
    <div className="card h-100 w-100">
      <img 
        className="card-img-top" 
        src={"https://dummyimage.com/400x250/000/fff&text=" + props.imagen}
        alt={props.nombre} 
      />
      <div className="card-body d-flex flex-column">
        <h5 className="card-title">{props.nombre}</h5>
        <p className="card-text">{props.genero}</p>
        <div className="mt-auto">
          <button className="btn btn-primary w-100" onClick={handleDescripcion}>
            Descripción
          </button>
        </div>
      </div>
    </div>
  );
}

export default SerieComponent;