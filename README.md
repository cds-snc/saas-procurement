# SAAS Procurement App 

The SAAS Procurement app is a Python django project that will aide with the procurement process

## Local Development with Containers

This project uses [Visual Studio Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers).

Here are the instructions to get started with developing locally.

### Requirements:

- Docker installed and running
- VS Code


### Steps:

1. Clone the repo
2. Open VS Code with Dev Container (see [Quick start: Open an existing folder in a container](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container))
3. Go to the saas_app folder ```cd saas_app```
4. Add a ``.env`` file to the ``/workspace/app`` folder (Contact SRE team for the project specific .env setup)
5. Install Python dependencies

```
make install-dev
```
6. Generate migrations
``` 
make migration
```
7. Migrate the migrations
``` 
make migrate
```
8. Create a superuser to access the Django admin dashboard
``` 
make superuser
```
9. Open up a new python shell ```python manage.py shell``` and type:
```
from django.contrib.sites.models import Site
new_site = Site.objects.create(domain='127.0.0.1:8000', name='127.0.0.1:8000')
print (new_site.id)
```
10. Take the site id that is generated and update the settings.py file with the site_id generated above in the SITE_ID variable.
``` 
cd saas_app
vim settings.py
SITE_ID = [site id from step 8]
```
11. Run the application
```
cd ..
make run
```
12. Log into Django admin dashboard (http://127.0.0.1:8000/admin) using the credentials you created in 8.
13. Go to the Social applications table in Django admin and add a new Social application:
```
    Provider: Google
    Name: [choose a name]
    Client id: [client id from google developer api console]
    Secret key: [key from google developer api console]
    Chosen site: Pick the 127.0.0.1:8000 site 
```
