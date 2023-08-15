
# Simple_Chatbot
Creating a simple chatbot program that uses the OpenAI "text-davinci-003" NLP pretrained model to generate responses for user input.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Version Control](#version-control)
- [License](#license)


## Introduction

This project demonstrates the creation of a basic chatbot that utilizes the OpenAI "text-davinci-003" model to generate conversational responses. The chatbot engages in interactive conversations with users, providing answers and responses based on the input it receives.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:

- Python (3.x)
- OpenAI API key (sign up at https://beta.openai.com/signup/ if you don't have one)
- Visit your API Keys page to retrieve the secret API key you'll use in your requests

## Usage
Choose one of the following methods to run the chatbot:
### Method 1: Create an Environment and Install Dependencies

1. Open a terminal (e.g., Anaconda Prompt)
 
2. Create and activate a virtual environment (optional but recommended):
   
    ```bash
    conda create --name chatbot_env
    conda activate chatbot-env
    
3. navigate to the project folder (e.g., cd C:\Users\YourUsername\Projects\Chatbot)

4. Install the required dependencies:
    ```bash
    pip install openai

5. Paste the API key you obtained into the designated location within the `chatbot.py` file (openai.api_key = 'your_API_Key')
   
6. Run the chatbot script:

   ```bash
   python chatbot.py

7.Engage in a conversation with the chatbot. Type your messages and receive responses based on the input.

8.To exit the conversation, type "exit."

### Method 2: Run the python file in an IDE

1. Open the `chatbot.py` file in your preferred IDE.

2. Install the OpenAI library using the terminal within your IDE:
    ```bash
    pip install openai

3. Paste the API key you obtained into the designated location within the `chatbot.py` file (openai.api_key = 'your_API_Key')
 
4. Run the `chatbot.py` script in your IDE

5.Engage in a conversation with the chatbot. Type your messages and receive responses based on the input.

6.To exit the conversation, type "exit."

## Implemented Functions

Here's a brief overview of the functions implemented in the `chatbot.py` script:

### `generate_response(input_text)`

This function generates a response from the GPT-3 model based on the user's input text.

**Parameters:**
- `input_text` (str): The user's input text as a prompt for generating the response.

**Returns:**
- A string containing the generated response from the GPT-3 model.

**Usage Example:**

    response = generate_response("Give me 5 things to do every morning")
 
print("Chatbot:", response) ; (To view a collection of uploaded screenshots)

The `main()` function on the other hand initializes the chatbot conversation loop, where users can interact with the chatbot by typing 
their input, and the bot responds using the generate_response() function.

## Configuration

To configure the chatbot behavior, you can modify the following settings in the `chatbot.py` script:

- `api_key`: Set your OpenAI API key.
- `model`: Choose the NLP language model engine to use. For example, `model = "text-davinci-003"` specifies the text-    davinci-003 engine. You can replace this with other GPT-3 engines as needed.
- `prompt`: The input text provided to the language model to generate responses.
- `max_tokens`: Adjust the maximum number of tokens for generated responses. This parameter controls the length of       the response.
- `n`: Specifies the number of responses to generate from the model. Use `n=1` to generate a single response.
- `stop`: An optional string that can be used to specify an early stopping point for the generated text.
- `temperature`: Controls the randomness of the generated text. A higher value (e.g., 0.8) makes the output more         random, while a lower value (e.g., 0.2) makes it more focused.

## Contributing
Contributions are welcome! If you'd like to enhance the chatbot's capabilities, fix bugs, or make any improvements, 

please follow these steps:

- Fork the repository.
  
- Create a new branch for your feature or bug fix.
  
- Make your changes and ensure that the code is well-documented.
  
- Open a pull request.

## Version control
 
This project uses Git and GitHub for version control. Below are the steps to set up version control, commit your code, connect to GitHub, and push your code to the repository.
By consistently using essential Git commands such as `clone`, `add`, `commit`, `push`, `pull`, you can efficiently tracked changes and maintained the integrity of the codebase. GitHub issues were utilized to keep track of tasks, enhancements, and bugs, enabling structured project management.

First, navigate to your local project folder (where your code is) using the Git Bash terminal (e.g.,cd Desktop/chatbot
)

### Clone and Navigate to the Repository

To get started with the project, you can clone the existing repository from GitHub and navigate into the cloned directory using the following commands in Git Bash:


    git clone https://github.com/your name/repository_name.git
    
 

### Git Configuration

Before you begin, make sure to configure your Git settings with your name and email using the following commands:

  
    git config --global user.name "Your Name"
    git config --global user.email "youremail@example.com"



1- Initialize Git
To start version control for your project, navigate to your project folder in Git Bash and run:

       
    git init

2-Commit Code changes
    
    git add .  # Stage all changes for commit
    git commit -m "Initial commit"  # Commit with a descriptive message

3-Connect to GitHub

To connect your local repository to your GitHub repository, use the following command (replace <repository_url> with your GitHub repository URL):

  
    git remote add origin <repository_url>

4-Push Your Code
Once connected to GitHub, push your code to your GitHub repository (I pushed it in the `main` branch) using the following command:

  
    git push -u origin main


## License
This project is governed by the terms of the MIT License. For further details, please refer to the LICENSE file.

