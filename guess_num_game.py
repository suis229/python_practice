import math
import random

print("数値当てクイズ")

while True:
  try:
    n, m = input("数値の最小値と最大値を空白区切りで入力してください: ").split()
    if n > m:
        print("最小値を先に入力してください")
        continue
    n = int(n)
    m = int(m)
    break
  except ValueError:
    print("正しく入力してください")

answer = random.randint(n,m)
number_attempt = (m - n) // 3

print("クイズ開始")
for i in range(number_attempt):
    while True:
        try:
            guess = input(str(n) + "以上" + str(m) + "以下の数値を入力してください：")
            guess = int(guess)
            if guess < n or m < guess:
                print("範囲外の数値が入力されました。入力しなおしてください。")
                continue
            break
        except ValueError:
            print("正しく入力してください")


    if guess == answer:
        print("正解！")
        break
    elif i == number_attempt-1:
        print("残念")
    else:
        print("不正解です。挑戦回数はあと" + str(number_attempt - i - 1) + "回です。")

