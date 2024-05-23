#!/usr/bin/env bash

# Check OS type
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
elif [[ "$OSTYPE" == "cygwin" ]]; then
    OS="windows"
elif [[ "$OSTYPE" == "msys" ]]; then
    OS="windows"
else
    echo "Unsupported OS type: $OSTYPE"
    exit 1
fi

# Create and activate virtual environment
echo "Creating Virtual Environment"
python3 -m venv myenv

if [[ "$OS" == "windows" ]]; then
    echo "Activating Virtual Environment on Windows"
    source myenv/Scripts/activate
else
    echo "Activating Virtual Environment on Linux/MacOS"
    source myenv/bin/activate
fi

# Installing requirements
echo "Installing Requirements"
pip install --upgrade pip
pip install -r requirements.txt
echo "Requirements Installed"

# Make migrations
echo "Look Makemigrations"
python manage.py makemigrations

# Migrate
echo "Start Migrate"
python manage.py migrate

# Create admin user
echo "Creating Admin User"
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@admin.com','Bakwein41.' )" | python manage.py shell

# Run server
echo "Start Server"
#python manage.py runserver 0.0.0.0:8000
python manage.py runsslserver 0.0.0.0:8000 --certificate www.quipster.com.crt --key www.quipster.com.key
