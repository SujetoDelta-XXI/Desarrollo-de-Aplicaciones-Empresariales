import { useState, useEffect } from 'react';
import items from '../data/Items';
import ItemCard from './ItemCard';

function SkeletonCard() {
    return (
        <div className="card mb-4" aria-hidden="true">
            <div className="card-body">
                <div className="placeholder-glow">
                    <div className="placeholder col-12 mb-2" style={{ height: 150 }}></div>
                    <span className="placeholder col-6"></span>
                    <span className="placeholder col-4"></span>
                </div>
            </div>
        </div>
    );
}

function ItemList() {
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Simula carga de datos
        const timer = setTimeout(() => setLoading(false), 1500);
        return () => clearTimeout(timer);
    }, []);

    return (
        <div className="row">
            {loading
                ? Array.from({ length: 6 }).map((_, idx) => (
                        <div className="col-md-4" key={idx}>
                            <SkeletonCard />
                        </div>
                    ))
                : items.map(item => (
                        <div className="col-md-4" key={item.id}>
                            <ItemCard item={item} />
                        </div>
                    ))}
        </div>
    );
}

export default ItemList;