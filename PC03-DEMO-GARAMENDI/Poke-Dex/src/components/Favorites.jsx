import { useState, useEffect } from "react";

function Favorites() {
  const [favs, setFavs] = useState([]);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem("favorites")) || [];
    setFavs(data);
  }, []);

  return (
    <div className="container mt-5">
      <h2>Mis Favoritos</h2>
      <div className="row">
        {favs.map(p => (
          <div className="col-md-3 mb-4" key={p.id}>
            <div className="card">
              <img src={p.sprite} className="card-img-top" alt={p.name} />
              <div className="card-body text-center">
                <h5>{p.name}</h5>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Favorites;
