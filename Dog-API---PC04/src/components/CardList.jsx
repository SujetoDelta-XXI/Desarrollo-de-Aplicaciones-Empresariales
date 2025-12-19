const CardList = ({dogs}) => {
    return(
        <div>
            {dogs.map(dog =>(
                <div key={dog.id}>
                <div className="card">
                <div className="card-body">
                    <h4>Rasas</h4>
                    <h5 className="card-title">{dog.message}</h5>
                </div>
                </div>
                </div>
            )) }
        </div>
    );
}

export default CardList;
