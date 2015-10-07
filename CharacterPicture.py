#By: Andrew Morales
#edited by David Kamkar
#Code takes a list? and prints the variables it one at a time.
#https://automatetheboringstuff.com/chapter4/
#the project is at the end of the page

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printGrid(gridPicture):
	listNumber = 0
	indexNumber = 0
	rowPrint = ''
	while indexNumber < len(grid[0]): 
		while listNumber < len(gridPicture): #length of the grid 9, want to print 
			rowPrint+=gridPicture[listNumber][indexNumber]
			listNumber+=1
		print(rowPrint)
		indexNumber= indexNumber+1

printGrid(grid)
#print len(grid)
#print len(grid[0])