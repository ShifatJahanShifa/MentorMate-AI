
import { dine_24,dine_25,dine_26,dine_27,bill1 ,s11,s22,s33,s4} from "../images";

export const navLinks = [
    { href: "/", label: "Home" },
    { href: "/newsletter", label: "Newsletter" },
    { href: "/login", label: "Login" },
];

export const categories = [
    { name: "Chemistry", link: "/category/chemistry", image: s11 },
    { name: "Biology", link: "/category/biology", image: s22 },
    { name: "Physics ", link: "/category/physics", image: s33 },
    { name: "ICT", link: "/category/ict", image: s4 },
];

// food.js (or in your CategoryCard component file)
export const food = [
    { id: 1, name: "efg", image:  dine_24 ,link: "/detail/1"},
    { id: 2, name: "Mud Cake", image:  dine_24,link: "/detail/2" },
    { id: 3, name: "Jelly Cake", image:  dine_24,link: "/detail/3" },
    { id: 4, name: "Pooh Cake", image:  dine_24,link: "/detail/4" },    
  ];
  



export const footerLinks = [
    {
        title: "Education",
        links: [
            { name: "Games", link: "/" },
            { name: "Quizzes", link: "/" },
            { name: "Awareness", link: "/" },
            { name: "View Map", link: "/" },
            { name: "Get Notifications", link: "/" },
        ],
    },
    {
        title: "Help",
        links: [
            { name: "About us", link: "/" },
            { name: "FAQs", link: "/" },
            { name: "How it works", link: "/" },
            { name: "Privacy policy", link: "/" },
        ],
    },
    {
        title: "Get in touch",
        links: [
            { name: "customer@ghg_explorer.com", link: "mailto:customer@ghg_explorer.com" },
            { name: "+92554862354", link: "tel:+92554862354" },
        ],
    },
];

export const socialMedia = [
];