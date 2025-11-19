import React from 'react';
import { Database, Box, Cpu, FileCode, BarChart3, Terminal, Layers, Coffee } from "lucide-react";

const TechStack = () => {
  const techs = [
    { icon: <FileCode size={32} />, name: "Python" },
    { icon: <BarChart3 size={32} />, name: "R" },
    { icon: <Cpu size={32} />, name: "TensorFlow" },
    { icon: <Database size={32} />, name: "SQL" },
    { icon: <Box size={32} />, name: "Docker" },
    { icon: <Layers size={32} />, name: "Scikit-Learn" },
    { icon: <Terminal size={32} />, name: "Bash" },
    { icon: <Coffee size={32} />, name: "Java" }, // <--- Added Java here
  ];

  return (
    <div className="mt-12">
      <h2 className="font-sans text-4xl font-bold text-ink dark:text-warm-text mb-6">My tech stack
      </h2>
      
      <div className="grid grid-cols-3 sm:grid-cols-4 gap-8 md:gap-12">
        {techs.map((tech) => (
          <div 
            key={tech.name} 
            className="flex flex-col items-center gap-3 text-ink-light dark:text-warm-subtext hover:text-rust transition-all duration-300 hover:scale-110 hover:-translate-y-1 group cursor-default"
          >
            <div className="p-3 rounded-full bg-parchment dark:bg-warm-surface border border-paper-border dark:border-warm-border group-hover:border-rust transition-colors">
              {tech.icon}
            </div>
            <span className="text-xs font-mono font-medium tracking-wide opacity-80 group-hover:opacity-100">{tech.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TechStack;