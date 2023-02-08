# SAAS Procurement App 

The SAAS Procurement app is a Python django project that will aide with the procurement process

## Local Development with Containers

This project uses [Visual Studio Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers).

Here are the instructions to get started with developing locally.

Requirements:

- Docker installed and running
- VS Code

Steps:

1. Clone the repo
2. Open VS Code with Dev Container (see [Quick start: Open an existing folder in a container](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container))
3. Go to ```saas-procurement/saas_app```folder
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

8. Create a superuser to access the Django admin dashoard
``` 
make superuser
```

9. Run application
``` 
make run
``` 
