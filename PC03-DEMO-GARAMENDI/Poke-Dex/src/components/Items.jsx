import { useState } from "react";
import SearchBar from "../components/SearchBar";
import PokemonGrid from "../components/PokemonGrid";
import useDebounce from "../hooks/useDebounce";

function Items() {
  const [query, setQuery] = useState("");
  const debouncedQuery = useDebounce(query, 300);

  return (
    <div className="container mt-5">
      <h2 className="mb-3">Pokédex</h2>
      <SearchBar value={query} onChange={setQuery} />
      <PokemonGrid search={debouncedQuery} />
    </div>
  );
}

export default Items;
