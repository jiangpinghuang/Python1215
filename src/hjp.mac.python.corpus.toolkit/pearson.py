import math

def pearson(p, t):
    x = []
    sx = 0
    y = []
    sy = 0
    for lx in open(p, 'r'):
        x.append(float(lx.strip()))
        sx = sx + float(lx.strip())
    for ly in open(t, 'r'):
        y.append(float(ly.strip()))
        sy = sy + float(ly.strip())
    print sx
    print sy
    t = len(x)
    ax = sx / t
    ay = sy / t
    print ax
    print ay
    for i in range(t):
        x[i] = x[i] - ax
        y[i] = y[i] - ay
    
    xy = 0
    xn = 0
    yn = 0
    print x
    print y
    for j in range(t):
        xy = xy + x[j] * y[j]
        xn = xn + x[j] * x[j]
        yn = yn + y[j] * y[j]
    
    print xy
    print math.sqrt(xn)*math.sqrt(yn)
    val = xy / (math.sqrt(xn)*math.sqrt(yn))
    print val


if __name__ == "__main__":
    p = "/home/hjp/Downloads/p.txt"
    t = "/home/hjp/Downloads/t.txt"
    pearson(p, t)