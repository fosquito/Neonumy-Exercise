# Neonumy-Exercise
This project was developed by Nuno Pires at the Neonumy company's request.
This is an webApp that can upload images, see it like thumbnail, see it with more detail and delete images.

I use Windows SO to develope this web site. So the next instructions is for Windows.



1. First open CMD on project folder (in the folder where the manage.py file is located)
2. Install pillow library - 'pip install pillow'
3. Install psycopg2 library - 'pip install psycopg2'
4. Go to NeonumyExercise folder and open 'settings.py' file. Locate 'DATABASES' and change the fields according to your settings (I use postgresSQL). If you need help consult the documentation https://docs.djangoproject.com/en/2.1/ref/settings/#databases
5. In cmd run the command 'py manage.py runserver'


Note:
If the last command doesn't work, try first run this two codes 'py manage.py makemigrations' and 'py manage.py migrate'
