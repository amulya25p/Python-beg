#dictionay and word count in file. 

file=input("enter the file name   ")
fhand=open(file)

count=dict()
for line in fhand:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1


print(count)
    
