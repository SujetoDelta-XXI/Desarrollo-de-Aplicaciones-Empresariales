import { useParams } from "react-router-dom";

function DescripcionComponent() {
  const { nombre, genero } = useParams();

  return (
    <div className="container mt-5">
      <div className="card p-4">
        <h2>Descripción de la serie</h2>
        <p>
          <strong>{nombre}</strong> es una serie de <strong>{genero}</strong> y te la recomiendo ver.
        </p>
      </div>
    </div>
  );
}

export default DescripcionComponent;