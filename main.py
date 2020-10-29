def miles_to_kilometers(miles_to_convert):
    return miles_to_convert * 0.621371


try:
    miles = float(input("Hello! Please enter the number of miles driven: "))
    # print(miles_to_kilometers(miles))
except ValueError:
    print("Error, you did not enter a valid number. Please try again.")

else:
    print(miles_to_kilometers(miles))
    print(miles, 'miles equals', miles_to_kilometers(miles), 'kilometers.')
