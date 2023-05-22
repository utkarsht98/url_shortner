﻿# URL Shortner App
 
 ## Steps to setup the project - 
 
 - For this project, we need to have Mysql installed on the device. 
 - Create a folder named **"url_shortner"**.
 - Move into the above folder clone this repo using git clone command.
 - Install the libraries given in "requirements.txt" file.
 - Create a database named **"url_shortner"** using either the MySql command line or Mysql workbench.
 - In settings.py file, Configure the database (Line 77) section by adding your root username, password, host and port for db connection.
 - Run the command **"python manage.py makemigrations"** and **"python manage.py migrate"** from **"url_shortner"** directory. This will create the schema in your database.
 - To start the server run command **"python manage.py runserver"**.
 - Try the API's on POSTMAN app. (all the details regarding the API's contract is shared through postman collection).
