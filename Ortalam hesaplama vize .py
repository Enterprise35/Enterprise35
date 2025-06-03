A = float(input("Import your first midterm: "))
B = float(input("Import your second midterm: "))
C = float(input("Import your final exam: "))

A = A*30/100
B = B*30/100
C = C*40/100

result = A+B+C
if result >= 50:
    print("Geçti")
else:
    print("Kaldı")
    
