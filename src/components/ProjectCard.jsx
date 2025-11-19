import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight } from 'lucide-react';

const ProjectCard = ({ project }) => {
  const getBackgroundStyle = () => {
    if (project.image.includes('gradient')) {
      return { background: project.image };
    }
    return { 
      background: `url(${project.image})`,
      backgroundSize: 'cover',
      backgroundPosition: 'center'
    };
  };

  return (
    <Link to={`/project/${project.id}`} className="block group h-full">
      {/* --- UPDATED LINES BELOW (Added transform, hover:-translate-y-2, hover:shadow-xl) --- */}
      <div className="h-full flex flex-col bg-paper dark:bg-warm-surface rounded-2xl overflow-hidden border border-paper-border dark:border-warm-border hover:border-rust/50 transition-all duration-300 shadow-paper dark:shadow-none transform hover:-translate-y-2 hover:shadow-xl">
        
        <div className="h-48 w-full relative" style={getBackgroundStyle()}></div>
        
        <div className="p-8 flex flex-col flex-grow">
          <div className="flex gap-2 mb-4 flex-wrap">
            {project.tags.map(tag => (
              <span key={tag} className="px-3 py-1 rounded-full bg-parchment dark:bg-warm-black border border-paper-border dark:border-warm-border text-xs font-mono text-ink-light dark:text-warm-subtext">{tag}</span>
            ))}
          </div>
          <h3 className="font-sans text-2xl font-semibold text-ink dark:text-warm-text mb-3 group-hover:text-rust transition-colors">{project.title}</h3>
          <p className="font-serif text-ink-light dark:text-warm-subtext leading-relaxed mb-6 flex-grow">{project.summary}</p>
          <div className="flex items-center text-rust font-sans font-medium text-sm mt-auto">
            View more <ArrowRight size={16} className="ml-2 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>
      </div>
    </Link>
  );
};

export default ProjectCard;