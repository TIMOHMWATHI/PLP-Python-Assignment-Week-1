weight=float(input("Enter your weight in kgs: "))
height=float(input("Enter your height in meters:"))

BMI= weight / height ** 2

if BMI < 18.5 :
    print("Under weight")
elif BMI < 25:
    print("Healthy Weight")
else:
    print ("Over weight")
 
