#Write a Python function called max_num()to find the maximum of three numbers.
from operator import truediv


def max_num(num1, num2, num3):
    if(num1 >= num2 and num1 >= num3):
        return num1
    elif (num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3

print(max_num(5,10,15))
print(max_num(5,3,4))
print(max_num(5,6,1))

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
    product = 1
    for num in list:
        product = product * num
    return product

nums_list = [5,4,3]
print(mult_list(nums_list))

#Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    revstring = ""
    for i in string:
        revstring = i +revstring
    return revstring

string = "Apples and Bananas"
print(string + " backwards is " + rev_string(string))

#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(target, begin, end):
    for i in range(begin, end):
        if i == target:
            return True
    return False

print(num_within(20,1,10))
print(num_within(5,1,10))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    #define the first row of the triangle
    pascal_first_row = [0,1,0]
    #an innner function which can create the next line by using the previous
    def next_row(previous_row):
        next_row = [0]
        for i in range(1, len(previous_row)-1):
            next_row.append(previous_row[i] + previous_row[i-1])
            next_row.append(previous_row[i] + previous_row[i+1])
        next_row.append(0)
        return next_row
    #iterate n times, printing the new row each time
    row_to_print = pascal_first_row
    while n > 0:
        #print the row in the proper format (string, separated by spaces, no 0s)
        str_output = ""
        for num in row_to_print:
            if num != 0:
                str_output = str_output + str(num) + " "
        print(str_output)   
        row_to_print = next_row(row_to_print)
        n = n - 1


#call the function to test
pascal(5)
           







