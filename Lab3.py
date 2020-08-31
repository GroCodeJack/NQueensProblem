import time
import random
import math
import copy


class Board(object):
    """An N-queens solution attempt."""

    def __init__(self, queens):
        """Instances differ by their queen placements."""
        self.queens = queens.copy()  # No aliasing!

    def __len__(self):
     
     return len(self.queens)

    def display(self):
        """Print the board."""
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    print 'Q',
                else:
                    print '-',
            print
        print

    def moves(self):
        """Return a list of possible moves given the current placements."""
        poss = dict()
        for i in range(len(self.queens)):
        	if(self.queens[i] == 7):
        		oneMove = []
        		oneMove.append(i)
        		oneMove.append(6)
        		poss[i] = oneMove
        	elif(self.queens[i] == 0):
        		oneMove = []
        		oneMove.append(i)
        		oneMove.append(1)
        		poss[i] = oneMove
        	else:
        		twoMove = []
        		twoMove.append(i)
        		rand = random.randint(0, 1)
        		if(rand == 0):
        			twoMove.append(self.queens[i] - 1)
        			twoMove.append(self.queens[i] + 1)
        			poss[i] = twoMove
        		else:
        			twoMove.append(self.queens[i] + 1)
        			twoMove.append(self.queens[i] - 1)
        			poss[i] = twoMove

        return poss
        


    def neighbor(self, move):
        """Return a Board instance like this one but with one move made."""
        self.queens[move[0]] = move[1]
        tmpboard = Board(self.queens)
        return tmpboard


    def cost(self):
        """Compute the cost of this solution."""
        n = len(self.queens)
        cost = 0
        for i in range(0, n):
        	for j in range(i + 1, n):
        		if(self.queens[i] == self.queens[j]):
        			cost += 1
        		diag = j - i
        		if self.queens[i] == self.queens[j] - diag or self.queens[i] == self.queens[j] + diag:
        			cost += 1
     
        return cost


class Agent(object):
    """Knows how to solve an n-queens problem with simulated annealing."""

    def anneal(self, board):
        """Return a list of moves to adjust queen placements."""
        tmpboard = copy.deepcopy(board)
        temp = 1
        moveStack = []
        solved = False

        while temp > .0001:
        	poss = tmpboard.moves()
        	rm = random.randint(0, 7)        	
        	move = poss[rm]
        	nBoard = copy.deepcopy(tmpboard)
        	nBoard.neighbor(move)
        	     	
        	if nBoard.cost() < tmpboard.cost():
        		tmpboard = copy.deepcopy(nBoard)
        		moveStack.append(move)
        		if(tmpboard.cost() == 0):
        			solved = True
        			break
        	else:
        		c = tmpboard.cost() - nBoard.cost()
        		p = math.exp(c / temp)
        		x = random.uniform(0, 1)
        		if c > 0 or p > x:
        			tmpboard = copy.deepcopy(nBoard)
        			moveStack.append(move)
        	temp *= 0.9995

       	if solved == False:
       		print("NO SOLUTION FOUND AT THIS TEMPERATURE!")
       	else:
       		return moveStack




def main():
    """Create a problem, solve it with simulated anealing, and console-animate."""

    queens = dict()
    for col in range(8):
        row = random.choice(range(8))
        queens[col] = row
    print(queens)

    board = Board(queens)
    board.display()

    agent = Agent()
    path = agent.anneal(board)
    moves = board.moves()

    while path:
        move = path.pop(0)
        board = board.neighbor(move)
        time.sleep(0.1)
        board.display()


if __name__ == '__main__':
    main()