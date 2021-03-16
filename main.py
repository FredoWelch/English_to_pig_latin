def Eng_to_Pig():
    words = str(input("Input Sentence:")).split()
    for word in words:
        print(word[1:] + word[0] + "ay", end = " ")


Eng_to_Pig()


