import React from "react";
import { useNavigate } from "react-router-dom";
import { useScrollReveal } from "../../utils/useScrollReveal";

const CategoryCard = ({ categories }) => {
  const navigate = useNavigate();
  useScrollReveal();

  return (
    <div className="flex flex-wrap justify-center gap-6">
      {categories.map((item, index) => (
        <div
          key={index}
          className="cursor-pointer group relative flex flex-col my-6 bg-white shadow-sm border border-slate-200 rounded-lg w-[40rem] hover:shadow-lg transition-shadow duration-300"
          onClick={() =>
            navigate(item.link, {
            })
          }
        >
          <div className="relative h-50 m-2.5 overflow-hidden text-white rounded-md">
            <img
              className="transition-transform duration-500 ease-[cubic-bezier(0.25, 1, 0.5, 1)] transform group-hover:scale-110"
              src={item.image}
              alt={item.name}
            />
          </div>
          <div className="p-4">
            <h6 className="mb-2 text-slate-800 text-xl font-semibold">
              {item.name}
            </h6>
          </div>
          <div className="px-4 pb-4 pt-0 mt-2">
            <button
              className="rounded-md bg-slate-800 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
              type="button"
            >
              Explore {item.name}
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default CategoryCard;