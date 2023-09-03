import openai

# Initialize your conversation memory as an empty dictionary
conversation_memory={}

# Setting your OpenAI API key 
openai.api_key = 'Your_Api_Key'


def generate_response(input_text):
    
    conversation_memory["user_input"] = input_text
    
    # Use the conversation history in the prompt
    prompt = "\n".join(list(conversation_memory.values()))
    
    response = openai.Completion.create(
        model = "text-davinci-003",  # or another GPT-3 engine
        prompt=prompt,
        max_tokens=1000, # Adjust as needed
        n=1, 
        stop = None,
        temperature = 0.5,)
    
    reply = response.choices[0].text.strip()
    
    # Add the chatbot's reply to the conversation memory
    conversation_memory["chatbot_reply"] = reply
    
    return reply



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



