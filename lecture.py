# print(5/0) <-- ZeroDivisionError
# guess = int(input("Number: "))  <-- ValueError
try:
    # print(5/0)
    guess = input("Number: ")
    num = guess + '1' 
# except:
#     print("Nope!")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("That's a string (expecting a number)")
except TypeError:
    print("Concatenation error")
except Exception as e:
    print(f"Unexpected... {e}")