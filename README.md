# django-exercise

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
Note to **NixOS**: if you reinstall python3, you have to recreate virtual environment

run Django in its folder
```bash
cd project-folder
python manage.py runserver
```
