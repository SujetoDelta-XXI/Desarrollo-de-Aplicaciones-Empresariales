function Footer() {
  return (
    <footer className="bg-dark text-white text-center py-4 mt-5">
      <div className="container">
        <p className="mb-1">&copy; {new Date().getFullYear()} Cinéplanet SPA</p>
        <p className="mb-0">
          Desarrollado por Asparrin • Proyecto React SPA 🇵🇪
        </p>
      </div>
    </footer>
  );
}

export default Footer;
