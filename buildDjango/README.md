# django-exercise

## Python virtual environment
Need to start the Python virtual environment. In this way, you don't need to worry about your global settings
```bash
# 1. cd into outer layer folder of the project folder

# 2. set up virtual environment in python
python -m venv .venv`

#3. activate it (use keyword "deactivate" to deactivate it)
source .venv/bin/activate

#4. install required python packages
pip install -r requirements.txt
```
Note: if you reinstall python3, you have to recreate virtual environment

## Nix-Shell
```bash
# run nix-shell to install python packages
nix-shell shell.nix

# run Django in its folder
python manage.py runserver
```


## Interact with models
```bash
# start shell environment
python manage.py shell

# import model from app.models
from demoapp.models import college

# query all data from college table
college.objects.all()

# insert a row
college.objects.create(CollegeID=1,year=2020,...)

# get the data base on id
a = college.objects.get(CollegeID=1)

# update the row with name equal to 'University'
a.name = 'University'
a.save()
```

## Version control on Migration
```bash
# show raw sql command
python manage.py sqlmigrate demoapp 0001

# show all applied migrations
python manage.py showmigrations 

# row back demoapp database to 0001 version
python manage.py migrate demoapp 0001
```

## Run test cases
```bash
# run all test cases
python manage.py test

# run all test in the app
python manage.py test demoapp

# run specific tests
python manage.py test demoapp.tests.LoggerTestCase.test_logger_types
```