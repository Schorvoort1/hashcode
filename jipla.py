f = open('a_example.txt','r')
x = f.readlines()
y = []
for i in range(len(x)):
    y.append(x[i].split())
print(y)
