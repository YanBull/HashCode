rows, columns, min_of_each_ingridient, cells_max_inoneslice  = 0, 0 ,0 ,0
pizza = []
pizza2 = []

with open(r'C:\Users\Yan\Downloads\b_small.in') as f: # исправить а свой путь
    for c in f.read():
        pizza.append(c)
        pizza2.append(c)



def array_set_to_zero(a=[]):
    b = len(a)
    for i in range(b):
        a[i] = 0


j = 0
k = 0
intData2 = [0, 0, 0, 0]
intData = []

for i in range(len(pizza)):
    a = ord(pizza[i])

    if a < 58 and a > 31:
        b = chr(a)
        intData.append(b)
        pizza2.remove(b)
        pizza2.remove("\n")
del pizza2[0]

a = 0

for i in range(len(intData)):
    a = ord(intData[i])
    if a > 48 and a < 57:
        a = a - 48
        intData2[j] = a
        j += 1

print("\n")
print(pizza2)
print("\n")

rows = intData[0]
columns= intData2[1]
min_of_each_ingridient =intData2[2]
cells_max_inoneslice = intData2[3]



