from openai import OpenAI
client =OpenAI(api_key="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")
prompt=" "
while True:
    prompt= input("You :")
    chat_completion= client.chat.completions.create(
        messages=[{
            "role" : "users",
            "content" : prompt
        }
            
        ],
        model="gpt-4o-mini"
    )
    response_message=chat_completion.choices[0].message.content
    print("AI :",response_message)