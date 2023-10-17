import random
battlepkmn = True
rmslct = False
mslct = False
pmc = 0
start = 0

class pokemon():
        def __init__(self, typ: str, a: int, b: int, c: int, d: str, e,f,g,h):
                self.typ = typ
                self.atk = a
                self.hp = b
                self.spd = c
                self.name = d
                self.move1 = e
                self.move2 = f
                self.move3 = g
                self.move4 = h
                self.usemove = 0
                self.opponent = 0

class move():
        def __init__(self, name: str,typ: str, pri: int, power: int,am: int,spdm: int):
                self.name = name
                self.typ = typ
                self.power = power
                self.pri = pri
                self.am = am
                self.spdm = spdm

#SET MOVES
m1 = move('Water Gun.','Water',1,0.4,0,0)

m2 = move('Tackle','Normal',1,0.3,0,0)

m3 = move('Growl',"Normal",1,0,0.8,0)

m4 = move('-','-',0,0,0,0)

m5 = move('Screech','Normal',1,0,0,0.8)

m6 = move('Ember', 'Fire', 1, 0.4,0,0)

m7 = move('Vine Whip', 'Grass' , 1, 0.4, 0, 0)

m8 = move('Quick Attack', 'Normal', 10, 0.2, 0, 0)

m9 = move('Slam', 'Normal', 1, 0.4, 0,0)

m10 = move('Gust', 'Flying', 1, 0.4, 0,0)

m11 = move('Flamethrower' , 'Fire' ,1, 0.8, 0,0)

m12 = move('Surf' , 'Water' , 1, 0.8, 0,0)

m13 = move('Rock Throw', 'Rock' ,1,0.4,0,0)

m14 = move('Mud Shot' , 'Ground',1,0.2,0,0.9)

m15 = move('Bite' , 'Dark' ,1,0.4,0.8,0)

m16 = move('Peck', 'Flying' , 1, 0.3, 0 ,0)

#SET STATS    
p1 = pokemon('Water',10,21,7,'Mudkip',m1,m2,m3,m4)


#SET STATS 2
p2 = pokemon('Fire',11,18,9,'Torchic',m6,m2,m5,m4)



#SET STATS 3
p3 = pokemon('Grass',10,18,10,'Treeko',m2,m3,m7,m4)


while battlepkmn == True:
        if start == 0:
                print('choose your pkmn \n 1 - Mudkip the water pokemon \n 2 - Torchic the fire pokemon \n 3 - Treeko the plant pokemon')
                ppc = input('> ')



                if ppc == '1':
                    yourpkmn = p1

                if ppc == '2':
                    yourpkmn = p2

                if ppc == '3':
                    yourpkmn = p3

                print('--------')
                print('Name: '+str(yourpkmn.name))
                print('Type: '+str(yourpkmn.typ))
                print('--------')
                print("Stats:")
                print('Atk: '+str(yourpkmn.atk)+' HP: '+ str(yourpkmn.hp)+' Speed: '+str(yourpkmn.spd))
                print('--------')

                print('choose rival')
                rivalpkmn = input('> ')


                if rivalpkmn == '1':
                    rivalpkmn = p1
                        
                if rivalpkmn == '2':
                    rivalpkmn = p2

                if rivalpkmn == '3':
                    rivalpkmn = p3

                    print('--------')
                    
                    print('Name: '+str(rivalpkmn.name))
                    print('Type: '+str(rivalpkmn.typ))
                    print('--------')
                    print("Stats:")
                    print('Atk: '+str(rivalpkmn.atk)+' HP: '+ str(rivalpkmn.hp)+' Speed: '+str(rivalpkmn.spd))
                    print('--------')
                rivalpkmn.opponent = yourpkmn
                yourpkmn.opponent = rivalpkmn

                print('Start battle?')
                print('1. Yes')
                print('2. No (Quit)')
                print('3. Choose New PKMN')
                start = input('> ')
        if start != '1' and start != '2' and start != '3':
                start = 0
        if start == '3':
                start = 0
        if start == '2':
                break
        if start == '1':
                rivalpkmnmoves = [rivalpkmn.move1,rivalpkmn.move2,rivalpkmn.move3,rivalpkmn.move4]
                rivalpkmn.usemove = random.choice(rivalpkmnmoves)
                rmslct = True
                if rivalpkmn.usemove.name == '-':
                        rmslct = False
                if rmslct == True:
                        print()
                        print('____________')
                        print('1. ' + (str(yourpkmn.move1.name)+' | Type: '+str(yourpkmn.move1.typ)))
                        print('2. ' + (str(yourpkmn.move2.name)+' | Type: '+str(yourpkmn.move2.typ)))
                        print('3. ' + (str(yourpkmn.move3.name)+' | Type: '+str(yourpkmn.move3.typ)))
                        print('4. ' + (str(yourpkmn.move4.name)+' | Type: '+str(yourpkmn.move4.typ)))
                        print('____________')
                        print()
                        pmc = input('> ')
                        print()
                        if pmc != '1' and pmc != '2' and pmc != '3' and pmc != '4':
                                mslct = False
                        if pmc == '1':
                                yourpkmn.usemove = yourpkmn.move1
                                mslct = True
                        elif pmc == '2':
                                yourpkmn.usemove = yourpkmn.move2
                                mslct = True
                        elif pmc == '3':
                                yourpkmn.usemove = yourpkmn.move3
                                mslct = True
                        elif pmc == '4':
                                yourpkmn.usemove = yourpkmn.move4
                                mslct = True
                        if yourpkmn.usemove.name == '-':
                                mslct = False
                                print("You cannot select that move!")
                if mslct == True and rmslct == True:
                        if rivalpkmn.usemove.pri > yourpkmn.usemove.pri:
                            #RIVAL TURN
                                dmg = rivalpkmn.atk * rivalpkmn.usemove.power
                                if dmg < 1 and dmg > 0:
                                                dmg = 1
                                yourpkmn.hp = yourpkmn.hp - int(dmg)
                                if rivalpkmn.usemove.am > 0:
                                        yourpkmn.atk = yourpkmn.atk * rivalpkmn.usemove.am
                                        print('Your '+str(yourpkmn.name)+"'s ATK fell")
                                if rivalpkmn.usemove.spdm > 0:
                                        yourpkmn.spd = yourpkmn.spd * rivalpkmn.usemove.spdm
                                        print('Your '+str(yourpkmn.name)+"'s SPD fell")
                                print("The Opponent's " +str(rivalpkmn.name) + ' used ' + str(rivalpkmn.usemove.name))
                                if yourpkmn.hp <= 0:
                                        yourpkmn.hp = 0
                                        print(str(yourpkmn.hp))
                                        print("Your "+str(yourpkmn.name) + ' has fainted')
                                        battlepkmn = False
                                else:
                                        print("Your "+str(yourpkmn.name) + ' has ' + str(yourpkmn.hp)+ ' hp')

                            #MY TURN
                                dmg = yourpkmn.atk * yourpkmn.usemove.power
                                if dmg < 1 and dmg > 0:
                                                dmg = 1
                                rivalpkmn.hp = rivalpkmn.hp - int(dmg)
                                if yourpkmn.usemove.am > 0:
                                        rivalpkmn.atk = rivalpkmn.atk * yourpkmn.usemove.am
                                        print("The Opponent's "+str(rivalpkmn.name)+"'s ATK fell")
                                if yourpkmn.usemove.spdm > 0:
                                        rivalpkmn.spd = rivalpkmn.spd * yourpkmn.usemove.spdm
                                        print("The Opponent's "+str(rivalpkmn.name)+"'s SPD fell")
                                print("Your "+str(yourpkmn.name) + ' used '  + str(yourpkmn.usemove.name))
                                if rivalpkmn.hp <= 0:
                                        rivalpkmn.hp = 0
                                        print(str(rivalpkmn.hp))
                                        print("The Opponent's " +str(rivalpkmn.name) + ' has fainted')
                                        battlepkmn = False
                                else:
                                        print("The Opponent's " +str(rivalpkmn.name) + ' has ' + str(rivalpkmn.hp)+ ' hp')

                        elif yourpkmn.usemove.pri > rivalpkmn.usemove.pri:
                                #MY TURN
                                dmg = yourpkmn.atk * yourpkmn.usemove.power
                                if dmg < 1 and dmg > 0:
                                                dmg = 1
                                rivalpkmn.hp = rivalpkmn.hp - int(dmg)
                                if yourpkmn.usemove.am > 0:
                                        rivalpkmn.atk = rivalpkmn.atk * yourpkmn.usemove.am
                                        print("The Opponent's "+str(rivalpkmn.name)+"'s ATK fell")
                                if yourpkmn.usemove.spdm > 0:
                                        rivalpkmn.spd = rivalpkmn.spd * yourpkmn.usemove.spdm
                                        print("The Opponent's "+str(rivalpkmn.name)+"'s SPD fell")
                                print("Your "+str(yourpkmn.name) + ' used '  + str(yourpkmn.usemove.name))
                                if rivalpkmn.hp <= 0:
                                        rivalpkmn.hp = 0
                                        print(str(rivalpkmn.hp))
                                        print("The Opponent's " +str(rivalpkmn.name) + ' has fainted')
                                        battlepkmn = False
                                else:
                                        print("The Opponent's " +str(rivalpkmn.name) + ' has ' + str(rivalpkmn.hp)+ ' hp')
                                #RIVAL TURN
                                dmg = rivalpkmn.atk * rivalpkmn.usemove.power
                                if dmg < 1 and dmg > 0:
                                                dmg = 1
                                yourpkmn.hp = yourpkmn.hp - int(dmg)
                                if rivalpkmn.usemove.am > 0:
                                        yourpkmn.atk = yourpkmn.atk * rivalpkmn.usemove.am
                                        print('Your '+str(yourpkmn.name)+"'s ATK fell")
                                if rivalpkmn.usemove.spdm > 0:
                                        yourpkmn.spd = yourpkmn.spd * rivalpkmn.usemove.spdm
                                        print('Your '+str(yourpkmn.name)+"'s SPD fell")
                                print("The Opponent's " +str(rivalpkmn.name) + ' used ' + str(rivalpkmn.usemove.name))
                                if yourpkmn.hp <= 0:
                                        yourpkmn.hp = 0
                                        print(str(yourpkmn.hp))
                                        print("Your "+str(yourpkmn.name) + ' has fainted')
                                        battlepkmn = False
                                else:
                                        print("Your "+str(yourpkmn.name) + ' has ' + str(yourpkmn.hp)+ ' hp')
                        elif yourpkmn.spd >= rivalpkmn.spd:
                                #MY TURN
                                dmg = yourpkmn.atk * yourpkmn.usemove.power
                                if dmg < 1 and dmg > 0:
                                                dmg = 1
                                rivalpkmn.hp = rivalpkmn.hp - int(dmg)
                                if yourpkmn.usemove.am > 0:
                                       rivalpkmn.atk = rivalpkmn.atk * yourpkmn.usemove.am
                                       print("The Opponent's "+str(rivalpkmn.name)+"'s ATK fell")
                                if yourpkmn.usemove.spdm > 0:
                                        rivalpkmn.spd = rivalpkmn.spd * yourpkmn.usemove.spdm
                                        print("The Opponent's "+str(rivalpkmn.name)+"'s SPD fell")
                                if rivalpkmn.hp <= 0:
                                        rivalpkmn.hp = 0
                                        print(str(rivalpkmn.hp))
                                        print("The Opponent's " +str(rivalpkmn.name) + ' has fainted')
                                        battlepkmn = False
                                else:
                                        print("The Opponent's " +str(rivalpkmn.name) + ' has ' + str(rivalpkmn.hp)+ ' hp')
                                #RIVAL TURN
                                dmg = rivalpkmn.atk * rivalpkmn.usemove.power
                                if dmg < 1 and dmg > 0:
                                                dmg = 1
                                yourpkmn.hp = yourpkmn.hp - int(dmg)
                                print("The Opponent's " +str(rivalpkmn.name) + ' used ' + str(rivalpkmn.usemove.name))
                                if rivalpkmn.usemove.am > 0:
                                        yourpkmn.atk = yourpkmn.atk * rivalpkmn.usemove.am
                                        print('Your '+str(yourpkmn.name)+"'s ATK fell")
                                if rivalpkmn.usemove.spdm > 0:
                                        yourpkmn.spd = yourpkmn.spd * rivalpkmn.usemove.spdm
                                        print('Your '+str(yourpkmn.name)+"'s SPD fell")
                                if yourpkmn.hp <= 0:
                                        yourpkmn.hp = 0
                                        print(str(yourpkmn.hp))
                                        print("Your "+str(yourpkmn.name) + ' has fainted')
                                        battlepkmn = False
                                else:
                                        print("Your "+str(yourpkmn.name) + ' has ' + str(yourpkmn.hp)+ ' hp')
                        elif rivalpkmn.spd > yourpkmn.spd:
                                        #RIVAL TURN
                                        dmg = rivalpkmn.atk * rivalpkmn.usemove.power
                                        if dmg < 1 and dmg > 0:
                                                dmg = 1
                                        yourpkmn.hp = yourpkmn.hp - int(dmg)
                                        print("The Opponent's " +str(rivalpkmn.name) + ' used ' + str(rivalpkmn.usemove.name))
                                        if rivalpkmn.usemove.am > 0:
                                                yourpkmn.atk = yourpkmn.atk * rivalpkmn.usemove.am
                                                print('Your '+str(yourpkmn.name)+"'s ATK fell")
                                        if rivalpkmn.usemove.spdm > 0:
                                                yourpkmn.spd = yourpkmn.spd * rivalpkmn.usemove.spdm
                                                print('Your '+str(yourpkmn.name)+"'s SPD fell")
                                        if yourpkmn.hp <= 0:
                                                yourpkmn.hp = 0
                                                print(str(yourpkmn.hp))
                                                print("Your "+str(yourpkmn.name) + ' has fainted')
                                                battlepkmn = False
                                        else:
                                                print("Your "+str(yourpkmn.name) + ' has ' + str(yourpkmn.hp)+ ' hp')

                                        #MY TURN
                                        dmg = yourpkmn.atk * yourpkmn.usemove.power
                                        rivalpkmn.hp = rivalpkmn.hp - int(dmg)
                                        if yourpkmn.usemove.am > 0:
                                               rivalpkmn.atk = rivalpkmn.atk * yourpkmn.usemove.am
                                               print("The Opponent's "+str(rivalpkmn.name)+"'s ATK fell")
                                        if yourpkmn.usemove.spdm > 0:
                                                rivalpkmn.spd = rivalpkmn.spd * yourpkmn.usemove.spdm
                                                print("The Opponent's "+str(rivalpkmn.name)+"'s SPD fell")
                                        if rivalpkmn.hp <= 0:
                                                rivalpkmn.hp = 0
                                                print(str(rivalpkmn.hp))
                                                print("The Opponent's " +str(rivalpkmn.name) + ' has fainted')
                                                battlepkmn = False
                                        else:
                                                print("The Opponent's " +str(rivalpkmn.name) + ' has ' + str(rivalpkmn.hp)+ ' hp')
                                
