#Heart Rate Monitor
#Objective :To determine if a heart rate is within a healthy range.
#Ths project was done by: Sidra Alshaal>
import json

#Opening the Json file
with open("p1.json","r") as file:
    Heart_rate_monitor=json.load(file)

age=int(input("Enter your age: "))
heart_rate=int(input("Enter your resting heart rate(beats per minute): "))
post_exercise_hr=int(input("Enter your heart rate after exercise: "))
min_hr=int(input("Enter you heart rate after 1 minute: "))

patients={"Age: ": age,"Resting heart rate: ":heart_rate,"Heart rate after exercising: ":post_exercise_hr,"Heart rate after one minute from exercising:" :min_hr}
Heart_rate_monitor.append(patients)

print("------------------------------------------------------------------------")

#Resting Heart Rate Classification
maximum_healthy_heart_rate=220-age
print(f"Your Maximum heart rate is: {maximum_healthy_heart_rate} bpm")
if heart_rate<60:
    print("Your resting heart rate is in the athlete range!")
elif 60<heart_rate<100:
    print("Your resting heart rate is in the normal range!")
elif heart_rate>100:
    print("Your resting heart rate is in the high range")

#Heart Rate Recovery Check
HRRe = post_exercise_hr - min_hr  # Heart rate recovery
if HRRe < 12:
    print("Your heart rate recovery is poor!")
elif 12 <= HRRe <= 20:
    print("Your heart rate recovery is good!")
elif HRRe > 20:
    print("Your heart rate recovery is excellent!")

#Saving the new patients data in the JSON file
with open("p1.json","w") as file:
    json.dump(Heart_rate_monitor,file)