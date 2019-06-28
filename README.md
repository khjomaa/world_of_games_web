# World Of Games


### How To Run Locally
1. ```git clone https://github.com/khjomaa/world_of_games_web.git```
2. ```cd world_of_games_web```
2. ```docker-compuse up -d```
3. App URL: [0.0.0.0:8777](http://0.0.0.0:8777)


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