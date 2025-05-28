import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import HeaderComponent from "../components/HeaderComponent";

function CategoryFormPage({ categories, setCategories }) {
  const { idcategory } = useParams();
  const navigate = useNavigate();

  const isNew = idcategory === "new";

  const [formData, setFormData] = useState({
    nom: "",
  });

  useEffect(() => {
    if (!isNew) {
      const category = categories.find((c) => c.cod === parseInt(idcategory));
      if (category) {
        setFormData({ nom: category.nom });
      }
    }
  }, [idcategory, isNew, categories]);

  const handleChange = (e) => {
    setFormData({ nom: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (isNew) {
      const newCod = categories.length ? Math.max(...categories.map(c => c.cod)) + 1 : 1;
      const newCategory = { cod: newCod, nom: formData.nom };
      setCategories([...categories, newCategory]);
    } else {
      const updatedCategories = categories.map(c =>
        c.cod === parseInt(idcategory) ? { ...c, nom: formData.nom } : c
      );
      setCategories(updatedCategories);
    }

    navigate("/categories");
  };

  const handleCancel = () => {
    navigate("/categories");
  };

  return (
    <>
      <HeaderComponent />
      <div className="container mt-3">
        <div className="border-bottom pb-3 mb-3">
          <h3>{isNew ? "Nueva Categoría" : "Editar Categoría"}</h3>
        </div>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="nom" className="form-label">Nombre</label>
            <input
              type="text"
              id="nom"
              className="form-control"
              value={formData.nom}
              onChange={handleChange}
              required
              autoFocus
            />
          </div>
          <div className="mb-3 d-flex">
            <button type="submit" className="btn btn-primary me-2">Guardar</button>
            <button type="button" className="btn btn-secondary" onClick={handleCancel}>Cancelar</button>
          </div>
        </form>
      </div>
    </>
  );
}

export default CategoryFormPage;