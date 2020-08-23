import hangman
import random
a=[]
while True:
    y=input("適当な名前を入力してください")
    if y=="quit":
        break
    a.append(y)
    print(a)
u=random.randint(0,len(a)-1)
answer=a[u]    
hangman.hangman1(answer)
print(u)