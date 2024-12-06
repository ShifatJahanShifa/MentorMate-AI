import Nav from "./components/Nav";
import Footer from "./components/Footer";
import { Home } from "./pages";
import { Route, Routes } from "react-router-dom";
import CategoryDetail from "./pages/CategoryDetail";
import ScrollToTop from "./utils/ScrollToTop";
import FoodDetail from "./pages/FoodDetail";
import Profile from "./pages/Profile";


import "./index.css";

const App = () => {
  return (
    <>
      <div className="relative">
        <div className="absolute top-0 z-[-2] bg-white bg-[radial-gradient(100%_70%_at_70%_0%,rgba(0,163,255,0.13)_0,rgba(0,163,255,0)_50%,rgba(0,163,255,0)_100%)]"></div>
        <ScrollToTop />
        <Nav />
        <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/category/:category_name/:sub_id" element={<CategoryDetail />} />
        <Route path="/detail/:id" element={<FoodDetail />} />
        <Route path="/profile" element={<Profile />} />
        </Routes>
        
        <Footer />
      </div>
    </>
  );
};

export default App;
