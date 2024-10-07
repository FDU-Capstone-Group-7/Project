## Getting Started

### Prerequisites

1.Install Homebrew CLI:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2.Install Python 3 using Homebrew CLI: 
brew install python

3.Install config package with Brew
brew install mysql pkg-config

###########################################

1. Install Docker - https://docs.docker.com/compose/install/
2. CLI : git clone https://github.com/FDU-Capstone-Group-7/Project.git
3. CLI : cd Code/Source_code
4. CLI : pip install -r requirements.txt
5. CLI : docker-compose up
6. CLI : python3 manage.py runserver

Open a browser and go to: http://127.0.0.1:8000/admin
Log in : super_user - 12345

###########################################


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

