points = [(3,4),(6,5),(1,-4),(9,0)]

def euclideanDistance(x,y):
    x1=x[0]
    y1=x[1]
    x2=y[0]
    y2=y[1]

    a = (x2-x1)*(x2-x1)
    b = (y2-y1)*(y2-y1)
    mesafe = (a+b)**0.5
    return mesafe

distance = []
for i in range(len(points)):
    for j in range(i+1,len(points)):
        mesafe = euclideanDistance(points[i],points[j])
        distance.append(mesafe) 

print(distance)           
min_distance = min(distance) 
print(min_distance)
