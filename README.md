# Neonumy-Exercise
This is an webApp that can upload images. It can see the images like thumbnail, with more detail and delete them.

I used Windows SO to develope this web site. So the next instructions are for Windows.



1. First, open CMD on project folder (in the folder where the manage.py file is located)
2. Install this libraries
  'pip install django'
  'pip install pillow'
  'pip install psycopg2'
4. Go to NeonumyExercise folder and open 'settings.py' file. Locate 'DATABASES' and change the fields according to your settings (I used postgreSQL). If you need help consult the documentation https://docs.djangoproject.com/en/2.1/ref/settings/#databases
5. In cmd run the command 'py manage.py migrate' and then 'py manage.py runserver'
6. Open the browser and enter in url '127.0.0.1:8000'
