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

    def tap(self, to_left_hand, from_left_hand,playerturn):
        if playerturn:
            if to_left_hand:
                atck_value = self.player_one_left if from_left_hand else self.player_one_right
                self.player_two_left+=atck_value
                if self.player_two_left > 5:
                    self.player_two_left = self.player_two_left - 5
                
                print("was player 1 turn")
                print(self.player_two_left)
                self.playerturn = False
            else:
                atck_value = self.player_two_left if from_left_hand else self.player_two_right
                self.player_two_right+=atck_value
                if self.player_two_right > 5:
                    self.player_two_right = self.player_two_right - 5
                self.playerturn = False
                print("was player 1 turn")
                print(self.player_two_right)
        else:
            if to_left_hand:
                atck_value = self.player_two_left if from_left_hand else self.player_two_right
                self.player_one_left+=atck_value
                self.playerturn = True
                print("was player 2 turn")
                print(self.player_one_left)
            else:
                atck_value = self.player_two_left if from_left_hand else self.player_two_right
                self.player_one_right+=atck_value
                self.playerturn = True
                print("was player 2 turn")
                print(self.player_one_right)

game = Chop_Sticks()
while game.not_at_end:
    print("Left hand = 1 : Right hand = 0 ")
    hand = input()
    if hand == 1:
        game.tap(True,True,game.playerturn)
    elif hand == 9:
        game.tap(False,False,game.playerturn)
        
    else:
        print("try again")
