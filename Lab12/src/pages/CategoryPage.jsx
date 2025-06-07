import { useEffect } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import HeaderComponent from "../components/HeaderComponent";

function CategoryPage({ categories, setCategories }) {
  const navigate = useNavigate();
  const urlApi = "http://127.0.0.1:8000/api/categorias/";

  useEffect(() => {
    const loadData = async () => {
      try {
        const resp = await axios.get("http://127.0.0.1:8000/api/categorias/");
        console.log("Categorías cargadas:", resp.data);
        setCategories(resp.data);
      } catch (error) {
        console.error("Error cargando categorías:", error);
      }
    };

    loadData();
  }, []);

  const handleDelete = async (id) => {
    if (window.confirm("¿Está seguro de eliminar este registro?")) {
      await axios.delete(`${urlApi}${id}/`);
      const nLista = categories.filter((item) => item.id !== id);
      setCategories(nLista);
    }
  };

  const handleEdit = (id) => {
    navigate(`/categories/edit/${id}`);
  };

  return (
    <>
      <HeaderComponent />
      <div className="container mt-3">
        <div className="d-flex justify-content-between border-bottom pb-3 mb-3">
          <h3>Categorías</h3>
          <div>
            <Link className="btn btn-primary" to="/categories/new">
              Nuevo
            </Link>
          </div>
        </div>
        <table className="table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th className="text-center">Id</th>
              <th className="text-center" style={{ width: "100px" }}>
                Acciones
              </th>
            </tr>
          </thead>
          <tbody>
            {categories.map((item) => (
              <tr key={item.id}>
                <td>{item.nombre}</td>
                <td className="text-center">{item.id}</td>
                <td className="text-center">
                  <button
                    onClick={() => handleEdit(item.id)}
                    className="btn btn-secondary me-2 btn-sm"
                  >
                    <i className="bi bi-pencil-square"></i>
                  </button>
                  <button
                    onClick={() => handleDelete(item.id)}
                    className="btn btn-danger btn-sm"
                  >
                    <i className="bi bi-trash-fill"></i>
                  </button>
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
