import pygame
import random
import numpy as n
background_color = (251,247,245)
original_grid_element_color = (52, 31, 151)
buffer = 5

def new_sudoku():
    sudoku = n.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ])
    new_sudoku = n.copy(sudoku)

    # Swap rows within a block
    def swap_rows_in_block(grid):
        for block in range(0, 9, 3):
            rows = n.arange(block, block + 3)
            n.random.shuffle(rows)
            grid[block:block+3] = grid[rows]
        return grid

    # Transpose the grid 
    def transpose(grid):
        return grid.T
        

    # Swap columns within a block
    def swap_columns_in_block(grid):
        if n.random.choice([True, False]):
            for block in range(0, 9, 3):
                columns = n.arange(block, block + 3)
                n.random.shuffle(columns)
                grid[:, block:block+3] = grid[:, columns]
        return grid

    #Calling the functions
    new_sudoku = swap_rows_in_block(new_sudoku)
    new_sudoku = transpose(new_sudoku)
    new_sudoku = swap_columns_in_block(new_sudoku)

    return new_sudoku
grid=new_sudoku()
sdoku=grid.copy()

def remove_numbers(puzzle: list[list]): 
    for i in range(34):
        a=random.randint(0,8)
        b=random.randint(0,8)
        if puzzle[a][b] !=0:
            puzzle[a][b]=0
remove_numbers(grid)
grid_original=grid.copy()

def insert(win, position,myfont):
    i,j = position[1], position[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48): 
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10): 
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = myfont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return


def check(win,myfont):
    if (sdoku==grid).all():
        pass
    else:
        for i in range(9):
            if (grid[i]==sdoku[i]).all():
                pass
            else:
                for j in range (9):
                    if grid[i][j]==0:
                        pass
                    elif sdoku[i][j]==grid[i][j]:
                        pass
                    else:
                        text= "Wrong number, Try Again"
                        text_surface=myfont.render(text,True,(255,0,0))
                        text_rect=text_surface.get_rect()
                        text_rect.center=(250,550)
                        win.blit(text_surface,text_rect)
                        pygame.display.update(text_rect)
                        pygame.draw.rect(win,(251,247,245),text_rect)

                        
def finalcheck(win,myfont):
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==0:
                return
    if (grid==sdoku).all():
        text= "YOU WON!!"
        text_surface=myfont.render(text,True,(0,255,50))
        text_rect=text_surface.get_rect()
        text_rect.center=(250,550)
        win.blit(text_surface,text_rect)
    else:
        text= "YOU LOSE"
        text_surface=myfont.render(text,True,(255,0,0))
        text_rect=text_surface.get_rect()
        text_rect.center=(250,550)
        win.blit(text_surface,text_rect)

 


def main():    
    pygame.init()
    win = pygame.display.set_mode((550, 750))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
     
    
    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(win, (0,50,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(win, (0,50,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(win, (50,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(win, (50,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
     
    for i in range(0, 9):
        for j in range(0, 9):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 ))
                 
    pygame.display.update()
    
    while True: 
      
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50),myfont)
                check(win,myfont)
                finalcheck(win,myfont)
                
            if event.type == pygame.QUIT:
                pygame.quit()
                return
   
main()
 