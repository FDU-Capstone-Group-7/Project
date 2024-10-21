Prerequisites

1.Install Homebrew CLI: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2.Install Python 3 using Homebrew CLI: brew install python

3.Install config package with Brew CLI: brew install mysql pkg-config

###########################################

Install Docker - https://docs.docker.com/compose/install/
CLI : git clone https://github.com/FDU-Capstone-Group-7/Project.git
CLI : cd Code/Source_code
CLI : pip install -r requirements.txt
CLI : docker-compose up
CLI: mysql -u root -p (password: pass)
mySQL CLI: CREATE USER 'djangouser'@'localhost' IDENTIFIED BY 'userpass';
mySQL CLI: GRANT ALL PRIVILEGES ON djangodb.* TO 'djangouser'@'localhost';
mySQL CLI: FLUSH PRIVILEGES;
Delete file: Indie_Game/migrations/0001_initial.py
CLI : python3 manage.py makemigrations Indie_Game
CLI : python3 manage.py migrate
(Optional) CLI : python3 manage.py createsuperuser (set your User_Name and Password)
CLI : python3 python3 manage.py runserver_with_task
Open a browser and go to: http://127.0.0.1:8000/admin

P.S. If terminal tells you that Port is already occupied. Kill the process running in this port by executing:

lsof -i :8000 ##### to find the process ID
kill -9 'PID' ##### 'PID' is the second column in the row

####################################

If migration does not go well:
Delete all tables from DB 
DROP TABLE 'table name';

and delete DB history:
DELETE FROM django_migrations WHERE app = 'Indie_Game';

Then create makesmigrations and migrate


###########################################

Patch Note # 21.10.2024

1. Install: pip install gpt4all
2. Added LLM - folder with files inside
3. Added in Discussion.py 
        class Meta:
        db_table = 'Indie_Game_comment'
4. Added
    class Comment_temp(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments_temp')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'Indie_Game_comment_temp'
5. Added LLM_moderation.py
6. Changed forms.py:  
    from .model.Discussion import Discussion, Comment_carantine
    model = Comment_carantine
7. New folder - "management"
8. New command to run server: python3 manage.py runserver_with_task
9. Updated 
    class Comment_temp(models.Model):
        discussion = models.ForeignKey(
            Discussion,
            on_delete=models.CASCADE,
            related_name='temp_comments'

######################################