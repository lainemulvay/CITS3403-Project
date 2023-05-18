from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column("First Name", db.String(100), nullable=False)
    last_name = db.Column("Last Name", db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now)
    chat = db.relationship('Chat', backref='user', lazy=True)

    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

    def get_password(self):
        return self.password

class Chat(db.Model):
    __tablename__ = "chats"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    datetime = db.Column(db.DateTime, default=datetime.now)
    chat_questions = db.relationship('ChatQuestion', backref='chat', lazy=True)
    chat_responses = db.relationship('ChatResponse', backref='chat', lazy=True)
    
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<Chat %r>' % self.id

class ChatQuestion(db.Model):
    __tablename__ = "chat_questions"
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.Text, nullable=False)
    
    def __init__(self, chat_id, content, timestamp):
        self.chat_id = chat_id
        self.content = content
        self.timestamp = timestamp

    def __repr__(self):
        return '<ChatQuestion %r>' % self.id

class ChatResponse(db.Model):
    __tablename__ = "chat_responses"
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.Text, nullable=False)

    def __init__(self, chat_id, content, timestamp):
        self.chat_id = chat_id
        self.content = content
        self.timestamp = timestamp
        
    def __repr__(self):
        return '<ChatResponse %r>' % self.id