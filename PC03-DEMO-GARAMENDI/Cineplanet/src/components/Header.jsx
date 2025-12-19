import { Link } from "react-router-dom";
import { Navbar, Nav, Container } from "react-bootstrap";

function Header() {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <Container>
            <Link className="navbar-brand" to="/">Cineplanet</Link>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <Link className="nav-link" to="/">Home</Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link" to="/items">Peliculas</Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link" to="/contact">Contacto</Link>
                    </li>
                </ul>
            </div>
            </Container>
        </nav>
    );
}

export default Header;