import FavItemsList from "../components/FavItemsList";
import ItemList from "../components/ItemList";

function ItemsPage() {
  return (
    <div className="container">
      <h1>Canciones</h1>
      <p>La mayor biblioteca de música en tus manos</p>
      <FavItemsList/>
      <ItemList/>
    </div>
  );
}

export default ItemsPage;