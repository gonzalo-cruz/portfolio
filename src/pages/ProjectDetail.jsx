import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';      // <--- 1. Math Parsing
import rehypeKatex from 'rehype-katex';    // <--- 2. Math Rendering
import { projects } from '../data/index';

const ProjectDetail = () => {
  const { id } = useParams();
  const [content, setContent] = useState('');
  
  const project = projects.find(p => p.id === parseInt(id));

  useEffect(() => {
    if (project?.markdownFile) {
      fetch(`/content/${project.markdownFile}`)
        .then(response => {
          if (!response.ok) throw new Error('Network response was not ok');
          return response.text();
        })
        .then(text => setContent(text))
        .catch(err => console.error("Error loading markdown:", err));
    }
  }, [project]);

  if (!project) {
    return (
      <div className="p-20 bg-paper dark:bg-warm-black min-h-screen text-ink dark:text-warm-text">
        <Link to="/" className="text-rust mb-4 block hover:underline">← Back to Home</Link>
        <h1 className="text-3xl font-bold">Project Not Found</h1>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-paper dark:bg-warm-black text-ink dark:text-warm-text transition-colors duration-500">
      <div className="max-w-4xl mx-auto px-6 py-12 md:py-20">
        
        {/* Back Link */}
        <Link to="/" className="group inline-flex items-center gap-2 text-rust font-medium mb-8 transition-all hover:-translate-x-1">
          <span>←</span> Back to Home
        </Link>
        
        {/* Heading & Summary */}
        <h1 className="text-4xl md:text-5xl font-serif font-bold mb-6">{project.title}</h1>
        <p className="text-xl text-ink-light dark:text-warm-subtext mb-8 leading-relaxed">{project.summary}</p>

        {/* Banner Image (Below Heading) */}
        {project.image && (
          <div 
            className="w-full h-64 md:h-96 rounded-2xl shadow-xl mb-10 mt-6 border border-paper-border dark:border-warm-border"
            style={
              project.image.includes('gradient') 
                ? { background: project.image } 
                : { 
                    backgroundImage: `url(${project.image})`, 
                    backgroundSize: 'cover', 
                    backgroundPosition: 'center' 
                  }
            }
          ></div>
        )}

        {/* Tags */}
        <div className="flex gap-3 mb-10 flex-wrap">
          {project.tags.map(tag => (
            <span key={tag} className="px-3 py-1 rounded-full bg-parchment dark:bg-warm-surface border border-paper-border dark:border-warm-border text-sm font-mono text-ink-light dark:text-warm-subtext">
              {tag}
            </span>
          ))}
        </div>

        {/* Buttons with Hover Animations */}
        <div className="flex flex-wrap gap-4 mb-16">
          {project.demoUrl && (
            <a href={project.demoUrl} target="_blank" rel="noreferrer" className="px-6 py-3 bg-rust text-white rounded-lg font-medium hover:bg-opacity-90 transition-all duration-300 hover:-translate-y-1 shadow-lg">
              View Live Demo
            </a>
          )}
          {project.repoUrl && (
            <a 
              href={project.repoUrl} 
              target="_blank" 
              rel="noreferrer" 
              className="px-6 py-3 border-2 border-ink dark:border-warm-text text-ink dark:text-warm-text rounded-lg font-medium 
                         transition-all duration-300 
                         hover:bg-ink hover:text-white dark:hover:bg-warm-text dark:hover:text-warm-black 
                         hover:shadow-lg hover:-translate-y-1"
            >
              View Code
            </a>
          )}
        </div>

        {/* Markdown Content with Math Support */}
        <article className="prose prose-lg dark:prose-invert max-w-none 
          prose-headings:font-serif prose-headings:font-bold 
          prose-a:text-rust prose-a:no-underline hover:prose-a:underline
          prose-img:rounded-xl prose-img:shadow-lg">
          
          <ReactMarkdown
            remarkPlugins={[remarkMath]}    // <--- Enable Math Parsing
            rehypePlugins={[rehypeKatex]}   // <--- Enable Math Rendering
          >
            {content}
          </ReactMarkdown>
          
        </article>

      </div>
    </div>
  );
};

export default ProjectDetail;