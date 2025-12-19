import { useState } from 'react';
import { Toast, ToastContainer } from 'react-bootstrap';

function ContactForm() {
    const [showToast, setShowToast] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        setShowToast(true);
        e.target.reset();
    };

    return (
        <div>
            <h2>Contacto</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="name" className="form-label">Nombre</label>
                    <input
                        type="text"
                        className="form-control"
                        id="name"
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Correo Electrónico</label>
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        required
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="message" className="form-label">Mensaje</label>
                    <textarea
                        className="form-control"
                        id="message"
                        rows="4"
                        required
                    ></textarea>
                </div>
                <button type="submit" className="btn btn-primary">Enviar</button>
            </form>
            <ToastContainer position="top-end" className="p-3">
                <Toast
                    onClose={() => setShowToast(false)}
                    show={showToast}
                    delay={3000}
                    autohide
                    bg="success"
                >
                    <Toast.Header>
                        <strong className="me-auto">Mensaje enviado</strong>
                    </Toast.Header>
                    <Toast.Body>¡Gracias por contactarnos!</Toast.Body>
                </Toast>
            </ToastContainer>
        </div>
    );
}

export default ContactForm;
