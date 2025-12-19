import { Link } from 'react-router-dom';
import { Container, Row, Col } from 'react-bootstrap';

function Footer() {
    return (
        <footer className="bg-dark text-white py-4 mt-auto">
            <Container>
                <Row className="align-items-center">
                    <Col md={6} className="text-center text-md-start mb-2 mb-md-0">
                        <span>© 2023 Spotify Clone. All rights reserved.</span>
                    </Col>
                    <Col md={6} className="text-center text-md-end">
                        <Link to="/privacy" className="text-white me-3 text-decoration-none">
                            Privacy Policy
                        </Link>
                        <span className="text-secondary">|</span>
                        <Link to="/terms" className="text-white ms-3 text-decoration-none">
                            Terms of Service
                        </Link>
                    </Col>
                </Row>
            </Container>
        </footer>
    );
}

export default Footer;