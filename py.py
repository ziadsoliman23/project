#base image 
import string
#read files
file1=open("/home/ziad/Desktop/docker/project/New Empty File", "r")
file1=file1.read().lower()
file2=open("/home/ziad/Desktop/docker/project/New Empty File2", "r")
file2=file2.read().lower()
#to split words
book1=set(file1.translate(str.maketrans('', '', string.punctuation)).split())
book2=set(file2.translate(str.maketrans('', '', string.punctuation)).split())
intersection = book1.intersection(book2) 
print(intersection)
print(len(intersection))
diff = book1 - book2
print(diff)
print(len(diff))