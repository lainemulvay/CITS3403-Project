# MCV (Model-View-Controller) architecture

## Model
Contains four models `users`, `chats`, `chat_questions`, and `chat_responses` that represent the database tables.

### User: 
- A `users` instance represents a registered user.

### Chat:
- A `chat` instance represents a chat session of a user.

### ChatQuestion:
- A `chat_question` instance represents a question asked by a user in a chat session.

### ChatResponse:
- A `chat_response` instance represents a response to a question asked by a user in a chat session.
---
## controller
Contains functions that handle read and add operations on the database.

### Create:
```
add_user(email, first_name, last_name, hashed_pw): Creates a new user by adding a new User object to the database with the provided email, first name, last name, and hashed password.

add_chat(user_id): Creates a new chat by adding a new Chat object to the database, associated with the provided user_id.

add_chat_question(chat_id, content, timestamp): Creates a new chat question by adding a new ChatQuestion object to the database, associated with the provided chat_id, content, and timestamp.

add_chat_response(chat_id, content, timestamp): Creates a new chat response by adding a new ChatResponse object to the database, associated with the provided chat_id, content, and timestamp.
```

### Read:
```
get_user(): Retrieves the current user from the database based on the session id.

check_email(email): Retrieves a user from the database based on the provided email.

get_chat_ids(user_id): Retrieves a list of chat ids associated with the provided user_id.

get_chat_questions(chat_id): Retrieves a list of chat questions associated with the provided chat_id.

get_chat_responses(chat_id): Retrieves a list of chat responses associated with the provided chat_id.

get_chat(chat_id): Retrieves a chat consisting of chat questions and responses associated with the provided chat_id.

get_chat_records(user_id): Retrieves a list of chat records (ids and timestamps) associated with the provided user_id.
```

### Update:
```
update_user(id, email=None, first_name=None, last_name=None): Updates the user's information (email, first name, last name) based on the provided id. Only the provided fields will be updated.

change_password(id, newpassword): Updates the user's password based on the provided id. It generates a new hashed password using generate_password_hash and updates the corresponding user object in the database.
```

## View
- View is implemented in the `templates` folder. Rendered using flask and jinja.

