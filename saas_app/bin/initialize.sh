#!/bin/bash
# Script that validates if the project is properly initilized for development purposes.
# If not, initializes the project.

echo "Retrieving environment parameters and put them in an .env file"
python bin/get_parameters.py

# Apply all migrations. 
echo "Applying migrations"
python manage.py migrate
echo "Finished applying migrations"

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
    # create manager user
    # username: "manager"
    # email: "sylvia.mclaughlin@cds-snc.ca"
    # password: "manager"
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('manager', 'sylvia.mclaughlin+manager@cds-snc.ca', 'manager')"
    # 
else
    echo "There are users"
fi  

# Load the fixtures data so that the database is populated with some data for testing purposes
# check to see if Social account is installed
social_account=$(python manage.py shell -c "from allauth.socialaccount.models import SocialApp; print(len(SocialApp.objects.all()))")
if [ "${social_account}" -eq 0 ]; then
    # get the environment variables and replaces them in the fixtures file for the google social account
    # An extra precaution so that we don't leak the secrets
    social_app_model=$(jq '.[8].model' -r fixtures/fixtures_initial_data.json)
    if [ "${social_app_model}" = "socialaccount.socialapp" ]; then
        # Make a copy of file temporarily so that we can modify it
        cp fixtures/fixtures_initial_data.json fixtures/original_fixtures_initial_data.json
        jq '.[8].fields.client_id=env.SOCIAL_APPLICATION_CLIENT_ID | .[8].fields.secret=env.SOCIAL_APPLICATION_SECRET_KEY' fixtures/fixtures_initial_data.json >> tmp.json && mv tmp.json fixtures/fixtures_initial_data.json
        # Run the loaddata command
        echo "Installing initial database data"
        python manage.py loaddata fixtures/fixtures_initial_data.json
        # Now revert the file to its original state so that we don't accidentally commit the changes or leak the secrets
        mv fixtures/original_fixtures_initial_data.json fixtures/fixtures_initial_data.json
    else
        echo "Failed - check that the fixtures file is in the correct format and that the model is 'socialaccount.socialapp' at index 10"
    fi
else
    echo "Initial data is already installed"
fi

# Run collectstatic to generate the static files
echo "Generating static files"
python manage.py collectstatic --noinput

# Add the crontab entry so that we can run it every day
#echo "Starting cron service"
# Start the cron service
#service cron start
# Get the status of the cron service
#service cron status

# Add the crontab entry
#echo "Setting up crontab"
#python manage.py crontab remove 
#cronjob_id=$(python manage.py crontab add | grep -o '\([a-f0-9]\{32\}\)')
# Now if we are testing and the database is empty, make sure that we run the cronjob once to populate the database with data
#logs=$(python manage.py shell -c "from manage_saas.models import GoogleWorkspaceAppsLogin; print(len(GoogleWorkspaceAppsLogin.objects.all()))")
#if [ "${logs}" -eq 0 ]; then
    # now run the cronjob to genearte data
#    python manage.py crontab run ${cronjob_id}
#fi 

# See if the cron is set correctly 
#crontab -l

# Start up the application
echo "Starting up the application"
python manage.py runserver 0.0.0.0:8000