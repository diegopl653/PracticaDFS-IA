laberinto = [["S", ".", "#"], 
             [".", "#", "."], 
             [".", ".", "Q"]]

filas = len(laberinto)
columnas = len(laberinto[0])

direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

camino = []


def dfs(x, y, visitado):
    if x < 0 or x >= filas or y < 0 or y >= columnas:
        return False
    if laberinto[x][y] == "#" or (x, y) in visitado:
        return False

    camino.append((x, y))
    visitado.add((x, y))

    if laberinto[x][y] == "Q":
        return True

    for dx, dy in direcciones:
        if dfs(x + dx, y + dy, visitado):
            return True

    camino.pop()
    return False


for i in range(filas):
    for j in range(columnas):
        if laberinto[i][j] == "S":
            inicio = (i, j)

visitado = set()
if dfs(inicio[0], inicio[1], visitado):
    print("Camino encontrado hasta el queso:")
    print(camino)
else:
    print("No se encontró un camino al queso.")
