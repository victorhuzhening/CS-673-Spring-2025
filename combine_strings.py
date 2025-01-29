first_list = list(input("Please input the values of the first list (comma separated):").split(","))
second_list = list(input("Please input the values of the second list (comma separated):").split(","))

if len(first_list) == len(second_list):
    print([val for tupl in zip(first_list, second_list) for val in tupl])
else:
    print("Shape mismatch error. The input lists are not equal length.")