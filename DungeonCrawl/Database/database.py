#datbase file
#this database program is for the storing of player and enemy locations in the game

#Ryan McVicker


import sqlite3








class Database:


    def __init__(self):

        self.conn = sqlite3.connect("locations.db")
        self.c = self.conn.cursor()
        
        self.c.execute("CREATE TABLE IF NOT EXISTS player_locations(player_x INT,player_y INT)")#table for player location
        self.c.exeucte("CREATE TABLE IF NOT EXISTS enemy_locations(enemy_name TEXT, enemy_x INT, enemy_y INT)")#table for enemy location


    def update_player_location(self,playerx,playery):
        self.c.execute("UPDATE player_locations WHERE player_x = ? AND player_y = ?",(playerx,playery))


    def update_enemy_location(self,enemy_name): #should find the specific enemy with the name
        return

    #give 
    def update_player_location(self):
        
        

        
