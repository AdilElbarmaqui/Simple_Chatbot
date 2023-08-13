import openai

# Setting my OpenAI API key 
openai.api_key = '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'


def generate_response(input_text):
    response = openai.Completion.create(
        engine="davinci",  # or another GPT-3 engine
        prompt=input_text,
        max_tokens=100  # Adjust as needed
    )
    return response.choices[0].text.strip()


def main():
    print("Chatbot: Hello! I'm a basic conversational chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input) #we call the generate_response for every input text
        print("Chatbot:", response)

if __name__ == '__main__':
    main()



