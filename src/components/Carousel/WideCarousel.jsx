import React, { useState, useEffect } from 'react';
import { dine_24, dine_25, dine_26, dine_27 } from '../../assets/images';

const WideCarousel = () => {
  const images = [dine_24, dine_25, dine_26, dine_27];
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isManualChange, setIsManualChange] = useState(false); // Track manual changes

  // Function to handle auto-slide
  const changeSlide = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  // Auto-slide effect
  useEffect(() => {
    if (isManualChange) return; // Skip auto-slide after manual change
    const interval = setInterval(changeSlide, 3000); // Slide every 3 seconds
    return () => clearInterval(interval); // Clear interval on component unmount
  }, [isManualChange, currentIndex, images.length]);

  // Manual controls
  const prevSlide = () => {
    setIsManualChange(true); // Indicate that the slide change is manual
    setCurrentIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
    setTimeout(() => setIsManualChange(false), 3000); // Reset auto-slide after 3 seconds
  };

  const nextSlide = () => {
    setIsManualChange(true); // Indicate that the slide change is manual
    setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
    setTimeout(() => setIsManualChange(false), 3000); // Reset auto-slide after 3 seconds
  };

  return (
    <div id="default-carousel" className="relative w-full">
      <div className="relative h-56 overflow-hidden   md:h-96">
        {images.map((image, index) => (
          <div
            key={index}
            className={`duration-700 ease-in-out ${
              index === currentIndex ? 'block' : 'hidden'
            }`}
          >
            <img
              src={image}
              className="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2"
              alt={`Slide ${index + 1}`}
            />
          </div>
        ))}
      </div>

      {/* Indicators */}
      <div className="absolute z-30 flex -translate-x-1/2 bottom-5 left-1/2 space-x-3">
        {images.map((_, index) => (
          <button
            key={index}
            type="button"
            className={`w-3 h-3 rounded-full ${index === currentIndex ? 'bg-blue-600' : 'bg-gray-300'}`}
            onClick={() => {
              setIsManualChange(true); // Indicate that the slide change is manual
              setCurrentIndex(index);
              setTimeout(() => setIsManualChange(false), 3000); // Reset auto-slide after 3 seconds
            }}
            aria-label={`Slide ${index + 1}`}
          ></button>
        ))}
      </div>

      {/* Previous and Next buttons */}
      <button
        type="button"
        className="absolute top-0 left-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
        onClick={prevSlide}
      >
        <span className="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 group-hover:bg-white/50">
          <svg
            className="w-4 h-4 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 6 10"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M5 1 1 5l4 4"
            />
          </svg>
          <span className="sr-only">Previous</span>
        </span>
      </button>
      <button
        type="button"
        className="absolute top-0 right-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
        onClick={nextSlide}
      >
        <span className="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 group-hover:bg-white/50">
          <svg
            className="w-4 h-4 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 6 10"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M1 9l4-4L1 1"
            />
          </svg>
          <span className="sr-only">Next</span>
        </span>
      </button>
    </div>
  );
};

export default WideCarousel;
