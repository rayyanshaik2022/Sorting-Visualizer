import pygame
from settings import *
from button import Button
import random
import time
import threading

class Canvas:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('arial', 40)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.runsim = False
        self.current_sort = "Quick Sort"
        self.tick_rate = 10 # more = slower
        self.threads = []

    def new(self):

        self.array = [ [random.randint(1,40), COLORS['accent2']] for item in [1]*25 ]
        self.current_tick = 0
        self.iterations = 0

        for thread in self.threads:
            thread

        threads = []

        # switching
        self.i = 0
        self.j = 0
        self.k = 0

        # switching
        self.c = []
        self.p = 0
        self.u = 0

        if (self.current_sort == "Insertion Sort"):
            self.i = 1
            self.c = 1
        
        self.buttons_group = pygame.sprite.Group()
        self.start_button = Button((75,HEIGHT-150,200,100), ((88, 245, 140), (81, 224, 128)), self.buttons_group, 1, "Start")
        self.bubble_button = Button((300,HEIGHT-137,125,75), ((3, 186, 252), (2, 171, 232)), self.buttons_group, 1, "Bubble")
        self.selection_button = Button((450,HEIGHT-137,125,75), ((3, 186, 252), (2, 171, 232)), self.buttons_group, 1, "Selection")
        self.insertion_button = Button((600,HEIGHT-137,125,75), ((3, 186, 252), (2, 171, 232)), self.buttons_group, 1, "Insertion")
        self.quick_button = Button((750,HEIGHT-137,125,75), ((3, 186, 252), (2, 171, 232)), self.buttons_group, 1, "Quick")


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Controls update speed (FPS per second)
            self.events()
            self.sort()
            self.draw()

    def close(self):
        pygame.quit()
        quit()

    def sort(self):
        if (self.runsim):
            
            if (self.current_tick % 60 == 0): #120
                
                if (self.current_sort == "Bubble Sort"):
                    self.bubble_sort()
                if (self.current_sort == "Selection Sort"):
                    self.selection_sort()
                if (self.current_sort == "Insertion Sort"):
                    self.insertion_sort()
                if (self.current_sort == "Merge Sort"):
                    self.merge_sort()
                if (self.current_sort == "Quick Sort"):
                    self.quick_sort()
            

            self.current_tick += 1

    def bubble_sort(self):

        n = len(self.array)

        for bar in self.array:
            bar[1] = COLORS['accent2']

        def bubble_switch(self):
            while (self.i < n):

                while (self.j < n - self.i - 1):
                    
                    self.iterations += 1
                    if self.array[self.j] > self.array[self.j+1]:
                        self.array[self.j][1] = COLORS['accent3']
                        self.array[self.j+1][1] = COLORS['accent3']
                        self.array[self.j], self.array[self.j+1] = self.array[self.j+1], self.array[self.j]
                        self.j += 1        
                        return
                    self.j += 1
                
                self.j = 0
                self.i += 1
            self.runsim = False

        bubble_switch(self)
    
    def selection_sort(self):

        n = len(self.array)

        for bar in self.array:
            bar[1] = COLORS['accent2']            

        def selection_switch(self):

            while (self.i < n):

                min_index = self.i
                self.j = self.i + 1
                while (self.j < n):
                    if self.array[min_index][0] > self.array[self.j][0]:
                        min_index = self.j
                    self.j += 1
                    self.iterations += 1
                
                self.array[self.i][1], self.array[min_index][1] = COLORS['accent3'], COLORS['accent3']
                self.array[self.i], self.array[min_index] = self.array[min_index], self.array[self.i]
                

                self.j = 0
                self.i += 1
                return

        selection_switch(self)

    def insertion_sort(self):
        
        n = len(self.array)

        for bar in self.array:
            bar[1] = COLORS['accent2']

        def insertion_switch(self):

            while (self.i  < n):

                key = self.array[self.i][0]

                self.j = self.i - 1
                
                while (self.j >= 0 and key < self.array[self.j][0]):
                    self.array[self.j + 1][0] = self.array[self.j][0]
                    self.j -= 1
                    self.iterations += 1

                self.array[self.i][1], self.array[self.j + 1][1] = COLORS['accent3'], COLORS['accent3']
                self.array[self.j + 1][0] = key
                self.i += 1
                return

        insertion_switch(self)

    def merge_sort_deprecated(self):
        
        if (self.runsim == False):
            return
        
        n = len(self.array)
        for bar in self.array:
            bar[1] = COLORS['accent2']

        def merge_switch(arr):

            if (len(arr) > 1):
            
                midpoint = len(arr)//2
                Left = arr[:midpoint]
                Right = arr[midpoint:]

                merge_switch(Left)
                merge_switch(Right)

                i, j, k = 0, 0, 0

                while (i < len(Left) and j < len(Right)):
                    for bar in self.array:
                        bar[1] = COLORS['accent2']
                    if Left[i][0] < Right[j][0]:
                        arr[k][1], Left[i][1] = COLORS['accent3'], COLORS['accent3']
                        arr[k] = Left[i]
                        i += 1
                    else:
                        arr[k][1], Right[i][1] = COLORS['accent3'], COLORS['accent3']
                        arr[k] = Right[j]
                        j += 1
                    self.iterations += 1
                    self.draw()
                    time.sleep(0.1)
                    k += 1
                
                
                
                while i < len(Left):
                    for bar in self.array:
                        bar[1] = COLORS['accent2']
                    arr[k][1], Left[i][1] = COLORS['accent3'], COLORS['accent3']
                    arr[k] = Left[i] 
                    self.iterations += 1
                    i+=1
                    k+=1
                    self.draw()
                    time.sleep(0.1)
            
                while j < len(Right): 
                    for bar in self.array:
                        bar[1] = COLORS['accent2']
                    arr[k][1], Right[j][1] = COLORS['accent3'], COLORS['accent3']
                    arr[k] = Right[j] 
                    self.iterations += 1
                    j+=1
                    k+=1
                    self.draw()
                    time.sleep(0.1)
            
        
        merge_switch(self.array)
        self.threads[0].stop()
        self.threads.pop(0)
        self.runsim = False

    def merge_sort(self):

        def merge_switch(array, t_array):
            
            width = 1
            while (width < len(array)):

                i = 0
                while ( i < len(array) ):

                    left = i
                    middle = i + width
                    right = i + (2 * width)

                    merge_switch(array, left, middle, right, t_array)

                    i = i + (2 * width)

                width *= 2
        
        def merge(array, iLeft, iMiddle, iRight, t_array):
            i = iLeft
            j = iMiddle
            k = iLeft

            while ( i < iMiddle or l < iRight):
                if i < iMiddle and j < iRight:
                    if array[i] < array[j]:
                        k += 1
                        i += 1
                        t_array[k+1] = array[i+1]
                    

        self.runsim = False

    def quick_sort(self):

        def quick_setup():
            if self.p == 0:
                low = 0
                high = len(self.array) - 1

                self.c.append((low, high))
                self.p = 1

        def partition(low, high):
            pivot = self.array[high]

            pIndex = low

            for i in range(pIndex, high):

                if self.array[i][0] <= pivot[0]:

                    self.array[i], self.array[pIndex] = self.array[pIndex], self.array[i]
                    pIndex += 1
                    self.iterations += 1

            self.array[pIndex], self.array[high] = self.array[high], self.array[pIndex]

            return pIndex 

        def iterative_quick_switch():

            for bar in self.array:
                bar[1] = COLORS['accent2']

            if (self.c != []):
                 
                low = self.c[-1][0]; high = self.c[-1][1]
                self.c.pop()

                self.array[low][1], self.array[high][1] = COLORS['accent3'], COLORS['accent3']
                pivot = partition(low, high)

                if pivot - 1 > low:
                    self.c.append((low, pivot - 1))
                
                if pivot + 1 < high:
                    self.c.append(((pivot + 1), high))
                
            else:
                 self.runsim = False
            

        quick_setup()
        iterative_quick_switch()

    def draw(self):
        self.font = pygame.font.SysFont('arial', 40)
        self.screen.fill(COLORS['background'])
        pygame.draw.line(self.screen, COLORS['accent1'], (50, HEIGHT - 200), (WIDTH - 50, HEIGHT -200), 5 )

        min_point = HEIGHT - 225
        for x, bar in enumerate(self.array):
            pygame.draw.rect(self.screen, bar[1], (75 + (x * 34), min_point, 34, bar[0] * -10))
        for x, bar in enumerate(self.array):
            pygame.draw.line(self.screen, COLORS['background'], (75 + (x * 34) + 34, min_point), (75 + (x * 34) + 34, 0))

        self.buttons_group.draw(self.screen)
        
        # Top left corner text
        text = self.font.render("Iterations: " + str(self.iterations), True, (250,250,250))
        self.screen.blit(text, (75,50))
        # Top text
        text = self.font.render("Algorithm: " + self.current_sort, True, (250,250,250))
        self.screen.blit(text, (400,50))

        # text start_button
        text = self.font.render(self.start_button.text, True, (23, 23, 23))
        self.screen.blit(text, (self.start_button.rect.x + int(0.275* self.start_button.rect.width),self.start_button.rect.y+ int(0.25* self.start_button.rect.height)))

        # text bubble button
        self.font = pygame.font.SysFont('arial', 25)
        text = self.font.render(self.bubble_button.text, True, (23, 23, 23))
        self.screen.blit(text, (self.bubble_button.rect.x + int(0.21* self.bubble_button.rect.width),self.bubble_button.rect.y+ int(0.3* self.bubble_button.rect.height)))

        # text selection button
        text = self.font.render(self.selection_button.text, True, (23, 23, 23))
        self.screen.blit(text, (self.selection_button.rect.x + int(0.11* self.selection_button.rect.width),self.selection_button.rect.y+ int(0.3* self.selection_button.rect.height)))
        
        # text insertion button
        text = self.font.render(self.insertion_button.text, True, (23, 23, 23))
        self.screen.blit(text, (self.insertion_button.rect.x + int(0.13* self.insertion_button.rect.width),self.insertion_button.rect.y+ int(0.3* self.insertion_button.rect.height)))

        # text insertion button
        text = self.font.render(self.quick_button.text, True, (23, 23, 23))
        self.screen.blit(text, (self.quick_button.rect.x + int(0.13* self.quick_button.rect.width),self.quick_button.rect.y+ int(0.3* self.quick_button.rect.height)))

        pygame.display.flip()

    def events(self):
        # catch all events here
        m_x, m_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
            
            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons_group:
                    if button.rect.collidepoint(m_x, m_y):
                        button.color = button.colors[0]
                        button.recolor()

                        if (button == self.start_button):
                            self.runsim = True
                            self.new()
                        elif (button == self.bubble_button):
                            self.current_sort = "Bubble Sort"
                            self.runsim = False
                        elif (button == self.selection_button):
                            self.current_sort = "Selection Sort"
                            self.runsim = False
                        elif (button == self.insertion_button):
                            self.current_sort = "Insertion Sort"
                            self.runsim = False
                        elif (button == self.quick_button):
                            self.current_sort = "Quick Sort"
                            self.runsim = False
                        
    
                
        if (pygame.mouse.get_pressed()[0] == 1):
            for button in self.buttons_group:
                    if button.rect.collidepoint(m_x, m_y):
                        button.color = button.colors[1]
                        button.recolor()
                    elif (button.color == button.colors[1]):
                        button.color = button.colors[0]
                        button.recolor()

# create the game object
if __name__ == "__main__":
    
    c = Canvas()
    c.new()
    c.run()