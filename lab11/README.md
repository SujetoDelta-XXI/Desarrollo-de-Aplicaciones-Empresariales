# Desarrollo-de-Aplicaciones-Empresariales
Repositorio de los laboratorios del curso Desarrollo de Aplicaciones Empresariales de la carrera de Diseño y Desarrollo de Software - Ciclo IV

# 📚 Desarrollo de Aplicaciones Empresariales – Proyecto SeriesApp

Repositorio de los laboratorios del curso **Desarrollo de Aplicaciones Empresariales** de la carrera de **Diseño y Desarrollo de Software - Ciclo IV**.

Este proyecto, llamado **SeriesApp**, fue desarrollado en React y consiste en una aplicación CRUD que permite gestionar series y categorías con almacenamiento local. Además, la estructura está lista para integrarse con una API REST (por ejemplo, Django o Node.js).

---

## 📺 SeriesApp - CRUD con React + LocalStorage

**SeriesApp** permite crear, editar, eliminar y visualizar series y categorías de forma interactiva, usando React y `localStorage` para persistencia en el navegador.

---

## 🚀 Funcionalidades Principales

### ✅ Categorías
- Listado completo en formato tabla.
- Crear nuevas categorías.
- Editar categorías existentes.
- Eliminar categorías con confirmación.
- Persistencia local mediante `localStorage`.

### ✅ Series
- Visualización con tarjetas (`card` Bootstrap).
- Asociación a categorías.
- Subida de imágenes en formato Base64 (almacenadas localmente).
- CRUD completo de series.
- Persistencia local con `localStorage`.

### ✅ Login visual
- Formulario de inicio de sesión sin backend.
- Redirección automática a la vista de series tras ingresar.
- Preparado para futura autenticación real.

---

## 🛠️ Tecnologías Utilizadas

- [React](https://react.dev/) – Framework principal.
- [React Router DOM](https://reactrouter.com/) – Navegación por rutas.
- [Bootstrap 5](https://getbootstrap.com/) – Estilos y componentes visuales.
- [LocalStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) – Persistencia de datos en el navegador.
- Vite – Herramienta de desarrollo moderna y rápida.

---

## 📦 Persistencia de Datos

- Los datos de **series** y **categorías** se almacenan en `localStorage`.
- Las **imágenes** se guardan en Base64 con claves dinámicas (ej: `serie-img-1`).
- Los datos persisten incluso al cerrar o actualizar el navegador.

---

## 🔒 PrivateRoute – Control de acceso a rutas

### 📌 ¿Qué hace PrivateRoute?

El componente `PrivateRoute` se encarga de **restringir el acceso a ciertas rutas** asegurando que solo los usuarios autenticados puedan acceder.

### 🧠 Lógica interna:

```jsx
import { Navigate } from "react-router-dom";

function PrivateRoute({ isAuthenticated, children }) {
  return isAuthenticated ? children : <Navigate to="/" />;
}

## 🧪 Cómo ejecutar el proyecto

1.Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/seriesapp.git
   cd seriesapp

 ## Instalar dependencias
npm install

## Ejecutar proyecto
npm run dev

## Abrir en Navegador:
http://localhost:5173/home

🔑 Datos de acceso de prueba
Correo: admin@tecsup.edu.pe

Contraseña: 123456

✍️ Autor
👤 Carlos Asparrin
👤 Lopez Romero
👤 Villena Gomez

Proyecto realizado para el curso Desarrollo de Aplicaciones Empresariales - IV ciclo

