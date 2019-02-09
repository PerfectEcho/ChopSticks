#Chop Sticks
#Brandon Abbott
import sys

class Chop_Sticks:
    def __init__(self):
        self.player_one_left =  1
        self.player_one_right = 1
        self.player_two_left = 1
        self.player_two_right= 1
        self.computer_on = True
        self.player_one_turn = True
        self.not_at_end = True

        #self.computer_two = False

    def tap(self, to_left_hand, from_left_hand):
        if self.player_one_turn:
            atck_value = self.player_one_left if from_left_hand else self.player_one_right
            if to_left_hand:
                self.player_two_left+=atck_value
            else:
                self.player_two_right+=atck_value

game = Chop_Sticks()
while game.not_at_end:
    hand = input()
    if hand == 1:
       game.tap(True,True)
       print(game.player_two_left)
       print("left was clicked")
    else:
        game.tap(False, False)
        print(game.player_two_right)
        print("right was clicked")

