import random
import numpy as np
from sklearn.cluster import KMeans
import pygame


BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 105, 180)
WHITE = (255, 255, 255)

class Rat:
    def __init__(self, man, woman):
        self.man = man
        self.woman = woman
        self.harizm = 0.2
        self.model = KMeans(n_clusters=2, n_init=1) 

    def train(self):
        X = []
        for _ in range(self.man):
            X.append([0])

        for _ in range(self.woman):
            X.append([1])

        return self.model.fit(X)

    def predict(self):
        random_stat = [[random.random()]]
        self.predict_cluster = self.model.predict(random_stat)

        if self.predict_cluster == 0:
            self.man += 1
        else:
            self.woman += 1
            
        if random.random() < self.harizm:

            if self.predict_cluster == 0:
                self.woman -= 10
                self.man += 10
            else:
                self.man -= 10
                self.woman += 10

        return self.man, self.woman



pygame.init()


screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ДИНАМИКА")

clock = pygame.time.Clock()


n = Rat(100, 100)

num_iterations = 1000   

for _ in range(num_iterations):
    n.train()

for _ in range(1000):
    man, woman = n.predict()

    screen.fill(BLACK)  

    
    pygame.draw.rect(screen, BLUE, (100, 100, man, 50))  
    pygame.draw.rect(screen, PINK, (100, 200, woman, 50))  

    
    font = pygame.font.Font(None, 36)
    text = font.render("сочных мужчин: " + str(man) + "  посудомоек: " + str(woman), True, WHITE)
    screen.blit(text, (100, 300))

    pygame.display.flip()  

    clock.tick(60)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
