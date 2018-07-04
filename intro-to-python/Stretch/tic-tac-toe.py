
# the grid (x,y) coords
grid = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
player1 = []
player2 = []
moves= []

# draw the grid on the screen
def draw_grid():
    b1, b2, b3 = "X", "X", "X"
    b4, b5, b6 = "O", "X", "X"
    b7, b8, b9 = "O", "O", "X" 
    
    print(" --- --- ---")
    print("|",b1,"|",b2,"|",b3,"|")
    print(" --- --- ---")
    print("|",b4,"|",b5,"|",b6,"|")
    print(" --- --- ---")
    print("|",b7,"|",b8,"|",b9,"|")
    print(" --- --- ---")
draw_grid()

def take_input(): 
    valx = int(input("Enter the 'X' cood: "))
    valy = int(input("Enter the 'y' cood: "))
    val = (valx,valy)
    return val

print(take_input())
print("a"+str(1))
#def play():
    
##valx = int(input("THe axdd: "))
##valy = int(input("THe axdd: "))
##val =(valx,valy)
##print(val)

 