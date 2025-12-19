import items from '../data/Items';
import ItemCard from './ItemCard';
import { useState, useEffect } from 'react';

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

function CardList() {
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => setLoading(false), 1200);
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
                : items.slice(0, 6).map(item => (
                        <div className="col-md-4" key={item.id}>
                            <ItemCard item={item} />
                        </div>
                    ))}
        </div>
    );
}

export default CardList;