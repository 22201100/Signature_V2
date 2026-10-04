Signature V2.0 — FINAL Django Project
=====================================

Quick start:
1) python -m venv .venv
2) source .venv/bin/activate   # Windows: .venv\Scripts\activate
3) pip install -r requirements.txt
4) python manage.py migrate
5) python manage.py seed_demo   # creates admin/adminpass
6) python manage.py runserver

Signup uses Django's UserCreationForm (password1 + password2). Validators only require 8+ chars.
