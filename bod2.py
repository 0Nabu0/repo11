x1 = int(input())
y1 = int(input())
z1 = int(input())
x2 = int(input())
y2 = int(input())
tsonh = x2 * y2
box1 = x1 * y1
box2 = x1 * z1
box3 = y1 * z1
if tsonh >= box1 and tsonh >= box2 and tsonh >= box3:
    print("{}, {} хэмжээтэй цонхоор хайрцаг багтна".format(x2, y2))
else :
    print("{}, {} хэмжээтэй цонхоор хайрцаг багтахгүй".format(x2, y2))