data_b = open("file2.txt")
data_a = open("file1.txt") 
f3 = data_a.read()
f4 = data_b.read()
a = open("file1.txt","w")
a.write(f4)
with open("file2.txt", "w")as b:
    b.write(f3)
    


