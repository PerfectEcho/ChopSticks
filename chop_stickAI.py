#Chop Sticks
#Brandon Abbott
import sys

RECURSION_DEPTH = 9

class Chop_Sticks:
    def __init__(self):
        self.player_one_left =  1
        self.player_one_right = 1
        self.player_two_left = 1
        self.player_two_right= 1
        self.playerturn = True

    def get_state(self):
        return {'p1l': self.player_one_left, 'p1r': self.player_one_right, 'p2l': self.player_two_left, 'p2r':self.player_two_right, 'playerturn': self.playerturn}
    
    def set_state(self, state):
        self.player_one_left = state['p1l']
        self.player_one_right = state['p1r']
        self.player_two_left = state['p2l']
        self.player_two_right = state['p2r']
        self.playerturn = state ['playerturn']
    
    def player_defeat(self):
        if self.player_one_left == self.player_one_right == 0:
            print('Player 1 Defeated')
            return True
        else:
            print('Player 2 Defeated')
            return False

    def ended(self):
        if (self.player_one_left == self.player_one_right == 0) or (self.player_two_left == self.player_two_right == 0):
            return True
        else:
            return False

    def swap(self):
        if self.playerturn:
            temp = self.player_one_left
            self.player_one_left = self.player_one_right
            self.player_one_right = temp
            print("\n")
            print(self.player_two_left,"        ",self.player_two_right)
            print(self.player_one_left,"        ",self.player_one_right)
            print("\n")
        else:
            temp = self.player_two_left
            self.player_two_left = self.player_two_right
            self.player_two_right = temp
            print("\n")
            print(self.player_two_left,"        ",self.player_two_right)
            print(self.player_one_left,"        ",self.player_one_right)
            print("\n")

    def split(self):
        total_one = (self.player_one_left + self.player_one_right)
        total_two = (self.player_two_left + self.player_two_right)
        if self.playerturn:
            if total_one % 2 != 0 :
                print("Can't split")
                return False
            else:
                if self.player_one_left == self.player_one_right:
                    print("Can't split")
                    return False
                else:
                    self.player_one_left = total_one / 2
                    self.player_one_right = total_one / 2
        else:
            if total_two % 2 != 0 :
                print("Can't split")
                return False
            else:
                if self.player_two_left == self.player_two_right:
                    print("Can't split")
                    return False
                else:
                    self.player_two_left = total_two / 2
                    self.player_two_right = total_two / 2
        self.playerturn = not self.playerturn
        return True

    def tap(self, to_left_hand):
        if self.playerturn:
            if to_left_hand:
                #Player 1's left hand taps Player 2's left hand
                if self.player_two_left == 0 or self.player_one_left == 0: 
                    print('That hand is out try again')
                    return False
                else:
                    self.player_two_left += self.player_one_left
                    if self.player_two_left >= 5:
                        self.player_two_left = 0
            else:
                #Player 1's right hand taps Player 2's right hand
                if self.player_two_right == 0 or self.player_one_right == 0: 
                    print('That hand is out try agian')
                else:
                    self.player_two_right += self.player_one_right
                    if self.player_two_right >= 5:
                        self.player_two_right = 0
        else:
            if to_left_hand:
                #Player 2's left hand taps Player 1's left hand
                if self.player_one_left == 0 or self.player_two_left == 0: 
                    print('That hand is out try agian')
                    return False
                else:
                    self.player_one_left += self.player_two_left
                    if self.player_one_left >= 5:
                        self.player_one_left = 0
            else:
                #Player 2's right hand taps Player 1's right hand
                if self.player_one_right == 0 or self.player_two_right == 0: 
                    print('That hand is out try agian')
                    return False
                else:
                    self.player_one_right += self.player_two_right
                    if self.player_one_right >= 5:
                        self.player_one_right = 0

        print("\n")
        print(self.player_two_left,"        ",self.player_two_right)
        print(self.player_one_left,"        ",self.player_one_right)
        print("\n")
        self.playerturn = not self.playerturn
        return True

class AI:
    def make_move(self):
        node = ai.score_moves(game)
        print(node)
        for move in node:
            #print("Move: ", move['move'])
            #print(move['move'], move['score'])
            if  move['score'] > move['score']:
                print(move['move'])
            else:
                print(move['move'])

    #     node = self.score_moves(game)
    #     for move in node:
    #         if move['score'][node] > move['score']:
    #             node = move
    #     print(move['move'], move['score'])
    #     print (node)
            
    def score_moves(self, real_game):
        state = real_game.get_state()
        fake_game = Chop_Sticks()
        fake_game.set_state(state)
        root_node = {'children': [], 'score': 0}
        self.recurse_bfs(fake_game, root_node, RECURSION_DEPTH)
        return root_node['children']


    def recurse_bfs(self, game, node, depth):
        depth -= 1
        if depth == 0:
            return 0
        if game.ended():
            if game.player_defeat():
                return -1
            else: 
                return 1
        else:
            print('LL')
            state = game.get_state()
            if game.tap(True):
                node['children'].append({'children': [], 'score': 0, 'move': 'LL'})
                node['score'] += self.recurse_bfs(game, node['children'][-1], depth)
                game.set_state(state)

            print('RR')
            state = game.get_state()
            if game.tap(False):
                node['children'].append({'children': [], 'score': 0, 'move': 'RR'})
                node['score'] += self.recurse_bfs(game, node['children'][-1], depth)
                game.set_state(state)

            print('LR')
            state = game.get_state()
            game.swap()
            if game.tap(True):
                node['children'].append({'children': [], 'score': 0, 'move': 'LR'})
                game.swap()
                node['score'] += self.recurse_bfs(game, node['children'][-1], depth)
                game.set_state(state)
            else:
                game.swap()

            print('RL')
            state = game.get_state()
            game.swap()
            if game.tap(False):
                node['children'].append({'children': [], 'score': 0, 'move': 'RL'})
                game.swap()
                node['score'] += self.recurse_bfs(game, node['children'][-1], depth)
                game.set_state(state)
            else:
                game.swap()

            print('split')
            state = game.get_state()
            if game.split():
                node['children'].append({'children': [], 'score': 0, 'move': 'split'})
                node['score'] += self.recurse_bfs(game, node['children'][-1], depth)
                game.set_state(state)

            return node['score']

game = Chop_Sticks()   
try:
    ai = AI()
    moves = ai.score_moves(game)
    print(moves)
    for move in moves:
        print("Move: ", move['move'])
 
except RuntimeError:
    print('Stack overflow')
    exit()

# while not game.player_defeat:
#     if not game.player_defeat():
#         if ai.make_move() == 'LL':
#             game.tap(True)
#         elif ai.make_move() == 'RR':
#             game.tap(False)
#         elif ai.make_move() == 'LR':
#             game.swap()
#             game.tap(False)
#         elif ai.make_move() == 'RL':
#             game.swap()
#             game.tap(True)
#         elif ai.make_move() == 'split':
#             game.split()
#         else:
#             print("try again")
