import sys

msg = ["Enter an equation", 
      "Do you even know what numbers are? Stay focused!",
      "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
      "Yeah... division by zero. Smart move...",
      "Do you want to store the result? (y / n):",
      "Do you want to continue calculations? (y / n):",
      " ... lazy",
      " ... very lazy",
      " ... very, very lazy",
      "You are",
      "Are you sure? It is only one digit! (y / n)",
      "Don't be silly! It's just one number! Add to the memory? (y / n)",
      "Last chance! Do you really want to embarrass yourself? (y / n)"]

valid_operators = ["+", "-", "*", "/"]

memory = 0.0

store = None

another_calc = None

def is_one_digit(v):
    """ 
    A function that will return True is a input is a single-digit integer, otherwise returns False 
    Unfortunately, due to the way question is asked, the "user" in the question in the last stage enters numbers
    as a "number" and "number.0" and expects the program to treat both as integers. If this shown ahead of time, this
    string logic in the function could have been avoided. 
    """
    v = str(v)
    if v[1:] != ".0" and len(v) != 1:
            return False
    if float(v) > -10 and float(v) < 10:  
            return True
    else:
        return False

        
def check(v1, v2, operator):
    global msg
    """
    This function takes in three parameters. v1 and v2 are meant to be integers, while v3 is the user requested
    operation to be conducted on both ints. Depending on what the inputs are, a message will certain message
    will be printed.
    """
    message = ""
    if is_one_digit(v1) and is_one_digit(v2):
        message = message + msg[6]
    if (float(v1) == 1.0 or float(v2) == 1.0) and operator == "*":
        message = message + msg[7]
    if (float(v1) == 0 or float(v2) == 0) and (operator == "*" or operator == "+" or operator == "-"):
        message = message + msg[8]
    if message != "":
        message = msg[9] + message 
        print(message)


while True:
    print(msg[0])
    user_calc = input().split()
    if user_calc[0] == "M":
        user_calc[0] = memory
    if user_calc[2] == "M":
        user_calc[2] = memory
    try:
        float(user_calc[0])
        float(user_calc[2])
    except ValueError:
        print(msg[1])
        continue
    if user_calc[1] not in valid_operators:
        print(msg[2])
        continue
    check(user_calc[0], user_calc[2], user_calc[1])
    if user_calc[1] == "+":
        result = float(user_calc[0]) + float(user_calc[2])
        print(result)
    elif user_calc[1] == "-":
        result =float(user_calc[0]) - float(user_calc[2])
        print(result)
    elif user_calc[1] == "*":
        result = float(user_calc[0]) * float(user_calc[2])
        print(result)
    elif user_calc[1] == "/":
        if float(user_calc[2]) == 0:
            print(msg[3])
            continue
        result = float(user_calc[0]) / float(user_calc[2])
        print(result)
    print(msg[4])
    store_calc = input().lower()
    while store_calc == "n":
        print(msg[5])
        another_calc = input().lower()
        if another_calc == "n":
            sys.exit()
        break
    while store_calc == "y":
        if is_one_digit(result):
            msg_index = 10
            print(msg[msg_index])
            is_user_sure = input().lower()
            while is_user_sure == "y" and is_user_sure != "n":
                if msg_index < 12:
                    msg_index = msg_index + 1
                    print(msg[msg_index])
                    is_user_sure = input().lower()
                    continue
                if is_user_sure == "n":
                    break
                elif is_user_sure == "y":
                    memory = result
                    break
        else:
            memory = result
        print(msg[5])
        another_calc = input().lower()
        if another_calc == "y":
            break
        elif another_calc == "n":
            sys.exit()
        else:
            continue
    
    
    
