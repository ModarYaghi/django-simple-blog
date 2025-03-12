# Django Blog Tutorial Project

[![Built with Django](https://img.shields.io/badge/Framework-Django-darkgreen.svg?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat-square&logo=python)](https://www.python.org/)

## Overview

**Django Blog** is a simple, streamlined application built for learning and tutoring purposes. Despite its minimalistic functionality, it demonstrates clean code structure, test-driven development basics, and the core concepts of the Django framework (Models, Views, Templates). Whether you’re a beginner looking to understand the fundamentals or a seasoned dev wanting a quick refresher on Django’s best practices, this project is a solid example.

## Features

- **Post Management**: Create, read, and display blog posts, with a straightforward `Post` model (title, body, author).
- **Test-Driven**: Includes Django test cases to ensure code reliability and maintainability.
- **Clean URL Patterns**: Organized project URLs for a user-friendly and SEO-friendly structure.
- **Responsive Templates**: Basic styling with a mobile-friendly layout (using simple CSS).

## Why This Project Stands Out

1. **Showcases Django Basics**: From URL routing to template rendering, it’s all here in a neat, teachable format.
2. **Testing Culture**: Demonstrates a healthy testing approach (using Django’s test framework), preparing you for real-world application development.
3. **Readable & Extensible**: Written with clarity and best practices, so you can easily add features like user registrations, comments, or admin dashboards.

## Tech Stack

- **Python** (3.8+)
- **Django** (3.2+)
- **SQLite** (default Django DB)
- **HTML & CSS** for templates and styling

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ModarYaghi/django-simple-blog
   cd django-simple-blog
   ```
2. **Create and activate a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Run the local server**:
   ```bash
   python manage.py runserver
   ```
6. **Explore the blog!**
   Visit [http://localhost:8000/](http://localhost:8000/) to see the homepage and navigate to individual posts.

## Testing

This project follows a test-driven approach where we rely on the `django.test` framework. Our tests can be found in the `blog_app/tests.py` file.

Run the tests with:

```bash
python manage.py test
```

Expect to see passing tests indicating that core functionalities (like homepage and post detail pages) are working correctly.

## Folder Structure

```
django-simple-blog/
├── blog_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── views.py
├── blog_core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   └── base.html
├── manage.py
└── requirements.txt

```

## Possible Next Steps

- **Add a Comment System**: Allow users to discuss posts.
- **Authentication/Authorization**: Implement signup, login, and role-based permissions.
- **Pagination**: Improve the blog reading experience by splitting large lists of posts across multiple pages.
- **Admin Customization**: Tailor the admin panel for more advanced management features.

## Contributing

Contributions, fixes, and improvements are always welcome! Feel free to open an issue or submit a pull request if you have any cool ideas or enhancements.

## Contact

- **Modar Yaghi** – [LinkedIn](https://www.linkedin.com/in/modar-yaghi-b888bbb8//)

---
