import { useState, useEffect } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import axios from "axios";
import HeaderComponent from "../../components/HeaderComponent";

const initData = {
  id: '',
  nombre: '',
}

function CategoryEditFormPage() {
  const { id } = useParams();
  const urlApi = 'http://localhost:8000/api/categorias/';
  const navigate = useNavigate();
  const [data, setData] = useState(initData);

  useEffect(() => {
    const fetchData = async () => {
      const resp = await axios.get(`${urlApi}${id}/`);
      setData(resp.data);
    };
    fetchData();
  }, [id]);

  const onChangeNombre = (e) => {
    setData({ ...data, nombre: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.put(`${urlApi}${id}/`, data);
    navigate("/categories");
  };

  return (
    <>
      <HeaderComponent />
      <div className="container mt-3">
        <div className="border-bottom pb-3 mb-3">
          <h3>Editar - Categoría</h3>
        </div>
        <form onSubmit={handleSubmit} className="row">
          <div className="mb-3">
            <label className="form-label">Nombre</label>
            <input
              type="text"
              onChange={onChangeNombre}
              className="form-control"
              value={data.nombre}
              required
            />
          </div>
          <div className="mb-3">
            <button className="btn btn-primary me-2">Guardar</button>
            <Link className="btn btn-secondary" to="/categories">Cancelar</Link>
          </div>
        </form>
      </div>
    </>
  );
}

export default CategoryEditFormPage;
