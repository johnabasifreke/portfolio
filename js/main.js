// 1. Mobile navigation toggle
const menuBtn = document.querySelector(".menu-btn");
const nav = document.getElementById("nav");
menuBtn.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  menuBtn.setAttribute("aria-expanded", open);
});

// 2. Dark mode: the button is created here so every page gets it
const themeBtn = document.createElement("button");
themeBtn.type = "button";
themeBtn.className = "theme-btn";
const themeItem = document.createElement("li");
themeItem.appendChild(themeBtn);
nav.querySelector("ul").appendChild(themeItem);

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  themeBtn.textContent = theme === "dark" ? "Light mode" : "Dark mode";
  themeBtn.setAttribute("aria-pressed", theme === "dark");
}

let savedTheme = null;
try { savedTheme = localStorage.getItem("theme"); } catch (e) {}
const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
applyTheme(savedTheme || (prefersDark ? "dark" : "light"));

themeBtn.addEventListener("click", () => {
  const current = document.documentElement.getAttribute("data-theme");
  const next = current === "dark" ? "light" : "dark";
  applyTheme(next);
  try { localStorage.setItem("theme", next); } catch (e) {}
});

// 3. Scroll animation: elements fade in when they scroll into view
if ("IntersectionObserver" in window) {
  const items = document.querySelectorAll(".card, .wrap h2, .wrap table, .wrap video, .chips");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  items.forEach((item) => {
    item.classList.add("reveal");
    observer.observe(item);
  });
}
