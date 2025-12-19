import { Link } from "react-router-dom";
import { Navbar, Nav, Container } from "react-bootstrap";

function HeaderHero() {
    return (
        <div className="d-flex align-items-center justify-content-center text-center bg-dark text-white" style={{ 
            backgroundImage: 'url(https://peruretail.sfo3.cdn.digitaloceanspaces.com/wp-content/uploads/6SMoUnNh8Hs2YiDg.jpg)', 
            height: '90%', 
            backgroundSize: 'cover', 
            color: 'white' 
        }}>
            <div>
                <h1>Bienvenido a Cineplanet</h1>
                <p>Explora y buca la pelicula que desea visualizar</p>
                <div>
                    <Link to="/items" className="btn btn-primary me-2">Peliculas</Link>
                    <Link to="/contact" className="btn btn-secondary">Contacto</Link>
                </div>
            </div>
        </div>
    )
}

export default HeaderHero;