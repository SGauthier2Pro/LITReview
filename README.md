# LITReview
LITReview

LITReview is a web application which allows users to shared some asks and reviews about books and articles.
This webapp is developped under Jango Framework 
***
***
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Start JustStreamIt UI](#Start-JustStreamIt-UI)
5. [FAQs](#faqs)
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

***
## Installation
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
![authentication_template](https://user-images.githubusercontent.com/99419487/189898320-784a9368-e801-4660-8dda-8c30f0d475c9.png)
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
### download and run API OCMovies
***
You have now to clone the distant repository for OCMovies API on your computer.
1. type the following command in Gitbash console :
  
  ```
        $ git clone https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR.git
  ```
  you can refere to the README to know how install it and execute it.

***
### installing VS Code
***
For any OS, you can follow the link bellow to install VS-Code :

https://code.visualstudio.com/docs/setup/setup-overview

***
### installing LiveServer
***
You can install LiveServer directly from the extension menu in VS-Code or going to this adress :

https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer
 
***
## Start-JustStreamIt-UI
***
Go in the project directory and open the index.html file and enjoy !


***
## FAQs
***

N/A
