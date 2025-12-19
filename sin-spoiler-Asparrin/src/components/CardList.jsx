
const CardList = ({ data }) => {
  return (
    <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      {data.map((item) => {
        const { id, title, description, duration, backdrop } = item;

        return (
          <div key={id} className="col">
            <div className="card shadow-sm">
              <img src={backdrop} className="card-img-top" alt="Card image cap" />
              <div className="card-body">
                <h2 className="card-title">{title}</h2>
                <p className="card-text">{description.slice(0, 128)}...</p>
                <div className="d-flex justify-content-between align-items-center">
                  <div className="btn-group"> <button type="button" className="btn btn-sm btn-outline-secondary">View</button> <button
                    type="button" className="btn btn-sm btn-outline-secondary">Edit</button> </div> <small
                      className="text-body-secondary">{duration}</small>
                </div>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default CardList;