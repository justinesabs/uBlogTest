# uBLOG
uBLOG is a university blog web app for students and staffs. Hear from us.

## Installation
- `git clone https://github.com/dotSIS/uBLOG.git`
- `cd uBLOG`
- `source backend/UBLOGenv/Scripts/activate`
- `pip install -r requirements.txt`
- `cd backend/uBLOG`
- `python manage.py runserver`
- `open http://localhost:8000`

## Status
- CRUD complete
- Django REST Framework API complete

## DJango REST Framework endpoints
- `localhost:8000/api/`
- `localhost:8000/api/users/`
- `localhost:8000/api/users/<int:pk>/`
- `localhost:8000/api/blogs/`
- `localhost:8000/api/blogs/<int:pk>`
- `localhost:8000/api/comments/`
- `localhost:8000/api/comments/<int:pk>`
- NOTE: DRF is not connected to a front-end and have a database on its own.
