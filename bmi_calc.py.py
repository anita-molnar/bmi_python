# BMI Calculator
while True:
    try:
        weight = float(input("Insert your weight in kg: "))
        height = float(input("Insert your height in meter: "))
        break
    except ValueError as e:
        print("\nWrong input:", e)
bmi = weight / height ** 2
if bmi <= 18.4:
    print("Underweight")
elif 24.9 >= bmi >= 18.5:
    print("in range")
elif 39.9 >= bmi >= 25:
    print("Overweight")
elif bmi > 40:
    print("Obese")


# lbs kgs - calculator
while True:
    try:
        print("\npress '1' for lbs to kgs")
        print("press '2' for kgs to lbs")
        user_input = input("-> ")
        if user_input != "1" and user_input != "2":
            print("\nAError: the required input is just 1 or 2")
            continue
        break
    except ValueError: 
        print("\nError: the required input is just 1 or 2")

if user_input == "1":
    lbs = float(input("\ninsert lbs: "))
    kgs = lbs * 0.45
    print(f"{lbs} lbs are {kgs} kgs")
elif user_input == "2":
    kgs = float(input("\ninsert kgs: "))
    lbs = kgs * 2.2
    print(f"{kgs} kgs are {lbs} lbs")