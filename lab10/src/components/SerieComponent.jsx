import { useNavigate } from "react-router-dom";

import friendsImg from '../assets/friends.png';
import lawAndOrderImg from '../assets/law-and-order.png';
import bigBangImg from '../assets/the-big-bang-theory.png';
import strangerThingsImg from '../assets/stranger-things.png';
import drHouseImg from '../assets/dr-house.png';
import xFilesImg from '../assets/the-x-files.png';

const imagesMap = {
  'friends.png': friendsImg,
  'law-and-order.png': lawAndOrderImg,
  'the-big-bang-theory.png': bigBangImg,
  'stranger-things.png': strangerThingsImg,
  'dr-house.png': drHouseImg,
  'the-x-files.png': xFilesImg,
};

function SerieComponent(props) {
    const navigate = useNavigate();

    const gotoUrl = (codigo) => {
        navigate("/series/edit/" + codigo);
    };

    const imagenSrc = imagesMap[props.imagen] || 'https://via.placeholder.com/400x250?text=No+Image';

    return (
        <div className="card">
            <img 
                className="card-img-top" 
                src={imagenSrc} 
                alt={props.nombre} />
            <div className="card-body">
                <h5 className="card-title">{props.nombre}</h5>
                <p className="card-text">{props.categoria}</p>
                <div className="d-flex justify-content-between">
                    <button onClick={() => gotoUrl(props.codigo)} className="btn btn-secondary">Editar</button> 
                    <button className="btn btn-danger">Eliminar</button>
                </div>
            </div>
        </div>
    );
}

export default SerieComponent;