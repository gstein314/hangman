#!/usr/bin/env python
# coding: utf-8

# # Python pra chap10

# In[4]:


def hangman(word):
    wrong = 0
    stages = ["",
              "____________            ",
              "                        ",
              "|                       ",
              "|            |          ",
              "|            0          ",
              "|        　／|＼        ",
              "|        　／ ＼        ",
              "|                       ",
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してください。"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n". join(stages[0:e]))
        if "_" not in board:
            print("win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("Lose {}.".format(word))


# In[5]:


hangman("tomato")


# In[ ]:




