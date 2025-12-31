
import random
simple_ex1 = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
simple_ans1 = "534678912672195348198342567859761423426853791713924856961537284287419635345286179"
simple_ex2 = "538016079000380541241500000060900000000035090090004002600200930129040050054690008"
simple_ex3 = "020456789457080236689237040005362974274090653396574800040618397761040528938725060"
simple_ex4 = "999999999999999999999999999999999999999999999999999999999999999999999999999999999"
'''
Examples of Sudoku boards
'''

class Board:
    def __init__(self, string="000000000000000000000000000000000000000000000000000000000000000000000000000000000"):
        self.string = string

    '''
    Initializes the sudoku board, takes in a string of 81 digits with default having all squares as zeros
    '''

    def __str__(self):
        board1 = self.string[0:9]
        board2 = self.string[9:18]
        board3 = self.string[18:27]
        board4 = self.string[27:36]
        board5 = self.string[36:45]
        board6 = self.string[45:54]
        board7 = self.string[54:63]
        board8 = self.string[63:72]
        board9 = self.string[72:81]
        return (board1 + "\n" + board2 + "\n" + board3 + "\n" + board4 + "\n" + board5 + "\n" + board6 + "\n" + board7 + "\n" + board8 + "\n" + board9)

    '''
    Initializes the string of the board
    Need to change it to a better looking board
    '''

    def checkrow(self, row):
        #print(self.string[9*row-9:9*row])
        check = self.string[9*row-9:9*row]
        for char in set(check):
            counts = check.count(char)
            #print(char, counts)
            if (counts > 1):
                return False
        return True

    '''
    Checks a row for duplicates, prints false if there are, prints truth otherwise
    '''

    def checkcol(self, col):
        column = self.string[col-1] + self.string[9+col-1] + self.string[18+col-1] + self.string[27+col-1] + self.string[36+col-1] + self.string[45+col-1] + self.string[54+col-1] + self.string[63+col-1] + self.string[72+col-1]
        #print(column)
        for char in set(column):
            counts = column.count(char)
            #print(char, counts)
            if (counts > 1):
                return False
        return True

    '''
    Checks a column for duplicates, prints false if there are, prints truth otherwise
    '''

    def checkquad(self, quad):
        #quadrant1 = self.string[0:3] + self.string[9:12] + self.string[18:21]
        #quadrant2 = self.string[3:6] + self.string[12:15] + self.string[21:24]
        #quadrant3 = self.string[6:9] + self.string[15:18] + self.string[24:27]
        #quadrant4 = self.string[27:30] + self.string[36:39] + self.string[45:48]
        #quadrant5 = self.string[30:33] + self.string[39:42] + self.string[48:51]
        #quadrant6 = self.string[33:36] + self.string[42:45] + self.string[51:54]
        #quadrant7 = self.string[54:57] + self.string[63:66] + self.string[72:75]
        #quadrant8 = self.string[57:60] + self.string[66:69] + self.string[75:78]
        if (quad < 4):
            quadrant = self.string[quad*3-3:quad*3] + self.string[quad*3+6:quad*3+9] +self.string[quad*3+15:quad*3+18]
        if (4 <= quad < 7):
            val = quad-3
            quadrant = self.string[val*3+24:val*3+27] + self.string[val*3+33:val*3+36] + self.string[val*3+42:val*3+45]
        if (quad>6):
            val = quad - 6
            quadrant = self.string[val*3+51:val*3+54] + self.string[val*3+60:val*3+63] + self.string[val*3+69:val*3+72]
        #print(quadrant)
        for char in set(quadrant):
            counts = quadrant.count(char)
            #print(char, counts)
            if (counts > 1):
                return False
        return True

    '''
    Checks a quadrants for duplicates, prints false if there are, prints truth otherwise
    '''

    def isComp(self):
        if "0" in self.string:
            return False
        else:
            return True

    '''
    Checks whether or not it is a complete board, aka all values are actual numbers and not 0
    '''

    def isWin(self):
        count = 1

        while (count<10):
            if (self.checkrow(count) == False):
                return False
            if (self.checkcol(count) == False):
                return False
            if (self.checkquad(count) == False):
                return False
            count = count + 1
        return True

    '''
    Checks whether or not the board is a correct wining board
    '''

    def rowPts(self):
        counter = 1
        points = 0
        while (counter < 10):
            check = self.string[9*counter-9:9*counter]
            for char in set(check):
                counts = check.count(char)
                if (counts > 1):
                    points = points + counts
            counter = counter + 1
        return points

    '''
    Checks all rows and assigns a value for how "good" the rows are based on amount of duplicates
    '''

    def colPts(self):
        counter = 1
        points = 0
        while (counter < 10):
            column = self.string[counter-1] + self.string[9+counter-1] + self.string[18+counter-1] + self.string[27+counter-1] + self.string[36+counter-1] + self.string[45+counter-1] + self.string[54+counter-1] + self.string[63+counter-1] + self.string[72+counter-1]
            for char in set(column):
                counts = column.count(char)
                if (counts > 1):
                    points = points + counts
            counter = counter +1
        return points

    '''
    Checks all columns and assigns a value for how "good" the columns are based on amount of duplicates
    '''

    def quadPts(self):
        counter = 1
        points = 0
        while (counter < 10):
            if (counter < 4):
                quadrant = self.string[counter*3-3:counter*3] + self.string[counter*3+6:counter*3+9] +self.string[counter*3+15:counter*3+18]
            if (4 <= counter < 7):
                val = counter-3
                quadrant = self.string[val*3+24:val*3+27] + self.string[val*3+33:val*3+36] + self.string[val*3+42:val*3+45]
            if (counter>6):
                val = counter - 6
                quadrant = self.string[val*3+51:val*3+54] + self.string[val*3+60:val*3+63] + self.string[val*3+69:val*3+72]
            for char in set(quadrant):
                counts = quadrant.count(char)
                if (counts > 1):
                    points = points + counts
            counter = counter + 1
        return points

    '''
    Checks all quadrants and assigns a value for how "good" the quadrants are based on amount of duplicates
    '''

    def heuristic(self):

        '''
        count = 1
        while (count<10):
            if (self.checkrow(count) == True):
                good = good + 5
            if (self.checkcol(count) == True):
                good = good + 5
            if (self.checkquad(count) == True):
                good = good + 5
            count = count + 1
        '''
        good = self.colPts() + self.rowPts() + self.quadPts()
        return good

    '''
    Heuristic function that checks all rows, columns, and quadrants for amount of duplicates and gives the board a total score for how "good" it is
    '''



    def complete(self):
        new = ""
        for char in self.string:
            if (char == '0'):
                new += str(random.randint(1,9))
            else:
                new += char
        newBoard = Board(new)
        return newBoard

    '''
    Fills in any zeros in the board with a random digit
    '''

class geneAlg:
    def __init__(self, board, population):
        self.start = board
        self.list = []
        self.gen = 1
        self.zeros = []
        count = 0
        while (count < population):
            new = board.complete()
            self.list.append(new)
            count = count + 1
        count1 = 0
        for char in self.start.string:
            if (char == '0'):
                self.zeros.append(count1)
            count1 += 1

    '''
    Initializes the Genetic Algorithm, it takes in a sudoku board and the population number, it creates that many randomized
    sudoku boards and puts it in a list. It initializes start which is the initial board, list which is the list of boards
    , gen which is the generation number of the algorithm aka how many iterations the algorithm has gone through, and it
    initializes zeros which keeps track of where the free spaces in the board are
    '''

    def __str__(self):
        count = 0
        string = ""
        while (count < len(self.list)):
            string = string + self.list[count].string + "\n"
            count = count + 1
        return string

    '''
    Initializes the string of the genetic algorithm, it prints the strings of all the boards in the population
    '''

    def crossover(self, board1, board2):
        cutPoint1 = random.randint(1,79)
        cutPoint2 = random.randint(1,79)
        #print(cutPoint)
        #print(board1.string[0:cutPoint])
        #print(board2.string[cutPoint:81])
        if (cutPoint1 < cutPoint2):
            new = board1.string[0:cutPoint1] + board2.string[cutPoint1:cutPoint2] + board1.string[cutPoint2:81]
        elif (cutPoint1 > cutPoint2):
            new = board1.string[0:cutPoint2] + board2.string[cutPoint2:cutPoint1] + board1.string[cutPoint1:81]
        else:
            new = board1.string[0:cutPoint1] + board2.string[cutPoint1:81]

        newBoard = Board(new)
        return newBoard

    '''
    The crossover function takes in two boards and randomly selects a cut point in the string where the left side of the
    cut is take from board 1 and the right side of the cut is taken from board 2 and the function stitches them together
    into a new board
    '''

    def mutation(self, board):
        mutPoint = self.zeros[random.randint(0, (len(self.zeros)-1))]
        string = board.string
        rand = str(random.randint(1,9))
        newstring = string[0:mutPoint] + rand + string[mutPoint:len(board.string)]
        board.string = newstring

    '''
    The mutation function takes in a board and randomly changes one of the originally empty digits in the board to another one
    '''

    def sort(self):
        for i in range(len(self.list)):
            for j in range(i+1, len(self.list)):
                if (self.list[i].heuristic() > self.list[j].heuristic()):
                    hold = self.list[i]
                    self.list[i] = self.list[j]
                    self.list[j] = hold

        if (self.list[0].heuristic() == 0):
            return True
        else:
            return False

    def csort(self):
        A = self.list
        n = len(self.list) - 1
        k = 243
        newList1 = []
        newList2 = []
        count = 0
        while count < 244:
            newList2.append[0]
            count += 1
        count1 = 0
        while count1 < len(self.list)-1:
            newList2[self.list[count1].heuristic] = newList2[self.list[count1].heuristic] + 1
            count1 +=1






    '''
    Sorts the list of boards ordered by their score given by the heuristic function with the best score at index 0 and 
    gets worse, also checks if there is a correct board and returns true if there is.
    Need to change it to a better sort
    '''

    def alg(self, sRate, mRate):
        print(self.gen)
        win = self.sort()
        if (win == True):
            print("Finished")
            print("Generation " + str(self.gen))
            print(self.list[0])
            return self.list[0]
        print("current best inividual has score: " + str(self.list[0].heuristic()))
        sPercent = sRate / 100
        length = len(self.list)
        sele = length * sPercent
        newList = []
        count = 0
        while (count < length):
            num1 = random.randint(0,sele-1)
            num2 = random.randint(0,sele-1)
            newItem = self.crossover(self.list[num1],self.list[num2])
            mut = random.randint(1,100)
            if (mut<=mRate):
                self.mutation(newItem)
            newList.append(newItem)
            count = count + 1
        self.gen = self.gen + 1
        self.list = newList
        self.alg(sRate,mRate)

    '''
    This function it the main algorithm, it takes in two percentages sRate and an mRate which is the selection rate and 
    mutation rate of the genetic algorithm.
    1: it sorts the list and checks if there is a winning board and prints out the board and current generation if there is one.
    2: it selects two random boards within the selection rate's parameters and crosses them over to make a new board.
    3: it uses the mutation rate and randomly chooses to either mutate or leave the new board unmutated
    4: it does step 2 and 3 until there is enough new boards to replace the original population and a new generation is made
    The algorithm recursively calls itself increasing the generation everytime until there is a winning board or until 
    the algorithm gets stuck which is something we do not want.
    '''




if __name__ == '__main__':
    ex3 = Board(simple_ex3)
    ex3.heuristic()
    print(ex3)

    ex4 = Board(simple_ex4)
    print(ex4.heuristic())
    print(ex4)

    algo = geneAlg(ex3, 100)
    #algo.alg(10,50)










