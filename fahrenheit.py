for i in range(3):

    fahrenheit = int(input("Enter fahrenheit value: "))

    def celcius(fahrenheit):
        cel = round((fahrenheit-32)*.5556)
        return cel

    result = celcius(fahrenheit)
    print("The conversion answer is:", result)
