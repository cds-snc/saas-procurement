# SAAS Procurement App 
lkajdfklaj

The SAAS Procurement app is a Python django project that will aide with the procurement process

## Local Development with Containers

This project uses [Visual Studio Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers).

Here are the instructions to get started with developing locally.

### Requirements:

- Docker installed and running
- VS Code


### Steps:

The easiest way to get started is to use codespaces. 

1. Clone the repo
2. Spin up a codespace
3. Or in Visual studio, having the Codespaces extension open up a new codespace and connect to it.
4. The container should run and the initialize.sh script will populate the database with all the required data.
5. If there is an issue with the database, you can manually run the initialize script. 
6.  Run the application
```
cd saas_app
make run
``` 
