"""
Upper and Lower
"""
# Provide your solution here
def count_upper_lower(my_string:str) -> int:
    upper = 0
    if my_string.isupper() == True:
        for upper in my_string:
            upper =+ 1

    lower = 0
    if my_string.isupper() == True:
        for lower in my_string:
            lower =+ 1

    print(f"No. of Upper case characters: {upper}")
    print(f"No. of Lower case characters: {lower}")

"""
Check 33
"""
# Provide your solution here
def has_33(my_list: [int]) -> bool:
    for occurrence in my_list:
        print("3" in my_list)
        second_occurrence = occurrence + [1]

        if occurrence == second_occurrence:
            return True
        else:
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")
count_upper_lower("Martina feels NerVous.")
count_upper_lower("Leon said: Use 'Print' in Python.")
count_upper_lower("Tomorrow is a new day.")

has_33([1,3,3])
has_33([1,3,1,3])
has_33([3,1,3])
