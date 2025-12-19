import { useEffect, useState } from "react";
import axios from "axios";
import PokemonCard from "./PokemonCard";

function PokemonGrid({ search }) {
  const [pokemons, setPokemons] = useState([]);

  useEffect(() => {
    async function fetchPokemons() {
      const res = await axios.get("https://pokeapi.co/api/v2/pokemon?limit=151");
      const details = await Promise.all(res.data.results.map(p =>
        axios.get(p.url).then(res => res.data)
      ));
      setPokemons(details);
    }

    fetchPokemons();
  }, []);

  const filtered = pokemons.filter(p =>
    p.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="row">
      {filtered.map(p => (
        <div className="col-md-3 mb-4" key={p.id}>
          <PokemonCard pokemon={p} />
        </div>
      ))}
    </div>
  );
}

export default PokemonGrid;
