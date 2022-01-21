# Program: Analysis of COVID-19 and CBC Test Results
# Author: Jeffrey Chumley
# Date: 1/19/2022
# Description: This program analyzes a dataset of COVID-19
#  and CBC test results and displays summaries of the data.
#  See README.md file.

# import modules for statistical analysis and plotting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_analysis_functions import *


# This function displays the menu options for the user to select from.
# The number of options is tied to the get_menu_selection function and
# the match-case selection in the main section.
def display_menu():
    print("""\nMenu Options:
        1. CBC Cell Counts
        2. RBC Indices
        3. WBC Differential (absolute count)
        4. WBC Differential (relative percent)
        5. Leukocyte count comparison
        6. Low platelet count comparison
        7. Description of the dataset
        8. Exit""")

# This function gets a menu selection from the user
def get_menu_selection():
    
    display_menu()
    selection = None

    # prompt for selection until valid one is received
    while selection not in range(1, 9):
        selection = int(input("Select an output to display (enter 1-8): "))

        # notify of invalid selection and redisplay menu
        if selection not in range(1, 9):
            print("\nInvalid selection.")
            display_menu()
    
    return selection

# set the data file name and create a DataFrame from the csv file
data_file_name = "full_einstein_25col.csv"
covid_cbc_df = pd.read_csv(data_file_name, header=0, index_col='ID', parse_dates=['Date'])

# rename several columns for ease of use
covid_cbc_df.rename(columns={'y': 'COVID', 'Leukocytes':'WBC', 'RedBloodCells': 'RBC', 'Platelets':'PLT'}, inplace=True)

# create new column identifying if platelet is below the normal range of 150
covid_cbc_df['PLTref'] = np.where(covid_cbc_df['PLT'] < 150, 'low', 'normal/high')

# prompt user for what to display
menu_selection = get_menu_selection()

# continue showing options and results until user quits
while menu_selection < 8 and menu_selection > 0:
    
    if (menu_selection == 1):
        plot_cell_counts(covid_cbc_df)
    elif (menu_selection == 2):
        plot_rbc_indices(covid_cbc_df)
    elif (menu_selection == 3):
        plot_wbc_abs_diff(covid_cbc_df)
    elif (menu_selection == 4):
        plot_wbc_rel_diff(covid_cbc_df)
    elif (menu_selection == 5):
        wbc_covid_comp(covid_cbc_df)
    elif (menu_selection == 6):
        platelet_covid_comp(covid_cbc_df)
    elif (menu_selection == 7):
        summarize_dataset(covid_cbc_df)
    else:
        print()
    
    menu_selection = get_menu_selection()