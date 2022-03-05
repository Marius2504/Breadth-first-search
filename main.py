def BFS(node):
    queue = [node]
    index = 0
    check[node] = 1
    while len(queue) > index:
        node = queue[index]
        for i in matrix[node]:
            if check[i] == 0:
                queue.append(i)
                check[i] = 1
                father[i] = node
                distance[i] = distance[node] + 1
        index = index + 1

def read(name):
    graph = name.readlines()
    for line in graph:
        line = line.split()
        ind = line.index(':')
        numb = int(line[ind-1])
        for elm in range(ind+1,len(line)):
            matrix[numb].append(int(line[int(elm)]))

name = open("graph")
n = int(name.readline())
matrix = [[] for i in range(n+1)]
read(name)
father = [0 for j in range(n+1)]
distance = [0 for j in range(n+1)]
check = [0 for j in range(n+1)]
BFS(1)
print(matrix)
print(father)

