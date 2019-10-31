for i in range(1,10):
    for j in range(1, i+1):
        f = i*j
        print(f)
for i in range (1,10):
    empty = []
    for j in range(1,i+1):
        f = i*j
        empty.append(f)
    print(empty)



# # A simpler approach :
for i in range(1,10):
    for j in range(1, i+1):
        print((i *j) ,end=" ")
    print("\n")  