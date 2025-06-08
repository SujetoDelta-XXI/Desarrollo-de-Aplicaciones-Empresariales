import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import HeaderComponent from "../components/HeaderComponent";

const initData = {
  nombre: '',
  descripcion: '',
  imagen_url: '',
  categoria: '',
};

function SerieFormPage() {
  const { idserie } = useParams();
  const navigate = useNavigate();
  const isNew = idserie === "new";
  const [formData, setFormData] = useState(initData);
  const [categories, setCategories] = useState([]);
  const urlApi = 'http://localhost:8000/api/series/';
  const urlCat = 'http://localhost:8000/api/categorias/';

  // Cargar categorías SIEMPRE desde la API
  useEffect(() => {
    axios.get(urlCat).then(resp => setCategories(resp.data));
  }, []);

  useEffect(() => {
    if (!isNew) {
      axios.get(`${urlApi}${idserie}/`).then(resp => setFormData(resp.data));
    }
  }, [idserie, isNew]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isNew) {
      await axios.post(urlApi, formData);
    } else {
      await axios.put(`${urlApi}${idserie}/`, formData);
    }
    navigate("/series");
  };

  return (
    <>
      <HeaderComponent />
      <div className="container mt-3">
        <div className="border-bottom pb-3 mb-3">
          <h3>{isNew ? "Nueva Serie" : "Editar Serie"}</h3>
        </div>
        <form className="row" onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Nombre</label>
            <input
              name="nombre"
              type="text"
              className="form-control"
              value={formData.nombre}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Descripción</label>
            <textarea
              name="descripcion"
              className="form-control"
              value={formData.descripcion}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Imagen URL</label>
            <input
              name="imagen_url"
              type="url"
              className="form-control"
              value={formData.imagen_url}
              onChange={handleChange}
              required
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Categoría</label>
            <select
              name="categoria"
              className="form-select"
              value={formData.categoria}
              onChange={handleChange}
              required
            >
              <option value="">Seleccione una categoría</option>
              {categories.map(cat => (
                <option key={cat.id} value={cat.id}>
                  {cat.nombre}
                </option>
              ))}
            </select>
          </div>
          <button className="btn btn-primary me-2">Guardar</button>
          <button className="btn btn-secondary" onClick={() => navigate("/series")}>Cancelar</button>
        </form>
      </div>
    </>
  );
}

export default SerieFormPage;
