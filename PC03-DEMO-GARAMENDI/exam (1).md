# Examen Práctico React – Proyecto Mini-App SPA 🇵🇪🌎

Este examen tiene **duración máxima de 2 horas** y se realiza en React 19 con Vite. Debes entregar un repositorio público en GitHub que incluya todo el código, un video demostrativo (≤ 2 min) y un README con instrucciones claras. El objetivo es crear una pequeña SPA (Single Page Application) con tres páginas principales: Inicio, Listado de Ítems y Contacto, usando hooks, React Router y algunas librerías UI.

---

## Instrucciones Generales 📝

1. **Clona o crea** un repositorio nuevo en tu cuenta de GitHub (por ejemplo, `mi-mini-spa`).

2. Estructura mínima del proyecto:

   ```
   mi-mini-spa/
   ├── public/
   │   └── favicon.ico
   ├── src/
   │   ├── components/
   │   ├── css/
   │   ├── data/
   │   ├── utils/
   │   ├── App.jsx
   │   └── main.jsx
   ├── .gitignore
   ├── index.html
   ├── package.json
   └── README.md
   ```

3. Usa **Vite** como bundler y **React 19** (sin `import React`).

4. Escoge un **framework CSS** (Tailwind, Bootstrap, Material UI u otro) para agilizar el diseño.

5. La aplicación debe funcionar localmente con:

   ```bash
   npm install
   npm run dev
   ```

6. En tu `README.md` incluye:

   * Título y breve descripción del proyecto.
   * Tecnologías y versiones empleadas.
   * Pasos para instalar y ejecutar la aplicación.
   * Cómo navegar por la SPA.
   * Capturas de pantalla (opcional).

7. **Video demostrativo** (≤ 2 min) mostrando:

   * Clonar el repo e instalar (`npm install`).
   * Ejecutar la aplicación (`npm run dev`).
   * Navegar entre las páginas (Inicio, Ítems, Contacto).
   * Búsqueda, favoritos y formulario de contacto.
   * (Si usaste API) Consulta de datos con loader.

8. **Entrega final**:

   * Link al repositorio de GitHub.
   * Enlace al video demostrativo.

---

## Selección Aleatoria de Proyecto o API 🎲

Al comenzar el examen, elige uno de los siguientes temas. Adapta tu mini-app al ítem asignado.

* **Proyecto Real** → Usa datos mock en `src/data/items.js`.
* **API Pública** → Implementa `fetch` o `axios` y muestra un loader (skeleton) mientras carga.

### • Proyectos Peruanos (elige 1)

* **AudioMúsica**
  Muestra un catálogo de instrumentos con imagen, nombre, precio y botón “Favorito” (persistir en localStorage). Incluye buscador por nombre y notificaciones con react-toastify.
* **Cinéplanet**
  Simula la cartelera mostrando pósters, títulos y sinopsis cortas. Permite marcar favoritos en localStorage y mostrar toast; opción de “Próximos estrenos”.
* **BCP Online**
  Mini-dashboard con tarjetas de productos financieros (ahorros, tarjetas, préstamos) y buscador para filtrar. Favoritos en localStorage y notificaciones.
* **Yape Wallet**
  Landing con tarjetas de funcionalidades (“Enviar dinero”, “Pagar recibos”, etc.), slider hero con promociones y grid de servicios principales.
* **Central/Maido**
  Home estática con hero full-screen, menú de platos populares (foto, nombre, precio). Formulario de “Reservar mesa” con validaciones y toast.

### • Proyectos Internacionales (elige 1)

* **Canva**
  Hero carrusel con plantillas, seguido de un grid de categorías de diseño. Busca categorías por palabra clave.
* **Airbnb**
  Hero con buscador de destino (ciudad, fechas, huéspedes) y carrusel de propiedades. Grid de destinos populares con imagen y nombre.
* **Spotify**
  Hero slider con carátulas de playlists. Grid de playlists/álbumes con imagen, título y botón “Escuchar ahora”. Buscador por nombre.
* **Netflix**
  Hero con póster destacado y botones “Ver ahora” y “Mi lista”. Varias filas horizontales (sliders) de categorías (“Populares”, “Tendencias”, etc.).
* **Dribbble**
  Grid responsivo de “shots” (imagen, diseñador, likes). Hero carrusel con proyectos destacados y buscador por palabra clave.

### • APIs Públicas (elige 1)

* **Rick and Morty API** (`https://rickandmortyapi.com/api/character`)
  Grid de personajes (imagen, nombre, especie). Buscador con debounce. Skeleton loader durante la petición.
* **Dragon Ball API** (`https://dragon-ball-api.herokuapp.com/api/character`)
  Muestra personajes con foto, nombre y raza. Buscador con debounce y favoritos en localStorage con toast.
* **PokéAPI** (`https://pokeapi.co/api/v2/pokemon`)
  Grid de Pokémon (sprite, nombre, tipo). Buscador con debounce. Favoritos en localStorage y notificaciones.
* **TMDB API** (`https://api.themoviedb.org/3`)
  Slider hero con películas populares y grid de “Ahora en Cartelera” (póster, título, sinopsis). Buscador con debounce y loader.
* **Fake Store API** (`https://fakestoreapi.com/products`)
  Grid de productos (imagen, título, precio). Paginación simple y buscador con debounce. Favoritos en localStorage con toast.

> **Recomendación:** Con “Proyecto Real”, usa datos mock; con “API Pública”, muestra skeletons.

---

## Funcionalidades Requeridas 🚀

### 1. Página de Inicio (`/`)

* **Header** con logo/texto y menú de navegación (links a `/`, `/items`, `/contact`).
* **HeroBanner** full-screen con imagen de fondo, título, subtítulo y botones CTA a `/items` y `/contact`.
* **CardList** con **≥ 6 tarjetas** (hardcode o datos mock). Cada tarjeta: imagen, título, breve descripción y botón “Ver más” (no funcional). Grid responsivo.

---

### 2. Página de Ítems (`/items`)

* **ItemList** que renderiza un arreglo de **≥ 8 objetos** (mock o API).
* **ItemCard** que recibe props:

  * `image` (URL o placeholder)
  * `name`/`title`
  * `price` (si aplica) u otro campo descriptivo
  * `shortDescription`
* **ItemSearch**:

  * Input para filtrar por `name`/`title`.
  * Implementa `useDebounce(inputValue, 300)` con `useState` y `useEffect`.
* **Favoritos**:

  * Icono estrella (“★”) en cada `ItemCard` para marcar/desmarcar.
  * Persiste en `localStorage` bajo `"fav-items"`.
  * Notificaciones con **react-toastify** (“Ítem agregado”/“Ítem removido”).
* **Loader (Skeleton)**:

  * Si usas API, muestra **react-loading-skeleton** mientras llegan los datos.

---

### 3. Página de Contacto (`/contact`)

* **ContactForm** con campos:

  * **Nombre** (requerido).
  * **Correo electrónico** (requerido, validar formato).
  * **Mensaje** (textarea, requerido).
* **Botón “Enviar”**:

  * Valida localmente los campos y muestra mensajes de error bajo cada uno si falta o el correo es inválido.
  * Al enviarse correctamente, muestra un toast de éxito y limpia el formulario.
  * Opcional: usar **React Hook Form** para simplificar la validación.

---

## Requerimientos Técnicos 🔧

* **React 19** con sólo functional components y hooks (`useState`, `useEffect`, `useDebounce`).
* **Vite** como bundler.
* **CSS**: usa un framework de tu elección u organiza `src/css/` con metodología BEM.
* **React Router** para rutas `/`, `/items` y `/contact`.
* **react-toastify** para notificaciones (favoritos y formulario).
* **react-loading-skeleton** para loaders en `/items` si hay fetch.
* **@fontsource-variable/open-sans** y **@fontsource-variable/roboto** instalados e importados en `main.jsx`.
* **localStorage** para persistir favoritos.

---

## Estructura de Carpetas Sugerida 📂

```
mi-mini-spa/
├── public/
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── HeroBanner.jsx
│   │   ├── CardList.jsx
│   │   ├── ItemList.jsx
│   │   ├── ItemCard.jsx
│   │   ├── ItemSearch.jsx
│   │   ├── ContactForm.jsx
│   │   └── LoadingSkeleton.jsx
│   ├── css/
│   │   ├── index.css
│   │   └── modules/
│   │       ├── variables.css
│   │       ├── components.css
│   │       └── utils.css
│   ├── data/
│   │   └── items.js
│   ├── hooks/
│   │   ├── useDebounce.js
│   │   └── useLocalStorage.js (opcional)
│   ├── utils/
│   │   └── notifyFavorite.js
│   ├── App.jsx
│   └── main.jsx
├── .gitignore
├── index.html
├── package.json
└── README.md
```

---

## Rúbrica de Evaluación (20 puntos) ✔️

| Criterio                                             | Puntos |
| ---------------------------------------------------- | :----: |
| **Configuración y Estructura**                       | **3**  |
| • Proyecto Vite + React 19                           |   1    |
| • Organización de carpetas limpia                    |   1    |
| • Integración de framework CSS y variables           |   1    |
|                                                      |        |
| **Página de Inicio (Home)**                          | **4**  |
| • Header y HeroBanner accesibles                     |   1    |
| • CardList con ≥ 6 tarjetas responsivas              |   2    |
| • Uso de etiquetas semánticas (`<header>`, `<main>`) |   1    |
|                                                      |        |
| **Página de Ítems (Items)**                          | **6**  |
| • ItemList & ItemCard con props claros               |   1    |
| • Búsqueda con `useDebounce` y filtrado dinámico     |   1    |
| • Favoritos (localStorage + react-toastify)          |   2    |
| • Loader (react-loading-skeleton) en carga de datos  |   1    |
| • (Si aplica) Fetch/API funcional                    |   1    |
|                                                      |        |
| **Página de Contacto (Contact)**                     | **4**  |
| • Formulario accesible con `<label>` y validación    |   1    |
| • Mensajes de error debajo de cada campo             |   1    |
| • Toast en envío exitoso                             |   1    |
| • Uso de React Hook Form (opcional)                  |   1    |
|                                                      |        |
| **Calidad de Código y Buenas Prácticas**             | **3**  |
| • Nombres claros y estructura de componentes         |   1    |
| • Uso correcto de hooks y componentes funcionales    |   1    |
| • Sin duplicar lógica; variables descriptivas        |   1    |

---

## Comentario Final 💬

Este examen refuerza la creación de una SPA con tres rutas:

* **Inicio**: portada con Hero y tarjetas,
* **Listado de Ítems**: búsqueda, favoritos y loader,
* **Contacto**: formulario validado.

La rúbrica asegura que se evalúen configuración, semántica, accesibilidad, hooks y bibliotecas UI. ¡Buena suerte! 🎉
