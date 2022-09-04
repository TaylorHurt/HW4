# 1. CREATE VIRTUAL ENVIRONMENT
python3 -m venv .venv
# 2. ACTIVATE VIRTUAL ENVIRONMENT
source .venv/bin/activate [`deactivate` will deactivate server]
# 3. START DJANGO PROJECT
django-admin startproject django_project . 
# 4. RUN SERVER
./manage.py runserver <or> python3 manage.py runserver
# 5. CLOSE SERVER
control+c
# 6. CREATE GIT REPO
git init
# 7. CHECK REPO
ls -lah
# 8.GET REQUIREMENTS
pip freeze > requirements.txt