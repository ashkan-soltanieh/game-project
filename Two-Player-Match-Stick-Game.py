''' Match Stick Game:
    
    Rules & Conditions: 
    1) Two player only
    2) Each player can take maximum of 4 sticks in each round.
    3) Total of 31 sticks for User vs Computer mode
    4) Total of 51 sticks for Computer vs Computer mode
    5) User inputs how many rounds to be played
    
    Mode Options:
    1) User vs Computer in easy mode
    2) User vs Computer in hard mode
    3) Computer vs Computer 
'''
import random

class Player:
    ''' player class is used to create instances for each user and 
        used each time according to user selected mode options.
        computer vs computer always runs in easy mode
    '''
    def __init__(self, name = None):
        self.name = name
        self.choice = None
    
    def Difficulty(self, total, selection):
        """ Based on user mode selection and most recent total
            computer stratagize its play.
            Input:
            ---------
            Number of sticks left, difficullty mode
            
            Output:
            ---------
            Decising on the right choice. number ofstick to pick
            
            Example:
            ---------
            >>> Player('Comp').Difficulty(5, 2)
            4

            >>> Player('Comp').Difficulty(4, 2)
            3
            
            >>> Player('Comp').Difficulty(8, 3)
            2

            >>> Player('Comp').Difficulty(12, 3)
            1
        """
        self.selection = selection
        self.total = total
        
        #Computer plays based on below script if user select hard mode        
        if self.selection == 3:
            self.total = total
            if self.total > 5:
                while True:
                    if self.total == 6:
                        self.choice = random.randint(1,4)
                        return self.choice
                        break
                    elif self.total % 5 != 0:                    #computer will win if 1st or 6th units of each tens left for player1.
                        self.choice = random.randint(1,4) 
                        if ((self.total - self.choice) == 5*int(self.total/5)+1):  #try it until it left 1st or 6th left to opponent
                            return self.choice
                            break
                        continue
                    else:
                        self.choice = random.randint(1,4) 
                        if ((self.total - self.choice) == 5*((self.total/5)-1)+1):
                            return self.choice
                            break
                        continue            
            else:
                while True:
                    self.choice = random.randint(1,self.total)             #computer makes first guess which is not more than total
                    if ((self.total - self.choice) != 1) and (self.total != 1): #THIS BLOCK ONLY MAKES THE GAME HARDER
                        while True:                               #loop that gives right guess to player2 to leave last stick to player1
                            self.choice = random.randint(1,4)
                            if (self.total - self.choice == 1):            #As soon as last stick left to player 2 loop ends
                                return self.choice
                                break
                    return self.choice
                    break               
        
        #Computer plays based on below script if user select easy mode or computer vs computer mode 
        else:
            if self.total > 5:
                self.choice = random.randint(1,4) 
                return self.choice
            else:
                while True:
                    self.choice = random.randint(1,self.total)             #computer makes first guess which is not more than total
                    if ((self.total - self.choice) != 1) and (self.total != 1): #THIS BLOCK ONLY MAKES THE GAME HARDER
                        while True:                               #loop that gives right guess to player2 to leave last stick to player1
                            self.choice = random.randint(1,4)
                            if (self.total - self.choice == 1):            #As soon as last stick left to player 2 loop ends
                                return self.choice
                                break
                    return self.choice
                    break            
class Display:
    """ Display class the results of n number rounds on a pie chart. 
    
        Inputs:
        -------
        results list := list of winner and loser in each round. 
        for example if player one wins in first round and loses 
        in second run result list will carry [[1,0],[0,1]]
        
        Output:
        -------
        pie chart of the result. the pie chart for example above split eqally between two players
    """
    def __init__(self, results):
            import matplotlib.pyplot as plt
            results = results
            player_one_wins = sum([item[0] for item in results])
            player_two_wins = sum([item[1] for item in results])
            total = sum([1 for item in results])
            X_percent = player_one_wins/total
            Y_percent = player_two_wins/total
            fig, ax = plt.subplots()
            ax.pie([X_percent, Y_percent], labels = ['Player 1','Player 2'], autopct='%1.1f%%')
            ax.axis('equal')
            plt.show();          

def Trial(round_num):
    ''' Runs computer simulated game
        
        Input:
        ---------
        User input number of rounds to play
        
        Output:
        ---------
        A list sowing winner and loser at each round.
        
        Example
        ----------
        If winner is player one in round one and player two in round two. In total of two rounds the output will be
        [[1,0],[0,1]]
    '''
    result = []
    for i in range(round_num):
        print('\nROUND:'+str(i+1))
        player_one = Player(name = 'Comp1')
        player_two = Player(name = 'Comp2')
        total = 51
        counter1, counter2 = 0, 0
        while total > 5:
            player_one.Difficulty(total, 1)
            total = total - player_one.choice
            counter1 = counter1 + 1
            if total <= 5:
                break
            player_two.Difficulty(total, 1)
            total = total - player_two.choice
            counter2 = counter2 + 1
        if counter1 > counter2:
            while total <= 5:
                player_two.Difficulty(total, 1)            #computer makes first guess which is not more than total
                total = total - player_two.choice
                if total == 1:
                    print('Winner is {}'.format(player_two.name))
                    result.append([0,1])
                    break
                if total == 0:
                    print('Winner is {}'.format(player_one.name))
                    result.append([1,0])
                    break
                player_one.Difficulty(total, 1)            #computer makes first guess which is not more than total
                total = total - player_one.choice
                if total == 1:
                    print('Winner is {}'.format(player_one.name))
                    result.append([1,0])
                    break
                if total == 0:
                    print('Winner is {}'.format(player_two.name))
                    result.append([0,1])
                    break            
        else:
            while total <= 5:
                player_one.Difficulty(total, 1)
                total = total - player_one.choice
                if total == 1:
                    print('Winner is {}'.format(player_one.name))
                    result.append([1,0])
                    break
                if total == 0:
                    print('Winner is {}'.format(player_two.name))
                    result.append([0,1])
                    break
                player_two.Difficulty(total, 1)
                total = total - player_two.choice     
                if total == 1:
                    print('Winner is {}'.format(player_two.name))
                    result.append([0,1])
                    break
                if total == 0:
                    print('Winner is {}'.format(player_one.name))
                    result.append([1,0])
                    break
    return(result)

def main():
    ''' Controls the game play:
        -Part 1: Game mode selection
       
       -Part 2: 
         + For User vs Computer game it returns a list showing winner in each round.
            
            Example
            ----------
           If winner is player one in round one and player two in round two. In total of two rounds the output will be
           [[1,0],[0,1]]
        
        + For Computer vs Computer game it refers Trial function to play
    '''
    print("\t\t\t\t***Welcome to Match Stick Game***")
    while True:
        try:
            print('1. Computer vs Computer\n2. User vs Computer(Easy)\n3. User vs Computer(Hard)\n4. Exit\n')
            menu_selection = int(input('Which game mode would you like to select? '))
            if menu_selection > 4 or menu_selection < 0:
                raise ValueError('Please select one of the valid menu options: 1, 2 or 3')
            elif menu_selection == 4:
                print('Thank you for playing!\n')
                return None
            else:
                break
        except:
            continue
    game_num = int(input('How many rounds would you like to play?'))
    
    sticks = 31
    
    if menu_selection in [2 , 3]:
        name = input('Player1: Please input your name: ')
        player_one = Player(name = name)
        player_two = Player(name = 'Comp')
        print('Hello, {}! You will be playing against {}.'.format(player_one.name, player_two.name))
        result_list = []
        for i in range(game_num):
            print('\nROUND {}: \n'.format(i+1))
            total = sticks
            while True:
                while True:
                    try:
                        player_one.choice = int(input('How many match stick you would like to pick:'))
                        if total - player_one.choice < 0:
                            print('Only {} left on foor, you cannot pick {}'.format(total, player_one.choice))
                            continue
                    except:
                        print('Please enter an integer number.')
                        continue
                    if player_one.choice > 4:
                        print('Four sticks is the maximum you can pick up!!')
                        continue
                    if player_one.choice <= 0:
                        print('You need to pick up at least one stick, you cannot skip!!')
                        continue
                    break    
                total = total - player_one.choice #keeps updated total left
                if total == 1:
                    print('Congratulations! Winner is {}!'.format(player_one.name))
                    result_list.append([1,0])
                    break
                if total == 0:
                    print('You picked all remaining sticks. Winner is {}!'.format(player_two.name))
                    result_list.append([0,1])
                    break
                player_two.Difficulty(total, menu_selection)
                print('{} picked {}\nRemaining {}'.format(player_two.name, player_two.choice, total - player_two.choice))
                total = total - player_two.choice
                if total <= 1:
                    print('You need to pick the last stick. Winner is {}!'.format(player_two.name))
                    result_list.append([0,1])
                    break
                continue
        print('-------------------------------------------')
        print('\nPlayer 1: {}\nPlayer 2: Comp'.format(name))
        Display(result_list)
    
    if menu_selection is 1:
        comp_play = Trial(game_num)
        print('---------------------------------')
        print('\nComp1: Player 1\nComp2: Player 2')
        Display(comp_play)

if __name__ == '__main__':
    main()
