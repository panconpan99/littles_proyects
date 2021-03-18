from random import shuffle
import time
#exercise for POO
suite = 'H D S C'.split()
ranks= '2 3 4 5 6 7 8 9 10 J Q K A'.split()
cards=[]
def who_won(player,comp):
    if len(comp.mano.cartas)==0:
        print("gano el jugador")
    else:
        print("gano la computadora")
for r in ranks:
    for s in suite:
        cards.append((s,r))

class Deck:
    def __init__(self):
        print("creando cartas")
        self.allcards=[(s,r) for s in suite for r in ranks]

    def shuffle(self):
        print("revolviendo cartas...\n")
        shuffle(self.allcards)

    def split(self):
        split_cards=self.allcards[:26],self.allcards[26:]
        return split_cards

class mano:
    def __init__(self,cartas):
        print("creando mano")
        self.cartas=cartas

    def __str__(self):
        return "contiene {} cartas".format(len(self.cartas))

    def add(self,new_card):
        self.cartas.extend(new_card) 
    
    def rm(self):
        return self.cartas.pop()


class player:
    def __init__(self,name, mano):
        self.name=name
        self.mano=mano

    def jugada(self):
        carta_jugada = self.mano.rm()
        print("{} ha jugado {}".format(self.name,carta_jugada))
        return carta_jugada

    def quitar_carta(self):
        cartas_war=[]
        if len(self.mano.cartas) < 1:
            return self.mano.cartas
        else:
            for x in range(1):
                cartas_war.append(self.mano.rm())
            return cartas_war
    
    def has_cards(self):
        return len(self.mano.cartas) != 0

#game

d= Deck()
d.shuffle()
half_1,half_2=d.split()

#constructores
comp = player("computadora" , mano(half_1))
jugador = player("jugador", mano(half_2))

rondas=0
war_count=0
tablas=[]
while jugador.has_cards() and comp.has_cards():
    rondas+=1
    print("ronda " +str(rondas))
    print("el jugador tiene "+str(len(jugador.mano.cartas))+" cartas" )
    print("el computador tiene "+str(len(comp.mano.cartas))+" cartas")
    print("\n")
     
    comp_card = comp.jugada()
    player_card = jugador.jugada()
    tablas.append(player_card)
    tablas.append(comp_card)
    print(tablas)
    if player_card[1] == comp_card[1]:
        war_count+=1

        print("war")

        tablas.extend(jugador.quitar_carta())
        tablas.extend(comp.quitar_carta())
    else:
        if ranks.index(player_card[1]) < ranks.index(comp_card[1]):
            print("computadora gano jugada")
            comp.mano.add(tablas)
            tablas=[]
        else:
            print("jugador gano jugada")
            jugador.mano.add(tablas)
            tablas=[]
who_won(jugador,comp)
print("partida terminada\n")
print("rondas jugadas " +str(rondas))

    