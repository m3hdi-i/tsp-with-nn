import random

n=5

mat =[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i!=j:
            x = int(input(f'Enter distance between location {i} and location {j} : '))
            mat[i][j] = x

print('Distances Matrix is :')
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in mat]))

start= random.randint(0,n-1)
tour=[start]
total_distance=0

for i in range(n-1):

    m=next(x for x in list(range(0,n)) if x not in tour)

    for j in range(n):
        if j not in tour:
            if mat[start][j] < mat[start][m]:
                m=j

    total_distance+=mat[start][m]
    tour.append(m)
    start = m


tour.append(tour[0])
total_distance+=mat[start][tour[0]]

print(f"\nStart location : {tour[0]}")
print("Tour :",tour)
print(f"Total distance is : {total_distance}")