#
#
#War class code
class War:
    def playGame(self):
        self.playingField = Game(['King Crimson', 'Gold Experience Requiem'])
        self.playingField.dealCards()
        self.playingField.play()