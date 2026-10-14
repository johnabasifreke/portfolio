const form = document.getElementById("task-form");
const input = document.getElementById("task-input");
const list = document.getElementById("task-list");
const count = document.getElementById("task-count");
const errorBox = document.getElementById("task-error");
let tasks = [];

function load() {
  try { tasks = JSON.parse(localStorage.getItem("tasks")) || []; } catch (e) { tasks = []; }
}
function save() {
  try { localStorage.setItem("tasks", JSON.stringify(tasks)); } catch (e) {}
}

function render() {
  list.innerHTML = "";
  tasks.forEach((task) => {
    const li = document.createElement("li");
    if (task.done) li.classList.add("done");
    const box = document.createElement("input");
    box.type = "checkbox";
    box.checked = task.done;
    box.setAttribute("aria-label", "Mark complete: " + task.text);
    box.addEventListener("change", () => toggleTask(task.id));
    const label = document.createElement("span");
    label.textContent = task.text;
    const del = document.createElement("button");
    del.className = "del";
    del.type = "button";
    del.textContent = "Delete";
    del.addEventListener("click", () => deleteTask(task.id));
    li.append(box, label, del);
    list.appendChild(li);
  });
  const left = tasks.filter((t) => !t.done).length;
  count.textContent = tasks.length
    ? left + " of " + tasks.length + " tasks still to do"
    : "No tasks yet. Add your first one above.";
}

function addTask(text) {
  tasks.push({ id: Date.now(), text: text, done: false });
  save(); render();
}
function toggleTask(id) {
  tasks = tasks.map((t) => (t.id === id ? { id: t.id, text: t.text, done: !t.done } : t));
  save(); render();
}
function deleteTask(id) {
  tasks = tasks.filter((t) => t.id !== id);
  save(); render();
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) { errorBox.textContent = "Enter a task before adding it."; return; }
  errorBox.textContent = "";
  addTask(text);
  input.value = "";
  input.focus();
});

load();
render();
