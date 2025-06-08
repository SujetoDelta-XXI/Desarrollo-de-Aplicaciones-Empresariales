import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import HeaderComponent from "../components/HeaderComponent";
import { API_BASE_URL } from "../config";

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

  const urlApi = `${API_BASE_URL}series/`;
  const urlCat = `${API_BASE_URL}categorias/`;

  // Cargar categorías
  useEffect(() => {
    axios.get(urlCat)
      .then(resp => setCategories(resp.data))
      .catch(err => console.error("Error al cargar categorías:", err));
  }, []);

  useEffect(() => {
    if (!isNew) {
      axios.get(`${urlApi}${idserie}/`)
        .then(resp => setFormData(resp.data))
        .catch(err => console.error("Error al cargar serie:", err));
    }
  }, [idserie, isNew]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isNew) {
        await axios.post(urlApi, formData);
      } else {
        await axios.put(`${urlApi}${idserie}/`, formData);
      }
      navigate("/series");
    } catch (error) {
      console.error("Error al guardar serie:", error);
    }
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
          <div className="d-grid gap-3">
            <button className="btn btn-warning" type="submit">Guardar</button>
            <button className="btn btn-secondary" type="button" onClick={() => navigate("/series")}>Cancelar</button>
          </div>
        </form>
      </div>
    </>
  );
}

export default SerieFormPage;
