intro=input("Give AN Introduction")
print(intro)
charactercount=0
wordcount=1
for character in intro:
    charactercount=charactercount+1
    if(character==" "):
        wordcount=wordcount+1
print(wordcount,charactercount)