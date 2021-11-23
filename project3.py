from random import shuffle
#52 deck of cards

def deckOfCards():
	Deck = []
	for i in range(4):
		faceValues = ['A', 'J', 'Q', 'K']
		for card in range(2,11):
			Deck.append(card)
		for card in faceValues:
			Deck.append(card)

	return Deck

dC = deckOfCards()
shuffle(dC)			#shuffling the deck of 52 cards before starting play

discardPile = []	#discard Pile is empty at the beginning

class Player:
	def __init__(self, hand, score):
		self.hand = hand
		self.score = 0

	def printHand(self):		# printing the hand (3 x 2)
		
		for item in range(len(self.hand)):
			if item == 2:
				print('X ')
			else:
				print('X ', end='')


	def try1(self, var1, var2):	# initial play ie first try, taking two cards from hand to be faced UP 

		
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')		
				

	def try2(self, var1, var2, var3= -1): # 2nd try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')			


	def try3(self, var1, var2, var3= -1, var4= -1):	# 3rd try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')	

					

	def try4(self, var1, var2, var3= -1, var4= -1, var5= -1): # 4th try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')	



	def try5(self, var1, var2, var3= -1, var4= -1, var5= -1, var6= -1):  # 5th try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')	



	def try6(self, var1, var2, var3= -1, var4= -1, var5= -1, var6= -1, var7= -1):  # 6th try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')	



	def try7(self, var1, var2, var3= -1, var4= -1, var5= -1, var6= -1, var7= -1, var8= -1):  # 7th try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')



	def try8(self, var1, var2, var3= -1, var4= -1, var5= -1, var6= -1, var7= -1, var8= -1, var9= -1):  # 8th try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')				



	def try9(self, var1, var2, var3= -1, var4= -1, var5= -1, var6= -1, var7= -1, var8= -1, var9= -1, var10= -1):  # 9th try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9) or item == int(var10):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9) or item == int(var10):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')						



	def try10(self, var1, var2, var3= -1, var4= -1, var5= -1, var6= -1, var7= -1, var8= -1, var9= -1, var10= -1, var11= -1): # 10th try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9) or item == int(var10) or item == int(var11):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9) or item == int(var10) or item == int(var11):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')				

	'''
	def try11(self, var1, var2, var3= -1, var4= -1, var5= -1, var6= -1, var7= -1, var8= -1, var9= -1, var10= -1, var11= -1, var12= -1): # 11th try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9) or item == int(var10) or item == int(var11) or item == int(var12):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9) or item == int(var10) or item == int(var11) or item == int(var12):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')	
					

	def try12(self, var1, var2, var3= -1, var4= -1, var5= -1, var6= -1, var7= -1, var8= -1, var9= -1, var10= -1, var11= -1, var12= -1, var13= -1): # last try after choices function
		for item in range(6):
			if item == 2:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9) or item == int(var10) or item == int(var11) or item == int(var12) or item == int(var13):
					print(str(self.hand[item])+ ' ')
				else:
					print('X ')
			else:
				if item == int(var1) or item == int(var2) or item == int(var3) or item == int(var4) or item == int(var5) or item == int(var6) or item == int(var7) or item == int(var8) or item == int(var9) or item == int(var10) or item == int(var11) or item == int(var12) or item == int(var13):
					print(str(self.hand[item])+ ' ', end='')
				else:
					print('X ',end='')	
					
	'''

	def choices(self):			# three choices for the player to make on each try
		print('')
		choice = int(input("Enter number of choice: '1'- for taking card from Stock, '2'- for taking card from Discard '3'- for choosing to face UP one of your card in hand: "))
		if choice == 1:
			cardFromStock = dC.pop()
			print('card taken from Stock is: ', cardFromStock)
			input1= input('Would you like to swap: y/n: ')
			if input1 == 'y':
				input2 = int(input('choose card index to swap -> 0/1/2/3/4/5: '))
				self.hand[input2] = cardFromStock
				return input2
			else:
				discardPile.append(cardFromStock)
				return -1

		elif choice == 2:
			if len(discardPile) > 0:
				cardFromDiscard = discardPile.pop()
				input3 = int(input('Enter card index to be swaped -> 0/1/2/3/4/5: '))
				self.hand[input3] = cardFromDiscard
				return input3 


		elif choice == 3:
			input4 = int(input('Enter card index to be faced UP -> 0/1/2/3/4/5: '))
			return input4
				
	

	def setScore(self, playerName):
		print('Printing the hand in 3 X 2 order matrix for', playerName)
		for item in range(6):
			if item == 2:
				print(str(self.hand[item])+ ' ')
			else:
				print(str(self.hand[item])+ ' ', end='')

		input5 = input('Do you want to see the score? (y/n): ')
		if input5 == 'y':
			faceValues= { 'A': 1, 'J': 10, 'Q': 10, 'K': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10}			
			for card in self.hand:
				self.score += faceValues[str(card)]

			# index0 == index3 -> score = 0 (across that column)
			# index1 == index4 -> score = 0 (across that column)
			# index2 == index5 -> score = 0 (across that column)
			if self.hand[0] == self.hand[3]:
				if self.hand[0] == 'A':
					self.score = self.score - ( 2 * 1 )
				elif self.hand[0] == 'K':
					self.score = self.score - ( 2 * 0 )
				elif self.hand[0] == 'J' or self.hand[0] == 'Q':
					self.score = self.score - ( 2 * 10 )
				else:
					self.score = self.score - ( 2 * int(self.hand[0]) )


			if self.hand[1] == self.hand[4]:
				if self.hand[1] == 'A':
					self.score = self.score - ( 2 * 1 )
				elif self.hand[1] == 'K':
					self.score = self.score - ( 2 * 0 )
				elif self.hand[1] == 'J' or self.hand[1] == 'Q':
					self.score = self.score - ( 2 * 10 )
				else:
					self.score = self.score - ( 2 * int(self.hand[1]) )


			if self.hand[2] == self.hand[5]:
				if self.hand[2] == 'A':
					self.score = self.score - ( 2 * 1 )
				elif self.hand[2] == 'K':
					self.score = self.score - ( 2 * 0 )
				elif self.hand[2] == 'J' or self.hand[2] == 'Q':
					self.score = self.score - ( 2 * 10 )
				else:
					self.score = self.score - ( 2 * int(self.hand[2]) )


		print('Final score is: ', self.score)
		return self.score


	def rules(self):
		print('This is a 2 player game named golf card game')
		print('''
			THE INITIATION
			Each player is dealt 6 cards face down from the deck which consists of 52 cards. 
			The remainder of the cards in the deck are placed face down, and the top card is turned up to start the discard pile beside it. 
			Players arrange their 6 cards in 2 rows of 3 (2 rows X 3 columns) in front of them and turn 2 of these cards face up. 
			The remaining cards stay face down and cannot be looked at.

			THE GAMEPLAY
			The objective is for players to have the lowest value of the cards in front of them by either swapping them for lesser value cards or by pairing them up with cards of equal rank.
			The players take turns drawing single cards from either the stock or discard piles
			The drawn card may either be swapped for one of that player's 6 cards, or discarded into the discard pile. 
			If the card is swapped for one of the face down cards, the card swapped in remains face up. 
			The game continues till each player has taken 10 tries, after that the scores for each player is calculated even if all cards arent faced up.
			The player with the lowest total score is the winner!

			SCORING
			Each ace counts 1 point.
			Each numeral card from 2 to 10 scores face value.
			Each jack or queen scores 10 points.
			Each king scores zero points.
			A PAIR OF EQUAL CARDS IN THE SAME COLUMN SCORES ZERO POINTS FOR THE COLUMN.

			Hope you enjoy the game as much as I liked coding it!!
			Thank you Pirple for this wonderful course.

			''')

		resumeCommand = input("Please enter '--resume' to continue with the game: ")
		if resumeCommand == '--resume':
			return True


playerName1 = input('First player\'s name: ')
P1 = Player([dC.pop(), dC.pop(), dC.pop(), dC.pop(), dC.pop(), dC.pop()], 0)	# handing 6 cards to player1 from deck

playerName2 = input('Second player\'s name: ')
P2 = Player([dC.pop(), dC.pop(), dC.pop(), dC.pop(), dC.pop(), dC.pop()], 0)	# handing 6 cards to player2 from deck

tries = 0

# 1st try for both players
print('1st try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))

P1.printHand()
var1a = input("choose first card index to face up 0 -> 5 or type '--help' to read the rules: ")
if var1a == '--help':
	P1.rules()
	var1a = input("choose first card index to face up 0 -> 5: ")

var2a = input("choose second card index to face up 0 -> 5 or type '--help' to read the rules: ")
if var2a == '--help':
	P1.rules()
	var2a = input("choose second card index to face up 0 -> 5: ")

P1.try1(var1a, var2a)
tries += 1


print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))

P2.printHand()
var1b = input("choose first card index to face up 0 -> 5 or type '--help' to read the rules: ")
if var1b == '--help':
	P2.rules()
	var1b = input("choose first card index to face up 0 -> 5: ")

var2b = input("choose second card index to face up 0 -> 5 or type '--help' to read the rules: ")
if var2b == '--help':
	P2.rules()
	var2b = input("choose second card index to face up 0 -> 5: ")

P2.try1(var1b, var2b)



# 2nd try for both Players
print('\n')
print('2nd try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var3a = P1.choices()
tries += 1
P1.try2(var1a, var2a, var3a)
print(' ')
print(discardPile)


print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var3b = P2.choices()
P2.try2(var1b, var2b, var3b)
print(' ')
print(discardPile)




# 3rd try for both Players
print('\n')
print('3rd try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var4a = P1.choices()
tries += 1
P1.try3(var1a, var2a, var3a, var4a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var4b = P2.choices()
P2.try3(var1b, var2b, var3b, var4b)
print(' ')
print(discardPile)




# 4th try for both Players
print('\n')
print('4th try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var5a = P1.choices()
tries += 1
P1.try4(var1a, var2a, var3a, var4a, var5a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var5b = P2.choices()
P2.try4(var1b, var2b, var3b, var4b, var5b)
print(' ')
print(discardPile)




# 5th try for both Players
print('\n')
print('5th try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var6a = P1.choices()
tries += 1
P1.try5(var1a, var2a, var3a, var4a, var5a, var6a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var6b = P2.choices()
P2.try5(var1b, var2b, var3b, var4b, var5b, var6b)
print(' ')
print(discardPile)




# 6th try for both Players
print('\n')
print('6th try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var7a = P1.choices()
tries += 1
P1.try6(var1a, var2a, var3a, var4a, var5a, var6a, var7a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var7b = P2.choices()
P2.try6(var1b, var2b, var3b, var4b, var5b, var6b, var7b)
print(' ')
print(discardPile)




# 7th try for both Players
print('\n')
print('7th try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var8a = P1.choices()
tries += 1
P1.try7(var1a, var2a, var3a, var4a, var5a, var6a, var7a, var8a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var8b = P2.choices()
P2.try7(var1b, var2b, var3b, var4b, var5b, var6b, var7b, var8b)
print(' ')
print(discardPile)




# 8th try for both Players
print('\n')
print('8th try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var9a = P1.choices()
tries += 1
P1.try8(var1a, var2a, var3a, var4a, var5a, var6a, var7a, var8a, var9a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var9b = P2.choices()
P2.try8(var1b, var2b, var3b, var4b, var5b, var6b, var7b, var8b, var9b)
print(' ')
print(discardPile)




# 9th try for both Players
print('\n')
print('9th try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var10a = P1.choices()
tries += 1
P1.try9(var1a, var2a, var3a, var4a, var5a, var6a, var7a, var8a, var9a, var10a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var10b = P2.choices()
P2.try9(var1b, var2b, var3b, var4b, var5b, var6b, var7b, var8b, var9b, var10b)
print(' ')
print(discardPile)




# 10th try for both Players
print('\n')
print('Last try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var11a = P1.choices()
tries += 1
P1.try10(var1a, var2a, var3a, var4a, var5a, var6a, var7a, var8a, var9a, var10a, var11a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var11b = P2.choices()
P2.try10(var1b, var2b, var3b, var4b, var5b, var6b, var7b, var8b, var9b, var10b, var11b)
print(' ')
print(discardPile)



'''
# 11th try for both Players
print('\n')
print('11th try for both players')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var12a = P1.choices()
tries += 1
P1.try11(var1a, var2a, var3a, var4a, var5a, var6a, var7a, var8a, var9a, var10a, var11a, var12a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var12b = P2.choices()
P2.try11(var1b, var2b, var3b, var4b, var5b, var6b, var7b, var8b, var9b, var10b, var11b, var12b)
print(' ')
print(discardPile)




# 12th try for both Players
print('\n')
print('12th try for both players!')
print('Hello {fname}, its your turn'.format(fname = playerName1))
var13a = P1.choices()
tries += 1
P1.try12(var1a, var2a, var3a, var4a, var5a, var6a, var7a, var8a, var9a, var10a, var11a, var12a, var13a)
print(' ')
print(discardPile)

print('\n')
print('Hello {fname}, its your turn'.format(fname = playerName2))
var13b = P2.choices()
P2.try12(var1b, var2b, var3b, var4b, var5b, var6b, var7b, var8b, var9b, var10b, var11b, var12b, var13b)
print(' ')
print(discardPile)


'''

#calculating the scores for both players
score1= P1.setScore(playerName1)
score2= P2.setScore(playerName2)
print('\n')
if score1 > score2:
	print('{fname} is the winner!'.format(fname = playerName2))
elif score1 < score2:
	print('{fname} is the winner!'.format(fname = playerName1))
else:
	print('Its a draw!')












