import g4f

# Define the message for the request
user_input = """
hello
"""
request_messages = [{"role": "user", "content": user_input}]

# Capture the request JSON
request_payload = {
    "model": "gpt-3.5-turbo",
    "provider": g4f.Provider.DeepAi,
    "messages": request_messages
}

# Make the API request
response = g4f.ChatCompletion.create(**request_payload, stream=False)

# Print the request JSON and API response
print("Request Payload:")
print(request_payload)
print("\nAPI Response:")
print(response)
