# World Of Games


### How To Run Locally
1. ```git clone https://github.com/khjomaa/world_of_games_web.git```
2. ```cd world_of_games_web```
3. Set the following environment variables
    - **Mac**
        - ```export ENV=DEVELOPMENT```
        - ```export SECRET_KEY=my_secret_key```
        - ```export DB_USERNAME=user```
        - ```export DB_PASSWORD=user123```
        - ```export DB_HOST=localhost```
        - ```export DATABASE_NAME=wog```
    - **Windows**
        - ```set ENV=DEVELOPMENT```
        - ```set SECRET_KEY=my_secret_key```
        - ```set DB_USERNAME=user```
        - ```set DB_PASSWORD=user123```
        - ```set DB_HOST=localhost```
        - ```set DATABASE_NAME=wog```
4. ```pip install -r requirements.txt```
5. ```python manage.py db init```
6. ```python manage.py db migrate```
7. ```python manage.py db upgrade```
8. ```python manage.py runserver```
6. App URL: [0.0.0.0:5555](http://0.0.0.0:5555)


### How to run locally using Docker-Compose:
1. ```git clone https://github.com/khjomaa/world_of_games_web.git```
2. ```cd world_of_games_web```
3. ```docker-compose up -d```
4. App URL: [0.0.0.0:8777](http://0.0.0.0:8777)


### How To run in Jenkins:
1. Created credentials for Docker Hub following these steps:
    - Navigate to **Credentials** => **global** => **Add Credentials**
    - Kind: "Username with password"
    - Scope: "global"
    - Username: enter your Docker Hub ID
    - Password: enter your Docker Hub password
    - ID: DockerHub (**Important: DO NOT change value, otherwise you will need to edit Jenkinsfile**)
2. Create "New Item"
3. Enter a name
4. Choose "Pipeline"
5. Scroll down to "Pipeline" section and choose "Pipeline script from SCM"
6. Choose "Git" for SCM
7. Enter for Repository URL: https://github.com/khjomaa/world_of_games_web.git
8. Leave the rest as default 
9. Click on "Save"
10. Click on "Build Now"