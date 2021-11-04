def band_name():
    
  print("The best names come from your favorite things! \n")
  
  animal = input("What's your favorite animal? \n")
  color = input("What's your favorite color? \n")
  number = eval(input("What's your favorite number? \n"))
  new_name = str(number) + " " + color + " " + animal
  
  print(f"Your Band Name is {new_name}!")
  
band_name()
