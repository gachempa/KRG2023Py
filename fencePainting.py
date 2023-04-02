#Fence painting USACO easy problem

a, b = map(int, input(" Enter a b separated with a space: ").split())
c, d = map(int, input(" Enter c d separated with a space: ").split())

paintedlength = 0

# print(a, b, c, d)

# making sure that the variables are in sequence, a < c
if(c<a):
    x = a
    a = c
    c = x

    y = b
    b = d
    d = y

# print(a, b, c, d)

if(c>b):
    paintedlength = (b-a) + (d-c)
    # print("Painted lenght c>b = ", paintedlength)
elif(d>b and c<b):
    paintedlength = (d-a)
else:
    paintedlength = b-a

print("Painted lenght = ", paintedlength)

