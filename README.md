# Overview

This is a demonstration project showing the use of several libraries in Python to analyze and visualize data, including Pandas, NumPy, Matplotlib, and SciPy.

The dataset for this project is from Hospital Israelita Albert Einstien in São Paulo, Brazil. The data include patient demographics, COVID-19 Real-Time PCR test results, and Complete Blood Count (CBC) test results for patients seen at the hospital between November 1st, 2019 and August 11th, 2020. The data was sourced from [Kaggle](https://www.kaggle.com/rodrigomalossi/covid19-einstein-25-full). The following citation is for the original dataset: 

FAPESP (2020). FAPESP COVID-19 Data Sharing/BR, Available from https://repositoriodatasharingfapesp.uspdigital.usp.br/

I developed this script as an exercise to gain experience performing data analysis with Python and to familiarize myself with data analysis and visualization libraries. In addition to importing the data to a pandas dataframe and describing the dataset, I produced several plots based on COVID-19 test result status and performed statistical tests for white blood cell and platelet counts by COVID-19 test result.

[Software Demo Video]()

# Data Analysis Results

I approached this dataset with two questions:

1. Do patients with a negative COVID-19 RT-PCR result have a higher average white blood cell (WBC) count compared to patients with a positive COVID-19 RT-PCR result?

    I used a Mann-Whitney-Wilcoxon test to test the hypothesis that the COVID-19 negative population had a higher median WBC count. The p-value for the test was 2.95 x 10<sup>-163</sup>, indicating the higher median for this population is statistically significant. The magnitude of the difference in medians is 1.6 x 10<sup>3</sup> cells/uL.

2. Are patients with a positive COVID-19 test more likely to have a have a low platelet count (less than 150 x 10<sup>3</sup> platelets/uL) compared to those with a negative COVID-19 test result?

    The frequency of a low platelet count in the COVID-19 positive population was 17.0%, compared to 5.0% for the COVID-19 negative population. I used a Chi-Square test to test the hypothesis that the patient population with a positive COVID-19 test were more likely to have a low platelet count. The p-value for this test was 1.13 x 10<sup>-89</sup>, indicating that the frequency of a low platelet count was higher in the COVID-19 positive population than expected by chance. 


# Development Environment

* Visual Studio Code (v1.63.2)
* Python 3.9.7 64-bit
    * Pandas v1.3.5
    * SciPy v1.7.3
    * NumPy v1.22.1
    * Matplotlib v3.5.1
* Git / GitHub

# Useful Websites

* [Python Documentation, v.3.9](https://docs.python.org/3.9/)
* [Pandas Documentation, v1.3.5](https://pandas.pydata.org/docs/index.html)
* [SciPy Documentation, v1.7.3](https://docs.scipy.org/doc/scipy/index.html#)
* [NumPy Documentation, v1.22](https://numpy.org/doc/stable/)
* [Matplotlib Documentation, v3.5.1](https://matplotlib.org/stable/index.html)
* [Seaborn Documentation, v0.11.2](https://seaborn.pydata.org/)

# Future Work

* Use Seaborn library to place p-values on box plots
* Apply additional statistical tests for distribution normality
* Create a WebApp for displaying data without using the Terminal
* Search for additional datasets including Prothrombin Time and Activated Partial Thromboplastin Time