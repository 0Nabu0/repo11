import math
def num_check(i) :
    a = i/100
    b = i%100/10
    c = i%10
    niilber = math.pow(a,3) + math.pow(b, 3) + math.pow(c, 3)
    return niilber

for i in range(100, 999) :
    if i == num_check(i) :
        print(" ",i)
        
print(num_check(i))