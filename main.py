from model import Model

model = Model()

while True:
    user_input = input("입력해주세요 : ")

    PROMPT = '''당신은 유용한 AI 어시스턴트입니다. 사용자의 질의에 대해 친절하고 한국어로 정확하게 답변해야 합니다.'''

    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": user_input},
    ]

    print(model.chat(messages))

