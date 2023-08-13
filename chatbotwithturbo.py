import openai

# Set your OpenAI API key here
openai.api_key = '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'

completion=openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":"Give me 5 good habits I should do every morning to start my day off right"}])

print(completion.choices[0].message.content)