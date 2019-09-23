fib = open("2600-0.txt")
line = fib.read()  
def rotate_pair(): 
for i in line:
        word = line.strip()
        b = word.sort()
        c = 0
        if b[i] == b[i+1]:
                print(b)
        c = c + 1
        my_set  = set(b)
        print("Unique words are:", my_set)





