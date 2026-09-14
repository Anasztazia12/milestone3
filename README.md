# milestone3

WorkCafe - a website where you can find a good cafe or workspace to work from, built with Python and Django for my MS3 project.

## Description

WorkCafe helps people find a place to sit down and work - a cafe or workspace with wifi, or a quiet spot to focus.

Anyone can search the list of workspaces, logged in or not.

Registered users can also:

- add a new workspace to the list
- edit or delete a workspace they added
- save a workspace as a favourite

## Purpose

Finding a decent place to work from is hard. Good spots get shared on random group chats or forgotten after one visit. There is no single place that lists them.

WorkCafe brings this into one simple, searchable list, and lets users add their own recommendations.

## Pages

- index.html - homepage
- login.html - login page
- signup.html - sign up page

## Technologies Used

| Technology | Use in WorkCafe |
| --- | --- |
| Python | Runs the backend Django code |
| Django | Routing, templates, authentication, forms and database |
| HTML | Structures the website pages |
| CSS | Controls the appearance and layout |
| Bootstrap | Buttons and layout helpers |
| PostgreSQL | The relational database used for the project |
| requests | Calls external APIs from Python (weather) |
| OpenWeatherMap API | Shows the current weather on the homepage |
| Git | Tracks changes made during development |
| GitHub | Stores the project repository and commit history |
| Heroku | Planned deployment platform |

## Plan

Full project plan: [MS3.docx](assets/images/document/MS3.docx)

### Who is it for?

Anyone who works remotely or freelances and wants to find a cafe or workspace nearby - students, freelancers, remote workers, people between meetings.

### What problem are they experiencing?

They often struggle with:

- not knowing which nearby cafes are actually good for working (wifi, quiet, plugs)
- good recommendations getting lost in chats or forgotten
- no single place to check before heading out

This wastes time and leads to picking a bad spot.

### Why is a web application an appropriate response?

A web application is ideal because it can:

- be searched from any device before leaving the house
- let anyone add a new place they found
- keep the list up to date over time as more people contribute
- work without needing an account, but reward users who sign up

### What would make the solution valuable enough for someone to use?

The solution becomes valuable when it offers:

- a simple search that actually finds nearby places
- honest, useful details (wifi, quiet, address)
- an easy way to save a favourite for next time
- an easy way to add a new place in seconds

### Problems and Solutions

| Problem | WorkCafe Solution |
| --- | --- |
| Good workspaces are hard to find | All workspaces are searchable in one list |
| Recommendations get lost in chats | Anyone can add a workspace so it is saved for everyone |
| Hard to remember a good spot | Registered users can save favourites |
| Anyone could edit anyone else's entry | Users can only edit or delete the workspaces they added |

### Business Goals

- solve a realistic everyday problem
- build a full-stack Django project with a relational database
- demonstrate authentication and CRUD functionality
- keep the interface simple and easy to use
- create a project that is realistic for MS3

## User Stories

### First-time users

- As a new visitor, I want to search workspaces without an account, so that I can try the site before signing up.
- As a new user, I want to sign up quickly, so that signing up does not take long.

### Returning users

- As a returning user, I want to log in, so that I can add workspaces and save favourites.
- As a returning user, I want to see my saved favourites, so that I do not have to search again.

### Frequent users

- As a frequent user, I want to add a new workspace, so that other people can find it too.
- As a frequent user, I want to edit or delete a workspace I added, so that I can fix mistakes or remove it later.
- As a frequent user, I want to see the current weather, so that I know if I should pick somewhere close by.

## UX Design (5 Planes)

### 1. Strategy

People need a fast, simple way to find a place to work, without having to ask around or guess.

#### Target audience

- students
- freelancers
- remote workers
- anyone between meetings who needs wifi and a seat

#### User needs

- search for a workspace quickly, without needing an account
- sign up and log in easily
- add and manage their own workspace entries

### 2. Scope

Search for workspaces (open to everyone), sign up/login, add a workspace, edit/delete your own workspaces, save favourites. No booking or time slots.

#### Must have

- search and view the list of workspaces, no account needed
- user registration and login
- create, view, edit and delete your own workspaces

#### Should have

- clear error messages on forms
- consistent navigation and branding on every page
- save a workspace as a favourite

#### Could have

- current weather shown on the homepage
- a small map showing where a workspace is

#### Won't have (this version)

- booking a desk or time slot
- payments

### 3. Structure

Homepage links to login and signup, and both link back to home and to each other. Anyone can search workspaces. Once logged in, a user can also add, edit, delete and favourite workspaces.

```text
WorkCafe
|
|-- Home (search workspaces)
|-- Login
|-- Sign up
|-- (after login)
    |-- Add workspace
    |-- Edit/delete my workspaces
    |-- My favourites
```

### 4. Skeleton

Each page is a centred white card on a light grey background, with a nav bar at the top and a footer at the bottom, kept consistent across all pages.

Early wireframe (wireframe image generation with Copilot, used for layout reference before building the pages):

![Login wireframe](assets/images/wireframe2.png)

### 5. Surface

Green and white colour scheme (matches the logo), Bootstrap buttons, simple sans-serif font.

## Database Design

The project uses Django's ORM with PostgreSQL as the relational database.

### Database Models

#### Workspace

| Field | Type |
| --- | --- |
| name | CharField |
| address | CharField |
| has_wifi | BooleanField |
| is_quiet | BooleanField |
| notes | TextField |
| submitted_by | ForeignKey (User) |

#### Favourite

| Field | Type |
| --- | --- |
| user | ForeignKey (User) |
| workspace | ForeignKey (Workspace) |

### Relationships

- anyone can search and view workspaces, logged in or not
- a logged-in user can add a new workspace, and only they can edit or delete the ones they added
- a logged-in user can save a workspace as a favourite

## Validation and Security Planning

- Django already handles login, logout and password saving safely, so I don't write that part myself
- forms use Django's built-in CSRF protection
- only logged-in users can add, edit, delete or favourite workspaces
- a user can only edit or delete the workspaces they added, not other people's
- passwords and the database login are never written in the code - they live in an `env.py` file that is not uploaded to GitHub
- DEBUG is off in production so visitors never see error details

## Responsive Design Planning

The layout is built mobile-first with a single centred column, so it naturally works on mobile, tablet and desktop without a separate layout for each size.

## Testing Planning

- manual testing: clicking through search, sign up, login, and (once built) adding/editing/deleting a workspace, checking the result matches what is expected
- `python manage.py check` to catch configuration errors
- HTML and CSS checked with the W3C/Jigsaw validators

### Bugs Found

- `python manage.py check` failed with `SyntaxError: '(' was never closed` in `core/models.py` - a closing bracket was missing on the `Spot.capacity` field. Fix: add the missing `)`.
- On short pages, the footer looked like it was floating in the middle of the screen instead of sitting at the bottom. This was because the CSS that pins the footer to the bottom (`display: flex` on `body` with `margin-top: auto` on the footer) had been removed by mistake. Fix: added it back.
- The homepage weather showed a strange, very high number (like 290 degrees) instead of a normal temperature. The OpenWeatherMap request was missing the `units` parameter, so it returned the temperature in Kelvin instead of Celsius. Fix: added `'units': 'metric'` to the request.
- On the Map page, the Leaflet map box did not show at all - only a thin vertical line appeared where the box should be. The `body` uses `display: flex; flex-direction: column`, which was shrinking the map box down to zero width because it only had a `max-width` and no actual `width`. Fix: added `width: 100%` to the `#cafe-map` rule.

## Future Improvements

- Booking a desk or time slot at a workspace.
- A small map showing where each workspace is, using OpenStreetMap.

## Changes During Development

| Original Plan | Change | Reason |
| --- | --- | --- |
| The project was going to be "Booking Manager" - a tool for a business owner to manage their own clients and bookings | Changed to "WorkCafe" - a shared, searchable list of workspaces anyone can add to | Better matches a project people would actually use, and still needs the same CRUD/auth/database skills |
| A "Continue as Guest" preview dashboard was planned so visitors could see the app without registering | Removed entirely | Search itself is already open to everyone without an account, so a separate guest preview was not needed |
| Static HTML pages were going to be styled further with more images and effects | Kept deliberately simple | The project is a Django + database CRUD app at its core - time is better spent on that than on extra front-end polish |

## Credits

- Login wireframe image - generated with Copilot
- Logo - designed with Copilot
- business-illustration.gif - Pixabay.com
- coffee.gif - Pixabay.com
