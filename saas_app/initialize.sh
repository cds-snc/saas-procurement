#!/bin/bash
# Script that validates if the project is properly initilized for development purposes.
# If not, initializes the project.

#Update pip
pip install --upgrade pip

# Check if django is installed, if not, install requirements_dev.txt
django_installed=$(pip3 list  | grep -c django)
if [ "${django_installed}" -eq 0 ]; then
    echo "Django is not installed"
    echo  "Installing requirements_dev.txt"
    python -m pip install -r requirements_dev.txt
else
    echo "Django is installed, skipping requirements_dev.txt"
    echo "If you want to manually update the project packages, run: pip install -r requirements_dev.txt"
fi

# Check if there are migrations to apply, if there are store their count to a variable
migration_count=$(python manage.py showmigrations | grep -c "\[ \]")
# If migration_count is greater than 0, there are migrations to apply
if [ "${migration_count}" -gt 0 ]; then
    echo "There are migrations to apply"
    python manage.py migrate
else
    echo "There are no migrations to apply"
fi

# Variable storing the number of users in the django database
users_length=$(python manage.py shell -c "from django.contrib.auth.models import User; print(len(User.objects.all()))")
# If users_length equals 0, there are no users so we need to create at least one to log in.
if [ "${users_length}" -eq 0 ]; then
    echo "There are no users"
    # Create a superuser with following information:
    # username: "admin"
    # email: "admin@admin.com"
    # password: "admin"
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" 
else
    echo "There are users"
fi  
