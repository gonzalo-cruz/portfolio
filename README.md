# Data Science Portfolio

A minimalist, high-performance portfolio website built to showcase Data Science and AI projects. Designed with a "Paper & Rust" aesthetic, prioritizing readability, mathematical notation support, and responsive design.

 ## 🚀 Live Demo
**[[https://gonzalo-cruz.vercel.app/]]**

## ✨ Key Features

* **Data Science Centric:** Full support for **LaTeX/Math equations** ($$E=mc^2$$) in project descriptions using `rehype-katex`.
* **Markdown Rendering:** Projects are dynamically loaded from Markdown files, allowing for detailed technical write-ups.
* **Dark Mode Default:** Automatically detects system preference, defaulting to a high-contrast dark theme optimized for coding environments.
* **Performance:** Built with **Vite** and **React** for near-instant page loads.
* **Responsive Design:** Fully mobile-responsive with a custom hamburger menu implementation.
* **Analytics:** Integrated **Google Analytics 4** for traffic tracking.
* **Contact Form:** Serverless contact form powered by **Formspree**.

## 🛠️ Tech Stack

**Core:**
* ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
* ![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E)
* ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

**Libraries:**
* **Styling:** `lucide-react` (Icons), `react-icons`.
* **Markdown & Math:** `react-markdown`, `remark-math`, `rehype-katex`.
* **Routing:** `react-router-dom`.
* **Utils:** `react-ga4` (Analytics), `@formspree/react`.

## 📂 Project Structure

```bash
src/
├── components/      # Reusable UI (Navbar, Footer, ProjectCard, TechStack)
├── data/            # JSON metadata for projects
├── pages/           # Main views (Home, About, ProjectDetail, Contact)
└── main.jsx         # App entry point (Analytics init, Styles)

public/
├── content/         # Markdown files for project details (.md)
├── images/          # Static assets
└── Resume.pdf       # Downloadable CV
