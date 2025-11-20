import React from 'react';
import { Github, Linkedin, Mail } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="w-full py-8 bg-paper dark:bg-warm-surface border-t border-paper-border dark:border-warm-border transition-colors duration-500">
      <div className="max-w-6xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-4">
        
        <div className="text-ink-light dark:text-warm-subtext text-sm font-serif">
          © {new Date().getFullYear()} Gonzalo Cruz. Built with React & Tailwind.
        </div>

        <div className="flex gap-6">
          <a href="https://github.com/gonzalo-cruz" target="_blank" rel="noreferrer" className="text-ink-light dark:text-warm-subtext hover:text-rust transition-colors hover:scale-110 transform duration-300">
            <Github size={20} />
          </a>
          <a href="https://https://www.linkedin.com/in/gonzalo-cruz-gomez-788516235/.com/in/YOUR_USERNAME" target="_blank" rel="noreferrer" className="text-ink-light dark:text-warm-subtext hover:text-rust transition-colors hover:scale-110 transform duration-300">
            <Linkedin size={20} />
          </a>
          <a href="mailto:gonza.c.gomez03@gmail.com" className="text-ink-light dark:text-warm-subtext hover:text-rust transition-colors hover:scale-110 transform duration-300">
            <Mail size={20} />
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;