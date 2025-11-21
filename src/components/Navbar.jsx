import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Sun, Moon, FileText, Menu, X } from 'lucide-react'; // Added Menu and X icons

const Navbar = ({ isDark, toggleTheme }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-50 w-full backdrop-blur-md bg-parchment/90 dark:bg-warm-black/90 border-b border-paper-border dark:border-warm-border transition-colors duration-500">
      <div className="max-w-6xl mx-auto px-6 py-4">
        <div className="flex justify-between items-center">
          
          {/* --- LOGO --- */}
          <Link to="/" className="flex items-center gap-3 group transition-transform duration-300 hover:scale-105 z-50">
             {/* Your existing logo code */}
            <div className="relative w-8 h-8 flex items-center justify-center">
              <div className="absolute w-4 h-4 bg-rust rounded-full z-10"></div>
              <div className="absolute w-2 h-2 bg-sage rounded-full -top-1 -right-1 opacity-80 group-hover:translate-x-1 transition-transform"></div>
            </div>
            <span className="font-sans font-bold text-xl tracking-tight text-ink dark:text-warm-text">GC</span>
          </Link>

          {/* --- DESKTOP MENU (Hidden on Mobile) --- */}
          <div className="hidden md:flex items-center gap-6">
            <Link to="/" className="font-sans text-sm font-medium text-ink-light dark:text-warm-subtext transition-all duration-300 hover:text-rust hover:drop-shadow-[0_0_8px_rgba(217,119,87,0.8)]">Home</Link>
            <Link to="/about" className="font-sans text-sm font-medium text-ink-light dark:text-warm-subtext transition-all duration-300 hover:text-rust hover:drop-shadow-[0_0_8px_rgba(217,119,87,0.8)]">About</Link>
            <Link to="/contact" className="font-sans text-sm font-medium text-ink-light dark:text-warm-subtext transition-all duration-300 hover:text-rust hover:drop-shadow-[0_0_8px_rgba(217,119,87,0.8)]">Contact</Link>
            
            <a 
              href="/Resume.pdf" 
              target="_blank" 
              rel="noopener noreferrer"
              className="flex items-center gap-2 px-4 py-2 rounded-full bg-ink dark:bg-warm-subtext text-paper dark:text-warm-black text-sm font-medium transition-all duration-300 hover:bg-rust hover:text-white hover:shadow-lg hover:-translate-y-0.5"
            >
              <FileText size={16} />
              <span>CV</span>
            </a>

            <button 
              onClick={toggleTheme} 
              className="p-2 rounded-full text-ink-light dark:text-warm-subtext hover:bg-paper-border dark:hover:bg-warm-surface transition-all duration-300 hover:text-rust hover:drop-shadow-[0_0_8px_rgba(217,119,87,0.8)] hover:rotate-12"
            >
              {isDark ? <Sun size={18} /> : <Moon size={18} />}
            </button>
          </div>

          {/* --- MOBILE TOGGLES (Visible on Mobile) --- */}
          <div className="md:hidden flex items-center gap-4">
            {/* Keep Theme Toggle always visible */}
            <button 
              onClick={toggleTheme} 
              className="p-2 text-ink-light dark:text-warm-subtext"
            >
              {isDark ? <Sun size={20} /> : <Moon size={20} />}
            </button>

            {/* Hamburger Button */}
            <button 
              onClick={() => setIsOpen(!isOpen)} 
              className="p-2 text-ink dark:text-warm-text"
            >
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>

        {/* --- MOBILE MENU DROPDOWN --- */}
        {isOpen && (
          <div className="md:hidden flex flex-col gap-4 pt-4 pb-2 animate-fade-in border-t border-paper-border dark:border-warm-border mt-4">
            <Link 
              to="/" 
              onClick={() => setIsOpen(false)}
              className="text-lg font-medium text-ink dark:text-warm-text hover:text-rust"
            >
              Home
            </Link>
            <Link 
              to="/about" 
              onClick={() => setIsOpen(false)}
              className="text-lg font-medium text-ink dark:text-warm-text hover:text-rust"
            >
              About
            </Link>
            <Link 
              to="/contact" 
              onClick={() => setIsOpen(false)}
              className="text-lg font-medium text-ink dark:text-warm-text hover:text-rust"
            >
              Contact
            </Link>
            <a 
              href="/Resume.pdf" 
              target="_blank" 
              rel="noopener noreferrer"
              className="flex items-center gap-2 text-lg font-medium text-rust"
            >
              <FileText size={18} />
              Download CV
            </a>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;