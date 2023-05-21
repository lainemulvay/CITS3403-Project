from app.controller import add_chat, add_chat_question, add_chat_response, get_user
from flask import render_template,flash, redirect, url_for, session, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from app.chat import chat_blueprint

# Initialize the components for perform_query
os.environ["OPENAI_API_KEY"] = "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"

script_path = os.path.abspath(__file__)
faq_path = os.path.join(os.path.dirname(script_path), 'docs', 'faq.csv')
loader = CSVLoader(faq_path, encoding='utf-8')
question_bank = loader.load()

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(question_bank, embeddings)
retriever = db.as_retriever()


def perform_query(query):
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name='gpt-3.5-turbo'), chain_type="stuff", retriever=retriever)
    response = qa.run(query)
    return response


# handle query
@chat_blueprint.route('/perform_query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data['query']
    response = perform_query(query)
    return jsonify({'response': response})

# chat page
@chat_blueprint.route("/chat/")
def chat():
    # If the user is not logged in, redirect to the login page
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    username = get_user().first_name
    return render_template("chat_view.html", display = True, username=username)


@chat_blueprint.route('/logout/')
def logout():
    # Clear the session
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))


@chat_blueprint.route('/send-text/', methods=['POST'])
def save_chat():
    # Get the chat message data from the frontend
    data = request.get_json()
    questions = data['questions']
    print(questions[0])
    responses = data['responses']

    # Get the user id from the session and add chat to the database
    user_id= session['id']
    chat_id = add_chat(user_id)

    for question in questions:
        content = question[:-23]
        timestamp = question[(len(question)-23):]
        add_chat_question(chat_id, content, timestamp)
    
    for response in responses:
        content = response[:-23]
        timestamp = response[(len(response)-23):]
        add_chat_response(chat_id, content, timestamp)

    return jsonify({"success" : True, 'message': "Chat successfully saved"}), 200

# Disable caching for the chat page
@chat_blueprint.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Vary'] = 'User-Agent'
    return response