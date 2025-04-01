#github 
try:
    num = int(input("Enter the number: "))  
    if num > 0:
        reversed_num = int(str(abs(num))[::-1])  
    else:
        reversed_num = -(int(str(abs(num))[::-1]))  
    
    print(f"The reverse of {num} is {reversed_num}.")  

except ValueError:
    print("Please enter a valid integer.") 

INPUT:-
Enter the number: 1234

OUTPUT:-
The reverse of 1234 is 4321.
