def convert_str(nums_list):
    
    output_str = ""
    for i in nums_list:
        output_str += str(i) + " "
    return output_str
    
nums_list = list(map(int, input().split(",")))

random_num = int(input())

first_group = nums_list[random_num:]
second_group = nums_list[: -random_num]

print(convert_str(first_group))
print(convert_str(second_group))
