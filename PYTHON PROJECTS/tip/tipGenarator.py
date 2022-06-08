print("......Well come to tip calculator......")
bill = float(input("Enter your bill : "))
tip=int(input("what percentage tip would like to give :- 10 , 12 or 15 : "))
per = (bill*tip)/100
total_bill=bill+per
share=int(input("How many people to split this bill : "))
per_people=total_bill/share
print(f"Each person should pay :{per_people}")
