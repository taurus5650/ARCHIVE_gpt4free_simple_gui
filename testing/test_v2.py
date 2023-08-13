import g4f

# Initialize conversation
conversation = []

while True:
    # User input
    user_input = input("You (type '!!' for new line): ")

    # Allow the user to use "!!" to indicate a new line
    user_input_lines = user_input.split("!!")

    for line in user_input_lines:
        # Add user message to conversation
        conversation.append({"role": "user", "content": line.strip()})

        # Create API request
        request_payload = {
            "model": "gpt-3.5-turbo",
            "provider": g4f.Provider.opchatgpts,
            "messages": conversation
        }

        # Make the API request
        response = g4f.ChatCompletion.create(**request_payload, stream=False)

        # Get and print assistant response
        assistant_response = response
        print("Bot:", assistant_response)

        # Add assistant message to conversation
        conversation.append({"role": "assistant", "content": assistant_response})
