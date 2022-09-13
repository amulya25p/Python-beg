#file handling

#file opening and printing the text.......
"""fhand = open("text.txt")
count=0
for word in fhand:
    count+=1
    print(word)
print("line count", count)"""

#reading whole file at once.....
# fhand=open("text.txt")
# word=fhand.read()
# print(len(word))
# print(word[:120])

#searching 
fhand=open("text.txt")
for line in fhand:
    line=line.rstrip()
    if line.startswith('Ozymandias'):
        print(line)
        break   
    else:
        print("not found")
        break