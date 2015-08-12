import math

def closest_pair(p):
    '''Returns closest pair of points p1 and p2 along with the distance of it from a list of points p.\nDividing out of divide and conquer happens here.'''
    if len(p) <=3:
       pass 
    px = sorted(p, key = lambda attribute: attribute[0])
    py = sorted(p, key = lambda attribute: attribute[1])
    p1,p2 = rec_cp(px,py)
    distance = lambda x1,y1,x2,y2: math.sqrt( ( (y2-y1)**2 + (x2-x1)**2) )
    return distance(p1[0],p1[1],p2[0],p2[1]),p1,p2

def rec_cp(px,py):
    distance = lambda x1,y1,x2,y2: math.sqrt( ( (y2-y1)**2 + (x2-x1)**2) )
    if len(px) == 1:
        print("A pair of points wasn't provided")
        return(0,0)
    elif len(px) == 2:
        return(px)
    elif len(px) == 3:
        x1,y1,x2,y2 = px[0][0], px[0][1],px[1][0],px[1][1]
        min_dis = distance(x1,y1,x2,y2)
        p1,p2 = (x1,y1),(x2,y2)
        for i in range(len(px)):
            for j in range(i+1,len(px)):
                x1,y1,x2,y2 = px[i][0], px[i][1],px[j][0],px[j][1]
                if min_dis > distance(x1,y1,x2,y2):
                    min_dis = distance(x1,y1,x2,y2)
                    p1,p2 = (x1,y1),(x2,y2)
        return p1,p2
    else:
        mid = int(len(px)//2)
        qx,qy,rx,ry = px[:mid],py[:mid],px[mid:],py[mid:]
        q1,q2 = rec_cp(qx,qy)
        r1,r2 = rec_cp(rx,ry)
        
        delta = min(distance(q1[0],q1[1],q2[0],q2[1]),distance(r1[0],r1[1],r2[0],r2[1]))

        if delta == distance(q1[0],q1[1],q2[0],q2[1]):
           p1,p2 = q1,q2
           dist = delta
        else:
           p1,p2 = r1,r2
           dist = distance(r1[0],r1[1],r2[0],r2[1])

        x_Qend = px[mid][1]
        y_S = [each for each in py if abs(x_Qend - each[0]) < delta]
        
        for i in range(len(y_S)):
            k = i + 1
            while (k < len(y_S)) and ((y_S[k][1] - y_S[i][1]) < delta):
                if distance(y_S[k][0],y_S[k][1],y_S[i][0],y_S[i][1]) < dist:
                    p1,p2 = (y_S[k][0],y_S[k][1]),(y_S[i][0],y_S[i][1])
                k+=1
        return p1,p2

points = [(0,0), (-2,0), (4,0), (1,1),(3,3), (-2,2), (5,2)]
print(closest_pair(points))
