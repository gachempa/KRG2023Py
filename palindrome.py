int_number = 12321
res = [int(x) for x in str(int_number)]
reverse_res = res.copy()
reverse_res.reverse()
if res == reverse_res:
    print("true")
else:
    print("false")