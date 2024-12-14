print("enter your mrks")
markone=int(input())
markone1=int(input())
markone2=int(input())
markone3=int(input())
markone4=int(input())
total=markone+markone1+markone2+markone3+markone4
avg=total/5
if avg>=91 and avg<=100:
    print("your greade is a1")
elif avg>=81 and avg<91:
    print("your greade is a2")
elif avg>=71 and avg<81:
    print("your greade is b1")
elif avg>=61 and avg<71:
    print("your greade is b2")
elif avg>=51 and avg<61:
    print("your greade is c1")
elif avg>=41 and avg<51:
    print("your greade is c2")
elif avg>=31 and avg<41:
    print("your greade is d1")
elif avg>=21 and avg<31:
    print("your greade is d2")
elif avg>=0 and avg<21:
    print("your greade is e")
else:
    print("invaled input")