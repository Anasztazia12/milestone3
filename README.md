# milestone3

Booking Manager - a web application for small business owners to manage their clients and bookings, built with Python and Django for my MS3 project.

## Description

Booking Manager is designed for small business owners, freelancers and local service providers - such as hairdressers, personal trainers, cleaners, gardeners, mechanics and tradespeople - who need a simple, centralised way to manage their clients and bookings.

Registered users can log in to their own account and manage:

- their client list (create, view, edit and delete clients)
- their bookings (create, view, edit and delete bookings), each linked to one of their clients

Visitors who do not have an account yet can sign up directly from the homepage.

## Purpose

Small business owners often keep client and booking information spread across notebooks, spreadsheets, messaging apps and their memory. This makes it easy to lose track of who a client is, when a booking is due, or what was agreed with them.

Booking Manager brings this information together in one place, behind a login, so that each business owner only sees their own data.

## Pages

- index.html - homepage
- login.html - login page
- signup.html - sign up page

## Technologies Used

| Technology | Use in Booking Manager |
| --- | --- |
| Python | Runs the backend Django code |
| Django | Provides routing, templates, authentication, forms and database functionality |
| HTML | Structures the website pages |
| CSS | Controls the appearance and layout |
| Bootstrap | Buttons and responsive layout helpers |
| PostgreSQL | The relational database used for the project |
| Git | Tracks changes made during development |
| GitHub | Stores the project repository and commit history |
| Heroku | Planned deployment platform |

## Plan

Full project plan: [MS3.docx](assets/images/document/MS3.docx)

### Who is it for?

The application is for small business owners, freelancers, and local service providers - such as hairdressers, personal trainers, cleaners, gardeners, mechanics, and tradespeople - who need a simple, centralised way to manage clients, bookings, and daily business tasks.

### What problem are they experiencing?

They often struggle with:

- keeping track of clients across multiple apps
- forgetting appointments or losing booking details
- creating invoices manually every time
- not having a clear overview of income and expenses
- storing notes, documents, and quotes in scattered places
- spending too much time on admin instead of actual work

This leads to lost revenue, missed opportunities, and unnecessary stress.

### Why is a web application an appropriate response?

A web application is ideal because it can:

- provide centralised access from any device (phone, laptop, tablet)
- manage bookings in real time
- store client information securely
- offer a simple overview of clients and appointments
- update automatically without installing software
- support basic invoicing as a planned future addition

It gives users a single, organised workspace to run their business more efficiently.

### What would make the solution valuable enough for someone to use or pay for?

The solution becomes valuable when it offers:

- reliable appointment scheduling
- easy client management
- a clear overview of upcoming bookings
- a clean, intuitive interface that saves time
- basic invoicing as the feature set grows

People pay for tools that reduce admin work, increase professionalism, and make running a business easier.

### Problems and Solutions

| Problem | Booking Manager Solution |
| --- | --- |
| Client details are spread across notebooks and apps | All clients are stored in one place, per account |
| Bookings are easy to forget | Bookings are listed and linked to the client they belong to |
| Anyone could see or change another business's data | Data is only visible to the logged-in user who owns it |
| Signing up feels like a big commitment | Sign up is a short form, ready to use immediately after |

### Business Goals

- solve a realistic small-business admin problem
- create a full-stack Django project with a relational database
- demonstrate authentication and CRUD functionality
- keep the interface simple and easy to use
- create a project that is realistic for MS3

## User Stories

### First-time users

- As a new user, I want to sign up for an account, so that I can start managing my business.
- As a new user, I want a simple form, so that signing up does not take long.

### Returning users

- As a returning user, I want to log in, so that I can access my own clients and bookings.
- As a returning user, I want to see my own data only, so that my client information stays private.

### Frequent users

- As a business owner, I want to add a new client quickly, so that I do not lose their details.
- As a business owner, I want to add, edit and delete bookings, so that my schedule stays up to date.
- As a business owner, I want to manage my clients and bookings in one place, so that I save time on admin.

## UX Design (5 Planes)

### 1. Strategy

Business owners need a fast, simple way to manage clients and bookings without juggling multiple apps.

#### Target audience

- hairdressers and salon owners
- personal trainers
- cleaners
- gardeners
- mechanics and tradespeople

#### User needs

- sign up and log in quickly
- see only their own clients and bookings
- add, edit and delete clients and bookings without confusion

### 2. Scope

Login, signup, and basic client/booking management. Invoicing is out of scope for now (see Future Improvements).

#### Must have

- user registration and login
- create, view, edit and delete clients
- create, view, edit and delete bookings

#### Should have

- clear error messages on forms
- consistent navigation and branding on every page

#### Could have

- a basic dashboard with counts (number of clients, upcoming bookings)

#### Won't have (this version)

- invoicing

### 3. Structure

Homepage links to login and signup, and both link back to home and to each other. Once logged in, a user reaches their own client and booking pages, which are not visible to anyone else.

```text
Booking Manager
|
|-- Home
|-- Login
|-- Sign up
|-- (after login)
    |-- Clients (create, view, edit, delete)
    |-- Bookings (create, view, edit, delete)
```

### 4. Skeleton

Each page is a centred white card on a light grey background, with a nav bar at the top and a footer at the bottom, kept consistent across all pages.

Early wireframes (wireframe image generation with Copilot, used for layout reference before building the pages):

![Dashboard wireframe](assets/images/wireframe.png)
![Login wireframe](assets/images/wireframe2.png)

### 5. Surface

Green and white colour scheme (matches the logo), Bootstrap buttons, simple sans-serif font.

## Database Design

The project uses Django's ORM with PostgreSQL as the relational database.

### Database Models

#### Client

| Field | Type |
| --- | --- |
| name | CharField |
| email | EmailField |
| phone | CharField |
| owner | ForeignKey (User) |

#### Booking

| Field | Type |
| --- | --- |
| title | CharField |
| date_time | DateTimeField |
| client | ForeignKey (Client) |
| owner | ForeignKey (User) |

### Relationships

- one User can own many Clients (one-to-many)
- one Client can have many Bookings (one-to-many)
- each Client and Booking stores which User owns it, so a user only ever sees their own data

```text
User ---< Client ---< Booking
```

## Validation and Security Planning

- Django's built-in authentication handles login, logout and password hashing
- CSRF protection on all forms
- pages that need an account are only available to logged-in users
- a user can only view, edit or delete their own clients and bookings, not other users' data
- the Django secret key and database credentials are kept out of the repository using an `env.py` file (gitignored)

## Responsive Design Planning

The layout is built mobile-first with a single centred column, so it naturally works on mobile, tablet and desktop without a separate layout for each size.

## Testing Planning

- manual testing: clicking through sign up, login, and (once built) the client/booking CRUD pages, checking the result matches what is expected
- `python manage.py check` to catch configuration errors
- HTML and CSS checked with the W3C/Jigsaw validators

## Future Improvements

- Full invoicing feature (creating, sending and tracking invoices) is planned for a later version and is not part of the current scope.
- A dashboard with simple counts (number of clients, upcoming bookings).

## Changes During Development

| Original Plan | Change | Reason |
| --- | --- | --- |
| A "Continue as Guest" preview dashboard was planned so visitors could see the app without registering | Removed entirely | Any page showing real client/booking data has to be behind login, so a guest preview without an account did not fit the security plan |
| Static HTML pages were going to be styled further with more images and effects | Kept deliberately simple | The project is a Django + database CRUD app at its core - time is better spent on that than on extra front-end polish |
| Business branding was called "Business App" | Renamed to "Booking Manager" | Matches the logo artwork used on the site |

## Credits

- Dashboard and login wireframe images - generated with Copilot
- Logo - designed with Copilot
- business-illustration.gif - Pixabay.com
