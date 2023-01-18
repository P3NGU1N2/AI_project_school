def welcome():
    greetings = """ Hey this is my school project consisting of 9 + Programs 
    I have done each program in different def functions so its easy for me to organise

    And just edit the code by calling the function you want as i dont have time to make it simple bei 
"""
    print(greetings)

def kilo_to_mile():
    kilometr = float(input('Enter the km to convert: '))

    conv_fac = 0.621371
    miles = kilometr * conv_fac
    print("The kilometer is equal to", miles, "miles")


def triangles():
    a = float(input("Enter the value of first side: "))
    b = float(input("Enter the value of second side: "))
    c = float(input("Enter the value of third side: "))

    s = (a + b + c) / 2

    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5


    print("The area of the triangle is", area)

def factorial_to_number():
    num = int(input("Enter the number you want to convet: "))
    factorial = 1
    if num < 0:
        print("Sorry factorial doesnt exist for -ve number")
    elif num == 0:
        print("THe factiorial of 0 is 1 ")

    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)

def display_mult_table():
    num = int(input("Enter the number: "))
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)

def cels_to_fer():
    celsius = float(input("Enter the value to convrt to farenheit: "))
    farenheit =  (celsius*1.8) + 32
    print(celsius, "degree celsius is equal to", farenheit, "degree farenheit")

def swapping_var():
    x = input("Enter a value: ")
    y = input("Enter another value: ")

    temp = x 
    x = y 
    y = temp

    print("The value of x after swapping is", format(x))

    print("The value of x after swapping is", format(y))

def numbr_div():
    my_list = [74, 85, 12, 75, 12, 221, 65, 39]
    result = list(filter(lambda x: (x % 13 == 0), my_list))
    print("Numbers divisble by 13 are", result)

def find_accr():
    tp = int(input('Enter the tp: '))
    tn = int(input('Enter the tn: '))
    fp = int(input('Enter the fp: '))
    fn = int(input('Enter the fn: '))

    accuracy = (tp+tn)/(tp+tn+fp+fn)

    print("The accuracy of the model is \n", accuracy)

def precision_model():
    fp = int(input('Enter the fp: '))
    tp = int(input('Enter the tp: '))
    precescion = tp/(tp+fp)
    print("The precessiong of model is", precescion)

def find_f1_sore():
    tp = int(input('Enter the tp: '))
    tn = int(input('Enter the tn: '))
    fp = int(input('Enter the fp: '))
    fn = int(input('Enter the fn: '))   

    precescion = tp/(tp+fp)
    recall = tp/(tp+fn)

    f1_score = 2+precescion*recall/(precescion+recall)
    print("THe f1 score is", f1_score)

welcome()
