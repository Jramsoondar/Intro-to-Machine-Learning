import statistics
bmi_list = []
bmi_dic = {}
for i in range(10):
    name = input("Name: ")
    weight =float(input("Weight: "))
    height = input("Height(Ex. 6'2): ")
def calculate_bmi(weight,height):
    BMI = 703
    feet, inches = height.split("'")
    feet_to_inches = int(feet) * 12
    total_inches = feet_to_inches + int(inches)
    return (weight * BMI)/(total_inches * total_inches)

Bmi = calculate_bmi(weight, height)

bmi_dic[name] = Bmi

bmi_list.append(Bmi)

print(f'The minmum BMI is {min(Bmi)}')
print(f'The maximum BMI is {max(Bmi)}')
print(f'The mean of The BMI is {statistics.mean(Bmi)}')
print(f'The standard deviation of the BMI is {statistics.stdev(Bmi)}')
print(f'The variance of the BMI is {statistics.variance(Bmi)}')