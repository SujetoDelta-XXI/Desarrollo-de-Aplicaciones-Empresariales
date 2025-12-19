import { useEffect, useState } from "react";

function PokemonCard({ pokemon }) {
  const [fav, setFav] = useState(false);

  useEffect(() => {
    const favs = JSON.parse(localStorage.getItem("favorites")) || [];
    setFav(favs.some(f => f.id === pokemon.id));
  }, [pokemon]);

  const toggleFavorite = () => {
    let favs = JSON.parse(localStorage.getItem("favorites")) || [];
    if (fav) {
      favs = favs.filter(f => f.id !== pokemon.id);
    } else {
      favs.push({ id: pokemon.id, name: pokemon.name, sprite: pokemon.sprites.front_default });
    }
    localStorage.setItem("favorites", JSON.stringify(favs));
    setFav(!fav);
  };

  return (
    <div className="card">
      <img src={pokemon.sprites.front_default} className="card-img-top" alt={pokemon.name} />
      <div className="card-body">
        <h5>{pokemon.name}</h5>
        <p>Tipo: {pokemon.types.map(t => t.type.name).join(', ')}</p>
        <button onClick={toggleFavorite} className="btn btn-sm btn-warning">
          {fav ? "★ Favorito" : "☆ Agregar a Favoritos"}
        </button>
      </div>
    </div>
  );
}

export default PokemonCard;
