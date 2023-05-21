# CITS3403Project

[Note](https://github.com/lainemulvay/CITS3403-Project) FAQ chat system [CITS3403-Project](https://teaching.csse.uwa.edu.au/units/CITS3403/) semester 1, 2023 
by [Murray Lewin](https://github.com/GrassTree-Muzz) (22967374), [Laine Mulvay](https://github.com/lainemulvay) (22708032), [Vicky Cow](https://github.com/vicky-chow) (23638279) and [Yinghao Zhang](https://github.com/hznkyh) (23072214)

## Features


- A Question and Response box are provided where the user can access the Open AI API and ask it any question, where a response will be recieved.

## Design 
### Code structure 
```
app/                                      <--Main App Module-->
      ../                         <--Package User Assessment-->
                ""''

      chat/                            <--Chat Page functionality-->
                __init__.py               ---initialize blueprint for chat module---
                routes.py                 ---chat/logout/save_chat/add_header routes---

      history/                         <--Chat and Response History -->
                __init__.py               ---initialize blueprint for history module--- 
                routes.py                 ---history/logout/view_chat_id/add_header view routes---

      intro/                           <--Introduction page functionality-->
                __init__.py               ---initialize blueprint for intro module---
                routes.py                 ---User index route---

      login/                           <--Login page functionality-->
                __init__.py               ---initialize blueprint for login module---
                routes.py                 ---login/get_me/logout routes---

      profile/                         <--lodges database profile-->
                __init__.py               ---initialize blueprint for profile module---
                routes.py                 ---register profile route---

      register/                        <--Database initialize for registration-->
                __init__.py               ---initialize blueprint for register module---
                routes.py                 ---register route---


      static/                          <--Templates-->
                css/    
                          base_styles.css   --- styling for the base template html
                          chat_styles.css   --- styling for the chat page html              
                          hist_styles.css   --- styling for the history page html
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

tests/                                      <--Unit tests-->
      ../                                   <--Package User Assessment-->
                ""''

      functional/                           <--Test website functionality-->
                __init__.py                 ---init file for pytest---
                test_chat.py                ---Test chat page functionality---
      unit/                                 <--Test module functionality-->
                __init__.py                 ---init file for pytest---
                test_controller.py          ---Test controller.py---
                test_model.py               ---Test model.py---
      
      __init__.py                           ---init file for pytest---
      conftest.py                           ---Fixture setup for pytest---

chat.py                                     ---Application of chat db---
config.py                                   ---configuration---
requirements.txt                            ---text file containing modules for install---
selenium_test.py                            ---Selenium test---
    
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
- Can receive responses from the server based on questions
- Can view their individual history of past chats that have been saved 

## Testing
### Unit test coverage 
- ***CURD operation*** on user and submission model 
- User ***login*** and ***registration*** control mechanism and validation
- Submission control and validation 
- Auto marking 

### Selenium test coverage
- User register case
- User login case
- User chat case
- User history case
- User profile case
- User logout case

### Requirements
```
python 3.11.3 or above
```

If you don't have python installed, you can download it [here](https://www.python.org/downloads/)

### Installation
Download the project from github. Skip this step if you have already downloaded the project.
```
$ git clone https://github.com/lainemulvay/CITS3403-Project.git
```

Navigate to the project directory.
```
$ cd CITS3403-Project
```

## For Mac/Linux
```
If required, create a virtual environment. Skip this and the following step if you do not wish to use a virtual environment.
```
```
python3 -m venv venv
```

Activate the virtual environment.
```
$ source venv/bin/activate
```

Download the required modules.
```
$ pip install -r requirements.txt
```

Export the flask app.
```
$ export FLASK_APP=chat.py
```

## For Windows
```
If required, create a virtual environment. Skip this and the following step if you do not wish to use a virtual environment.
```
> py -3 -m venv venv
```

Activate the virtual environment.
```
> venv\Scripts\activate

if prompt says "cannot be loaded because running scripts is disabled on this system", run the following command, then try again:
> Set-ExecutionPolicy Unrestricted -Scope Process
```

Download the required modules.
```
> pip install -r requirements.txt
```
> setx FLASK_APP "chat.py"
```

### Launch
## For Mac/Linux and Windows
```
$ flask run
```
## Test
To run tests, run the following command in the root directory of the project:
```
python -m pytest -v
```

To view the coverage report, run the following command in the root directory of the project:
```
python -m pytest --cov=app
```

To run only the selenium tests, run the following command in the root directory of the project:
```
$ python selenium_test.py
```
## Libraries Used
- [Sweet Alert][https://sweetalert2.github.io/] - Used for displaying alerts to the user

## Acknowledgment
- [CITS3403 Lecture material](https://teaching.csse.uwa.edu.au/units/CITS3403/) by Dr Tim French
- [FLASK MEGA tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
