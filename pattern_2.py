# For row declaration
n = int(input("Enter the no of rows: ")) 

# To initialize count varibale
a = n

for i in range(0, n+1):
    a = a - 1
    print(str(a) *i + " " * (n-i))
         