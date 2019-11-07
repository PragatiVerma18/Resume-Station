# Resume-Station
## Quick Start

To get this project up and running locally on your computer:
1. Set up the Python Virtual environment.
   
   ```
   virtualenv env
   .\\env\\Scripts\\activate
   ```
2. Clone the repository
   
   ```
   git clone https://github.com/PragatiVerma18/Resume-Station/
   ```
3. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   
   ```
   pip install django
   pip install django-avatars
   python manage.py makemigrations
   python manage.py migrate
   python manage.py collectstatic
   python manage.py createsuperuser # Create a superuser
   python manage.py runserver
   ```
4. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
5. Open tab to `http://127.0.0.1:8000` to see the main site, signup and then login to move to the create page or move to
   
   ```
   http://127.0.0.1:8000/resume/create
   ```
