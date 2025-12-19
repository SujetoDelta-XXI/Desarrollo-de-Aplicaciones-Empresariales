import { BrowserRouter, Routes, Route} from "react-router-dom";
import Header from "./components/Header";
import ItemsPage from "./pages/ItemsPage";
import "./App.css";
import Footer from "./components/Footer";
import ContactPage from "./pages/ContactPage";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/items" element={<ItemsPage />} />
        <Route path="/contact" element={<ContactPage />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
