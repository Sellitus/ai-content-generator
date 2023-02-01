import json
import openai
import requests


def fine_tune_model(model_engine, prompt, n=1, max_tokens=1024):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


model_engine = "text-davinci-003"
initial_prompt = "Generate an extremely entertaining and funny TV script based on the show Friends, but in a world " \
                 "where every single person can't help but to fuck their lives up"
secondary_prompts = "Generate a TV script based on this initial prompt: {} and this TV script: ".format(initial_prompt)


# Load api key from the api_keys/openai file
try:
    with open('api_keys/openai') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
except FileNotFoundError as e:
    print(e)
    print('Create a file "openai" in the api_keys folder with the key on the first line of the file.')
    exit(-1)

openai_api_key = lines[0]
openai.api_key = openai_api_key

generated_text = fine_tune_model(model_engine, initial_prompt)
print('--- Generator A: ' + generated_text + '\n')

# while True:
#     generated_text = fine_tune_model(model_engine, secondary_prompts + generated_text)
#     print('--- Generator B: ' + generated_text + '\n')
#
#     generated_text = fine_tune_model(model_engine, secondary_prompts + generated_text)
#     print('--- Generator A: ' + generated_text + '\n')

generated_text = generated_text.replace('\n\n', '\n')

import pdb; pdb.set_trace()
