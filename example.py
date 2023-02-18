import random

# 問題と選択肢を定義
question = "日本の首都はどこですか？"
choices = ["東京", "大阪", "埼玉", "北海道"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。")

        
        
        
        
        摩訶般若波羅蜜多心経
●■観自在菩薩
行深般若波羅密多時
照見●五蘊皆空
度一切苦厄
舎利子
色不異空空不異色
色即是空空即是色
受想行識亦復如是
舎利子
是諸法空相
不生不滅不垢不浄不増不減
是故空中
無色無受想行識
無眼耳鼻舌身意
無色声香味触法
無眼界乃至無意識界
無無明亦無無明尽
乃至無老死
亦無老死尽
無苦集滅道無智亦無得
以無所得故
菩提薩垂
依般若波羅蜜多●故
心無圭礙無圭礙故無有恐怖
遠離一切顛倒夢想
究竟涅槃三世諸仏
依般若波羅蜜多●
故得阿耨多羅三藐三菩提
故知般若波羅蜜多
是大神呪是大明呪是無上呪是無等等呪
能除一切苦真実不虚
故説般若波羅蜜多呪
即説呪曰
●羯諦羯諦波羅羯諦波羅僧羯諦
菩提薩婆訶般若心経■▲



# 問題と選択肢を定義
question = "：「」の次は？"
choices = ["", "", "", ""]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")



import random

# 問題と選択肢を定義
question = "日本の首都はどこですか？"
choices = ["東京", "大阪", "埼玉", "北海道"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。")
