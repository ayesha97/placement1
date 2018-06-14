def smallest(a,b,c):
    if (a<b)and(a<c):
        smallest=a
    elif (b<a) and (b<c):
        smallest=b
    else:
        smallest=c
    x = int(input("enter a:"))
    y = int(input("enter b:"))
    z = int(input("enter c:"))
    print("the smallest number is ",smallest)
