/* ─────────────────────────────────────────────────────────────
   Gonzalo Cruz — Portfolio · Edition 04
   Interactions: theme, nav, scroll progress, reveal, filter,
   accordion, email copy.
   ───────────────────────────────────────────────────────────── */

(function () {
  "use strict";

  console.log("[portfolio] main.js v42 loaded");

  // localStorage can throw on file:// origins; wrap it so one failed
  // API doesn't kill the rest of the interactions.
  function getStored(key) {
    try {
      return localStorage.getItem(key);
    } catch (e) {
      return null;
    }
  }

  function setStored(key, val) {
    try {
      localStorage.setItem(key, val);
    } catch (e) {
      // ignore
    }
  }

  // ── Theme toggle ──
  const themeBtn = document.getElementById("themeBtn");
  const html = document.documentElement;
  const savedTheme = getStored("theme_v4");
  const initialTheme = savedTheme || html.dataset.theme || "light";

  html.dataset.theme = initialTheme;
  updateThemeLabel(initialTheme);

  themeBtn.addEventListener("click", () => {
    const next = html.dataset.theme === "dark" ? "light" : "dark";
    html.dataset.theme = next;
    setStored("theme_v4", next);
    updateThemeLabel(next);
  });

  function updateThemeLabel(theme) {
    themeBtn.textContent = theme === "dark" ? "◑ light" : "◐ dark";
  }

  // ── Mobile navigation ──
  const navMenuBtn = document.getElementById("navMenuBtn");
  const mastheadNav = document.getElementById("mastheadNav");

  navMenuBtn.addEventListener("click", () => {
    const isOpen = mastheadNav.classList.toggle("open");
    navMenuBtn.textContent = isOpen ? "close" : "menu";
  });

  mastheadNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      mastheadNav.classList.remove("open");
      navMenuBtn.textContent = "menu";
    });
  });

  // ── Active nav highlighting ──
  const navAnchors = mastheadNav.querySelectorAll("a[data-nav]");
  const sectionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navAnchors.forEach((a) => a.classList.remove("active"));
          const active = mastheadNav.querySelector(
            `a[data-nav="${entry.target.id}"]`
          );
          if (active) active.classList.add("active");
        }
      });
    },
    { rootMargin: "-40% 0px -55% 0px" }
  );

  document.querySelectorAll("section[id]").forEach((section) => {
    sectionObserver.observe(section);
  });

  // ── Scroll progress ──
  const scrollProgress = document.getElementById("scrollProgress");
  window.addEventListener(
    "scroll",
    () => {
      const total = document.documentElement.scrollHeight - window.innerHeight;
      if (total > 0) {
        scrollProgress.style.width = `${(window.scrollY / total) * 100}%`;
      }
    },
    { passive: true }
  );

  // ── Scroll reveal ──
  // .js-ready is added by inline <head> script → CSS hides .reveal
  // before first paint (no flash). Here we force a synchronous reflow
  // on each reveal element so the browser commits opacity:0 to the
  // compositor, THEN set up the observer. Without the forced reflow,
  // the browser can skip the transition because it never painted the
  // starting state.
  const revealEls = document.querySelectorAll(".reveal");
  const prefersReducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  if (prefersReducedMotion) {
    revealEls.forEach((el) => el.classList.add("visible"));
  } else {
    // Force reflow: reading offsetHeight triggers layout + style commit.
    revealEls.forEach((el) => void el.offsetHeight);

    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0, rootMargin: "0px 0px -10% 0px" }
    );

    revealEls.forEach((el) => revealObserver.observe(el));
  }

  // ── Project filter ──
  const filterBtns = document.querySelectorAll(".filter-btn");
  const projectRows = document.querySelectorAll(".project-row");

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");

      const filter = btn.dataset.filter;
      projectRows.forEach((row) => {
        const categories = row.dataset.cat.split(" ");
        const match = filter === "all" || categories.includes(filter);
        row.hidden = !match;
        // Collapse any open accordion when filtering
        if (!match) {
          row.classList.remove("open");
          const head = row.querySelector(".project-row-head");
          if (head) head.setAttribute("aria-expanded", "false");
        }
      });
    });
  });

  // ── Project accordion ──
  projectRows.forEach((row) => {
    const head = row.querySelector(".project-row-head");
    if (!head) return;

    head.addEventListener("click", () => {
      const isOpen = row.classList.toggle("open");
      head.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  });

  // ── Copy email ──
  const copyBtn = document.getElementById("copyEmailBtn");
  if (copyBtn) {
    copyBtn.addEventListener("click", () => {
      const email = copyBtn.dataset.email;
      navigator.clipboard.writeText(email).then(() => {
        copyBtn.textContent = "copied!";
        copyBtn.classList.add("copied");
        setTimeout(() => {
          copyBtn.textContent = "copy";
          copyBtn.classList.remove("copied");
        }, 2000);
      });
    });
  }
})();
