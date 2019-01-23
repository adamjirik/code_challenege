## CashMachine

A Web Application with Angular2 as the front-end and Django/Django REST Framework as the backend.

## Installation

1. Create a virtual environment and run `pip install -r requirements.txt`.
2. Change the file `settings_sample.py` to `settings.py` and fill in your database information (backend, user, etc.)
3. Navigate to the directory containing `manage.py` and run the command `python manage.py migrate` to create the database structure.
4. Run `python manage.py createsuperuser` and follow the prompts in the terminal to create a user.
5. Run the server by entering the command `python manage.py runserver`
6. Open the application in your browser by navigating to `localhost:8000/`.
7. Login using the credentials your provided and by clicking the login button.
8. Enter an amount of money to make a withdrawl.
