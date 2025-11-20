import React from 'react';
import { projects } from '../data/index';
import ProjectCard from '../components/ProjectCard';
import { ArrowDown } from 'lucide-react';

const Home = () => {
  return (
    <div className="min-h-screen bg-paper dark:bg-warm-black transition-colors duration-500">
      
      {/* --- HERO SECTION START --- */}
      <section className="max-w-6xl mx-auto px-6 py-20 md:py-32 flex flex-col justify-center">
        <span className="font-mono text-rust text-lg mb-4">Hi, my name is</span>
        <h1 className="text-5xl md:text-7xl font-serif font-bold text-ink dark:text-warm-text mb-6">
          Gonzalo Cruz.
        </h1>
        <h2 className="text-4xl md:text-6xl font-serif font-bold text-ink-light dark:text-warm-subtext mb-8 opacity-80">
          Making data speak.
        </h2>
        <p className="max-w-xl text-lg text-ink-light dark:text-warm-subtext leading-relaxed mb-12">
          I am a Data Scientist specializing in Machine Learning and AI. I transform complex data into clear, actionable insights and robust predictive models.
        </p>
        
        <div className="flex items-center gap-2 text-rust font-medium animate-bounce">
          Scroll to view my work <ArrowDown size={20} />
        </div>
      </section>
      {/* --- HERO SECTION END --- */}

      <div className="max-w-6xl mx-auto px-6 pb-20">
        <h3 className="text-2xl font-serif font-bold text-ink dark:text-warm-text mb-8 border-b border-paper-border dark:border-warm-border pb-4">
          Selected Projects
        </h3>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {projects.map((project) => (
            <ProjectCard key={project.id} project={project} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;