Let me brief the steps for deploying using Elastic Bean Stalk:
1. in settings.py, 
    * ALLOWED_HOSTS = ["*"] //when we get the domain name, we will change it to the domain name 
    * set DATABASES = {'default': {}} //rds credentials
2. in wsgi.py and manage.py add,
    ``` 
    import pymysql
    pymysql.install_as_MySQLdb()
   ```
3. In requirements.txt,
    ```
     Django==4.2.20
     djangorestframework==3.16.0
     gunicorn
     pymysql==1.1.0
   ```
4. create .ebextensions dir,
5. inside that dir add 'django.config' file, 
    ```   
    option_settings:
       aws:elasticbeanstalk:container:python:
              WSGIPath: <YOUR_PROJECT_NAME>.wsgi:application
    ```
6. Then, git commit all the changes ....
7. all configurations are done.. now time for elastic bean stalk deployment. Assumption you already installed the awscli & bean stalk cli
8. In cmd,
    ```
    eb init -p python-3.11 <YOUR_APPLICATION_NAME> -r ap-south-1
    eb create <VIRTUAL_ENV_NAME>
    ```

    after 5 min
+ check command "eb status"
     * Status: Launching -> Ready<br>
               Health: Green (this must be Green)......
        + that's it
        + now write "eb open" command or COPY "CNAME:" field it's deployed url