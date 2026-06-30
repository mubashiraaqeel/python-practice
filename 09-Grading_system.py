marks = float(input("Enter number:"))

if(marks >= 90 and marks <= 100):
    print("The Grade acc. to",marks,"is A")
elif(marks >= 80 and marks <= 90):
    print("The Grade acc. to",marks,"is B")
elif(marks >= 70 and marks <= 80):
    print("The Grade acc. to",marks,"is C")
elif(marks >= 60 and marks <= 70):
    print("The Grade acc. to",marks,"is D")
else:
    print("The Grade acc. to", marks, "is F")