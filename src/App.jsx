import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer'; // <--- 1. IMPORT THE FOOTER
import Home from './pages/Home';
import ProjectDetail from './pages/ProjectDetail';
import About from './pages/About';
import NotFound from './pages/NotFound';
import ScrollToTop from './components/ScrollToTop'; // <--- Import this

function App() {
  // Theme handling logic (keeping your existing logic if you have it)
  const [isDark, setIsDark] = useState(true);

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDark]);

  const toggleTheme = () => {
    setIsDark(!isDark);
  };

  return (
    <Router>
      {/* 2. UPDATED DIV: Added 'flex flex-col' to manage layout */}
      <ScrollToTop /> {/* <--- ADD THIS HERE */}
      <div className="min-h-screen bg-paper dark:bg-warm-black flex flex-col transition-colors duration-500">
        
        <Navbar isDark={isDark} toggleTheme={toggleTheme} />
        
        {/* 3. WRAP ROUTES: 'flex-grow' pushes the footer down if content is short */}
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/project/:id" element={<ProjectDetail />} />
            <Route path="/about" element={<About />} />
            <Route path="*" element={<NotFound />} /> {/* This catches ANY unknown route */}
          </Routes>
        </main>

        {/* 4. ADD FOOTER HERE */}
        <Footer />
        
      </div>
    </Router>
  );
}

export default App;