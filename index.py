import tkinter as tk

laberinto_original = [["S", ".", "#"],
                      [".", "#", "."],
                      [".", ".", "Q"]]

filas = len(laberinto_original)
columnas = len(laberinto_original[0])

TAM_CASILLA = 60
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

camino = []
laberinto = [fila[:] for fila in laberinto_original]
canvas = None
root = None

def encontrar_inicio():
    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] == "S":
                return (i, j)
    return None

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

def buscar_camino():
    global camino
    camino = []
    visitado = set()
    inicio = encontrar_inicio()
    if inicio:
        dfs(inicio[0], inicio[1], visitado)
        dibujar_laberinto()

def reiniciar():
    global laberinto, camino
    laberinto = [fila[:] for fila in laberinto_original]
    camino = []
    dibujar_laberinto()

def dibujar_laberinto():
    canvas.delete("all")
    for i in range(filas):
        for j in range(columnas):
            x1 = j * TAM_CASILLA
            y1 = i * TAM_CASILLA
            x2 = x1 + TAM_CASILLA
            y2 = y1 + TAM_CASILLA

            if laberinto[i][j] == "#":
                color = "black"
            elif laberinto[i][j] == "S":
                color = "green"
            elif laberinto[i][j] == "Q":
                color = "gold"
            else:
                color = "white"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

            if (i, j) in camino and laberinto[i][j] not in ("S", "Q"):
                canvas.create_oval(x1 + 20, y1 + 20, x2 - 20, y2 - 20, fill="blue")

def mostrar_laberinto():
    global canvas, root
    root = tk.Tk()
    root.title("Camino hacia el queso 🧀")

    canvas = tk.Canvas(root, width=columnas * TAM_CASILLA, height=filas * TAM_CASILLA)
    canvas.pack()

    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=10)

    btn_buscar = tk.Button(frame_botones, text="Buscar camino", command=buscar_camino)
    btn_buscar.pack(side=tk.LEFT, padx=5)

    btn_reiniciar = tk.Button(frame_botones, text="Reiniciar", command=reiniciar)
    btn_reiniciar.pack(side=tk.LEFT, padx=5)

    dibujar_laberinto()
    root.mainloop()

mostrar_laberinto()
