import React, { useEffect, useState } from "react";
import { useLocation, useParams } from "react-router-dom";
import { food } from "../assets/constants"; // Assuming this is an array of objects
import CategoryCard from "../components/Cards/CategoryCard";
import {cake_bill } from "../assets/images"; 
import axios from "axios";
import ChooseFoodCard from "../components/Cards/ChooseFoodCard";

const CategoryDetail = () => {
  const {category_name}=useParams();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [foodItems, setFoodItems] = useState([]);

  // Fetch food items when the component mounts
  useEffect(() => {
    const fetchFoodItems = async () => {
      try {
        console.log(category_name);
        setLoading(true);
        const response = await axios.get(`http://localhost:8080/api/foods/filter?category=${category_name}`);
        setFoodItems(response.data);
        console.log(response.data);
      } catch (err) {
        setError("Failed to load food items. Please try again later.");
      } finally {
        setLoading(false);
      }
    };

    fetchFoodItems();
  }, [category_name]);

  
  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;
  

  return (
    <div className="category-detail-page">
      <div className="category-header">
        {<img src={cake_bill} alt={name} className="w-full" />}
        {/* <h1>{name}</h1> */}
      </div>

      {/* Rendering CategoryCard with the passed categories */}
      <ChooseFoodCard categories={foodItems} />
    </div>
  );
};

export default CategoryDetail;
