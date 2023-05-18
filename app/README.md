# MCV (Model-View-Controller) architecture

## Model 
This model architecture allows you to store and retrieve user information, chat data, questions, and responses in a relational database using the SQLAlchemy ORM.


### User: 
Represents a user table with columns such as id, email, first_name, last_name, password, and date_added. It also has a relationship with the Chat table through the chat attribute.

### Chat:
Represents a chat table with columns such as id, user_id, and datetime. It has relationships with the ChatQuestion and ChatResponse tables through the chat_questions and chat_responses attributes, respectively.

### ChatQuestion:
Represents a chat question table with columns such as id, chat_id, content, and timestamp. It is related to the Chat table through the chat_id foreign key.

### ChatResponse:
 Represents a chat response table with columns such as id, chat_id, content, and timestamp. It is related to the Chat table through the chat_id foreign key.
\
---
## controller
Contains CURD operations for the controller

### Create:
add_user(email, first_name, last_name, hashed_pw): Creates a new user by adding a new User object to the database with the provided email, first name, last name, and hashed password.

add_chat(user_id): Creates a new chat by adding a new Chat object to the database, associated with the provided user_id.

add_chat_question(chat_id, content, timestamp): Creates a new chat question by adding a new ChatQuestion object to the database, associated with the provided chat_id, content, and timestamp.

add_chat_response(chat_id, content, timestamp): Creates a new chat response by adding a new ChatResponse object to the database, associated with the provided chat_id, content, and timestamp.

### Read:
get_user(): Retrieves the current user from the database based on the session id.

check_email(): Retrieves a user from the database based on the provided email.

get_chat_ids(user_id): Retrieves a list of chat ids associated with the provided user_id.

get_chat_questions(chat_id): Retrieves a list of chat questions associated with the provided chat_id.

get_chat_responses(chat_id): Retrieves a list of chat responses associated with the provided chat_id.

get_chat(chat_id): Retrieves a chat consisting of chat questions and responses associated with the provided chat_id.

get_chat_records(user_id): Retrieves a list of chat records (ids and timestamps) associated with the provided user_id.

### Update:
update_user(id, email=None, first_name=None, last_name=None): Updates the user's information (email, first name, last name) based on the provided id. Only the provided fields will be updated.

change_password(id, newpassword): Updates the user's password based on the provided id. It generates a new hashed password using generate_password_hash and updates the corresponding user object in the database.

### Delete:
No explicit delete operation is included in the provided code snippet. However, in a typical application, you would expect to have functions that handle deleting users, chats, questions, and responses from the database.

