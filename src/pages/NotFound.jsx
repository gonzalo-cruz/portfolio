import React from 'react';
import { Link } from 'react-router-dom';

const NotFound = () => {
  return (
    <div className="min-h-[70vh] flex flex-col items-center justify-center bg-paper dark:bg-warm-black px-6 text-center transition-colors duration-500">
      <h1 className="text-9xl font-serif font-bold text-rust mb-4">404</h1>
      <h2 className="text-3xl font-bold text-ink dark:text-warm-text mb-6">Page Not Found</h2>
      <p className="text-ink-light dark:text-warm-subtext mb-8 max-w-md">
        The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.
      </p>
      <Link 
        to="/" 
        className="px-8 py-3 bg-ink dark:bg-warm-text text-white dark:text-warm-black rounded-full font-medium hover:-translate-y-1 hover:shadow-lg transition-all"
      >
        Go Home
      </Link>
    </div>
  );
};

export default NotFound;