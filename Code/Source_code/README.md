## Getting Started

### Prerequisites

1.Install Homebrew CLI:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2.Install Python 3 using Homebrew CLI: 
brew install python

3.Install config package with Brew CLI:
brew install mysql pkg-config

###########################################

1. Install Docker - https://docs.docker.com/compose/install/
2. CLI : git clone https://github.com/FDU-Capstone-Group-7/Project.git
3. CLI : cd Code/Source_code
4. CLI : pip install -r requirements.txt
5. CLI : docker-compose up
6. CLI : python3 manage.py migrate
7. CLI : python3 manage.py makemigrations Indie_Game
8. CLI : python3 manage.py createsuperuser (set your User_Name and Password)
9. CLI : python3 manage.py runserver

Open a browser and go to: http://127.0.0.1:8000/admin

P.S. If terminal tells you that Port is already occupied. Kill the process running in this port by executing: 
1. lsof -i :8000       ##### to find the process ID
2. kill -9 'PID'       ##### 'PID' is the second column in the row

###########################################

Helpful docker and MYsql commands: 

docker ps
docker exec -it 'name of your image' /bin/bash
mysql -u root -p
show databases;
use 'database'
show tables;
SELECT * FROM tables;

/////////settings for image creation/////////////
docker run -d \
  --name my-django-mysql \
  -e MYSQL_DATABASE=djangodb \
  -e MYSQL_USER=djangouser \
  -e MYSQL_PASSWORD=userpass \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -p 3306:3306 \
  mysql:latest
/////////////////////////////////////////////////

