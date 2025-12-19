import { useState, useEffect } from 'react';
import itemsData from '../data/items';
import ItemCard from './ItemCard';
import ItemSearch from './ItemSearch';
import useDebounce from '../hooks/useDebounce';
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';

function ItemList() {
  const [items, setItems] = useState([]);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(true);

  const debouncedSearch = useDebounce(search, 300);

  useEffect(() => {
    // Simula carga con delay
    const timer = setTimeout(() => {
      setItems(itemsData);
      setLoading(false);
    }, 1000);
    return () => clearTimeout(timer);
  }, []);

  // Filtrar por título con debounce
  const filteredItems = items.filter(item =>
    item.title.toLowerCase().includes(debouncedSearch.toLowerCase())
  );

  return (
    <div className="container my-5">
      <h2 className="mb-4 text-center">Cartelera de Películas</h2>

      {/* Buscador */}
      <ItemSearch value={search} onChange={setSearch} />

      <div className="row g-4">
        {loading
          ? Array.from({ length: 8 }).map((_, i) => (
              <div className="col-sm-6 col-md-3" key={i}>
                <Skeleton height={300} />
              </div>
            ))
          : filteredItems.length > 0
            ? filteredItems.map(item => (
                <div className="col-sm-6 col-md-3" key={item.id}>
                  <ItemCard item={item} />
                </div>
              ))
            : <p className="text-center">No se encontraron resultados.</p>}
      </div>
    </div>
  );
}

export default ItemList;
