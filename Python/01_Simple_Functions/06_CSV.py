import csv
import numpy as np
with open('06_grades.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        int_grades = [int(x) for x in row[1:]]
        mean = np.mean(int_grades)
        name = row[0]
        print(name,":", mean)



"""
This code reads student grade data from a CSV file,
converts the grade entries to integers,
computes the mean grade for each student using NumPy,
and prints the student's name alongside their average grade.
"""