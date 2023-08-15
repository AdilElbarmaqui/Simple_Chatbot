import openai

# Setting your OpenAI API key 
openai.api_key = 'your_API_Key'


def generate_response(input_text):
    response = openai.Completion.create(
        model = "text-davinci-003",  # or another GPT-3 engine
        prompt=input_text,
        max_tokens=1000, # Adjust as needed
        n=1, 
        stop = None,
        temperature = 0.5,
        )
    return response.choices[0].text.strip()


def main():
    print("Chatbot: Hello! I'm a basic conversational chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input) #we call the generate_response function for every input text
        print("Chatbot:", response)

if __name__ == '__main__':
    main()



