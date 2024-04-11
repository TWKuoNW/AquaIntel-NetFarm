import openai

# 替换成您的OpenAI API密钥
api_key = "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"

# 初始化OpenAI客户端
openai.api_key = api_key

# 定义一个函数来与ChatGPT进行交互
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",  # 或者选择其他引擎，根据您的需求
        prompt = prompt,
        max_tokens = 100,  # 控制生成的响应长度
        temperature = 0.7,  # 控制生成的响应创造性（可调整）
        n = 1  # 控制生成的响应数目
    )
    return response.choices[0].text

# 与ChatGPT开始对话
while True:
    user_input = input("您: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_gpt(user_input)
    print(f"ChatGPT: {response}")

print("对话结束")
