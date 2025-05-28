import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import HeaderComponent from "../components/HeaderComponent";

function SerieFormPage({ series, setSeries, categories }) {  // Recibe categories
  const { idserie } = useParams();
  const navigate = useNavigate();

  const isNew = idserie === "new";

  const [formData, setFormData] = useState({
    nom: '',
    cat: '',
    img: '',
  });

  useEffect(() => {
    if (!isNew) {
      const serie = series.find(s => s.cod === parseInt(idserie));
      if (serie) {
        const savedImg = localStorage.getItem(`serie-img-${serie.cod}`);
        setFormData({
          nom: serie.nom,
          cat: serie.cat,
          img: savedImg || '',
        });
      }
    }
  }, [idserie, isNew, series]);

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData(prev => ({ ...prev, [id]: value }));
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setFormData(prev => ({
          ...prev,
          img: reader.result,
        }));
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (isNew) {
      const newCod = series.length ? Math.max(...series.map(s => s.cod)) + 1 : 1;
      const newSerie = {
        cod: newCod,
        nom: formData.nom,
        cat: formData.cat,
        img: '',
      };
      setSeries([...series, newSerie]);
      localStorage.setItem(`serie-img-${newCod}`, formData.img);
    } else {
      const updatedSeries = series.map(s =>
        s.cod === parseInt(idserie) ? { ...s, nom: formData.nom, cat: formData.cat } : s
      );
      setSeries(updatedSeries);
      localStorage.setItem(`serie-img-${idserie}`, formData.img);
    }

    navigate('/series');
  };

  const handleCancel = () => {
    navigate('/series');
  };

  return (
    <>
      <HeaderComponent />
      <div className="container mt-3">
        <div className="border-bottom pb-3 mb-3">
          <h3>{isNew ? "Nueva Serie" : "Editar Serie"}</h3>
        </div>
        <form className="row" onSubmit={handleSubmit}>
          <div className="col-md-4">
            <img
              id="fileImg"
              className="card-img-top"
              src={formData.img || "https://dummyimage.com/400x250/000/fff"}
              alt="img"
            />
          </div>
          <div className="col-md-8">
            <div className="mb-3">
              <label htmlFor="nom" className="form-label">Nombre</label>
              <input
                type="text"
                className="form-control"
                id="nom"
                value={formData.nom}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="cat" className="form-label">Categoria</label>
              <select
                className="form-select"
                id="cat"
                value={formData.cat}
                onChange={handleChange}
                required
              >
                <option value="">Seleccione una opción</option>
                {categories.map(cat => (
                  <option key={cat.cod} value={cat.nom}>
                    {cat.nom}
                  </option>
                ))}
              </select>
            </div>
            <div className="mb-3">
              <label htmlFor="inputImage" className="form-label">Imagen</label>
              <input
                type="file"
                className="form-control"
                id="inputImage"
                accept="image/*"
                onChange={handleFileChange}
              />
            </div>
            <div className="mb-3 d-flex">
              <button type="submit" className="btn btn-primary me-2">Guardar</button>
              <button type="button" className="btn btn-secondary" onClick={handleCancel}>Cancelar</button>
            </div>
          </div>
        </form>
      </div>
    </>
  );
}

export default SerieFormPage;