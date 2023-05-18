# CITS3403Project

[Note](https://github.com/lainemulvay/CITS3403-Project) FAQ chat system [CITS3403-Project](https://teaching.csse.uwa.edu.au/units/CITS3403/) semester 1, 2023 
by [Murray Lewin](https://github.com/GrassTree-Muzz) (22967374), [Laine Mulvay](https://github.com/lainemulvay) (22708032), [Vicky Cow](https://github.com/vicky-chow) (23638279) and [Hank Zhang](https://github.com/hznkyh) (23072214)

## Features


- A Question and Response box are provided where the user can access the Open AI API and ask it any question, where a response willbe recieved.

## Design 
### Code structure 
```
app/                                      <--Main App Module-->
      ../                         <--Package User Assessment-->
                ""''

      chat/                            <--Chat Page functionality-->
                __init__.py               ---initialize blueprint for chat module---
                routes.py                 ---chat/logout/save_chat/add_header routes---

      history/                         <--Chat and Reponse History -->
                __init__.py               ---initialize blueprint for history module--- 
                routes.py                 ---history/logout/view_chat_id/add_header view routes---

      intro/                           <--Introdution page functionality-->
                __init__.py               ---initialize blueprint for intro module---
                routes.py                 ---User index route---

      login/                           <--Login page functionality-->
                __init__.py               ---initialize blueprint for login module---
                routes.py                 ---login/get_me/logout routes---

      profile/                         <--lodges database profile-->
                __init__.py               ---initialize blueprint for profile module---
                routes.py                 ---register profile route---

      register/                        <--Database initialise for reigstration-->
                __init__.py               ---initialize blueprint for register module---
                routes.py                 ---register route---


      static/                          <--Templates-->
                css/    
                          base_styles.css   --- styling for the base template html
                          chat_styles.css   --- styling for the chat page html              
                          hist_styles.css   --- styling for the historu page html
                          login_styles.css  --- styling for the login page html
                images/   
                          UWA_Logo_Full.svg
                          UWA_Logo_small.png
                js/
                          chat.js           --- Sets up a chat interface where a user can input messages, which are then sent to the OpenAI Chat API for a response, and the conversation is displayed in real-time. Additionally, there is a functionality to send the conversation history to the server. and API
                          scripts.js        --- Implements various functionalities for a web application, including dropdown menu toggling, user authentication (login/logout), password validation, user registration, and chat history navigation.

      templates/                       <--Templates-->
                base_chat                   --- Formats the base template to be used on all the pages
                base                        --- Formats the base template to be used on all the pages
                chat_view                   --- Chat message page template
                hist_view                   --- History page template
                intro_view                  --- Introduction page template
                login_view                  --- Login page template
                profile_view                --- Visit profile 
                reg_view                    --- Registration page template
                ....html

authentify.py                               ---configuration---
chat.py                                     ---Application of chat db---
config.py                                   ---configuration---
requirements.txt                            ---text file containing modules for install---
    
```
### Model representations 
```
User(
    'id', Integer, PRIMARY KEY 
    'email', String(100)
    'first_name', String(100), NOT NULL
    'last_name', String(100), NOT NULL
    'password', String(100), NOT NULL
    'date_added', DateTime
)

Chat(
    'id', Integer, PRIMARY KEY
    'user_id', Integer, FOREIGN KEY
    'datetime', DataTime
)

ChatQuestions(
    'id', Integer, PRIMARY KEY
    'chat_id', Integer, FOREIGN KEY
    'content', TEXT, NOT NULL
    'timestamp', TEXT, NOT NULL
)

ChatResponse(
    'id', Integer, PRIMARY KEY
    'chat_id', Integer, FOREIGN KEY
    'content', TEXT, NOT NULL
    'timestamp' TEXT, NOT NULL
)

```
### User types 
![Anonymous](https://img.shields.io/badge/-Anonymous-black.svg)
- Can view introduction page
- Can register to become an user

![Registed Users](https://img.shields.io/badge/-User-yellow.svg)
- Can login and logout using username and password
- Can ask the chat questions
- Can recieve responses fromthe server based on questions
- Can view their individual history of past chats that have been saved 


## Project Management 

* Planing phase  

      > Inital planing were carried out to outline the content, scope and workflow. 
      > Estimation were made on required framework, library and implimentation time.
      
* Agile Methodology 

      > Scope of each iterations were outlined based on the analysis of requirements.
      > Determine functionalities that needs to be delivered. 

* Implimentation phase

      > Writing code.

* Testing

      > Basic unittest were automated and carried out at each iteration.


-------------------

## Testing
### Unit test coverage 
- ***CURD operation*** on user and submission model 
- User ***login*** and ***registration*** control mechanism and validation
- Submission control and validation 
- Auto marking 

### Selenium test coverage
- User register case
- User Login case
- User submission case

## Install
```
$ sudo apt install python3
$ sudo apt install python3-pip
$ sudo apt-get install python3-setuptools
$ sudo apt install python3-flask
$ git clone https://github.com/kurapikaaaa/CITS3403Project.git
$ pip3 install -r requirements.txt
$ export FLASK_APP=sidenote.py
```
## Launch
```
$ flask run
```
## Unittest
```
$ python3 -W ignore test.py
```
## Selenium Test
```
$ export DRIVER='**PATH_TO_WEB_DRIVER**'
$ python3 -W ignore seleniumTest.py
```
## Libraries Used
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [VexFlow](https://github.com/0xfe/vexflow)
- [GoogleFont](https://fonts.google.com/specimen/Zilla+Slab#standard-styles)

## Acknowledgment
- [CITS3403 Lecture material](https://teaching.csse.uwa.edu.au/units/CITS3403/) by Dr Tim French
- [FLASK MEGA tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
