import random
answer = random.randrange(0,99)
n=0
for i in range(10):
    guess = int(input("숫자를 입력하세요(범위:0~99): "))
    if guess == answer:
        n+=1
        print("정답입니다. {}번 만에 맞추셨습니다.".format(n))
        print("게임이 종료되었습니다.")
        break
    elif guess>answer:
        print("아닙니다. 더 작은 숫자입니다.")
        n+=1
    elif guess<answer:
        print("아닙니다. 더 큰 숫자입니다.")   
        n+=1