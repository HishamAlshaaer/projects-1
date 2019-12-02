def add_numbers(number1,number2):
      # Adding two numbers 
      # User might also enter float numbers 
      sum = float(number1) + float(number2) 
      
      # Display the sum 
      # will print value in float 
      print("The sum of {0} and {1} is {2}" .format(number1, number2, sum)) 

def multiply_numbers(number1,number2):
      multiply = float(number1) + float(number2) 
      
      # Display the sum 
      # will print value in float 
      print("The sum of {0} and {1} is {2}" .format(number1, number2, multiply))
            


def main():
      number1 = input("First number: ") 
      number2 = input("\nSecond number: ") 
      
      add_numbers(number1,number2)
      multiply_numbers(number1,number2)
