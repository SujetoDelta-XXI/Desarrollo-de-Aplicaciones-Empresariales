import { useState, useEffect } from "react";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function ItemCard({ item }) {
    const localStorageKey = `favorite-${item.id}`;
    const [isFavorite, setIsFavorite] = useState(false);

    useEffect(() => {
        const stored = localStorage.getItem(localStorageKey);
        setIsFavorite(stored === "true");
    }, [localStorageKey]);

    const handleFavorite = () => {
        const newFavorite = !isFavorite;
        setIsFavorite(newFavorite);
        localStorage.setItem(localStorageKey, newFavorite);
        toast[newFavorite ? "success" : "info"](
            newFavorite
                ? "Canción agregada a favoritos"
                : "Canción removida de favoritos"
        );
    };

    return (
        <div className="card mb-3">
            <img src={item.image} className="card-img-top" alt={item.title} />
            <div className="card-body">
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                    <h5 className="card-title">{item.title}</h5>
                    <span
                        style={{ cursor: "pointer", fontSize: "1.5rem", color: isFavorite ? "#FFD700" : "#ccc" }}
                        onClick={handleFavorite}
                        title={isFavorite ? "Quitar de favoritos" : "Agregar a favoritos"}
                        role="button"
                        aria-label="Favorito"
                    >
                        ★
                    </span>
                </div>
                <p className="card-text">{item.description}</p>
                <button className="btn btn-primary">
                    Ver más
                </button>
            </div>
        </div>
    );
}

export default ItemCard;
