import random

randnum = random.randint(1,10)

guess =""

while True:
	guess=input("Pick a number from 1 to 10: ")
	guess= int(guess)

	if guess> randnum:
		print("YOUR NUMBER IS TOO HIGH")
	elif guess< randnum:
		print("YOUR NUMBER IS TOO LOW")
	else:
		print("YOU WON")
		play_again=input("do you want to play again?(y/n)")
		if play_again=="y":
			guess=None
			randnum=random.randint(1,10)
		else:
			print("THANK YOU FOR PLAYING")
			break
			



