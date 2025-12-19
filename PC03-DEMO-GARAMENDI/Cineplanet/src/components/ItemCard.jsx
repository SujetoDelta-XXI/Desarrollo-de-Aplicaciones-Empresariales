import { useState, useRef, useEffect } from "react";
import { toast } from "react-toastify";

// 🔧 Funciones de manejo localStorage para favoritos
const getFavoritos = () => {
  const favs = localStorage.getItem("favoritos");
  return favs ? JSON.parse(favs) : [];
};

const setFavoritos = (favs) => {
  localStorage.setItem("favoritos", JSON.stringify(favs));
};

const toggleFavorito = (id) => {
  const favs = getFavoritos();
  const existe = favs.includes(id);
  const nuevosFavoritos = existe
    ? favs.filter((f) => f !== id)
    : [...favs, id];
  setFavoritos(nuevosFavoritos);
  return !existe;
};

const estaEnFavoritos = (id) => {
  return getFavoritos().includes(id);
};

// ⭐ Botón estrella
function StarButton({ isFavorite, onClick }) {
  return (
    <button
      type="button"
      className="btn btn-link p-0 ms-2"
      onClick={onClick}
      aria-label={isFavorite ? "Quitar de favoritos" : "Agregar a favoritos"}
      style={{
        fontSize: "1.5rem",
        color: isFavorite ? "#ffc107" : "#ccc"
      }}
    >
      {isFavorite ? "★" : "☆"}
    </button>
  );
}

// 🧩 Componente principal
function ItemCard({ item }) {
  const [favorite, setFavorite] = useState(false);
  const toastShown = useRef(false);

  // Al montar, verifica si el ítem ya es favorito
  useEffect(() => {
    setFavorite(estaEnFavoritos(item.id));
  }, [item.id]);

  const handleFavorite = () => {
    const nuevoEstado = toggleFavorito(item.id);
    setFavorite(nuevoEstado);

    if (!toastShown.current) {
      toast[nuevoEstado ? "success" : "info"](
        nuevoEstado ? "Agregado a favoritos" : "Quitado de favoritos"
      );
      toastShown.current = true;
      setTimeout(() => {
        toastShown.current = false;
      }, 500);
    }
  };

  return (
    <div className="card h-100 shadow-sm">
      <img src={item.image} className="card-img-top" alt={item.title} />
      <div className="card-body d-flex flex-column">
        <h5 className="card-title">{item.title}</h5>
        <p className="card-text">{item.description}</p>
        <div className="d-flex align-items-center mt-auto">
          <button className="btn btn-outline-primary" disabled>
            Ver más
          </button>
          <StarButton isFavorite={favorite} onClick={handleFavorite} />
        </div>
      </div>
    </div>
  );
}

export default ItemCard;
