#grid program
#meant to be used for displaying the location of enemies and the player


#Ryan McVicker
#2/13/18

'''

  
  char grid[5][5] = {{'0','0','0','0','0'},
                     {'0','0','0','0','0'},
                     {'0','0','0','0','0'},
                     {'0','0','0','0','0'},
                     {'0','0','0','0','0'}};
  '''




class Grid:



    def __init__(self):

        self.grid = [['0','0','0','0','0'],
                     ['0','0','0','0','0'],
                     ['0','0','0','0','0'],
                     ['0','0','0','0','0'],
                     ['0','0','0','0','0']]


    def get_grid(self):
        return self.grid #simply returns the grid








