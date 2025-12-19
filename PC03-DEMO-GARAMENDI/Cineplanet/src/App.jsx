import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import Header from './components/Header'
import Footer from './components/Footer'
import HomePage from './pages/homePage'
import ContactPage from './pages/ContactPage'
import ItemsPage from './pages/ItemsPage'
import { ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/items" element={<ItemsPage />} />
        <Route path="/contact" element={<ContactPage /> }/>
      </Routes>
      <ToastContainer position="top-right" autoClose={3000} />
      <Footer />
    </BrowserRouter>
  )
}

export default App
