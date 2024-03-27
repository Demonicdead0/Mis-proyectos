import pygame, sys
pygame.init()


def coordernadas(coord_x,coord_y):
    return (coord_x//10), (coord_y//10)

size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game = True
pausa = True
color = {
    "BLACK": (0,0,0),
    "WHITE": (255,255,255)
}

class cuadrado:
    diametro = 9
    estado = color["BLACK"]
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def mostrar(self):
        pygame.draw.rect(screen, self.estado, (self.x, self.y, self.diametro, self.diametro))
    def cambio(self):
        if self.estado == color["BLACK"]:
            self.estado = color["WHITE"]
        else:
            self.estado = color["BLACK"]

celdas = []
for i in range(80):
    for j in range(50):
        celda = cuadrado(i*10, j*10)
        celdas.append(celda)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            coord_x,coord_y = coordernadas(position[0], position[1])
            celdas[coord_x*50 + coord_y].cambio()
            print(celdas[coord_x*50 + coord_y].estado)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print(pausa)

                if pausa:
                    pausa = False
                else:
                    pausa = True
            if event.key == pygame.K_e:
                for i in celdas:
                    i.estado = color["BLACK"]
    screen.fill(color["WHITE"])
    cambios = []

    if not pausa:
        
        for x in range(1,79):
            for y in range(1,49):
                vivos = 0
                for s in [-1,0,1]:
                    for j in [-1,0,1]:
                        if s== 0 and j == 0:
                            continue
                        if celdas[(x-s)*50 + y-j].estado == color["WHITE"]: vivos += 1
                if vivos == 3 and celdas[x*50 + y].estado == color["BLACK"]: cambios.append(x*50 + y)
                # Una célula viva con 2 o 3 células vecinas vivas sigue viva,
                #  en otro caso muere (por "soledad" o "superpoblación").
                if vivos in [2,3] and celdas[x*50 + y].estado == color["WHITE"]:
                    continue
                else:
                    if celdas[x*50 + y].estado == color["WHITE"]:
                        cambios.append(x*50 + y)
    
    for celdita in celdas:
        celdita.mostrar()
    
    pygame.draw.line(screen, color["WHITE"],(0,0),(0,500))
    pygame.draw.line(screen, color["WHITE"],(0,0),(800,0))
    pygame.display.flip()
    clock.tick(20)
    for eventos in cambios:
        celdas[eventos].cambio()


if not game:
    sys.exit()
