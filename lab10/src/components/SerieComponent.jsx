import { useNavigate } from "react-router-dom";

function SerieComponent({ codigo, nombre, categoria, imagen, onDelete }) {
  const navigate = useNavigate();

  const gotoUrl = (codigo) => {
    navigate("/series/edit/" + codigo);
  };

  return (
    <div className="card">
      <img
        className="card-img-top"
        src={imagen}
        alt="img"
      />
      <div className="card-body">
        <h5 className="card-title">{nombre}</h5>
        <p className="card-text">{categoria}</p>
        <div className="d-flex justify-content-between">
          <button onClick={() => gotoUrl(codigo)} className="btn btn-secondary">
            Editar
          </button>
          <button onClick={() => onDelete(codigo)} className="btn btn-danger">
            Eliminar
          </button>
        </div>
      </div>
    </div>
  );
}

export default SerieComponent;
