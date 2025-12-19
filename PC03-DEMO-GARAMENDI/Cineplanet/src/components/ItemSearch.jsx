function ItemSearch({ value, onChange }) {
  return (
    <input
      type="text"
      className="form-control mb-4"
      placeholder="Buscar por título..."
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  );
}

export default ItemSearch;
