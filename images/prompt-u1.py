import os
import openai
import json
import time


if __name__ == '__main__':

    start = 0

    choice = "Userxx next student Courses"

    data_path = 'Your data'
    with open(data_path) as file:
        data = file.read()
    
    data = data.split('\n')

    for index, line in enumerate(data):
        data[index] = line.split(' ')[1:]

    openai.api_key =  ""
    
    save_path = 'result12.1.txt'

    for index in range(start, len(data)):

        history = '，'.join(data[index])
        
        messages=[
            {
                "role": "user", 
                "content": f"用户xx曾经交互过{history}等课程，请你从剩下的{choice}等课程中选出用户xx最有可能交互的课程,"
            }
        ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
        )

        anser = completion.choices[0].message.content
        print(f"{index + 1}/{len(data) - 1}\n", anser)

        with open(save_path, 'a') as file:
            file.write(f"{index + 1} {anser}\n")

        time.sleep(20)
