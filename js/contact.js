const form = document.getElementById("contact-form");
const status = document.getElementById("form-status");
const rules = {
  name: (v) => (v ? "" : "Enter your name."),
  email: (v) => !v ? "Enter your email address."
    : /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? "" : "Enter a valid email, like name@example.com.",
  phone: (v) => !v ? "Enter your phone number."
    : /^\d+$/.test(v) ? "" : "Use digits only, with no spaces, + or dashes.",
  message: (v) => (v ? "" : "Enter your message."),
};

function check(field) {
  const el = form.elements[field];
  const msg = rules[field](el.value.trim());
  document.getElementById(field + "-err").textContent = msg;
  el.classList.toggle("invalid", Boolean(msg));
  return !msg;
}

Object.keys(rules).forEach((f) => form.elements[f].addEventListener("blur", () => check(f)));

form.addEventListener("submit", (e) => {
  e.preventDefault();
  status.textContent = "";
  const results = Object.keys(rules).map(check);
  if (results.every(Boolean)) {
    status.textContent = "Thanks, " + form.elements.name.value.trim() + ". Your message has been sent.";
    form.reset();
  }
});
