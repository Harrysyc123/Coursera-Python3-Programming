VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():
    def __init__(self,name):
        self.name=name
        self.prizeMoney=0
        self.prizes=[]
    def addMoney(self,amt):
        self.prizeMoney+=amt
    def goBankrupt(self):
        self.prizeMoney=0
    def addPrize(self,prize):
        self.prizes.append(prize)
    def __str__(self):
        return '{} (${})'.format(self.name,self.prizeMoney)
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self,name):
        WOFPlayer.__init__(self,name)
    def getMove(self,category, obscuredPhrase, guessed):
        return '{} has \${}\nCategory:{}\nPharse:{}\nGuessed:{}\nGuess a letter, phrase, or type \'exit\' or \'pass\':'.format(self.name,self.prizeMoney,category,obscuredPhrase, guessed)
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES='ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self,name,difficulty):
        WOFPlayer.__init__(self,name)
        self.difficulty=difficulty
 
    def smartCoinFlip(self):
        x=random.randint(1, 10)
        if x>self.difficulty:
            return True
        else:
            return False
    def getPossibleLetters(self,guessed):
        letters=[]
        LETTERS_remove='BCDFGHJKLMNPQSTVWXYZ'
        if self.prizeMoney>VOWEL_COST:
            for l in LETTERS:
                if l not in guessed:
                    letters.append(l)
        else:
            for l in LETTERS_remove:
                if l not in guessed:
                    letters.append(l)
        return letters
    def getMove(self,category, obscuredPhrase, guessed):
        letters=self.getPossibleLetters(guessed)
        if letters==[]:
            return 'pass'
        decision=self.smartCoinFlip()
        if decision==True:
            for l in self.SORTED_FREQUENCIES:
                if l in letters:
                    return l
        else:
            rand_letter = random.choice(letters)
            return rand_letter
        
