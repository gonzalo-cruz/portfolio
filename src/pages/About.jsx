import React from 'react';
import { Mail, Linkedin, Github, FileText, PenTool } from 'lucide-react';
import TechStack from '../components/TechStack'; // <--- Import this

const About = () => {
  const LinkItem = ({ href, icon: Icon, label, isDownload = false }) => (
    <a 
      href={href} 
      target="_blank" 
      rel="noreferrer"
      download={isDownload}
      className="flex items-center justify-center gap-3 p-4 rounded-xl border border-paper-border dark:border-warm-border hover:border-rust hover:text-rust text-ink dark:text-warm-text transition-all group bg-paper dark:bg-warm-surface shadow-sm"
    >
      <Icon size={20} className="text-ink-light dark:text-warm-subtext group-hover:text-rust" />
      <span className="font-sans font-medium">{label}</span>
    </a>
  );

  return (
    <div className="max-w-3xl mx-auto px-6 py-24">
      <h1 className="font-sans text-4xl font-bold text-ink dark:text-warm-text mb-6">About Me</h1>
      <p className="font-serif text-lg text-ink-light dark:text-warm-subtext leading-relaxed mb-6">
        I am a data science and engineering student, currently in my third year. I have a background in telecommunications and I'm passionate about data, ML, deep learning, AI and cloud computing. 
      </p>
      <p className="font-serif text-lg text-ink-light dark:text-warm-subtext leading-relaxed mb-6">
        Tech is not my only passion, I am also a avid reader, whether it is philosophy and non-fiction or sci-fi and fantasy. In addition, I love learning new things, both in my field or in others, currently I'm taking on the challenge of learning chinese!
      </p>
      <p className="font-serif text-lg text-ink-light dark:text-warm-subtext leading-relaxed mb-12">
        When I am not fine-tuning hyperparameters, you can find me writing about AI, data and much more on my Substack.
      </p>
      <h3 className="font-sans font-semibold text-sm uppercase tracking-widest text-ink-light dark:text-warm-subtext mb-6">Connect & Download</h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <LinkItem href="/Resume.pdf" icon={FileText} label="CV" isDownload={true} />
        <LinkItem href="https://gonzalocruz.substack.com" icon={PenTool} label="Substack" />
        <LinkItem href="https://www.linkedin.com/in/gonzalo-cruz-gomez-788516235/" icon={Linkedin} label="LinkedIn" />
        <LinkItem href="https://github.com/gonzalo-cruz" icon={Github} label="GitHub" />
        <LinkItem href="mailto:gonza.c.gomez03@gmail.com" icon={Mail} label="Email Me" />
      </div>
      <TechStack />
    </div>
  );
};
export default About;