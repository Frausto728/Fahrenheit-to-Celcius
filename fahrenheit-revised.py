for i in range(3):
        choice = input("Would you like to convert Fahrenheit to Celsius or Celsius to Fahrenheit? ").lower()
    
        def celsius(fahrenheit):
                cel = round((fahrenheit-32)*.5556)
                return cel
        
        def fahrenheit(celsius):
                fah = round((celsius*.5556)+32)
                return fah

        if choice == "fahrenheit to celsius" or choice == "fahrenheit" :
                fahrenheit = int(input("Enter fahrenheit value: "))
                print(f"{fahrenheit} degrees fahrenheit converted to celsius is {celsius(fahrenheit)} degrees")

        elif choice == "celsius" or choice == "celsius to fahrenheit":
                celsius = int(input("Enter a celsius value: "))
                print(f"{celsius} degrees celsius converted to fahrenheit is {fahrenheit(celsius)} degrees")
            
        else:
                print("Please enter a valid option")

print("This is the end of the program")

