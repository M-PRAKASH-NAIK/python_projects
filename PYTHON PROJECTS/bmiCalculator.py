#calculator for BMI
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#Condition
bmi=weight/(height*height)
print(bmi)
if(bmi<18.5):
  print("underweight")
else:
  if(bmi>=18.5):
    if(bmi>=18.5 and bmi<25):
      print("normal weight")
    elif(bmi>=25 and bmi<30):
      print("over weight")
    elif(bmi>=30 and bmi<35):
      print("obese")
    else:
      print("clinically obese")
