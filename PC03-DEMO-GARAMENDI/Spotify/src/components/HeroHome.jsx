import{ Link } from 'react-router-dom';
import { Container } from 'react-bootstrap';

function HeroHome() {
    return (
        <div className="hero-home" style={
            { 
                backgroundImage: 'url(https://imusician.imgix.net/images/What-is-Spotify-for-Artists__meta.jpg?auto=compress&w=1200&h=630&fit=crop)', 
                height: '100%', 
                backgroundSize: 'cover', 
                color: 'white', 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center', 
                textAlign: 'center' 
            }
        }>
            <Container>
                <h1>Bienvenido a Spotify</h1>
                <p>Explora y busca la musica que quieres reproducir</p>
                <div>
                    <Link to="/items" className="btn btn-primary me-2">Musicas</Link>
                    <Link to="/contact" className="btn btn-secondary">Contacto</Link>
                </div>
            </Container>
        </div>
    );
}

export default HeroHome;