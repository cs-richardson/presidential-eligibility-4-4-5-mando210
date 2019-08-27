"""
This program asks the user their age, whether they are U.S. citizen or not,
and their years of residency to check the user's eligibility to become
the president of the U.S.
"""
#Miki Ando

age = int(input("Age: "))
born = str(input("Born in the U.S.? (Yes/No): "))
years = int(input("Years of Residency: "))

if age >= 35 and born == "Yes" and years>= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")
