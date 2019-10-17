def squaret():
    for i in range(4):
        print(i)

squaret()
def square(t,length):
    for i in range(4):
        fd(t,length)
        ld(t)
        square(bob,100)
def polygon(t,n, length):
     angle=360.0/n
     for i in range(n):
         fd(t,length)
         lt(t,angle)
         polygon(bob,7,70)
def circle(t,r):
      circumference=2 *math.pi * r
      n=50
      length=circumference/n
      polygon(t,n,length)
def circle(t,r):
    circumference=2*math.pi*r
    n=int(circumference/3)+1
    lengthh=circumference/n
    polyon(t,n,lenth)
def arc(t,r,angle):
    arc_lrngth=2*math.pi*r*anglr/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    for i in range(n):
        fd(t,step_length)
        lt(t,step_angle)
def polygon(t,n,length,angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)
def polygon(t,n,length):
    angle=360.0/n
    polyline(t,n,length,angle)
def arc(t,r,angle):
    arc_length=2*math.py*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=float(angle)/n
    polyline(t,n,step_length,step_angle)
def circle(t,r):
    arc(t,r,360)
def polyline(t,n,length,angle):
    """draws n line segments with the gien length and angle (in degrtees)betwen them. t is a turtle"""
    for i in range(n):
        fd(t,length)
        lt(t,length)
quotient=7/3
print(quotient)
remainder=7%3
print(remainder)
def print_n(s,n):
    if n <= 0:
        return
    print (s)
    print_n(s,n-1)
def draw(t,lengt,n):
    if n==0:
      return
    anle = 50
    fd(t,length*n)
    lt(t,anle)
    draw(t,length,n-1)
    rt(t,2*angle)
    draw(t,length,n-1)
    lt(t,anle)
    bk(t,length*n)
def koch(t,n):
    """draws a koch cure with length n."""
    if n<3:
        fd(t,n)
        return
    m = n/3.0
    koch(t,m)
    lt(t,60)
    koch(t,m)
    rt(t,120)
    koch(t,m)
    lt(t,60)
    koch(t,m)
def snowflake(t,n):
    """draws a snowflake (a triangle with a koch curve for each side)."""
    for i in range(3):
        koch(t,n)
        rt(t,120)
