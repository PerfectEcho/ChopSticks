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

    def player_defeat(self):
        if self.player_one_left == self.player_one_right == 0:
            print('Player Defeated')
            self.not_at_end = False
        elif self.player_two_left == self.player_two_right == 0:
            print('Player Defeated')
            self.not_at_end = False
        else:
            self.not_at_end =True

    def swap(self):
        if self.playerturn:
            temp = self.player_one_left
            self.player_one_left = self.player_one_right
            self.player_one_right = temp
            print("\n")
            print(self.player_two_left,"        ",self.player_two_right)
            print(self.player_one_left,"        ",self.player_one_right)
            print("\n")
            self.playerturn = True
        else:
            temp = self.player_two_left
            self.player_two_left = self.player_two_right
            self.player_two_right = temp
            print("\n")
            print(self.player_two_left,"        ",self.player_two_right)
            print(self.player_one_left,"        ",self.player_one_right)
            print("\n")
            self.playerturn = False

    def tap(self, to_left_hand):
        if self.playerturn:
            if to_left_hand:
                #Player 1's left hand taps Player 2's left hand
                if self.player_two_left == 0: 
                    print('That hand is out try again')
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
        print("\n")
        print(self.player_two_left,"        ",self.player_two_right)
        print(self.player_one_left,"        ",self.player_one_right)
        print("\n")


game = Chop_Sticks() 
while game.not_at_end:
    if not game.player_defeat():
        hand = input("Left hand = 1, Right hand = 0: ")
        if hand == 1:
            game.tap(True)
        elif hand == 0:
            game.tap(False)
        elif hand == 6:
            game.swap()
        else:
            print("try again")
