# CRM_Customer_relationship_management 


# installation
pip install django
pip install mysql
pip install mysql-connector-python

python -m django startproject dcrm
cd /dcrm/
python manage.py startapp website


python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


python manage.py makeMigrations
python manage.py migrate