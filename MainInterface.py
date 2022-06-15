
print("Welcome to the Boolean Calculator!")
boolean1 = input("Enter your Boolean: ")
boolean2 = input("Enter your Second Boolean: ")
convention = input("Enter your Convention: ")

if convention == "AND":
    if boolean1 == "True" and boolean2 == "True":
        print("True")
    else:
        print("False")

elif convention == "OR":
    if boolean1 == "True" or boolean2 == "True":
        print("True")
    else:
        print("False")

elif convention == "XOR":
    if boolean1 == "True" and boolean2 == "True":
        print("False")
    elif boolean1 == "True" and boolean2 == "False":
        print("True")
    elif boolean1 == "False" and boolean2 == "True":
        print("True")
    else:
        print("False")

elif convention == "NOT":
    if boolean1 == "True":
        print("False")
    else:
        print("True")

elif convention == "NAND":
    if boolean1 == "True" and boolean2 == "True":
        print("False")
    else:
        print("True")

elif convention == "NOR":
    if boolean1 == "True" or boolean2 == "True":
        print("False")
    else:
        print("True")

elif convention == "XNOR":
    if boolean1 == "True" and boolean2 == "True":
        print("True")
    elif boolean1 == "True" and boolean2 == "False":
        print("False")
    elif boolean1 == "False" and boolean2 == "True":
        print("False")
    else:
        print("True")

else:
    print("Invalid Convention")
