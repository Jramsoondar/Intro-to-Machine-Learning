BMI = 703
Weight = float(input("Enter your Weight" ))
height = input("Enter your height (Ex. 6'2) ")
feet, inches = height.split("'")
feet_to_inches = int(feet) * 12
total_inches = feet_to_inches + int(inches)
calculate_Bmi = (Weight * BMI)/(total_inches * total_inches)
print(f"Your total BMI is {calculate_Bmi}")
