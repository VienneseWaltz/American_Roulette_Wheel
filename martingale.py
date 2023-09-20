""""""  		  	   		   	 			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		   	 			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		   	 			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		   	 			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		   	 			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		   	 			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		   	 			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		   	 			  		 			 	 	 		 		 	
or edited.  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		   	 			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		   	 			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		   	 			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
Student Name: Stella Soh (replace with your name)  		  	   		   	 			  		 			 	 	 		 		 	
GT User ID: lsoh3 (replace with your User ID)  		  	   		   	 			  		 			 	 	 		 		 	
GT ID: 903641298 (replace with your GT ID)  		  	   		   	 			  		 			 	 	 		 		 	
"""  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import sys
  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
def author():  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    :return: The GT username of the student  		  	   		   	 			  		 			 	 	 		 		 	
    :rtype: str  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    return "lsoh3"  # replace tb34 with your Georgia Tech username.
  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
def gtid():  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    :return: The GT ID of the student  		  	   		   	 			  		 			 	 	 		 		 	
    :rtype: int  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    return 903641298  # replace with your GT ID number
  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
def get_spin_result(win_prob):  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		   	 			  		 			 	 	 		 		 	
  		  	   		   	 			  		 			 	 	 		 		 	
    :param win_prob: The probability of winning  		  	   		   	 			  		 			 	 	 		 		 	
    :type win_prob: float  		  	   		   	 			  		 			 	 	 		 		 	
    :return: The result of the spin.  		  	   		   	 			  		 			 	 	 		 		 	
    :rtype: bool  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    result = False
    if np.random.random() <= win_prob:  		  	   		   	 			  		 			 	 	 		 		 	
        result = True  		  	   		   	 			  		 			 	 	 		 		 	
    return result  		  	   		   	 			  		 			 	 	 		 		 	



def winning_strategy(win_prob, winning_cap, losing_cap):
    '''
    Winning_strategy is for one episode. It returns a 1-d Numpy array, winnings_array.
    :param winning_cap - The maximum winning amount to stop and walk away
    :param losing_cap - The maximum loss at which the gambler stops betting
    :return: winnings_array - The array that has episodes in rows, and Spin # in
                                columns. Value in each cell is the cumulative winnings.
    '''

    # winnings_array is a 1-d array to be returned
    winnings_array = np.zeros(1001)

    episode_winnings = 0
    spin_number = 0
    while episode_winnings < winning_cap and spin_number < 1000 and episode_winnings > losing_cap:
        won = False
        bet_amount = 1
        while not won and spin_number < 1000:
            # Bet on black. Let the roulette wheel spin.
            won = get_spin_result(win_prob)
            spin_number += 1
            if won == True:
                episode_winnings += bet_amount
            else:
                episode_winnings -= bet_amount
                bet_amount *= 2
                # To take care of the corner case bet should be $N, but you only have $M
                # where M < N
                bet_amount = min(bet_amount, episode_winnings - losing_cap)
            winnings_array[spin_number] = episode_winnings

    winnings_array[spin_number+1:] = episode_winnings

    return winnings_array

def build_winnings(num_episodes, win_prob, winning_cap, losing_cap):
    '''
    This function calls on winning_strategy() that returns winnings_array (a 1-d array)
    and builds up a 2-d array, winnings.
    :param num_episodes - The number of episodes
    :param winning_cap  - The target maximum winning amount
    :param losing_cap  -  The maximum loss at which gambler stops betting
    :return: winnings - A 2-d, (num_episodes x spin_number+1) array
    '''

    winnings = np.zeros((1001,num_episodes))
    for i in range(num_episodes):
        winnings[:, i] = winning_strategy(win_prob, winning_cap, losing_cap)

    return winnings

def test_code():  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    Method to test your code  		  	   		   	 			  		 			 	 	 		 		 	
    """  		  	   		   	 			  		 			 	 	 		 		 	
    win_prob = 18/38.0  # 18 blacks out of 38 possible numbers on the roulette table
    np.random.seed(gtid())  # do this only once

    # Flag saveFig set to True to disable "plt.show".
    saveFig = True

    # Experiment 1
    # Figure 1
    fig1_episodes = 10

    # Create a dataframe from winnings
    winnings = build_winnings(fig1_episodes, win_prob, 80, -sys.maxsize - 1)
    # winnings = build_winnings(fig1_episodes, win_prob, 80, -256)
    col_names = ['Episode' + str(i) for i in range(fig1_episodes)]
    df = pd.DataFrame(data=winnings, columns=col_names)
    ax = df.plot(title='Roulette Winnings (Fig.1)', fontsize=12)
    ax.set_xlabel(xlabel='Spin #')
    ax.set_xlim(0,300)
    ax.set_ylabel(ylabel='Cumulative Winnings ($)')
    ax.set_ylim(-256, 100)
    if saveFig:
        fig1 = plt.gcf()
        fig1.savefig('Figure1.png', format='png', dpi=100)
        plt.close(fig1)
    else:
        plt.show()


    # Figure 2
    fig2_episodes = 1000

    winnings = build_winnings(fig2_episodes, win_prob, 80, -sys.maxsize - 1)
    # Create a dataframe, df2 - a (episodes+1) x (episodes) array from winnings
    df2 = pd.DataFrame(data=winnings)
    # Iterate over columns to compute the mean across the rows for each round of the spins
    mean_episodes_2 = df2.mean(axis=1)
    # Iterate over the columns to get df2.std to compute line_above_mean and line_below_mean
    line_above_mean = mean_episodes_2 + df2.std(axis=1)
    line_below_mean = mean_episodes_2 - df2.std(axis=1)
    mean_episodes_2 = pd.DataFrame(mean_episodes_2.values, columns=['mean'])
    ax = mean_episodes_2.plot(title='Mean vs Spin # (Fig.2)', fontsize=12)
    ax.set_xlabel(xlabel='Spin #')
    ax.set_xlim(0,300)
    ax.set_ylabel(ylabel='Mean Wining Amount($)')
    ax.set_ylim(-256,100)
    line_above_mean = pd.DataFrame(line_above_mean.values, columns=['Std above mean'])
    line_below_mean = pd.DataFrame(line_below_mean.values, columns=['Std below mean'])
    line_above_mean.plot(label='Above mean', ax=ax)
    line_below_mean.plot(label='Below mean', ax=ax)
    if saveFig:
        fig2 = plt.gcf()
        fig2.savefig('Figure2.png', format='png', dpi=100)
        plt.close(fig2)
    else:
        plt.show()


    # Figure 3
    # Figure 3's simulator runs for 1000 episodes just as in Figure 2

    # Plot all the median values of winnings for each (round of spin?) episode
    median_episodes_3 = df2.median(axis=1)
    line_above_median = median_episodes_3 + df2.std(axis=1)
    line_below_median = median_episodes_3 - df2.std(axis=1)
    median_episodes_3 = pd.DataFrame(median_episodes_3.values, columns=['median'])

    ax = median_episodes_3.plot(title='Median vs Spin # (Fig.3)', fontsize=12)
    ax.set_xlabel(xlabel='Spin #')
    ax.set_xlim(0, 300)
    ax.set_ylabel(ylabel='Median Winning Amount($)')
    ax.set_ylim(-256, 100)

    line_above_median = pd.DataFrame(line_above_median.values, columns=['std above mean'])
    line_below_median = pd.DataFrame(line_below_median.values, columns=['std below mean'])
    line_above_median.plot(label='Above median', ax=ax)
    line_below_median.plot(label='Below median', ax=ax)
    if saveFig:
        fig3 = plt.gcf()
        fig3.savefig('Figure3.png', format='png', dpi=100)
        plt.close(fig3)
    else:
        plt.show()

    # Experiment 2
    # Figure 4
    winnings = build_winnings(fig2_episodes, win_prob, 80, -256)
    df4 = pd.DataFrame(data=winnings)
    mean_episodes_4 = df4.mean(axis=1)
    line_above_mean_4 = mean_episodes_4 + df4.std(axis=1)
    line_below_mean_4 = mean_episodes_4 - df4.std(axis=1)
    mean_episodes_4 = pd.DataFrame(mean_episodes_4.values, columns=['mean'])
    ax = mean_episodes_4.plot(title='Mean vs Spin # (Fig.4)', fontsize=12)
    ax.set_xlabel(xlabel='Spin #')
    ax.set_xlim(0, 300)
    ax.set_ylabel(ylabel='Mean Winning Amount ($)')
    ax.set_ylim(-256, 100)
    line_above_mean_4 = pd.DataFrame(line_above_mean_4.values, columns=['std above mean'])
    line_below_mean_4 = pd.DataFrame(line_below_mean_4.values, columns=['std below mean'])
    line_above_mean_4.plot(label='Above mean', ax=ax)
    line_below_mean_4.plot(label='Below mean', ax=ax)
    if saveFig:
        fig4 = plt.gcf()
        fig4.savefig('Figure4.png', format='png', dpi=100)
        plt.close(fig4)
    else:
        plt.show()


    # Figure 5
    median_episodes_5 = df4.median(axis=1)
    line_above_median_5 = median_episodes_5 + df4.std(axis=1)
    line_below_median_5 = median_episodes_5 - df4.std(axis=1)
    median_episodes_5 = pd.DataFrame(median_episodes_5, columns=['median'])
    ax = median_episodes_5.plot(title='Median vs Spin # (Fig.5)', fontsize=12)
    ax.set_xlabel(xlabel='Spin #')
    ax.set_xlim(0, 300)
    ax.set_ylabel(ylabel='Median Winning Amount($)')
    ax.set_ylim(-256, 100)
    line_above_median_5 = pd.DataFrame(line_above_median_5.values, columns=['std above mean'])
    line_below_median_5 = pd.DataFrame(line_below_median_5.values, columns=['std below mean'])
    line_above_median_5.plot(label='Above median', ax=ax)
    line_below_median_5.plot(label='Below median', ax=ax)
    if saveFig:
        fig5 = plt.gcf()
        fig5.savefig('Figure5.png', format='png', dpi=100)
        plt.close(fig5)
    else:
        plt.show()


if __name__ == "__main__":  		  	   		   	 			  		 			 	 	 		 		 	
    test_code()  		  	   		   	 			  		 			 	 	 		 		 	
