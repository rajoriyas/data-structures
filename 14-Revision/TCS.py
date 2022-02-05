import math
H = int(input())
A, B, C, D = map(int, input().split())
V1, V2, V3, V4 = map(int, input().split())
D1, D2, D3, D4 = map(str, input().split())

def dir(D):
    if D == 'U':
        D = 1
    elif D == 'D':
        D = -1
    return D
D1 = dir(D1)
D2 = dir(D2)
D3 = dir(D3)
D4 = dir(D4)
#print(D1, D2, D3, D4)

def minima(P1, P2, P3, V1, V2, V3, D1, D2, D3):
    P1P2 = math.sqrt((H**2)+(abs(P1-P2)**2))
    P2P3 = math.sqrt((H**2)+(abs(P2-P3)**2))
    Diagonal_P3P1 = math.sqrt((H**2)+(H**2))
    P3P1 = math.sqrt(Diagonal_P3P1**2+(abs(P3-P1)**2))
    S = (P1P2+P2P3+P3P1)/2
    area = math.sqrt(S*(S-P1P2)*(S-P2P3)*(S-P3P1))
    while True:
        P1P2 = math.sqrt((H**2)+(abs(P1-P2)**2))
        P2P3 = math.sqrt((H**2)+(abs(P2-P3)**2))
        P3P1 = math.sqrt(Diagonal_P3P1**2+(abs(P3-P1)**2))
        S = (P1P2+P2P3+P3P1)/2
        area = min(area, math.sqrt(S*(S-P1P2)*(S-P2P3)*(S-P3P1)))
        if (P1==H or P1==0) and (P2==H or P2==0) and (P3==H or P3==0):
        	break
        P1 += (V1*D1)
        if P1<0:
        	P1=0
        elif P1>H:
        	P1=H
        P2 += (V2*D2)
        if P2<0:
        	P2=0
        elif P2>H:
        	P2=H
        P3 += (V3*D3)
        if P3<0:
        	P3=0
        elif P3>H:
        	P3=H
    return area

def maxima(P1, P2, P3, V1, V2, V3, D1, D2, D3):
    P1P2 = math.sqrt((H**2)+(abs(P1-P2)**2))
    P2P3 = math.sqrt((H**2)+(abs(P2-P3)**2))
    Diagonal_P3P1 = math.sqrt((H**2)+(H**2))
    P3P1 = math.sqrt(Diagonal_P3P1**2+(abs(P3-P1)**2))
    S = (P1P2+P2P3+P3P1)/2
    area = math.sqrt(S*(S-P1P2)*(S-P2P3)*(S-P3P1))
    while True:
        P1P2 = math.sqrt((H**2)+(abs(P1-P2)**2))
        P2P3 = math.sqrt((H**2)+(abs(P2-P3)**2))
        P3P1 = math.sqrt(Diagonal_P3P1**2+(abs(P3-P1)**2))
        S = (P1P2+P2P3+P3P1)/2
        area = max(area, math.sqrt(S*(S-P1P2)*(S-P2P3)*(S-P3P1)))
        if (P1==H or P1==0) and (P2==H or P2==0) and (P3==H or P3==0):
        	break
        P1 += (V1*D1)
        if P1<0:
        	P1=0
        elif P1>H:
        	P1=H
        P2 += (V2*D2)
        if P2<0:
        	P2=0
        elif P2>H:
        	P2=H
        P3 += (V3*D3)
        if P3<0:
        	P3=0
        elif P3>H:
        	P3=H
    return area

def nearest(val):
    if val>int(val)+0.5:
        return math.ceil(val)
    else:
        return math.floor(val)

# In ABC,
ABC = maxima(A, B, C, V1, V2, V3, D1, D2, D3)
# In ADC,
ADC = maxima(A, D, C, V1, V4, V3, D1, D4, D3)

max_ = nearest(4*(((ABC)+(ADC))**2))

# In ABC,
ABC = minima(A, B, C, V1, V2, V3, D1, D2, D3)
# In ADC,
ADC = minima(A, D, C, V1, V4, V3, D1, D4, D3)

min_ = nearest(4*(((ABC)+(ADC))**2))

print(max_, min_)
