

x = input("What is your name?: ")
print('hello, ' + x)


def ft2mt(h):
	ft2meters = float(h) / 3.281
	return ft2meters
lo = True
while lo:
	h = (input("How tall are you in dah fokn feet?: "))
	if not h.isnumeric():
		print("Please input an actual fokn numbah")
	else:
		lo = False

#ft2meters = h / 3.281
poop = ft2mt(h)
message  = "You are " + str(poop) + " meters tall"
print(message)

def lb2kg(w):
	lb2kg= float(w) / 2.205
	return lb2kg
lo = True
while lo:
	w = input("How much o ah fokn fatso are you in pounds?: ")
	if w.isnumeric() == False:
		print("Shtap")
	else:
		lo = False

#lb2kg = w / 2.205
fat = lb2kg(w)
message2  = "You are " + str(fat) + " kg fat ya fatso"
print(message2)



bmi = fat / poop ** 2
message3 = "yo bmi is " + str(bmi) + " ye fokn fatah"
print(message3)

if bmi < 20:
	print("you are underweight")
if bmi > 20:
	print("you are fat")

