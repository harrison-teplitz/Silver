from openai import OpenAI
client = OpenAI()
import json

def call_chat(name,description,responses, query):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Your name is {name} and\
             these are your basic attributes: {description}.\
             Please refer to these questions and answers to learn more about yourself:\
             {responses}"},
            {
                "role": "user",
                "content": query
            }
        ]
    )
    return(completion.choices[0].message)

''' #Example of context
context = [{"role": "system", "content": f"Your name is {name} and\
             these are your basic attributes: {description}.\
             Please refer to these questions and answers to learn more about yourself:\
             {responses}"}]
'''
def call_chat_w_context(context):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=context)
    return(completion.choices[0].message.content)

'''For testing

test_name = "Beth"
test_description = "White girl in her late 20s"
with open(f"{test_name}_context.json", 'r') as json_file:
        initial_context = json.load(json_file)
context = [{"role": "system", "content": f'Your name is {test_name} and\
             these are your basic attributes: {initial_context["description"]}.\
             Please refer to these questions and answers to learn more about yourself:\
             {initial_context["responses"]}'}]
test_query = "tell me about your childhood"
context.append({"role": "user", "content": test_query})

print(call_chat_w_context(context))
'''
