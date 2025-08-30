sum = 0
while(True):
        UserInput = input("Enter The Item Price and enter q to Quit: \n")
        if (UserInput!='q'):
              UserInput= float(UserInput)
              sum = sum + UserInput
              print(f"Your Total bill so far{sum}.\n")
        else:
              print("Thanks for using our calculator")
              print(F"Your Total Bill is {sum}. Thanks for Shoping With US! \n")
              break



    


