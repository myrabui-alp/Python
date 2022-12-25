# Check if the first and last number of a list is the same
def check_first_last_number(a):
    if a[0] == a[len(a)-1]:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(
    f'\nnumbers_x: {numbers_x} \nThe result is {check_first_last_number(numbers_x)}')
print(
    f'\nnumbers_y: {numbers_y} \nThe result is {check_first_last_number(numbers_y)}')
