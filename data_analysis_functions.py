# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# this function returns a list with two series (filter by COVID)
def plot_by_covid(df, display_col):
    return [df.loc[df['COVID'] == 0, display_col], df.loc[df['COVID'] == 1, display_col]]

# this function plots the WBC, RBC, and Platelet cell counts for COVID v. non-COVID patients
def plot_cell_counts(df):
    # create a figure with 3 subplots (1 row and 3 columns)
    fig, (wbc_ax, rbc_ax, plt_ax) = plt.subplots(nrows=1, ncols=3, figsize=(14, 4.5))

    # add a figure title and adjust the spacing between the title and the plots
    fig.suptitle('Cell Counts by COVID Result', fontsize=16)
    fig.subplots_adjust(top=0.8)

    # adjust whitespace between subplots
    plt.subplots_adjust(wspace=0.4)

    # plot WBC count by COVID neg or COVID pos result
    wbc_ax.boxplot(plot_by_covid(df, 'WBC'),
                showfliers=False,
                widths=0.4,
                labels=['COVID Neg', 'COVID Pos'],
    )
    # set WBC subplot labels
    wbc_ax.set_title('WBC Count')
    wbc_ax.set_ylabel('WBC x 10^3 / uL')
    wbc_ax.set_ylim(ymin=0)

    # plot RBC count by COVID neg or COVID pos result
    rbc_ax.boxplot(plot_by_covid(df, 'RBC'),
                showfliers=False,
                widths=0.4,
                labels=['COVID Neg', 'COVID Pos']
    )
    # set RBC subplot labels
    rbc_ax.set_title('RBC Count')
    rbc_ax.set_ylabel('RBC x 10^6 / uL')
    rbc_ax.set_ylim(ymin=0)

    # plot PLT count by COVID neg or COVID pos result
    plt_ax.boxplot(plot_by_covid(df, 'PLT'),
                showfliers=False,
                widths=0.4,
                labels=['COVID Neg', 'COVID Pos']
    )
    # set PLT subplot labels
    plt_ax.set_title('Platelet Count')
    plt_ax.set_ylabel('Platelet x 10^3 / uL')
    plt_ax.set_ylim(ymin=0)

    # display the plot, then close it once user is done
    plt.show()
    plt.close()

# this function plots the RBC indices for COVID v. non-COVID patients
def plot_rbc_indices(df):
    # create a figure with 9 subplots (3 rows and 3 columns)
    #fig, ((hgb_ax, hct_ax, emp1_ax), (mcv_ax, mchc_ax, mch_ax), (rdw_ax, mpv_ax, emp2_ax)) = plt.subplots(nrows=3, ncols=3, figsize=(14, 15))
    fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(14, 13))
    
    # add a figure title and adjust the spacing between the title and the plots
    fig.suptitle('RBC Indices by COVID Result', fontsize=16)
    fig.subplots_adjust(top=0.93)

    # adjust whitespace between subplots
    plt.subplots_adjust(wspace=0.4, hspace=0.3)

    # list of all RBC info to display and their units. Empty for positions in the subplots that should have no data
    ax_name_units = [('Hemoglobin', 'g / dL'), ('Hematocrit', "%"), ('empty', 'empty'), ('MCV', 'fL'), ('MCHC', 'g/ dL'), ('MCH', 'pg'), ('RDW', '%'), ('MPV', 'fL'), ('empty', 'empty')]

    # set counter for ax_name_units list
    i = 0
    
    # loop through each subplot in fig
    for ax_array in axs:
        for ax in ax_array:
            # if subplot should have data in it
            if (ax_name_units[i][0] != 'empty'):
                # populate data
                ax.boxplot(plot_by_covid(df, ax_name_units[i][0]),
                            showfliers=False,
                            widths=0.4,
                            labels=['COVID Neg', 'COVID Pos']
                )
                # set subplot labels
                ax.set_title(ax_name_units[i][0])
                ax.set_ylabel(ax_name_units[i][1])
                ax.set_ylim(bottom=0, top=(ax.get_ylim()[1] * 1.1))
            else:
                # otherwise turn off the axis
                ax.axis('off')
            
            # increment ax_name_units counter
            i += 1

    # display the plot, then close it once user is done
    plt.show()
    plt.close()

# this function plots the absolute count of WBC cell subsets for COVID v. non-COVID patients
def plot_wbc_abs_diff(df):
    # create a figure with 6 subplots (2 rows and 3 columns)
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(14, 9))

    # add a figure title and adjust the spacing between the title and the plots
    fig.suptitle('WBC Differential (Absolute Count) by COVID Result', fontsize=16)
    fig.subplots_adjust(top=0.9)

    # adjust whitespace between subplots
    plt.subplots_adjust(wspace=0.4)

    # list of all WBC info to display. Empty for positions in the subplots that should have no data
    ax_name = ['Neutrophils', 'Lymphocytes', 'Monocytes', 'Eosinophils', 'Basophils', 'empty']

    # set counter for ax_name list
    i = 0

    # loop through each subplot in fig
    for ax_array in axs:
        for ax in ax_array:
            # if subplot should have data in it
            if (ax_name[i] != 'empty'):
                # plot data
                ax.boxplot(plot_by_covid(df, ax_name[i]),
                            showfliers=False,
                            widths=0.4,
                            labels=['COVID Neg', 'COVID Pos']
                )
                # set subplot labels
                ax.set_title(ax_name[i])
                ax.set_ylabel('Cells / uL')
                ax.set_ylim(bottom=0, top=(ax.get_ylim()[1] * 1.1))
            else:
                # otherwise turn off the axis
                ax.axis('off')
            
            # increment ax_name counter
            i += 1
    
    # display the plot, then close it once user is done
    plt.show()
    plt.close()

# this function plots the relative (%) count of WBC cell subsets for COVID v. non-COVID patients
def plot_wbc_rel_diff(df):
    # create a figure with 6 subplots (2 rows and 3 columns)
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(14, 9))

    # add a figure title and adjust the spacing between the title and the plots
    fig.suptitle('WBC Differential (Relative Count) by COVID Result', fontsize=16)
    fig.subplots_adjust(top=0.9)

    # adjust whitespace between subplots
    plt.subplots_adjust(wspace=0.4)

    # list of all WBC info to display. Empty for positions in the subplots that should have no data
    ax_name = ['Neutrophils%', 'Lymphocytes%', 'Monocytes%', 'Eosinophils%', 'Basophils%', 'empty']

    # set counter for ax_name list
    i = 0

    # loop through each subplot in fig
    for ax_array in axs:
        for ax in ax_array:
            # if subplot should have data in it
            if (ax_name[i] != 'empty'):
                # plot data
                ax.boxplot(plot_by_covid(df, ax_name[i]),
                            showfliers=False,
                            widths=0.4,
                            labels=['COVID Neg', 'COVID Pos']
                )
                # set subplot labels
                ax.set_title(ax_name[i][:-1])
                ax.set_ylabel(f'% of WBCs')
                ax.set_ylim(bottom=0, top=(ax.get_ylim()[1] * 1.1))
            else:
                # otherwise turn off the axis
                ax.axis('off')
            
            # increment ax_name counter
            i += 1
    
    # display the plot, then close it once user is done
    plt.show()
    plt.close()

# this function calculates the median WBC count for COVID negative and positive
# populations, then performs a Mann-Whitney-Wilcoxan test to determine if there
# is a statistically significant difference in the median.
def wbc_covid_comp(df):
    
    # get series of WBC counts for COVID negative and positive populations
    non_covid_wbc = df.loc[df['COVID'] == 0, 'WBC']
    covid_wbc = df.loc[df['COVID'] == 1, 'WBC']
    
    # perform Mann-Whitney-Wilcoxan test to compare medians
    p_value = stats.mannwhitneyu(non_covid_wbc, covid_wbc, alternative='greater')[1]

    # display results and interpretation
    print(f"""\nThe COVID negative population median WBC count is {non_covid_wbc.median():.2f} x 10^3 cells/uL.
The COVID positive population median WBC count is {covid_wbc.median():.2f} x 10^3 cells/uL.
\nMann-Whitney-Wilcoxon test for populations with a negative COVID test
having a higher median WBC count than populations with a positive COVID 
test has a p-value of {p_value:.2e}.""")
    if p_value < 0.05:
        print("""\nThe hypothesis that populations with a negative COVID test have
a higher median WBC count is statistically significant.""")
    else:
        print("\nThe difference in medians between these populations is not statistically significant")

# this function calculates the median platelet count for COVID negative and positive
# populations, then performs a Mann-Whitney-Wilcoxan test to determine if there
# is a statistically significant difference in the median. It also performs a Chi-Square
# test to evaluate if a low platelet count occurs more frequently in the COVID positive
# population
def platelet_covid_comp(df):
    
    # get series of platelet counts for COVID negative and positive populations
    non_covid_plt = df.loc[df['COVID'] == 0, 'PLT']
    covid_plt = df.loc[df['COVID'] == 1, 'PLT']
    
    # perform Mann-Whitney-Wilcoxan test to compare medians
    p_value = stats.mannwhitneyu(non_covid_plt, covid_plt, alternative='greater')[1]
    
    # display results and interpretation for Mann-Whitney-Wilcoxan test
    print(f"""\nThe COVID negative population median platelet count is {non_covid_plt.median():.2f} x 10^3 platelets/uL.
The COVID positive population median platelet count is {covid_plt.median():.2f} x 10^3 platelets/uL.
\nThe Mann-Whitney-Wilcoxon test for populations with a negative COVID test
having a higher median platelet count than patients with a positive COVID
test has a p-value of {p_value:.2e}.""")
    if p_value < 0.05:
        print("""\nThe hypothesis that populations with a negative COVID test have
a higher median platelet count is statistically significant.""")
    else:
        print("\nThe difference in medians between these populations is not statistically significant")
    
    # create a contingency table of paltlete results below the reference range and COVID result
    platelet_contingency = pd.crosstab(df['PLTref'], df['COVID'])
    
    # calculate frequencies
    low_plt_covid_freq = platelet_contingency.iloc[0][1] / (platelet_contingency.iloc[0][1] + platelet_contingency.iloc[1][1])
    low_plt_non_covid_freq = platelet_contingency.iloc[0][0] / (platelet_contingency.iloc[0][0] + platelet_contingency.iloc[1][0])
    
    # perform Chi-Square test to evaluate if frequencies are different than expected by chance
    chi2_result = stats.chi2_contingency(platelet_contingency)

    # display results and interpretation of Chi-Square test
    print(f"""\nThe frequency of a low platelet count in the COVID negative population is {low_plt_non_covid_freq:.2f}.
The frequency of a low platelet count in the COVID positive population is {low_plt_covid_freq:.2f}.
\nThe Chi-Square test for independence between COVID test result and 
a platelet count below the reference range (<150 x 10^3 platelets/uL) a p-value 
of {chi2_result[1]:.2e}.""")
    if chi2_result[1] < 0.05:
        print("""\nThe hypothesis that a low platelet count occurs more frequently in 
populations with a postiive COVID test result than expected by chance is statistically
significant.""")
    else:
        print("\nA low platelet count is not related to COVID test results in this dataset.")

# This function provides a summary of the dataset
def summarize_dataset(df):
    print(f"\nNumber of entries: {df.shape[0]}")
    print(f"Percent by Sex: {(df['Sex'].value_counts()[0] / df.shape[0] * 100):.1f}% Female, {(df['Sex'].value_counts()[1] / df.shape[0] * 100):.1f}% Male" )
    print(f"Average age: {df['Age'].mean():.1f} years (min: {df['Age'].min():.1f}, max: {df['Age'].max():.1f})")
    print(f"Percent COVID Positive: {(df['COVID'].value_counts()[1] / df.shape[0] * 100):.1f}%")
    print("Data fields: \n\t", end="")
    for col in df.columns:
        print (col, end=", ")
    print()

    