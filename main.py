vazn = [60, 70, 80, 90]
bo_y = [160, 170, 180, 190]

for i in range(len(vazn)):
    bmi = vazn[i] / ((bo_y[i] / 100) ** 2)
    if bmi < 18.5:
        print(f"Vazn: {vazn[i]} kg, Bo'y: {bo_y[i]} sm, BMI: {bmi:.2f}, Tasnif: Kam")
    elif 18.5 <= bmi <= 24.9:
        print(f"Vazn: {vazn[i]} kg, Bo'y: {bo_y[i]} sm, BMI: {bmi:.2f}, Tasnif: Normal")
    else:
        print(f"Vazn: {vazn[i]} kg, Bo'y: {bo_y[i]} sm, BMI: {bmi:.2f}, Tasnif: Ortiqcha")
