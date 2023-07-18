user_input = input("Enter three integers separated by commas: ")
integer_list = [int(x.strip()) for x in user_input.split(",")]
if integer_list[0] != integer_list[1] != integer_list[2]:
    max_value = max(integer_list)
    min_value = min(integer_list)
    print(f"min value is {min_value}")
    print(f"max value is {max_value}")
else:
    print("three number should be distinct")