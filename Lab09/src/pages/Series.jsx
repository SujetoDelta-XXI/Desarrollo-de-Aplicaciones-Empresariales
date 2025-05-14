import SerieComponent from '../components/SerieComponent'

function Series({ series }) {
  return (
    <div className="row">
      {series.map(serie => (
        <div key={serie.cod} className="col-md-4 mb-3">
          <SerieComponent
            codigo={serie.cod}
            nombre={serie.nom}
            genero={serie.cat}
            imagen={serie.img}
          />
        </div>
      ))}
    </div>
  )
}

export default Series;