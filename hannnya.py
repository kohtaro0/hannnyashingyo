import random

print("般若心経暗記")

# 問題と選択肢を定義
question = "「摩訶般若波羅蜜多心経」の次は？"
choices = ["観時在菩薩。", "京都", "大阪", "北海道"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
user_answer = int(input("回答を選択してください（1-4）: "))

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。")
