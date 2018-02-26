import math
import time


def smallest_number_to_add_to_be_palindrome(greater_than_number_str: str):
    digits = len(greater_than_number_str)
    # print(greater_than_number_str)
    # print(digits)
    result = None
    if digits % 2 == 1:
        if ''.join(set(greater_than_number_str)) == "9":
            result = 2
        elif digits == 1:
            result = 1
        else:
            number_to_add = smallest_number_to_add_to_be_palindrome(greater_than_number_str[1:digits - 1])
            if number_to_add == 2:
                result = number_to_add + 9
            else:
                result = number_to_add * 10
    else:
        if ''.join(set(greater_than_number_str)) == "9":
            result = 2
        elif digits == 2:
            result = 11
        else:
            number_to_add = smallest_number_to_add_to_be_palindrome(greater_than_number_str[1:digits - 1])
            if number_to_add == 2:
                result = number_to_add + 9
            else:
                result = number_to_add * 10
    return int(result)


def generate_smallest_palindrome_greater_than(greater_than_number: int):
    result = greater_than_number + smallest_number_to_add_to_be_palindrome(str(greater_than_number))
    return result

print(generate_smallest_palindrome_greater_than(10001))

start_time = time.time()

palindrome_list = [0]
last_palindrome = 0
for i in range(1, int(math.pow(11, 4))):
    last_palindrome = generate_smallest_palindrome_greater_than(last_palindrome)
    palindrome_list.append(last_palindrome)

print(len(palindrome_list))
# print(palindrome_list)

for i, a in enumerate(palindrome_list):
    # print(i+1, a)
    pass

print("time elapsed: {:.2f}s".format(time.time() - start_time))

def find_nth_palindrome(n):
    number_of_digits = 1
    palindrome_digit_count_list = [9]
    while(n > sum(palindrome_digit_count_list)):
        number_of_digits += 1
        palindrome_digit_count_list.append(9 * math.pow(10,int((number_of_digits-1)/2)))
        # print(number_of_digits)
        # print(palindrome_digit_count_list)
    smallest_palindrome_at_n_digits = int(math.pow(10,number_of_digits-1)) + 1
    # print(smallest_palindrome_at_n_digits)
    index_within_current_digits = (n - sum(palindrome_digit_count_list[:-1]) - 1)
    # print(index_within_current_digits)
    if(number_of_digits == 1):
        result = n
    elif (number_of_digits%2 ==1):
        # print(index_within_current_digits * math.pow(10, (number_of_digits-1)/2))
        # print(smallest_palindrome_at_n_digits + int(index_within_current_digits/10)*11)
        # print(int(index_within_current_digits/10) * math.pow(10, (number_of_digits-1)/2))
        result = index_within_current_digits * math.pow(10, (number_of_digits-1)/2) + \
                 smallest_palindrome_at_n_digits + int(index_within_current_digits/10)*11* math.pow(10, max(0, (number_of_digits-3)/2)) - \
                 int(index_within_current_digits/10) * math.pow(10, (number_of_digits-1)/2)
                #* math.pow(10, (number_of_digits-3)/2)
                # math.pow(10, int(math.log10(max(1, (n - sum(palindrome_digit_count_list[:-1])-1)))))
                 # math.pow(10, int((n - sum(palindrome_digit_count_list[:-1])-1)%10))# * int(math.pow(10,(number_of_digits-3)/2))
    else:
        # print(index_within_current_digits * 11 * math.pow(10, (number_of_digits-2)/2))
        # print(smallest_palindrome_at_n_digits + int(index_within_current_digits/10)*11)
        # print(int(index_within_current_digits/10) * 11 * math.pow(10, (number_of_digits-2)/2))
        result = index_within_current_digits * 11 * math.pow(10, (number_of_digits-2)/2) + \
                 smallest_palindrome_at_n_digits + int(index_within_current_digits/10)*11* math.pow(10, max(0, (number_of_digits-4)/2)) - \
                 int(index_within_current_digits/10) * 11 * math.pow(10, (number_of_digits-2)/2)
                    #* math.pow(10, max(0, (number_of_digits-4)/2))
    return result


n = [101, 198, 199, 208, 209, 218, 219, 298, 299, 308, 309]
for i in n:
    print(i, ":", int(find_nth_palindrome(i)), palindrome_list[i])


