import { useState } from 'react';
import { toast } from 'react-toastify';

function ContactForm() {
    const [form, setForm] = useState({
        name: '',
        email: '',
        message: ''
    });

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.id]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        toast.success('Mensaje enviado correctamente');
        setForm({ name: '', email: '', message: '' });
    };

    return(
        <div className="container mt-5">
            <h2>Contacto</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="name" className="form-label">Nombre</label>
                    <input
                        type="text"
                        className="form-control"
                        id="name"
                        required
                        value={form.name}
                        onChange={handleChange}
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Correo Electrónico</label>
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        required
                        value={form.email}
                        onChange={handleChange}
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="message" className="form-label">Mensaje</label>
                    <textarea
                        className="form-control"
                        id="message"
                        rows="4"
                        required
                        value={form.message}
                        onChange={handleChange}
                    ></textarea>
                </div>
                <button type="submit" className="btn btn-primary">Enviar</button>
            </form>
        </div>
    )
}

export default ContactForm;