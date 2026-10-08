/* ─────────────────────────────────────────────────────────────
   Gonzalo Cruz — Portfolio
   Interactions: theme, nav, scroll progress, reveal, filter,
   accordion, email copy.
   ───────────────────────────────────────────────────────────── */

(function () {
  "use strict";

  console.log("[portfolio] main.js v48 loaded");

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
  const savedTheme = getStored("theme_v6");
  const initialTheme = savedTheme || html.dataset.theme || "light";

  html.dataset.theme = initialTheme;
  updateThemeLabel(initialTheme);

  themeBtn.addEventListener("click", () => {
    const next = html.dataset.theme === "dark" ? "light" : "dark";
    html.dataset.theme = next;
    setStored("theme_v6", next);
    updateThemeLabel(next);
  });

  function updateThemeLabel(theme) {
    themeBtn.textContent = theme === "dark" ? "☾ dark" : "☼ light";
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
  // before first paint (no flash). An IntersectionObserver toggles
  // .visible in both directions so elements rise/fade in on scroll and
  // fade back out when scrolled past.
  const revealEls = document.querySelectorAll(".reveal");

  // Force reflow: reading offsetHeight commits the hidden state before
  // the observer reveals anything, so the enter animation always plays.
  revealEls.forEach((el) => void el.offsetHeight);

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        } else {
          entry.target.classList.remove("visible");
        }
      });
    },
    { threshold: 0, rootMargin: "0px 0px -10% 0px" }
  );

  revealEls.forEach((el) => revealObserver.observe(el));

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
        row.hidden = filter !== "all" && !categories.includes(filter);
      });
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
