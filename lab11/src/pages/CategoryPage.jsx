import HeaderComponent from "../components/HeaderComponent";
import { useNavigate } from "react-router-dom";

function CategoryPage({ categories, setCategories }) {
  const navigate = useNavigate();

  const handleDelete = (cod) => {
    if (window.confirm("¿Está seguro de eliminar esta categoría?")) {
      setCategories(categories.filter((c) => c.cod !== cod));
    }
  };

  const handleEdit = (cod) => {
    navigate(`/categories/edit/${cod}`);
  };

  const handleNew = () => {
    navigate("/categories/edit/new");
  };

  return (
    <>
      <HeaderComponent />
      <div className="container mt-3">
        <div className="d-flex justify-content-between border-bottom pb-3 mb-3">
          <h3>Categorías</h3>
          <button className="btn btn-primary" onClick={handleNew}>
            Nueva Categoría
          </button>
        </div>
        <table className="table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th className="text-center">Id</th>
              <th className="text-center" style={{ width: "150px" }}>
                Acciones
              </th>
            </tr>
          </thead>
          <tbody>
            {categories.map((item) => (
              <tr key={item.cod}>
                <td>{item.nom}</td>
                <td className="text-center">{item.cod}</td>
                <td className="text-center">
                  <div className="d-flex justify-content-center">
                    <button
                      className="btn btn-secondary me-2 btn-sm"
                      onClick={() => handleEdit(item.cod)}
                    >
                      <i className="bi bi-pencil-square me-1"></i>
                      Editar
                    </button>
                    <button
                      className="btn btn-danger btn-sm"
                      onClick={() => handleDelete(item.cod)}
                    >
                      <i className="bi bi-trash-fill me-1"></i>
                      Eliminar
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default CategoryPage;