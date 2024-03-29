# LITReview
LITReview

LITReview is a web application which allows users to shared some asks and reviews about books and articles.
This webapp is developped under Jango Framework 
***
***
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installing Environment](#Installing-Environment)
4. [Configuring Environment](#Configuring-Environment)
5. [Starting LITReview](#Starting-LITReview)
6. [LITReview architecture](#LITReview-architecture)
7. [PEP8 reports](#PEP8-reports)
8. [FAQs](#faqs)
***
***
## General Info
***
This program is in version 1.0 and aimed the purpose why it has been created.
I wait the result of the meeting with the askers to see if there was some modifications to bring to this version.

***
## Technologies
***
List of technologies used within this project : 
* [Windows 10](https://www.microsoft.com/fr-fr/software-download/windows10): version 21H2
* [Python](https://www.python.org/downloads/release/python-3100/):  version 3.10.0
* [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/): version 2021.2.3
* [git](https://git-scm.com/download/win): version 2.35.1.windows.2
* [Django](https://www.djangoproject.com/): version 4.1
* [Bootstrap](https://getbootstrap.com/): Version 5.2.0
* [JQuery](https://jquery.com/): version 3.6.1
* [flake8](https://pypi.org/project/flake8/): Version 4.0.0
* [flake8-html](https://pypi.org/project/flake8-html/): version 0.4.2

***
## Installing Environment
***
This process suggests that you have admin priviledges on you computer
### Python 3.10.0 installation
***
For installing Python 3.10.0 on your computer go to those adress following the OS you use :

For MacOS :

  Package :
    [Python 3.10.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0post2-macos11.pkg)
    
  Installation guide :
    [Installing Python 3 on MacOS](https://docs.python-guide.org/starting/install3/osx/)

For Linux :

  Package :
    [Python 3.10.0](https://www.python.org/downloads/release/python-3100/)
    [Gzipped source tarball](https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz)
    [XZ compressed source tarball](https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz)
    
 Installation guide :
    [Installing Python 3.10.0 on Linux](https://docs.python-guide.org/starting/install3/linux/)

For Windows :

  Package : 
    [Python 3.10.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)
    
  Installation guide :
    [installing Python 3.1.0 on Windows](https://docs.python.org/fr/3/using/windows.html)

***
### Git 2.35.1 installation
***
For installing Git on your computer go to this adress (all OS contents):

[Git installation guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

***
#### Git configuration 
***
(Even if you did not have done before, create an account on Github at the adress : https://github.com)

1. In order to configure your git IDs , see the following process in GitBash console :
   Type the following command
  
  ``` 
       $ git config --global user.name "your_github_username"
       $ git config --global user.email your_email@your_provider.com
  ```
2. Type the following command to configure the GitBash console interface (optional) :
  
  ```
       $ git config --global color.diff auto
       $ git config --global color.status auto 
       $ git config --global color.branch auto
  ```
***
### Clone the distant repository with Gitbash
***
You have now to clone the distant repository on your computer.
1. type the following command in Gitbash console :
  
  ```
        $ git clone https://github.com/SGauthier2Pro/LITReview.git
  ```
2. Verify that you got the source directory opening an explorator and verifying that all files are in:

![content_root](https://user-images.githubusercontent.com/99419487/189898295-e63ac66d-5160-4c3a-8585-ccc4cf853f6a.png)
![content authentication](https://user-images.githubusercontent.com/99419487/189898305-7d7d868d-6ad4-4726-af5d-f911a6fff690.png)
![authentication_template](https://user-images.githubusercontent.com/99419487/190015807-a1d01872-2e3f-4a0a-a95a-dad35fe754e8.png)
![content_LITReview](https://user-images.githubusercontent.com/99419487/189898335-bcad09a7-418a-4b89-ac68-9af9b005ef3e.png)
![content_review](https://user-images.githubusercontent.com/99419487/189898349-55c10aa0-9181-4227-98c2-be9db20e0b89.png)
![content_review_migration](https://user-images.githubusercontent.com/99419487/189898363-39b3bf55-4233-4cc0-8357-cb8099506aa8.png)
![content_review_templates](https://user-images.githubusercontent.com/99419487/189898378-9d2c7dbb-9eec-4541-bab1-7b528e6f18c9.png)
![content_review_partials](https://user-images.githubusercontent.com/99419487/189898391-efcf18c1-9fa5-4c50-a459-a5214a9bab1c.png)
![content_review_templatestags](https://user-images.githubusercontent.com/99419487/189898410-20b27be0-db2b-44ec-ae7b-e3d370985183.png)
![content_static_css](https://user-images.githubusercontent.com/99419487/189898418-34b6593d-45c0-4471-b443-99c19ed8682c.png)
![content_static_js](https://user-images.githubusercontent.com/99419487/189898430-8b00e5d9-9c2a-4611-a6b2-c8e5bc3d3faf.png)
![content_static_pictures](https://user-images.githubusercontent.com/99419487/189898445-10a4b156-fd4a-4c89-a2c6-568e6f0d6965.png)
![content_root_templates](https://user-images.githubusercontent.com/99419487/189898454-851706ff-ceca-4865-a75b-bbf64ff25d5b.png)


***
## Configuring environment
***
***
### Installation and execution with virtualenv
***
1. Move LITReview directory with ```$ cd LITReview```
2. Create a virtual environment for the project with ```$ python -m venv env``` on windows or ```$ python3 -m venv env``` on macos or linux.
3. Activate the virtual environment with ```$ env\Scripts\activate.bat``` on windows or ```$ source env/bin/activate``` on macos or linux.
4. Install project dependencies with ```$ pip install -r requirements.txt```
6. Create an admin user for your server with ```$ python manage.py createsuperuser``` on windows or ```$ python3 manage.py createsuperuser``` on macos or linux.
8. Start the server with ```$ python manage.py runserver``` on windows or ```$ python3 manage.py runserver```on macos or linux.

***
## Starting LITReview
***
- To access to LITReview application type ```http://172.0.0.1:8000/``` in your prefered navigator.
  - This is the list of users created in the database for testings :
    - Adda_41
    - Krum_daylite78
    - pilou_pilou
    - sabine_41
    - sgauthier
    - toto
    - vlad_tepes
      - They all use the same user password : LITReview01$
- To access to the web server admin page type ```http://172.0.0.1:8000/admin``` instead, using your superuser login informations.  
***
## LITReview architecture
***
This webapp is divided in 3 applications :

***
### 1. LITReview :
***
This module contains : 
   - The settings.py which has been modified in this way :
   
     - adding the two main applications :  
     ![settings_applications](https://user-images.githubusercontent.com/99419487/190012034-eea43c07-3953-4b9e-8705-a0e8b76737ef.png)
     - unactivating timezone :  
     ![settings_unactivated_timzone](https://user-images.githubusercontent.com/99419487/190012271-6966cfca-cee9-4b30-903e-5293490b5951.png)
     - modifiying static path :  
     ![settings_static_path](https://user-images.githubusercontent.com/99419487/190013238-90d7b8d4-e61f-45a5-b0af-d6bfe3a1ef9b.png)
     - adding login url :  
     ![settings_login_url](https://user-images.githubusercontent.com/99419487/190013802-ea02fc18-ed47-481e-ac94-58809ff852f7.png)
     - adding media url :  
     ![settings_media_url](https://user-images.githubusercontent.com/99419487/190013812-3539b274-7e87-484b-bad9-03ac9b33d373.png)
      
- the urls.py :
  - containing all pathway for each page of the application with their alias :
    - authentication path :  
    ![urls_authentication_pathpng](https://user-images.githubusercontent.com/99419487/190018220-21725cf4-ef95-43d5-80fc-8ab5ddce8dbd.png)
    - main section path :  
    ![urls_main_path](https://user-images.githubusercontent.com/99419487/190018233-5a1c1e64-f0b4-494c-bb9d-ab6cba7b1625.png)
    - modification path :  
    ![urls_functional_path](https://user-images.githubusercontent.com/99419487/190018245-c0a8ff5e-28c8-4be1-ac36-f8f74737248c.png)
    - debug static path :  
    ![urls_static_path](https://user-images.githubusercontent.com/99419487/190018254-4879fae1-0f15-4a9d-89d4-c7d471b8ca00.png)

***    
### 2. Authentication :
***
- This module contains all files linked to the signup and authentication system :  
  ![content authentication](https://user-images.githubusercontent.com/99419487/189898305-7d7d868d-6ad4-4726-af5d-f911a6fff690.png)
  
- You will find here 2 importants py files :
    - forms.py : containing the signupform and the userloginform
    - views.py : containing all view functions for signup and login
    - the models .py is empty, auhtentication use the native class from Django

  This directory contains the templates for those two functions

***
### 3. Review :
***
- This is the main module of this webapp. It contains the following elements :
  - admin.py :  
    - this file contains le registering of all class from models to be managed from the server admin site.  
  ![admin](https://user-images.githubusercontent.com/99419487/190025509-0d1e63a3-0eb8-40a3-8949-5f52dc8495b4.png)
  - forms.py :  
    - This file contains all forms for Tickets, Reviews and followings management  
    ![review_forms](https://user-images.githubusercontent.com/99419487/190026051-4a8cd92f-20de-4cf6-9770-64a3a8ffe6c3.png)  
  - models.py :  
    - This file contains class models populating the database  
    ![review_models](https://user-images.githubusercontent.com/99419487/190026262-4f9966a6-4e4f-4d6e-9204-df000a4cce5a.png)
  - views.py : 
    - This file contains all functions for each action made by user on webapp.  
    ![review_views](https://user-images.githubusercontent.com/99419487/190026855-72a25ac1-0933-4f19-9479-39771fe215de.png)  
  - templates directory :  
    - This directory contains all html file and snippets of the webapp  
    ![review_templates](https://user-images.githubusercontent.com/99419487/190027102-ea3e7dcf-a790-4556-9570-36bf7896c92f.png)  
    - Partials directory :
      - ticket_snippet.html the template displaying the tickets 
      - review_snippet.html the template displaying the reviews
      - validation_button_snippet.html the template displaying the validation button of creation forms  
    - Templatetags directory :
      - contains post_extras.py where you can find functions managing the displaying of name and dates in tickets and reviews  
      ![post_extras py](https://user-images.githubusercontent.com/99419487/190521128-9d6b16db-54a6-4e71-9607-7de08f1cacb2.png)  
***  
### 4. root directory:
***
In the root directory you will find two more important directories :
- static directory :
  - css directory containing style.css and bootstrap css :  
    ![static_css](https://user-images.githubusercontent.com/99419487/190028009-5060a468-2c33-4b11-9dea-562afa9b7681.png)  
  - js directory containing boostrap javascript and JQuery javascript :  
  ![static_js](https://user-images.githubusercontent.com/99419487/190028014-4ed230a3-9578-4bba-881c-316f833dec71.png)  
  - Pictures directory containing the main background and the brand logo :  
  ![static_pictures](https://user-images.githubusercontent.com/99419487/190028018-165d3c4a-62cf-4158-b747-6affc5e7dc44.png)  
- templates directory :  
  - This directory contains the main frame of the webapp, navbar and section block :  
  ![templates](https://user-images.githubusercontent.com/99419487/190028024-cab54127-1e49-4cdd-b93b-b8742ff4eda2.png)


***
## PEP8 reports
***

In order to generate the flake8-html report, type the following command from the program folder :

```
    flake8 --format=html --htmldir=flake8-report --exclude env ../LITReview
```  
***
## FAQs
***

N/A
