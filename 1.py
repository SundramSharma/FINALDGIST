inp = input("Enter a list of words: ")
words = inp.split()
lowerwords = []
for i in words:
  lowerwords.append(i.lower())

worddict={}
for i in lowerwords:
  if i not in worddict:
    worddict[i]=1
  else:
    worddict[i]+=1

print(worddict)