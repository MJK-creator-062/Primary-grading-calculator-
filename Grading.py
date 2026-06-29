print("--- Primary Grade Calculator ---")

try:
    name = input("Enter Student Name: ")
    
    # Get scores
    math = float(input("Math score: "))
    eng = float(input("English score: "))
    sci = float(input("Science score: "))
    sst = float(input("SST score: "))
    
    # Calculate average
    average = (math + eng + sci + sst) / 4
    print(f"\nStudent: {name}")
    print(f"Average Mark: {average:.1f}")
    
    # Grade assignment
    if average >= 80:
        print("Grade: (A)")
    elif average >= 70:
        print("Grade: (B)")
    elif average >= 60:
        print("Grade: (C)")
    elif average >= 50:
        print("Grade: (D)")
    else:
        print("Grade: (E)")

except ValueError:
    print("Error: Please enter valid numbers for the scores.")
  
