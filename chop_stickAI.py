#Chop Sticks
#Brandon Abbott
import sys

class Chop_Sticks:
    def __init__(self):
        self.player_one_left =  1
        self.player_one_right = 1
        self.player_two_left = 1
        self.player_two_right= 1
        self.not_at_end = True
        self.playerturn = True

    def tap(self, to_left_hand, from_left_hand):
        print("\n")
        print(self.player_one_left)
        print(self.player_two_left)
        print(self.player_two_right)
        print(self.player_one_right)
        print("\n")

        if self.playerturn:
            if to_left_hand:
                #Player 1's left hand taps Player 2's left hand
                if self.player_two_left == 0: 
                    print('That hand is out try agian')
                    self.playerturn = True
                else:
                    self.player_two_left += self.player_one_left
                    if self.player_two_left >= 5:
                        self.player_two_left = self.player_two_left % 5
                        self.playerturn = False
                    else: 
                        self.playerturn = False
            else:
                #Player 1's right hand taps Player 2's left hand
                if self.player_two_right == 0: 
                    print('That hand is out try agian')
                    self.playerturn = True
                else:
                    self.player_two_right += self.player_one_right
                    if self.player_two_right >= 5:
                        self.player_two_right = self.player_two_right % 5
                        self.playerturn = False
                    else: 
                        self.playerturn = False
        else:
            if to_left_hand:
                #Player 2's left hand taps Player 1's left hand
                if self.player_one_left == 0: 
                    print('That hand is out try agian')
                    self.playerturn = False
                else:
                    self.player_one_left += self.player_two_left
                    if self.player_one_left >= 5:
                        self.player_one_left = self.player_one_left % 5
                        self.playerturn = True
                    else: 
                        self.playerturn = True
            else:
                if self.player_one_right == 0: 
                    print('That hand is out try agian')
                    self.playerturn = False
                else:
                    self.player_one_right += self.player_two_right
                    if self.player_one_right >= 5:
                        self.player_one_right = self.player_one_right % 5
                        self.playerturn = True
                    else: 
                        self.playerturn = True


game = Chop_Sticks() # its not counting the first round?
while game.not_at_end:
    print("Left hand = 1 : Right hand = 0 ")
    hand = input()
    if hand == 1:
        game.tap(True,True)
    elif hand == 9:
        game.tap(False,False)
    else:
        print("try again")
