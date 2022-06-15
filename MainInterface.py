
def takeInputFromUser(): # Function to take input from user
    boolean1 = input("Enter your Boolean: ")
    boolean2 = input("Enter your Second Boolean: ")
    convention = input("Enter your Convention: ")
    return boolean1, boolean2, convention




 def calculateBooleanResult(boolean1, boolean2, convention):
    if convention == "AND":
        if boolean1 == "True" and boolean2 == "True":
            return "True"
        else:
            return "False"

    elif convention == "OR":
        if boolean1 == "True" or boolean2 == "True":
            return "True"
        else:
            return "False"

    elif convention == "XOR":
        if boolean1 == "True" and boolean2 == "True":
            return "False"
        elif boolean1 == "True" and boolean2 == "False":
            return "True"
        elif boolean1 == "False" and boolean2 == "True":
            return "True"
        else:
            return "False"

    elif convention == "NOT":
        if boolean1 == "True":
            return "False"
        else:
            return "True"

    elif convention == "NAND":
        if boolean1 == "True" and boolean2 == "True":
            return "False"
        else:
            return "True"

    elif convention == "NOR":
        if boolean1 == "True" or boolean2 == "True":
            return "False"
        else:
            return "True"

    elif convention == "XNOR":
        if boolean1 == "True" and boolean2 == "True":
            return "True"
        elif boolean1 == "True" and boolean2 == "False":
            return "False"
        elif boolean1 == "False" and boolean2 == "True":
            return "False"
        else:
            return "True"

    else:
        print("Invalid Convention")
        return "Invalid"

def run():
    takeInputFromUser()
    calculateBooleanResult()