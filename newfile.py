import csv
import pygame
import sys
import random
lo = True
pygame.init()
pygame.mixer.init()


battle = pygame.mixer.Sound("battle.wav")
vicfanfare = pygame.mixer.Sound("victoryfanfare.wav")
slorp = pygame.mixer.Sound("potiondrink.wav")
monah = pygame.mixer.Sound("chaching.wav")
playerfile = "player.data"
die = pygame.mixer.Sound("wilhelm.wav")

#check to see if there were any command line arguments, like debug mode adding a test comment
arguments = []
arguments = sys.argv[1:]
try:
	if arguments[0]:
		pass
except:
	arguments = ['normal']


#define an object class we are calling Fightman
class Fightman:
	#variables
	def __init__(self, name, hitpoints, potions, strength, exp, defence, gold):
		self.name = name
		self.hitpoints = hitpoints
		self.maxhitpoints = hitpoints
		self.potions = potions
		self.strength = strength
		self.exp = exp
		self.defence = defence
		self.natdefence = defence
		self.gold = gold

	#methods	
	def attack(self, attacker, defender):
		defender.hitpoints = defender.hitpoints - attacker.strength / defender.defence
		print(attacker.name + " attacks for " + str(attacker.strength/defender.defence))
		defender.defence = defender.natdefence

	def defend(self, defen):
		defen.defence = defen.defence + 1
		print(defen.name + " is gaurdin")

	def heal(self, user):
		print(self.name)
		if user.potions > 0:
			slorp.play()
			print("Drank potions for 100 hitpoints")
			user.hitpoints = user.hitpoints + 100
			if user.hitpoints > user.maxhitpoints:
				user.hitpoints = user.maxhitpoints
			user.potions = user.potions - 1
		else:
			print("You don't have any potions.")



#define functions

def shop(players):
	sho = True
	while sho:
		print("Welcome to the shop " + players[0].name + "!")
		print("You have " + str(players[0].gold) + " gold.")
		print("You have " + str(players[0].potions) + " potions.")
		shp = input("Buy [1] or Leave [2]")
		if shp == '1' and players[0].gold > 25:
			players[0].gold = players[0].gold - 25
			players[0].potions = players[0].potions + 1
			monah.play()
		if shp == '2':
			sho = False

def bgft(players,monster):
	turns = 0
	lo = True
	while lo:
		if turns == 0:
			battle.play()  #plays battle sound music
			print(players)
			print(players[0].name + " Vs Team " + monsters[0].name)
			for badguys in monsters:
				print(badguys.name + " max hp is: " + str(badguys.hitpoints) + "| max potions is " + str(badguys.potions) + "| strength is " + str(badguys.strength))

		print("You have " + str(players[0].hitpoints) +  " out of  "  +  str(players[0].maxhitpoints)) 
		i = input("Attack(1), Potion(2), Defend(3), or Flee(4) ")
		turns = turns + 1
		if i == '1':
			#How many monsters in list? If there are more then 1 monster ask whomstve to attack.
			if len(monsters) == 1:
				players[0].attack(players[0],monsters[0])
				print(monsters[0].hitpoints)
			if len(monsters) > 1:
				listomon = 0
				for monster in monsters:
					listomon = listomon + 1
					print(monster.name +  str(listomon))
				o = input("Whomstve killinate?")
				o = int(o) - 1
				print(o)
				print(monsters[0].name)
				print(monsters[1].name)
				players[0].attack(players[0],monsters[o])
				print(monsters[o].hitpoints)

		if i == '2':
			players[0].heal(players[0])

		if i == '3':
			players[0].defend(players[0])
		if i == '4':
			lo = False
		if i == '5': #and arguments[0] == 'debug':
			for badguys in monsters:
				badguys.hitpoints = 0
			Victory = True
		if players[0].hitpoints <= 0:
			die.play()
			lo = False
			print("You Lose")
			monster.exp = monster.exp + 25
		if monsters[0].hitpoints <= 0:
			die.play()
			players[0].exp = players[0].exp + 25
			players[0].gold = players[0].gold + monsters[0].gold
			print(players[0].name + " gained 25 exp and now has " + str(players[0].exp))
			print(players[0].name + " gained " + str(monsters[0].gold) + "  gold and now has " + str(players[0].gold))
			Victory = True
			lo = False
		if lo:
			for badguy in monsters:
				if badguy.hitpoints <= badguy.maxhitpoints/3 and badguy.potions > 0:
					badguy.heal(badguy)
				else:
					print("")
				#monster.attack(monster,players[0])
				#for badguy in monsters


Victory = False
ghp = random.randrange(80,120)
gpot = random.randrange(1,3)
gstr = random.randrange(8,10)
gexp = 0
gnatdef = 1
ggold = random.randrange(10,50)
file = open(playerfile,newline='')
reader = csv.reader(file)
data = []
for row in reader: 
#outfilewriter.writerow([players[0].name,players[0].maxhitpoints,players[0].potions,players[0].strength,players[0].exp,players[0].defence,players[0].gold])
	pname = row[0]
	php = int(row[1])
	ppot = int(row[2])
	pstr = int(row[3])
	pexp = int(row[4])
	pnatdef = int(row[5])
	pgold = int(row[6])
file.close()

#players[0] = Fightman('Pikachu',100,3,10,0, 1, 0)
monsters = []
players = []
tempplayer = Fightman(pname,php,ppot,pstr,pexp, pnatdef, pgold)
tempmonster = Fightman('Greg', ghp, gpot, gstr, gexp, gnatdef, ggold)
monster = Fightman('Greg', ghp, gpot, gstr, gexp, gnatdef, ggold)
monsters.append(tempmonster)
players.append(tempplayer)
monsters.append(Fightman('Chad',ghp,gpot,gstr,gexp,gnatdef,ggold))

lop = True
while lop:
	Victory = False
	ghp = random.randrange(80,120)
	gpot = random.randrange(1,3)
	gstr = random.randrange(8,10)
	gexp = 0
	gnatdef = 1
	ggold = random.randrange(10,50)
	file = open(playerfile,newline='')
	reader = csv.reader(file)
	data = []
	for row in reader: 
#outfilewriter.writerow([players[0].name,players[0].maxhitpoints,players[0].potions,players[0].strength,players[0].exp,players[0].defence,players[0].gold])
		pname = row[0]
		php = int(row[1])
		ppot = int(row[2])
		pstr = int(row[3])
		pexp = int(row[4])
		pnatdef = int(row[5])
		pgold = int(row[6])
	file.close()
 
	lo = False
	idle = True
	while idle:
		pq = input("Do you wish to go to the potion shop[1] or Fight monsters [2] or Quit [3]")
		if pq == '1':
			shop(players)
		if pq == '2':
			lo = True
			idle = False
			bgft(players, monsters)
		if pq == '3':
			idle = False
			lop = False

#This defines the battle and needs to be changed into a function
	#bgft(players, monsters)
	temphp = 0
	battle.stop()
	for badguys in monsters:
		temphp = temphp + badguys.hitpoints 
	print(temphp)
	if temphp >= 0:
		vicfanfare.play()
	if players[0].exp >= 200:
		players[0].exp = 0
		players[0].strength = players[0].strength + 1
		players[0].maxhitpoints = players[0].maxhitpoints + random.randrange(5,15) 
		print(players[0].name + " leveled up! " + players[0].name + " now has " + str(players[0].strength) + " stength! And now has " + str(players[0].maxhitpoints) + " Maxhitpoints") 
	qt = input("Press any buton to continue")
	vicfanfare.stop()

	outfile = open(playerfile,'w')
	outfilewriter = csv.writer(outfile,delimiter=',',lineterminator='')
	#outfilewriter.writerow(["name","Hp","Potion","Strength","Exp","Nat Defense","money"])
	outfilewriter.writerow([players[0].name,players[0].maxhitpoints,players[0].potions,players[0].strength,players[0].exp,players[0].defence,players[0].gold])
	outfile.close()
