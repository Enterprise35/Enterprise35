A =input("İmport your firs midterm:")
B =input("İmport your second midterm:")
C =input("İmport your final exam:")
float(A)
float(B)
float(C)

A = A*60/100
B = B*60/100
C = C*40/100

result = A+B+C
if result >= 50:
    print("Geçti")
else:
    print("Kaldı")
    
