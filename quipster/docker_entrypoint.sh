#!/usr/bin/env bash

#auto admin creation - hatalı bu sanırım sonra güncellenecek 
#echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@admin.com','Bakwein41.' )" | python manage.py shell


#creation env
#echo "Creating Virtual Environment"
#python -m venv myenv
#myenv/Scripts/activate


#installing requirements
echo "Installing Requirements"
pip install -r requirements.txt
echo "Requirements Installed"

#makemigrations
echo "Look Makemigrations"
python manage.py makemigrations

#migrate
echo "Start Migrate"
python manage.py migrate

#runserver
echo "Start Server"
python manage.py runserver 0.0.0.0:8000
#python manage.py runsslserver 0.0.0.0:8000 --certificate cert.pem --key key.pem -> burası https yaparken güncellenecek
