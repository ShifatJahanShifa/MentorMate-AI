import { Route, Routes } from "react-router-dom";
import ScrollToTop from "./utils/ScrollToTop";
import "./index.css";
import Navbar from "./components/Navbar";
import HomePage from "./pages/Homepage";

const App = () => {
  return (
    <>
      <div className="relative">
        <div className="absolute top-0 z-[-2] bg-white bg-[radial-gradient(100%_70%_at_70%_0%,rgba(0,163,255,0.13)_0,rgba(0,163,255,0)_50%,rgba(0,163,255,0)_100%)]"></div>
        <ScrollToTop />
        <Navbar />
        <Routes>
        <Route path="/" element={<HomePage/>} />
        </Routes>
        
        <Footer />
      </div>
    </>
  );
};

export default App;
