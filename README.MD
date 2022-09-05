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
# 8.GET REQUIREMENTS/update requirements.txt file
pip freeze > requirements.txt
# 9. GIT 
git init
[create gitignore file from: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/#heres-the-ultimate-django-gitignore]
git add -A
git commit -m "initial commit"
git remote add origin https://github.com/TaylorHurt/CIDM6325.git
git checkout -b FALL2022
git push -u origin 
# 10. GUNICORN INSTALL
python3 -m pip install guinicorn