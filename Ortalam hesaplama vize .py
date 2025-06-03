A =input("İmport your firs midterm:")
B =input("İmport your second midterm:")
C =input("İmport your final exam:")
float(A)
float(B)
float(C)
A = float(input("Import your first midterm: "))
B = float(input("Import your second midterm: "))
C = float(input("Import your final exam: "))

A = A*60/100
B = B*60/100
C = C*40/100
␍␊
A = A*30/100
B = B*30/100
C = C*40/100␊

result = A+B+C
if result >= 50:
    print("Geçti")
else:
    print("Kaldı")
