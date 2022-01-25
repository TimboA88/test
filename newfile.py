import csv
import pygame
pygame.init()
pygame.mixer.init()
import sys
battle = pygame.mixer.Sound("battle.ogg")
vicfanfare = pygame.mixer.Sound("victoryfanfare.wav")
slorp = pygame.mixer.Sound("potiondrink.wav")
monah = pygame.mixer.Sound("chaching.wav")
playerfile = "player.data"
die = pygame.mixer.Sound("wilhelm.wav")

import random
arguments = []
arguments = sys.argv[1:]
try:
	if arguments[0]:
		pass
except:
	arguments = ['normal']

class Pokemon:
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
	def attack(self, attacker, defender):
		defender.hitpoints = defender.hitpoints - attacker.strength / defender.defence
		print(attacker.name + " attacks for " + str(attacker.strength/defender.defence))
		defender.defence = defender.natdefence
#		attacksound.play()


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

def shop(player):
	sho = True
	while sho:
		print("You have " + str(player.gold) + " gold.")
		print("You have " + str(player.potions) + " potions.")
		shp = input("Buy [1] or Leave [2]")
		if shp == '1' and player.gold > 25:
			player.gold = player.gold - 25
			player.potions = player.potions + 1
			monah.play()
		if shp == '2':
			sho = False
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
#outfilewriter.writerow([player.name,player.maxhitpoints,player.potions,player.strength,player.exp,player.defence,player.gold])
		pname = row[0]
		php = int(row[1])
		ppot = int(row[2])
		pstr = int(row[3])
		pexp = int(row[4])
		pnatdef = int(row[5])
		pgold = int(row[6])
	file.close()
#player = Pokemon('Pikachu',100,3,10,0, 1, 0)
	monsters = []
	player = Pokemon(pname,php,ppot,pstr,pexp, pnatdef, pgold)
	monster = Pokemon('Greg', ghp, gpot, gstr, gexp, gnatdef, ggold)
	monsters.append(monster)
#	monsters.append(Pokemon('Chad',ghp,gpot,gstr,gexp,gnatdef,ggold))
 
	lo = False
	idle = True
	while idle:
		pq = input("Do you wish to go to the potion shop[1] or Fight monsters [2] or Quit [3]")
		if pq == '1':
			shop(player)
		if pq == '2':
			lo = True
			idle = False
		if pq == '3':
			idle = False
			lop = False


	turns = 0
	while lo:
		if turns == 0:
			battle.play()  #plays battle sound music
			print(player.name + " Vs " + monster.name)
			print(monster.name + " max hp is: " + str(monster.hitpoints) + "| max potions is " + str(monster.potions) + "| strength is " + str(monster.strength))

		print("You have " + str(player.hitpoints) +  " out of  "  +  str(player.maxhitpoints)) 
		i = input("Attack(1), Potion(2), Defend(3), or Flee(4) ")
		turns = turns + 1
		if i == '1':
			player.attack(player,monster)
			print(monster.hitpoints)
		if i == '2':
			player.heal(player)

		if i == '3':
			player.defend(player)
		if i == '4':
			lo = False
		if i == '5' and arguments[0] == 'debug':
			monster.hitpoints = 0
		if player.hitpoints <= 0:
			die.play()
			lo = False
			print("You Lose")
			monster.exp = monster.exp + 25
		if monster.hitpoints <= 0:
			die.play()
			lo = False
			player.exp = player.exp + 25
			player.gold = player.gold + monster.gold
			print(player.name + " gained 25 exp and now has " + str(player.exp))
			print(player.name + " gained " + str(monster.gold) + "  gold and now has " + str(player.gold))
			Victory = True
		if lo:
			for badguy in monsters:
				if badguy.hitpoints <= badguy.maxhitpoints/3 and badguy.potions > 0:
					badguy.heal(badguy)
				else:
				#monster.attack(monster,player)
				#for badguy in monsters
					badguy.attack(badguy,player)
	battle.stop()
	if Victory == True:
		vicfanfare.play()
	if player.exp >= 200:
		player.exp = 0
		player.strength = player.strength + 1
		player.maxhitpoints = player.maxhitpoints + random.randrange(5,15) 
		print(player.name + " leveled up! " + player.name + " now has " + str(player.strength) + " stength! And now has " + str(player.maxhitpoints) + " Maxhitpoints") 
	qt = input("Press any buton to continue")
	vicfanfare.stop()

	outfile = open(playerfile,'w')
	outfilewriter = csv.writer(outfile,delimiter=',',lineterminator='')
	#outfilewriter.writerow(["name","Hp","Potion","Strength","Exp","Nat Defense","money"])
	outfilewriter.writerow([player.name,player.maxhitpoints,player.potions,player.strength,player.exp,player.defence,player.gold])
	outfile.close()
