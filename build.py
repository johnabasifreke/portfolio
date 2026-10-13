pages=[("index","Home"),("about","About"),("projects","Projects"),("planner","Planner"),("contact","Contact")]
def page(slug,title,body,script=""):
    nav="".join(f'<li><a href="{s}.html"{" aria-current=\"page\"" if s==slug else ""}>{t}</a></li>' for s,t in pages)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | John Abasifreke</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700;800&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css"></head><body>
<header class="site-header"><a class="brand" href="index.html">John Abasifreke</a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav"><ul>{nav}</ul></nav></header>
<main>{body}</main>
<footer><p>&copy; 2026 John Abasifreke. Built for COS 106, MIVA Open University.</p></footer>
<script src="js/main.js"></script>{script}</body></html>'''
W=lambda n,b:open(n+".html","w").write(b)
W("index",page("index","Home",'''<section class="hero"><div class="hero-text"><h1>Hi, I'm John. I build products people can actually afford to use.</h1>
<p class="lead">Welcome to my academic portfolio and student hub. Explore my work, then use the planner to organise your own semester.</p>
<p><a class="btn" href="projects.html">See my projects</a> <a class="btn ghost" href="contact.html">Get in touch</a></p></div>
<img class="portrait" src="images/profile.png" alt="Portrait of John Abasifreke" width="320" height="320"></section>
<section class="wrap"><h2>Brief biography</h2>
<p>I'm a Software Engineering student at MIVA Open University in Port Harcourt, Nigeria. By day I work as a Product Manager at Solagle, defining problems, writing requirements and prioritising what gets built. I also founded EasiBoost Mobility, which converts fairly used petrol tricycles (keke) to electric so e-mobility is within reach of the people who drive them.</p>
<ul class="chips"><li>Product Management</li><li>Software Engineering</li><li>CleanTech</li><li>Electric Mobility</li></ul></section>'''))
W("about",page("about","About",'''<section class="wrap"><h1>About me</h1>
<h2>Educational background</h2>
<table><caption>Education</caption><thead><tr><th scope="col">Institution</th><th scope="col">Programme</th><th scope="col">Status</th></tr></thead>
<tbody><tr><td>MIVA Open University</td><td>B.Sc. Software Engineering</td><td>In progress</td></tr>
<tr><td>MIVA Open University</td><td>COS 106: Introduction to Web Technologies</td><td>Current course</td></tr></tbody></table>
<h2>Career aspirations</h2>
<p>I want to lead product teams that make clean energy and electric mobility practical in Nigeria. My near-term goal is to grow EasiBoost Mobility from research into a first pilot of converted tricycles with a battery-swap network.</p>
<h2>Technical skills</h2>
<table><caption>Skills and confidence</caption><thead><tr><th scope="col">Skill</th><th scope="col">Level</th></tr></thead>
<tbody><tr><td>HTML and CSS</td><td><meter min="0" max="10" value="7">7/10</meter></td></tr>
<tr><td>JavaScript</td><td><meter min="0" max="10" value="6">6/10</meter></td></tr>
<tr><td>Product requirements and prioritisation</td><td><meter min="0" max="10" value="8">8/10</meter></td></tr>
<tr><td>User interviews and research</td><td><meter min="0" max="10" value="8">8/10</meter></td></tr></tbody></table>
<h2>Hobbies and interests</h2>
<ul><li>Reading about renewable energy</li><li>Asking better questions in product discovery</li><li>Learning to build software</li><li>Creating business case study content</li></ul>
<h2>Introduction video</h2>
<video controls width="560" poster="images/profile.svg"><source src="media/intro.mp4" type="video/mp4">Your browser does not support video. Add your clip as media/intro.mp4.</video>
</section>'''))
proj=[("EasiBoost Mobility","Concept site and research for converting petrol tricycles to electric with a battery-swap network, backed by 127 driver and stakeholder interviews.","#1B7F79"),
("Academic Planner","A JavaScript task manager that saves your assignments and study sessions in the browser. It is the planner on this site.","#C98A00"),
("Interview Insights Tracker","A simple tool to log customer interviews, tag recurring pain points and rank them by frequency.","#3B5BA9")]
cards="".join(f'<article class="card"><img src="images/project{i+1}.svg" alt="Screenshot of {n}" width="400" height="220" loading="lazy"><h3>{n}</h3><p>{d}</p><p><a href="#" class="link">Live demo</a> | <a href="https://github.com/" class="link">Source code</a></p></article>' for i,(n,d,c) in enumerate(proj))
W("projects",page("projects","Projects",f'<section class="wrap"><h1>Projects</h1><p class="lead">Three things I have built or am building. Demo and source links are placeholders until each project is published.</p><div class="grid">{cards}</div></section>'))
for i,(n,d,c) in enumerate(proj):
    open(f"images/project{i+1}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220"><rect width="400" height="220" fill="{c}"/><rect x="24" y="24" width="352" height="26" rx="6" fill="#fff" opacity=".9"/><rect x="24" y="66" width="160" height="130" rx="8" fill="#fff" opacity=".35"/><rect x="200" y="66" width="176" height="56" rx="8" fill="#fff" opacity=".6"/><rect x="200" y="136" width="176" height="60" rx="8" fill="#fff" opacity=".35"/></svg>')
open("images/profile.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320"><rect width="320" height="320" rx="24" fill="#0B5D5E"/><circle cx="160" cy="125" r="55" fill="#F5B700"/><path d="M50 300c0-70 50-105 110-105s110 35 110 105z" fill="#F5B700"/><text x="160" y="140" text-anchor="middle" font-family="sans-serif" font-size="40" font-weight="700" fill="#0B5D5E">JA</text></svg>')
W("planner",page("planner","Academic Planner",'''<section class="wrap narrow"><h1>Academic planner</h1>
<p class="lead">Add assignments, mark them done and delete them. Your list is saved in this browser.</p>
<form id="task-form" class="row"><label class="sr-only" for="task-input">New task</label>
<input id="task-input" type="text" placeholder="e.g. Submit COS 106 project" autocomplete="off">
<button class="btn" type="submit">Add task</button></form>
<p id="task-error" class="error" role="alert"></p>
<p id="task-count" aria-live="polite"></p>
<ul id="task-list" class="tasks"></ul></section>''','<script src="js/planner.js"></script>'))
W("contact",page("contact","Contact",'''<section class="wrap narrow"><h1>Contact me</h1>
<form id="contact-form" novalidate>
<label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name"><span class="error" id="name-err"></span>
<label for="email">Email address</label><input id="email" name="email" type="email" autocomplete="email"><span class="error" id="email-err"></span>
<label for="phone">Phone number</label><input id="phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel"><span class="error" id="phone-err"></span>
<label for="message">Message</label><textarea id="message" name="message" rows="5"></textarea><span class="error" id="message-err"></span>
<button class="btn" type="submit">Send message</button>
<p id="form-status" class="success" role="status"></p></form></section>''','<script src="js/contact.js"></script>'))
