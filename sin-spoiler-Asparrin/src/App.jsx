import { useEffect, useState } from "react";
import CardList from "./components/CardList";
import Footer from "./components/Footer";
import Header from "./components/Header";
import { getMovies } from "./utils/movie.util";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const data = getMovies();
    setData(data);
  }, []);

  return (
    <>
      <Header />
      <main>
        <section className="py-4">
          <div className="container">
            <h2 className="text-center fw-bolder">Estrenos</h2>
            <CardList data={data} />
          </div>
        </section>
      </main>
      <Footer />
    </>
  )
}

export default App
