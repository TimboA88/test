from asyncio.windows_events import NULL
import csv
from hashlib import new
from multiprocessing.connection import wait
import pygame
import sys
import random
from pyparsing import null_debug_action
import requests
import json
from  random import randint
import time

#why is this here?
lo = True


#initalize the pygame engine, needs to be done before loading assets.
pygame.init()
pygame.mixer.init()

#filename needs to be specified sometime before the playerfile is LOADED or SAVED.
playerfile = "player.data"

#loads assets
battle = pygame.mixer.Sound("battle.wav")
vicfanfare = pygame.mixer.Sound("victoryfanfare.wav")
slorp = pygame.mixer.Sound("potiondrink.wav")
monah = pygame.mixer.Sound("chaching.wav")
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
		self.baits = 0

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
		print("You have " + str(players[0].baits) + " baits.")
		shp = input("Buy Potions[1] - Buy Bait [2] - Leave Store [3]")
		if shp == '1' and players[0].gold > 25:
			players[0].gold = players[0].gold - 25
			players[0].potions = players[0].potions + 1
			monah.play()
		if shp == '2' and players[0].gold > 25:
			players[0].gold = players[0].gold - 25
			players[0].baits = players[0].baits + 1
			print("you now have " + str(players[0].baits) + " baits" )
			#uncommenting this code will not implement the change. 
			#your homework is toto actually make a function that does these things
			#1.)create a new monster
			#2.)append it to the list of monsters.
			#3.)charge the player some amount of money.
			#4.) make sure they have enough money to do it.
			# here is some code that you wrote earlier that might help you 
			
			#if you make a request to
			#https://namey.muffinlabs.com/name.json1

			#it returns a random name!
			
			##players[0] = Fightman('Pikachu',100,3,10,0, 1, 0) 
			##monsters.append(Fightman('Chad',ghp,gpot,gstr,gexp,gnatdef,ggold))
			
			pass
		if shp == '3':
			sho = False
		

def bgft(players,monster):
	turns = 0
	lo = True

	while lo:
		if turns == 0:
			battle.play()  #plays battle sound music
		#	print(players)
		#	print(players[0].name + " Vs Team " + monsters[0].name)
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
			#or you could remove the bad guys from the list later on
			for badguys in monsters:
				badguys.hitpoints = 0
			Victory = True
		if players[0].hitpoints <= 0:
			die.play()
			lo = False
			print("You Lose")
			monster.exp = monster.exp + 25
		if monsters[0].hitpoints <= 0:
			# after each monster dies, make sure that as they die, they get removed from the list. you're eventually going to have to do this.
			die.play()
			players[0].exp = players[0].exp + 25
			players[0].gold = players[0].gold + monsters[0].gold
			print(players[0].name + " gained 25 exp and now has " + str(players[0].exp))
			print(players[0].name + " gained " + str(monsters[0].gold) + "  gold and now has " + str(players[0].gold))
			Victory = True
			lo = False

		if lo:
			#as long as we're still fighting, it's the monster's turn to attack!
			for badguy in monsters:
				if badguy.hitpoints <= badguy.maxhitpoints/3 and badguy.potions > 0:
					#artificial inteligence
					badguy.heal(badguy)
				else:
					print("")
				#badguy.attack(badguy,players[0])
				#i think we disabled this when we were debugging. this is where the monster should be hitting you back. 
				



Victory = False

#this randomizes the new monsters hitpoints and gold, and anything else you want
ghp = random.randrange(80,120)
gpot = random.randrange(1,3)
gstr = random.randrange(8,10)
gexp = 0
gnatdef = 1
ggold = random.randrange(10,50)


#this reads in the playerfile, turn it into a function and make sure that it gets called before the main loop.
file = open(playerfile,newline='')
reader = csv.reader(file)

#i'm not sure what this data list is for it's not being used as far as i can tell i think you can delete it.
data = []

#these are the things you are writing to the playerfile
#outfilewriter.writerow([players[0].name,players[0].maxhitpoints,players[0].potions,players[0].strength,players[0].exp,players[0].defence,players[0].gold])
for row in reader: 
	pname = row[0]
	php = int(row[1])
	ppot = int(row[2])
	pstr = int(row[3])
	pexp = int(row[4])
	pnatdef = int(row[5])
	pgold = int(row[6])
file.close()
#this is the end of the reading player file in.


#players[0] = Fightman('Pikachu',100,3,10,0, 1, 0) 
# ?name=pikachu&maxhp=100&potions=3&strength=10&exp=0&natdef=1&gold=100

#name:pikachu
#maxhp:100
#potions:3
#strength:10
#exp:10
#natdef:1
#gold:100

#create an empty list of monsters and players
monsters = []
players = []

#create temporary player and monster
tempplayer = Fightman(pname,php,ppot,pstr,pexp, pnatdef, pgold)
tempmonster = Fightman('Greg', ghp, gpot, gstr, gexp, gnatdef, ggold)

#do you still need this one???? i hope not! remove it sometime and find out.
monster = Fightman('Greg', ghp, gpot, gstr, gexp, gnatdef, ggold)

#add temp monster and player to their respective lists.
monsters.append(tempmonster)
players.append(tempplayer)


#monsters.append(Fightman('Chad',ghp,gpot,gstr,gexp,gnatdef,ggold))

#main outer loop begin

def printQuote(s, firstnames):
    #now that it's finished, print it
    print( "hello I am " + str(firstnames.name) + " " + s['insult'])

def HeroprintQuote(s, firstnames):
	print(s['insult'])

def hi(one,two):
	pass

def requestQuote(monster):
    #get some random quote
	url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
	req = requests.get(url)
	fnames = req.text
	insult = json.loads(fnames)
    #now call the function using the insult.
	
	fnames = NULL
	return insult['insult']



if __name__ == '__main__':

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
	
		#main inner loop
		lo = False
		idle = True
		sal = "0"
		while idle:
			pq = input("Do you wish to go to the potion shop[1] or Fight monsters [2], or Saloon [3], or Quit [4]")
			if pq == '1':
				shop(players)
			if pq == '2':
				lo = True
				idle = False
			


				url = 'https://namey.muffinlabs.com/name.json?type=first&frequency=RARE&count='+str(players[0].baits)
				req = requests.get(url)
				fnames = req.text
				firstnames = json.loads(fnames)

				
				oldinsult = requestQuote(monsters[0])
				print(oldinsult)


				if players[0].baits > 0:
					print("you unpack all " + str(players[0].baits) + " of your baits and a few enemies appear!") 
					qwlo = True

					newinsult = "0"
					#oldinsult = "0"
					atemmpts = 0
					atemmptsfail = False
					for x in range(0, players[0].baits):					
						ghp = random.randrange(80,120)
						gpot = random.randrange(1,3)
						gstr = random.randrange(8,10)
						gexp = 0
						gnatdef = 1
						ggold = random.randrange(10,50)
						tempmonster = Fightman(firstnames[x], ghp, gpot, gstr, gexp, gnatdef, ggold)
						newinsult = requestQuote(tempmonster)
						monsters.append(tempmonster)
						time.sleep(4)
						if newinsult == oldinsult:
							while qwlo:
								newinsult = requestQuote(tempmonster)
								atemmpts = atemmpts + 1
								if not newinsult == oldinsult:
									qwlo = False
									atemmpts = 0
								if atemmpts > 4:
									qwlo = False
									atemmpts = 0
									atemmptsfail = True
								time.sleep(4)
								print("Generating insult.....")
						if atemmptsfail == False:
							print(newinsult)
						else: 
							print("fuck you.")
							atemmptsfail = False				
						oldinsult = newinsult
						
					

				players[0].baits = 0
				#print(players[0].baits)
				bgft(players, monsters)
			if pq == '3':
				print("Welcome to Saloon. Whatcha getin?")
				sallop = True
				while sallop:
					sal = input("Pals[1], Drink[2], or Leave[3]")
					if sal == '3':
						sallop = False
			if pq == '4':
				idle = False
				lop = False


		#stops the pokemon battle music.
		battle.stop()
		
		
		temphp = 0
		
		#there should only be one guy in the list at this point if you removed them from the list as they died!
		for badguys in monsters:
			temphp = temphp + badguys.hitpoints 
		#print(temphp)
		if temphp >= 0:
			vicfanfare.play()
			requestQuote(players[0], HeroprintQuote)


		#the player gained enough experience to level up
		#turn this into a function.
		if players[0].exp >= 200:
			players[0].exp = 0
			players[0].strength = players[0].strength + 1
			players[0].maxhitpoints = players[0].maxhitpoints + random.randrange(5,15) 
			print(players[0].name + " leveled up! " + players[0].name + " now has " + str(players[0].strength) + " stength! And now has " + str(players[0].maxhitpoints) + " Maxhitpoints") 
		
		
		
		qt = input("Press any buton to continue")
		vicfanfare.stop()

		
		# writes the playerfile
		#turn this into a function
		outfile = open(playerfile,'w')
		outfilewriter = csv.writer(outfile,delimiter=',',lineterminator='')
		#outfilewriter.writerow(["name","Hp","Potion","Strength","Exp","Nat Defense","money"])
		outfilewriter.writerow([players[0].name,players[0].maxhitpoints,players[0].potions,players[0].strength,players[0].exp,players[0].defence,players[0].gold])
		outfile.close()
