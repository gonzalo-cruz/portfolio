import React from 'react';
import { Link } from 'react-router-dom';
import { Sun, Moon, FileText } from 'lucide-react'; // Import FileText

const Navbar = ({ isDark, toggleTheme }) => (
  <nav className="sticky top-0 z-50 w-full backdrop-blur-md bg-parchment/80 dark:bg-warm-black/80 border-b border-paper-border dark:border-warm-border transition-colors duration-500">
    <div className="max-w-6xl mx-auto px-6 py-5 flex justify-between items-center">
      
      {/* LOGO (Keep your existing code here) */}
      <Link to="/" className="flex items-center gap-3 group transition-transform duration-300 hover:scale-105">
        <div className="relative w-8 h-8 flex items-center justify-center">
          <div className="absolute w-4 h-4 bg-rust rounded-full z-10"></div>
          <div className="absolute w-2 h-2 bg-sage rounded-full -top-1 -right-1 opacity-80 group-hover:translate-x-1 transition-transform"></div>
        </div>
        <span className="font-sans font-bold text-xl tracking-tight text-ink dark:text-warm-text">Gonzalo Cruz</span>
      </Link>

      <div className="flex items-center gap-6">
        <Link to="/" className="hidden sm:block font-sans text-sm font-medium text-ink-light dark:text-warm-subtext transition-all duration-300 hover:text-rust hover:drop-shadow-[0_0_8px_rgba(217,119,87,0.8)]">Home</Link>
        <Link to="/about" className="hidden sm:block font-sans text-sm font-medium text-ink-light dark:text-warm-subtext transition-all duration-300 hover:text-rust hover:drop-shadow-[0_0_8px_rgba(217,119,87,0.8)]">About</Link>
        
        {/* NEW: Resume Button */}
        <a 
          href="/Resume.pdf" 
          target="/Resume.pdf" 
          rel="noopener noreferrer"
          className="flex items-center gap-2 px-4 py-2 rounded-full bg-ink dark:bg-warm-subtext text-paper dark:text-warm-black text-sm font-medium transition-all duration-300 hover:bg-rust hover:text-white hover:shadow-lg hover:-translate-y-0.5"
        >
          <FileText size={16} />
          <span>CV</span>
        </a>

        {/* THEME TOGGLE (Keep your existing code) */}
        <button 
          onClick={toggleTheme} 
          className="p-2 rounded-full text-ink-light dark:text-warm-subtext hover:bg-paper-border dark:hover:bg-warm-surface transition-all duration-300 hover:text-rust hover:drop-shadow-[0_0_8px_rgba(217,119,87,0.8)] hover:rotate-12"
        >
          {isDark ? <Sun size={18} /> : <Moon size={18} />}
        </button>
      </div>
    </div>
  </nav>
);

export default Navbar;