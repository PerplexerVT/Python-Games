#Missing Features
# Program King Check - Checking
# Program Win Condition
# Program En passant

#Class for piece values
class piece():
    def __init__(self,symbol,player,value,mtype):
        self.symbol = symbol
        self.player = player
        self.value = value
        self.moves = []
        self.mtype = mtype
#Class for locations, containing a piece object
class place():
    def __init__(self,x,y,piece):
        self.x = y
        self.y = x
        self.bctrl = 0
        self.wctrl = 0
        self.piece = piece
        
        
#Update board function, used after moves
def board():
  a = [a1.piece.symbol,a2.piece.symbol,a3.piece.symbol,a4.piece.symbol,a5.piece.symbol,a6.piece.symbol,a7.piece.symbol,a8.piece.symbol]
  b = [b1.piece.symbol,b2.piece.symbol,b3.piece.symbol,b4.piece.symbol,b5.piece.symbol,b6.piece.symbol,b7.piece.symbol,b8.piece.symbol]
  c = [c1.piece.symbol,c2.piece.symbol,c3.piece.symbol,c4.piece.symbol,c5.piece.symbol,c6.piece.symbol,c7.piece.symbol,c8.piece.symbol]
  d = [d1.piece.symbol,d2.piece.symbol,d3.piece.symbol,d4.piece.symbol,d5.piece.symbol,d6.piece.symbol,d7.piece.symbol,d8.piece.symbol]
  e = [e1.piece.symbol,e2.piece.symbol,e3.piece.symbol,e4.piece.symbol,e5.piece.symbol,e6.piece.symbol,e7.piece.symbol,e8.piece.symbol]
  f = [f1.piece.symbol,f2.piece.symbol,f3.piece.symbol,f4.piece.symbol,f5.piece.symbol,f6.piece.symbol,f7.piece.symbol,f8.piece.symbol]
  g = [g1.piece.symbol,g2.piece.symbol,g3.piece.symbol,g4.piece.symbol,g5.piece.symbol,g6.piece.symbol,g7.piece.symbol,g8.piece.symbol]
  h = [h1.piece.symbol,h2.piece.symbol,h3.piece.symbol,h4.piece.symbol,h5.piece.symbol,h6.piece.symbol,h7.piece.symbol,h8.piece.symbol]
  
  ay = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
  by = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9]
  cy = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]
  dy = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9]
  ey = [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9]
  fy = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9]
  gy = [g0,g1,g2,g3,g4,g5,g6,g7,g8,g9]
  hy = [h0,h1,h2,h3,h4,h5,h6,h7,h8,h9]
  zy = [z0,z1,z2,z3,z4,z5,z6,z7,z8,z9]
  vy = [v0,v1,v2,v3,v4,v5,v6,v7,v8,v9]
  
  grid = [zy,ay,by,cy,dy,ey,fy,gy,hy,vy]
  
  county = 1
  countx = 0
  while county < 9:
    countx = 0
    while countx < 8:
      countx += 1
      if grid[county][countx].piece.player != 0:
        grid[county][countx].piece.moves = []
    county += 1  
  county = 1
  countx = 0
  while county < 9:
    countx = 0
    while countx < 8:
      countx += 1
      if grid[county][countx].piece.player != 0:
        movelist(grid[county][countx])
    county += 1
      
  
  print('-------------------------------------------')
  print(' h - '+ str(h)+'\n')
  print(' g - '+ str(g)+'\n')
  print(' f - '+ str(f)+'\n')
  print(' e - '+ str(e)+'\n') 
  print(' d - '+ str(d)+'\n')
  print(' c - '+ str(c)+'\n')
  print(' b - '+ str(b)+'\n')
  print(' a - '+ str(a))
  print('    ' + '  |    |    |    |    |    |    |    | ')
  print('    ' + '  1    2    3    4    5    6    7    8 ')
  print('-------------------------------------------')
        
#Move function, checks turn, gets 2 inputs and trys to move them. 
def move(turn):
        while True:
          try:
            print("Select Piece")
            place1 = eval(input('>'))
            print(place1.piece.mtype + " selected")
            print("Move to")
            place2 = eval(input('>'))
            print(place2)
            if place1.piece.player == turn and place2 in place1.piece.moves:
              if place2 in place1.piece.moves:
                score[turn] = score[turn] + place2.piece.value
                place2.piece = place1.piece
                place1.piece = null
                board()
                break
          except:
            print("Please select a valid piece")
          
        

#Globals for the game
game = True
yl = [0,'a','b','c','d','e','f','g','h']
score = [0,0,0]
turn = 2

#Pieces for the game
null = piece('_',0,0,'null')
wking = piece('K',1,100,'king')
wqueen = piece('Q',1,9,'queen')
wrook1 = piece('R',1,5,'rook')
wrook2 = piece('R',1,5,'rook')
wbisharp1 = piece('B',1,4,'bisharp')
wbisharp2 = piece('B',1,4,'bisharp')
wknight1 = piece('H',1,4,'knight')
wknight2 = piece('H',1,4,'knight')
wpawn1 = piece('P',1,1,'pawn')
wpawn2 = piece('P',1,1,'pawn')
wpawn3 = piece('P',1,1,'pawn')
wpawn4 = piece('P',1,1,'pawn')
wpawn5 = piece('P',1,1,'pawn')
wpawn6 = piece('P',1,1,'pawn')
wpawn7 = piece('P',1,1,'pawn')
wpawn8 = piece('P',1,1,'pawn')
bking = piece('k',2,100,'king')
bqueen = piece('q',2,9,'queen')
brook1 = piece('r',2,5,'rook')
brook2 = piece('r',2,5,'rook')
bbisharp1 = piece('b',2,4,'bisharp')
bbisharp2 = piece('b',2,4,'bisharp')
bknight1 = piece('h',2,4,'knight')
bknight2 = piece('h',2,4,'knight')
bpawn1 = piece('p',2,1,'pawn')
bpawn2 = piece('p',2,1,'pawn')
bpawn3 = piece('p',2,1,'pawn')
bpawn4 = piece('p',2,1,'pawn')
bpawn5 = piece('p',2,1,'pawn')
bpawn6 = piece('p',2,1,'pawn')
bpawn7 = piece('p',2,1,'pawn')
bpawn8 = piece('p',2,1,'pawn')

#Locations of the board including an outer layer for checks
z0 = place(0,0,'error')
z1 = place(0,1,'error')
z2 = place(0,2,'error')
z3 = place(0,3,'error')
z4 = place(0,4,'error')
z5 = place(0,5,'error')
z6 = place(0,6,'error')
z7 = place(0,7,'error')
z8 = place(0,8,'error')
z9 = place(0,9,'error')
a0 = place(1,0,'error')
a1 = place(1,1,wrook1)
a2 = place(1,2,wknight1)
a3 = place(1,3,wbisharp1)
a4 = place(1,4,wking)
a5 = place(1,5,wqueen)
a6 = place(1,6,wbisharp2)
a7 = place(1,7,wknight2)
a8 = place(1,8,wrook2)
a9 = place(1,9,'error')
b0 = place(2,0,'error')
b1 = place(2,1,wpawn1)
b2 = place(2,2,wpawn2)
b3 = place(2,3,wpawn3)
b4 = place(2,4,wpawn4)
b5 = place(2,5,wpawn5)
b6 = place(2,6,wpawn6)
b7 = place(2,7,wpawn7)
b8 = place(2,8,wpawn8)
b9 = place(2,9,'error')
c0 = place(3,0,'error')
c1 = place(3,1,null)
c2 = place(3,2,null)
c3 = place(3,3,null)
c4 = place(3,4,null)
c5 = place(3,5,null)
c6 = place(3,6,null)
c7 = place(3,7,null)
c8 = place(3,8,null)
c9 = place(3,9,'error')
d0 = place(4,0,'error')
d1 = place(4,1,null)
d2 = place(4,2,null)
d3 = place(4,3,null)
d4 = place(4,4,null)
d5 = place(4,5,null)
d6 = place(4,6,null)
d7 = place(4,7,null)
d8 = place(4,8,null)
d9 = place(4,9,'error')
e0 = place(5,0,'error')
e1 = place(5,1,null)
e2 = place(5,2,null)
e3 = place(5,3,null)
e4 = place(5,4,null)
e5 = place(5,5,null)
e6 = place(5,6,null)
e7 = place(5,7,null)
e8 = place(5,8,null)
e9 = place(5,9,'error')
f0 = place(6,0,'error')
f1 = place(6,1,null)
f2 = place(6,2,null)
f3 = place(6,3,null)
f4 = place(6,4,null)
f5 = place(6,5,null)
f6 = place(6,6,null)
f7 = place(6,7,null)
f8 = place(6,8,null)
f9 = place(6,9,'error')
g0 = place(7,0,'error')
g1 = place(7,1,bpawn1)
g2 = place(7,2,bpawn2)
g3 = place(7,3,bpawn3)
g4 = place(7,4,bpawn4)
g5 = place(7,5,bpawn5)
g6 = place(7,6,bpawn6)
g7 = place(7,7,bpawn7)
g8 = place(7,8,bpawn8)
g9 = place(7,9,'error')
h0 = place(8,0,'error')
h1 = place(8,1,brook1)
h2 = place(8,2,bknight1)
h3 = place(8,3,bbisharp1)
h4 = place(8,4,bking)
h5 = place(8,5,bqueen)
h6 = place(8,6,bbisharp2)
h7 = place(8,7,bknight2)
h8 = place(8,8,brook2)
h9 = place(8,9,'error')
v0 = place(9,0,'error')
v1 = place(9,1,'error')
v2 = place(9,2,'error')
v3 = place(9,3,'error')
v4 = place(9,4,'error')
v5 = place(9,5,'error')
v6 = place(9,6,'error')
v7 = place(9,7,'error')
v8 = place(9,8,'error')
v9 = place(9,9,'error')

#The board display

a = [a1.piece.symbol,a2.piece.symbol,a3.piece.symbol,a4.piece.symbol,a5.piece.symbol,a6.piece.symbol,a7.piece.symbol,a8.piece.symbol]
b = [b1.piece.symbol,b2.piece.symbol,b3.piece.symbol,b4.piece.symbol,b5.piece.symbol,b6.piece.symbol,b7.piece.symbol,b8.piece.symbol]
c = [c1.piece.symbol,c2.piece.symbol,c3.piece.symbol,c4.piece.symbol,c5.piece.symbol,c6.piece.symbol,c7.piece.symbol,c8.piece.symbol]
d = [d1.piece.symbol,d2.piece.symbol,d3.piece.symbol,d4.piece.symbol,d5.piece.symbol,d6.piece.symbol,d7.piece.symbol,d8.piece.symbol]
e = [e1.piece.symbol,e2.piece.symbol,e3.piece.symbol,e4.piece.symbol,e5.piece.symbol,e6.piece.symbol,e7.piece.symbol,e8.piece.symbol]
f = [f1.piece.symbol,f2.piece.symbol,f3.piece.symbol,f4.piece.symbol,f5.piece.symbol,f6.piece.symbol,f7.piece.symbol,f8.piece.symbol]
g = [g1.piece.symbol,g2.piece.symbol,g3.piece.symbol,g4.piece.symbol,g5.piece.symbol,g6.piece.symbol,g7.piece.symbol,g8.piece.symbol]
h = [h1.piece.symbol,h2.piece.symbol,h3.piece.symbol,h4.piece.symbol,h5.piece.symbol,h6.piece.symbol,h7.piece.symbol,h8.piece.symbol]

#The actual grid for navigation and values
ay = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
by = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9]
cy = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]
dy = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9]
ey = [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9]
fy = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9]
gy = [g0,g1,g2,g3,g4,g5,g6,g7,g8,g9]
hy = [h0,h1,h2,h3,h4,h5,h6,h7,h8,h9]
zy = [z0,z1,z2,z3,z4,z5,z6,z7,z8,z9]
vy = [v0,v1,v2,v3,v4,v5,v6,v7,v8,v9]

grid = [zy,ay,by,cy,dy,ey,fy,gy,hy,vy]

#Movelist function for compiling every move possible for each piece per turn

def movelist(square):
  s = square
  sp = square.piece
  if sp.mtype == 'null':
    return('null')
  elif sp.mtype == 'king':
    if grid[s.y+1][s.x].piece != 'error':
      if grid[s.y+1][s.x].piece.player != sp.player:
        sp.moves.append(grid[s.y+1][s.x])
    if grid[s.y+1][s.x+1].piece != 'error':
      if grid[s.y+1][s.x+1].piece.player != sp.player:
        sp.moves.append(grid[s.y+1][s.x+1])
    if grid[s.y+1][s.x-1].piece != 'error':
      if grid[s.y+1][s.x-1].piece.player != sp.player:
        sp.moves.append(grid[s.y+1][s.x-1])
    if grid[s.y][s.x-1].piece != 'error':
      if grid[s.y][s.x-1].piece.player != sp.player:
        sp.moves.append(grid[s.y][s.x-1])
    if grid[s.y][s.x+1].piece != 'error':
      if grid[s.y][s.x+1].piece.player != sp.player:
        sp.moves.append(grid[s.y][s.x+1])
    if grid[s.y-1][s.x].piece != 'error':
      if grid[s.y-1][s.x].piece.player != sp.player:
        sp.moves.append(grid[s.y-1][s.x])
    if grid[s.y-1][s.x+1].piece != 'error':
      if grid[s.y-1][s.x+1].piece.player != sp.player:
        sp.moves.append(grid[s.y-1][s.x+1])
    if grid[s.y-1][s.x-1].piece != 'error':
      if grid[s.y-1][s.x-1].piece.player != sp.player:
        sp.moves.append(grid[s.y-1][s.x-1])
  elif sp.mtype == 'knight':
    if s.y+2 >0 and s.y+2 < 9 and s.x-1 >0 and s.x-1 <9:
      if grid[s.y+2][s.x-1].piece.player != sp.player:
        sp.moves.append(grid[s.y+2][s.x-1])
    if s.y+2 >0 and s.y+2 < 9 and s.x+1 >0 and s.x+1 <9:
      if grid[s.y+2][s.x+1].piece.player != sp.player:
        sp.moves.append(grid[s.y+2][s.x+1])
    if s.y-2 >0 and s.y-2 < 9 and s.x-1 >0 and s.x-1 <9:
      if grid[s.y-2][s.x-1].piece.player != sp.player:
        sp.moves.append(grid[s.y-2][s.x-1])
    if s.y-2 >0 and s.y-2 < 9 and s.x+1 >0 and s.x+1 <9:
      if grid[s.y-2][s.x+1].piece.player != sp.player:
        sp.moves.append(grid[s.y-2][s.x+1])
    if s.y-1 >0 and s.y-1 < 9 and s.x-2 >0 and s.x-2 <9:
      if grid[s.y-1][s.x-2].piece.player != sp.player:
        sp.moves.append(grid[s.y-1][s.x-2])
    if s.y-1 >0 and s.y-1 < 9 and s.x+2 >0 and s.x+2 <9:
      if grid[s.y-1][s.x+2].piece.player != sp.player:
        sp.moves.append(grid[s.y-1][s.x+2])
    if s.y+1 >0 and s.y+1 < 9 and s.x-2 >0 and s.x-2 <9:
      if grid[s.y+1][s.x-2].piece.player != sp.player:
        sp.moves.append(grid[s.y+1][s.x-2])
    if s.y+1 >0 and s.y+1 < 9 and s.x+2 >0 and s.x+2 <9:
      if grid[s.y+1][s.x+2].piece.player != sp.player:
        sp.moves.append(grid[s.y+1][s.x+2])
  elif sp.mtype == 'pawn':
    if sp.player == 1:
      if grid[s.y+1][s.x].piece.player == 0:
          sp.moves.append(grid[s.y+1][s.x])
      if grid[s.y+1][s.x+1].piece != 'error':
        if grid[s.y+1][s.x+1].piece.player == 2:
          sp.moves.append(grid[s.y+1][s.x+1])
      if grid[s.y+1][s.x-1].piece != 'error':
        if grid[s.y+1][s.x-1].piece.player == 2:
          sp.moves.append(grid[s.y+1][s.x-1])
      if s.y == 2:
        if grid[s.y+1][s.x].piece.player == 0:
          sp.moves.append(grid[s.y+1][s.x])
          if grid[s.y+2][s.x].piece.player == 0:
            sp.moves.append(grid[s.y+2][s.x])
    if sp.player == 2:
      if grid[s.y-1][s.x].piece.player == 0:
          sp.moves.append(grid[s.y-1][s.x])
      if s.y == 7:
        if grid[s.y-1][s.x].piece.player == 0:
          sp.moves.append(grid[s.y-1][s.x])
          if grid[s.y-2][s.x].piece.player == 0:
            sp.moves.append(grid[s.y-2][s.x])
      if grid[s.y-1][s.x+1].piece != 'error':
        if grid[s.y-1][s.x+1].piece.player == 1:
          sp.moves.append(grid[s.y-1][s.x+1])
      if grid[s.y-1][s.x-1].piece != 'error':
        if grid[s.y-1][s.x-1].piece.player == 1:
          sp.moves.append(grid[s.y-1][s.x-1])
  elif sp.mtype == 'bisharp':
    if sp.player == 1:
      n = 1
      while True:
        if grid[s.y+n][s.x+n].piece != 'error':
          if grid[s.y+n][s.x+n].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+n])
            n += 1
          else: 
            break
        else:
          break
      n = -1 
      while True:
        if grid[s.y+n][s.x+n].piece != 'error':
          if grid[s.y+n][s.x+n].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+n])
            n -= 1
          else:
            break
        else:
          break
      n = 1
      m = -1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 1
            m -= 1 
          else:
            break
        else:
          break
      n = -1
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n -= 1
            m += 1 
          else:
            break
        else:
          break
    if sp.player == 2:
      n = 1
      while True:
        if grid[s.y+n][s.x+n].piece != 'error':
          if grid[s.y+n][s.x+n].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+n])
            n += 1
          else: 
            break
        else:
          break
      n = -1 
      while True:
        if grid[s.y+n][s.x+n].piece != 'error':
          if grid[s.y+n][s.x+n].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+n])
            n -= 1
          else:
            break
        else:
          break
      n = 1
      m = -1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 1
            m -= 1 
          else:
            break
        else:
          break
      n = -1
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n -= 1
            m += 1 
          else:
            break
        else:
          break
  elif sp.mtype == 'rook':
    if sp.player == 1:
      n = 1
      m = 0
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 1
            m += 0
          else:
            break
        else:
          break
      n = -1
      m = 0
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n -= 1
            m += 0
          else: 
            break
        else:
          break
      n = 0
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 0
            m += 1
          else: 
            break
        else:
          break
      n = 0
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 0
            m -= 1
          else: 
            break
        else:
          break
    if sp.player == 2:
      n = 1
      m = 0
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+m][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 1
            m += 0
          else: 
            break
        else:
          break
      n = -1
      m = 0
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n -= 1
            m += 0
          else: 
            break
        else:
          break
      n = 0
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 0
            m += 1
          else: 
            break
        else:
          break
      n = 0
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 0
            m -= 1
          else: 
            break
        else:
          break
  elif sp.mtype == 'queen':
    if sp.player == 1:
      n = 1
      while True:
        if grid[s.y+n][s.x+n].piece != 'error':
          if grid[s.y+n][s.x+n].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+n])
            n += 1
          else: 
            break
        else:
          break
      n = -1 
      while True:
        if grid[s.y+n][s.x+n].piece != 'error':
          if grid[s.y+n][s.x+n].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+n])
            n -= 1
          else:
            break
        else:
          break
      n = 1
      m = -1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 1
            m -= 1 
          else:
            break
        else:
          break
      n = -1
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n -= 1
            m += 1 
          else:
            break
        else:
          break
      n = 1
      m = 0
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 1
            m += 0
          else:
            break
        else:
          break
      n = -1
      m = 0
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n -= 1
            m += 0
          else: 
            break
        else:
          break
      n = 0
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 0
            m += 1
          else: 
            break
        else:
          break
      n = 0
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 2:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 0
            m -= 1
          else: 
            break
        else:
          break
    if sp.player == 2:
      n = 1
      while True:
        if grid[s.y+n][s.x+n].piece != 'error':
          if grid[s.y+n][s.x+n].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+n])
            n += 1
          else: 
            break
        else:
          break
      n = -1 
      while True:
        if grid[s.y+n][s.x+n].piece != 'error':
          if grid[s.y+n][s.x+n].piece.player == 0 or grid[s.y+n][s.x+n].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+n])
            n -= 1
          else:
            break
        else:
          break
      n = 1
      m = -1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 1
            m -= 1 
          else:
            break
        else:
          break
      n = -1
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n -= 1
            m += 1 
          else:
            break
        else:
          break
      n = 1
      m = 0
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+m][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 1
            m += 0
          else: 
            break
        else:
          break
      n = -1
      m = 0
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n -= 1
            m += 0
          else: 
            break
        else:
          break
      n = 0
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 0
            m += 1
          else: 
            break
        else:
          break
      n = 0
      m = 1
      while True:
        if grid[s.y+n][s.x+m].piece != 'error':
          if grid[s.y+n][s.x+m].piece.player == 0 or grid[s.y+n][s.x+m].piece.player == 1:
            sp.moves.append(grid[s.y+n][s.x+m])
            n += 0
            m -= 1
          else: 
            break
        else:
          break



#Main
board()
print("Select piece/space by inputing row letter and number column (e.g. b1)")
print();
change = True
while game == True:
  if turn == 1:
    turn = 2
    print("It's Blacks(LowerCase)'s Turn")
    print()
  elif turn == 2:
    turn = 1
    print("It's Whites(UpperCase)'s Turn")
    print()
  move(turn)
