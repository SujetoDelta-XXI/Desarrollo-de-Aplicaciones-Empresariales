import React from 'react';
import ItemList from '../components/ItemList';
import FavItemList from '../components/FavItemList';

function ItemsPage() {
  return (
    <div className="container my-5"> 
      <FavItemList /> 
      <ItemList />
    </div>
  );
}

export default ItemsPage;
