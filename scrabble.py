import random

line00 = ['|',' ','|','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','|']
lineXX = ['+---+-------------------------------+']
line01 = ['|','a','|','!','-','-','#','-','-','-','!','-','-','-','#','-','-','!','|']
line02 = ['|','b','|','-','+','-','-','-','@','-','-','-','@','-','-','-','+','-','|']
line03 = ['|','c','|','-','-','+','-','-','-','#','-','#','-','-','-','+','-','-','|']
line04 = ['|','d','|','#','-','-','+','-','-','-','#','-','-','-','+','-','-','#','|']
line05 = ['|','e','|','-','-','-','-','+','-','-','-','-','-','+','-','-','-','-','|']
line06 = ['|','f','|','-','@','-','-','-','@','-','-','-','@','-','-','-','@','-','|']
line07 = ['|','g','|','-','-','#','-','-','-','#','-','#','-','-','-','#','-','-','|']
line08 = ['|','h','|','!','-','-','#','-','-','-','*','-','-','-','#','-','-','!','|']
line09 = ['|','i','|','-','-','#','-','-','-','#','-','#','-','-','-','#','-','-','|']
line10 = ['|','j','|','-','@','-','-','-','@','-','-','-','@','-','-','-','@','-','|']
line11 = ['|','k','|','-','-','-','-','+','-','-','-','-','-','+','-','-','-','-','|']
line12 = ['|','l','|','#','-','-','+','-','-','-','#','-','-','-','+','-','-','#','|']
line13 = ['|','m','|','-','-','+','-','-','-','#','-','#','-','-','-','+','-','-','|']
line14 = ['|','n','|','-','+','-','-','-','@','-','-','-','@','-','-','-','+','-','|']
line15 = ['|','o','|','!','-','-','#','-','-','-','!','-','-','-','#','-','-','!','|']
key = "! : 3x word value\r\n+ : 2x word value\r\n@ : 3x letter value\r\n# : 2x letter value"

intro01 = ['|','d','|','#','-','-','+','-','-','-','#','-','-','-','+','-','-','#','|'] + list("  Welcome to Scrabble,")
intro02 = ['|','e','|','-','-','-','-','+','-','-','-','-','-','+','-','-','-','-','|'] + list("  a word game in which")
intro03 = ['|','f','|','-','@','-','-','-','@','-','-','-','@','-','-','-','@','-','|'] + list("  two to four players")
intro04 = ['|','g','|','-','-','#','-','-','-','#','M','#','-','-','-','#','-','-','|'] + list("  score points by placing")
intro05 = ['|','h','|','!','-','-','#','S','C','R','A','B','B','L','E','-','-','!','|'] + list("  tiles bearing a single")
intro06 = ['|','i','|','-','-','#','-','-','-','#','S','#','-','-','-','#','-','-','|'] + list("  letter onto a board")
intro07 = ['|','j','|','-','@','-','-','-','@','-','T','-','@','-','-','-','@','-','|'] + list("  divided into a 15×15")
intro08 = ['|','k','|','-','-','-','-','+','-','-','E','-','-','+','-','-','-','-','|'] + list("  grid of squares.")
intro09 = ['|','l','|','#','-','-','+','-','-','-','R','-','-','-','+','-','-','#','|']

indexes = {'a':3,'b':4,'c':5,'d':6,'e':7,'f':8,'g':9,'h':10,'i':11,'j':12,'k':13,'l':14,'m':15,'n':16,'o':17}

class Game:
	playerList = []
	turn = 0
	turnOne = True
	def addPlayer(self, player):
		self.playerList.append(player)
		self.turn = 1
		self.turnOne = True
		# print(player.name)
	def introduction(self):
		self.playerList = []
		b.buildBoard(False, b.intro)
		while(True):
			try:
				noPlayers = int(input("How many players? : "))
				if (noPlayers > 1 and noPlayers < 5):
					break
				else:
					print("Minimum of 2 players, maximum of 4.")
			except (ValueError) as e:
				print("Invalid input, whole numbers only...")
		for i in range(noPlayers):
			while(True):
				try:
					p = Player(input(f"Player {i+1}, please enter your name : "),[])
					g.addPlayer(p)
					break
				except:
					print("Invalid input")
	def start(self):
		for p in g.playerList:
			p.giveTiles(p)
		b.buildBoard(True, b.board)
	def gameLoop(self):
		while(True):
			self.playerList[self.turn -1].showTiles()
			while(True):
				while(True):
					# try:
					tempList = self.playerList[self.turn -1].tiles
					wordToUse = input(self.playerList[self.turn -1].name + ", your word: ").upper()
					# print(self.playerList[self.turn -1].tiles)
					whereToUse = input("Where would you like to place '" + wordToUse + "'? (x,y,r|d): ")
					# print("WTU:", whereToUse)
					coords = whereToUse.lower().split(",")
					x = indexes[coords[0]]
					y = indexes[coords[1]]
					direction = coords[2]
					if direction == 'd' or direction == 'r':
						print(x,y,direction)
						if self.turnOne:
							if 'h' not in coords:
								print("Invalid spot, you must place the first word over (h,h)")
							else:
								print("we got stuff to do here")
								value = 0
								for letter in wordToUse:
									print(b.board[y][x])
									value += b.getValue(letter, b.board[y][x], g)
									b.board[y][x] = letter
									if direction == "d":
										y += 1
									else:
										x += 1
								print("pre multi : ", value)
								print("::::",self.playerList[self.turn -1].wordMulti)
								if self.playerList[self.turn -1].wordMulti != None:
									print("Word Value : " , value * self.playerList[self.turn -1].wordMulti)
								else:
									print("Word Value : ", value)
								self.playerList[self.turn -1].score += value
								print("Player Score : ", self.playerList[self.turn -1].score)
								self.turnOne = False
								break
						else:
							print("we got stuff to do here")
							break
					else:
						print("Invalid direction, you must go either (r)ight or (d)own")
					# except:
					# 	continue
				for co in coords:
					print("C:",co)
				for letter in wordToUse:
					if letter not in tempList:
						raise ValueError("Not valid")
					else:
						tempList.remove(letter)
				break
			b.buildBoard(True, b.board)
			if self.turn == len(self.playerList):
				self.turn = 1
			else:
				self.turn += 1


class Board:
	board = []
	intro = []
	def __init__(self):
		self.board = [lineXX, line00, lineXX, line01,line02,line03,line04,line05,line06,line07,line08,line09,line10,line11,line12,line13,line14,line15, lineXX]
		self.intro = [lineXX, line00, lineXX, line01,line02,line03,line04,intro01,intro02,intro03,intro04,intro05,intro06,intro07,intro08,intro09,line13,line14,line15, lineXX]
	def buildBoard(self, showKey, board):
		i = 0
		for line in board:
			printLine = ""
			for char in line:
				printLine += char + " "
			print(printLine)
			i += 1
		if showKey:
			print(key)
	def showBoard(self, board):
		self.board = board
		i = 0
		for line in self.board:
			printLine = ""
			for char in line:
				printLine += char + " "
			print(printLine)
			i += 1
		print(key)
	def letterValue(self, letter):
		return t.valueDict[letter]
	def getValue(self, letter, boardPos, g):
		#HERE IS WHERE I NEED TO HANDLE MULTI WORD COMBINATION
		#Issue with object access...
		lv = b.letterValue(letter)
		if boardPos == "-":
			print("normal slot")
		elif boardPos == "!":
			print("3x word")
			p.wordMulti = 3
		elif boardPos == "+":
			print("2x word")
			p.wordMulti = 2
		elif boardPos == "@":
			print("3x letter")
			lv *= 3
		elif boardPos == "#":
			print("2x letter")
			lv *= 2
		elif boardPos == "*":
			print("middle square")
		else:
			print("existing letter")
		return lv


class Tiles:
	letterDict = {}
	valueDict = {}
	def __init__(self):
		self.letterDict = {' ' : 2,'A' : 9,'B' : 2,'C' : 2,'D' : 4,'E' : 1,'F' : 2,'G' : 3,'H' : 2,'I' : 9,'J' : 1,'K' : 1,'L' : 4,'M' : 2,'N' : 6,'O' : 8,'P' : 2,'Q' : 1,'R' : 6,'S' : 4,'T' : 6,'U' : 4,'V' : 2,'W' : 2,'X' : 1,'Y' : 2,'Z' : 1}
		self.valueDict = {' ' : 0,'A' : 1,'B' : 3,'C' : 3,'D' : 2,'E' : 1,'F' : 4,'G' : 2,'H' : 4,'I' : 1,'J' : 8,'K' : 5,'L' : 1,'M' : 3,'N' : 1,'O' : 1,'P' : 3,'Q' : 10,'R' : 1,'S' : 1,'T' : 1,'U' : 1,'V' : 4,'W' : 4,'X' : 8,'Y' : 4,'Z' : 10}
	def clearEmpties(self):
		remove = []
		for letter in self.letterDict.items():
		    if letter[1] == 0:
		    	remove.append(letter[0])
		for removal in remove:
			del self.letterDict[removal]
	def lettersRemaining(self):
		for letter in self.letterDict.items():
		    print(letter[0] + " has " + str(letter[1]) + " tiles remaining")


class Player:
	tiles = []
	score = 0;
	wordMulti = None
	def __init__(self, name, tiles):
		self.name = name
		self.tiles = tiles
		self.score = 0
		self.wordMulti = None
	def setMulti(self, multiplier):
		self.wordMulti = multiplier
	def giveTiles(self, player):
		i = 0
		while len(self.tiles) < 7:
			totalTiles = 0
			for k, v in t.letterDict.items():
				# print(k,v)
				totalTiles += v
			# print("total : ", totalTiles)
			r = random.randint(1,totalTiles)
			# print("random : ", r)
			tileCounter = 0
			i = 0
			for k, v in t.letterDict.items():
				tileCounter += v
				if tileCounter >= r:
					# print("t.ld[k] : ", t.letterDict[k])
					t.letterDict[k] = t.letterDict[k] - 1
					letter = k
					break
				i += 1
			t.clearEmpties()
			player.tiles.append(letter)
			i += 1
	def showTiles(self):
		print("Letters: ",self.tiles)
		valueList = []
		for tile in self.tiles:
			value = t.valueDict[tile]
			valueList.append(str(value))
		print("Values:  ",valueList)




"""
	--------- SCRABBLE ---------
"""
g = Game()
b = Board()
t = Tiles()
g.introduction()
g.start()
g.gameLoop()