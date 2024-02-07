
user_input = input("Enter a list of numbers separated by spaces: ")
input_list = [int(num) for num in user_input.split()]

print("Original List:", input_list)

#sorted the list
input_list.sort(reverse=False)

#removing duplicated using set(default function)
unduplicated= set(input_list)
print("Set without Duplicates:", unduplicated)


result_tuple = tuple(unduplicated)
print("Final Tuple:", result_tuple)
