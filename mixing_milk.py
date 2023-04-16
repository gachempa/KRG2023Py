input_all = open("mixmilk.in")

first = list(map(int,input_all.readline().strip().split()))
second = list(map(int,input_all.readline().strip().split()))
third = list(map(int,input_all.readline().strip().split()))

capacity1 = first[0]
capacity2 = second[0]
capacity3 = third[0]

amount1 = first[0]
amount2 = first[1]
amount3 = first[2]

count = 0

while True:
    if count == 100:
        break

    #one to two
    if amount1 + amount2 >capacity2:
        amount1 = (amount1+amount2) - capacity2
        amount2 = capacity2
    else:
        amount2 = amount1 + amount2
        amount1 = 0

    #one to two
    if amount2 + amount3 >capacity3:
        amount2 = (amount2+amount3) - capacity3
        amount3 = capacity3
    else:
        amount3 = amount2 + amount3
        amount2 = 0
    count +=1
    
if count == 100:

    #one to two
    if amount1 + amount2 >capacity2:
        amount1 = (amount1+amount2) - capacity2
        amount2 = capacity2
    else:
        amount2 = amount1 + amount2
        amount1 = 0
    




