def guess_tomato():
	print("alright", name, "the final question. the reason why we are playing. which fruit am I thinking of?")
	tomato = input("guess the fruit")
	if tomato.lower() == "tomato":
		print("whoop whoop celebration. well done. I knew you would be able to do it my friend", name,"I hope you had some fun in my guessing game :)")
	else:
		print("ah come on you are so close! please guess again baka", name)
		guess_tomato()


def ice_tomato():
	print("second last question. would you like it as icecream?")
	guess = input("do you like this as icecream?")
	if guess.lower == "Yes":
		print("iewl you have such a bad taste in icecream. I scream for your taste in icecream. please tell me you're joking and say no :')")
		ice_tomato()
	else:
		print("u scream I scream we all scream for people that like this as icecream")
		guess_tomato()


def tros_tomato():
	print("does it grow alone or in bulk")
	tros = input("does it grow alone or in bulk")
	if tros.lower() == "bulk":
		print("alright, alright you're about to guess right")
		ice_tomato()
	else:
		print("you are wrong", name, "i would suggest that you guess again :3")
		tros_tomato()


def color_tomato():
	print("which color do you think it is? ", name)
	color = input("guess which color")
	print("so you're guessing: ",color, "?")
	if color.lower() != "red":
		print("wrong!", name, "you better try again :p")
		color_tomato()
	else:
		tros_tomato()

print("Hi!")
print("what is your name?")
name = input("What's your name? ")
print("can you guess which fruit I am thinking of",name, "be aware I am case sensitive" )
print("on which difficulty do you wanna play? atm there only is easy :')", name)
stage = input("choose between 'easy', 'medium' or 'hard'")
if stage.lower == "easy":
    color_tomato()
else:
	print("nice try ", name,"but there's only one difficulty so let's play")
	color_tomato()
