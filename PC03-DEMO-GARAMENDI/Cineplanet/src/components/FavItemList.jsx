import { useEffect, useState } from 'react';
import ItemCard from './ItemCard';
import items from '../data/items'; // Tu mock completo

function FavItemList() {
  const [favItems, setFavItems] = useState([]);

  useEffect(() => {
    const storedIds = JSON.parse(localStorage.getItem('favoritos')) || [];
    const filtered = items.filter(item => storedIds.includes(item.id));
    setFavItems(filtered);
  }, []);

  if (favItems.length === 0) {
    return <p className="text-center">No tienes favoritos guardados.</p>;
  }

  return (
    <div className="container my-5">
      <h3 className="mb-4 text-center">🎉 Tus Películas Favoritas</h3>
      <div className="row g-4">
        {favItems.map((item) => (
          <div className="col-sm-6 col-md-3" key={item.id}>
            <ItemCard item={item} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default FavItemList;
