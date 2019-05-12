from random import randint
carre=[[str(i) for i in range(k,k+3)]for k in range(1,8,3)]
def show():
  for i in range(len(carre)):
    print(" ".join(carre[i]))
def colonecarre():
  return [[carre[i][j] for i in range(3)] for j in range(3)]
def diagone():
  return [carre[i][i] for i in range(3)]
def diagtwo():
  return [carre[0][2],carre[1][1],carre[2][0]]
def test(c):
  diag1,diag2,cl=diagone(),diagtwo(),colonecarre()
  b=0
  for i in range(3):
    if cl[i].count(c)==3 or carre[i].count(c)==3:
      return True 
  if diag1.count(c)==3 or diag2.count(c)==3:
    return True
  return False
def play(c,u):
    nb=input(u)
    if int(nb) in range(4):
      index=carre[0].index(nb) 
      carre[0][index]=c
    elif int(nb) in range(4,7):
      index=carre[1].index(nb) 
      carre[1][index]=c
    elif int(nb) in range(7,10):
      index=carre[2].index(nb) 
      carre[2][index]=c
    show()
bienv="BIENVENUE DANS MON PETIT JEU  X O DE BADREDDINE MOUHASSINE"
print("*"*(8+len(bienv)))
print("\tBIENVENUE DANS MON PETIT JEU  X O DE BADREDDINE MOUHASSINE")
print("*"*(8+len(bienv)))
print("voici le carré initialement vide avec des case numéroté de 1 jusqu'à 9")
print(show())
cara1=input("le premier joueur ,souhaitez vous jouer avec X ou O ?:\n")
cara2=""
currentplayer=1
if cara1=="X":
        cara2="O"
else:
        cara2="X"
k=9
ui="entrer le numéro du case où vous souhaitez jouer :  "
for i in range(k):
    if currentplayer==1:
      play(cara1,ui)
      currentplayer=2
    elif currentplayer==2:
      play(cara2,ui)
      currentplayer=1
    if test(cara1):
      print("felicitation le premier joueur gagne!!")
      k=i
      ui="press any key to exit and click enter"
      show()
    elif test(cara2):
      print("felicitation le deuxième joueur gagne!!")
      k=i
      ui="press any key to exit and click enter"
      show()
