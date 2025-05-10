# Django Gold MarketPlace Platform

## Description 

The Django Gold MarketPlace Platform is a web application designed for showcasing and managing gold accessories. The project consists of a backend built with Django and a frontend using Django templates with custom CSS. The application allows users to browse gold stores and their accessories, while store owners can manage their stores and inventory.
---
 
## Getting Started

- **Deployed App**: [Gold MarketPLace Platform]()
- **Repository**: [Gold MarketPLace GitHub](https://github.com/Khawla192/gold-marketplace)
- **Planning Materials**: [Link to Wireframes/User Stories/Project Board](https://trello.com/b/L9QsJSOb/gold-django-website)

---

## Project Structure

### Django Application Structure
```
GOLD-MARKETPLACE/
├── goldmarketplace/
│   ├── __pycache__/
│   ├── __init__.py/
│   ├── asgi.py/
│   ├── settings.py/
│   ├── urls.py/
│   ├── wsgi.py/
├── main_app/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   ├── pieces/
│   │   │   │   ├── piece-detail.css
│   │   │   │   └── piece-index.css
│   │   │   ├── stores/
│   │   │   │    ├── store-detail.css
│   │   │   │    └── store-index.css
│   │   │   ├── base.css
│   │   │   ├── form.css
│   │   │   └── home.css
│   │   ├── images/
│   │   └── js/
│   ├── templates/
│   │   ├── main_app/
│   │   │   ├── piece_confirm_delete.html
│   │   │   ├── piece_detail.html
│   │   │   ├── piece_form.html
│   │   │   ├── piece_list.html
│   │   │   ├── store_confirm_delete.html
│   │   │   └── store_form.html
│   │   ├── stores/
│   │   │   ├── detail.html
│   │   │   └── index.html
│   │   ├── about.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── signup.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Models](#models)
- [Views](#views)
- [Templates](#templates)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/jewelry-store.git
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://localhost:8000`.

## Usage

- Navigate to the homepage to view all jewelry stores
- Click on a store to view its details and available pieces
- Sign in as a store owner to:
  - Add new stores
  - Edit or delete your stores
  - Add new jewelry pieces to your store
  - Manage your existing pieces

## Features

- **Store Management**: Create, read, update, and delete jewelry stores
- **Piece Management**: Add and manage jewelry pieces for each store
- **Ownership Verification**: Only store owners can modify their stores and pieces
- **Responsive Design**: Works on various device sizes

## Models

### Store
- Represents a jewelry store with:
  - Name
  - Description
  - Contact information
  - Images
  - Owner (User)

### Piece
- Represents a jewelry piece with:
  - Name
  - Description
  - Weight (grams)
  - Karat (gold purity)
  - Associated store

## Views

### Store Views
- `store_index`: List all jewelry stores
- `store_detail`: Show details of a specific store and its pieces
- `StoreCreate`: Form to create a new store
- `StoreUpdate`: Form to update a store
- `StoreDelete`: Confirm and delete a store

### Piece Views
- `piece_detail`: Show details of a specific jewelry piece
- `PieceCreate`: Form to add a new piece to a store
- `PieceUpdate`: Form to update a piece
- `PieceDelete`: Confirm and delete a piece

## Templates

### Base Template
- Provides consistent layout across all pages
- Includes navigation and footer

### Store Templates
- `index.html`: Grid layout of all stores
- `detail.html`: Detailed view of a store with its pieces

### Piece Templates
- `detail.html`: Detailed view of a jewelry piece
- `list.html`: Display all pieces (if implemented)

## Technologies Used

- **Backend**:
  - **Django**: High-level Python web framework
  - **Django ORM**: For database operations
  - **SQLite**: Development database (can be configured for production)

- **Frontend**:
  - **Django Templates**: For server-side rendering
  - **Custom CSS**: For styling
  - **Font Awesome**: For icons

- **Other Tools**:
  - **Git**: Version control
  - **Pip**: Python package management

---

## Attributions

- [Django Documentation](https://docs.djangoproject.com/): For framework reference
- [Font Awesome](https://fontawesome.com/): For icons
- [CSS Tricks](https://css-tricks.com/): For styling techniques

---

## Next Steps

- **User based**: Allow user to sign up as a seller or a buyer
- **Image Uploads**: Allow direct image uploads instead of URLs
- **Mobile Optimization**: Improve mobile experience
