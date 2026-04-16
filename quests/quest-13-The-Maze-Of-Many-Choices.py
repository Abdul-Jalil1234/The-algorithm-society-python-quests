#!/usr/bin/python3
score = float(input("Enter a score (0-100): "))
if 90 <= score <= 100:
     print("A")
elif 80 <= score < 90:
     print("B")
elif 70 <= score < 80:
     print("C")
elif 0 <= score < 70:
     print("Needs Improvement")
else:
     print("Error: Please enter a score between 0 and 100.")

