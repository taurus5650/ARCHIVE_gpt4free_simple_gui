import logging
from flask import Flask, render_template, request

import g4f

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Initialize conversation
conversation = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        conversation.append({"role": "user", "content": user_input})

        request_payload = {
            "model": "gpt-3.5-turbo",  # gpt-3.5-turbo
            "provider": g4f.Provider.DeepAi,
            "messages": conversation
        }

        response = g4f.ChatCompletion.create(**request_payload, stream=False)
        assistant_response = response

        conversation.append(
            {"role": "assistant", "content": assistant_response})
        logging.debug(conversation)

    return render_template('gui.html', conversation=conversation)


if __name__ == '__main__':
    config = {
        'host': '0.0.0.0',
        'port': 1336,
        'debug': True
    }

    app.run(**config)
