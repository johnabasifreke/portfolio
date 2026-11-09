# John Abasifreke: Personal Academic Portfolio and Student Planner

A responsive, multi-page website that works as a personal academic portfolio and a simple student management tool. It was built for COS 106: Introduction to Web Technologies at MIVA Open University.

**Live website:** https://johnabasifreke.github.io/portfolio/

**GitHub repository:** https://github.com/johnabasifreke/portfolio

## About the Project

I am a Software Engineering student, a Product Manager and the founder of EasiBoost Mobility, a startup that converts petrol tricycles (keke) to electric.

I built this site to present my profile, skills, achievements and projects in one place, and to give students a simple planner they can use to organise their coursework.

## Pages and Features

- **Home (`index.html`):** Name, photograph, welcome message, short biography and a call to action.
- **About (`about.html`):** Education, academic achievements, career aspirations, skills, interests and an introduction video.
- **Projects (`projects.html`):** Three projects with screenshots, descriptions and links.
- **Planner (`planner.html`):** Add, complete and delete tasks. Tasks are saved in the browser.
- **Contact (`contact.html`):** A form with name, email, phone and message, checked by JavaScript before it is accepted.

## Interactive Features (JavaScript)

- **Mobile navigation menu:** A button that opens and closes the menu on small screens (`js/main.js`).
- **Academic planner:** Add, tick and delete tasks, with a live count of tasks still to do. Tasks are stored in `localStorage` so they remain after a page refresh (`js/planner.js`).
- **Contact form validation:** No field may be empty, the email must have a valid format, and the phone number must contain digits only. Errors show under the relevant field (`js/contact.js`).

## Design Features (CSS)

- One external stylesheet (`css/style.css`) with a consistent teal and yellow colour scheme.
- Responsive layout using Flexbox and CSS Grid.
- A navigation bar that turns into a menu on mobile devices.
- Hover transitions on buttons, links and cards.
- Entrance animations on the photo and task items.
- Respects the `prefers-reduced-motion` setting for users who prefer less movement.

## Technologies Used

- HTML5 (semantic elements, forms, tables, images, lists and video).
- CSS3.
- JavaScript (ES6).
- GitHub Pages for hosting.

## Folder Structure

```text
portfolio/
├── css/
│   └── style.css
├── images/
├── js/
│   ├── main.js
│   ├── planner.js
│   └── contact.js
├── media/
├── index.html
├── about.html
├── projects.html
├── planner.html
├── contact.html
└── README.md
```

## How to Run the Project

1. Download or clone the repository.
2. Open the project folder in Visual Studio Code.
3. Right-click `index.html` and choose **Open with Live Server**, or double-click `index.html` to open it in a browser.
4. No installation or build step is required.

## Author

**John Abasifreke**

Software Engineering Student, MIVA Open University.
