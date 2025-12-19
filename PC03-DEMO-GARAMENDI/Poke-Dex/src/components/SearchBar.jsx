function SearchBar({ value, onChange }) {
  return (
    <input
      type="text"
      className="form-control mb-4"
      placeholder="Buscar Pokémon..."
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  );
}

export default SearchBar;
