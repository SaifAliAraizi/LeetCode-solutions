# Creating an empty list
# my_list = []
# target = 7

# # Using a while loop to get user input and append values to the list
# while True:
#     user_input = input("Enter a value (type 'done' to finish): ")

#     # Check if the user wants to finish entering values
#     if user_input.lower() == 'done':
#         break  # Exit the loop if the user enters 'done'
    
#     # Append the user input to the list
#     my_list.append(int(user_input))  # Convert user input to integer

# # Displaying the final list
# print("Final List:", my_list)

# # Checking for pairs that sum up to the target
# result_list = []
# for i in range(len(my_list)):
#     for j in range(i+1, len(my_list)):  # Avoid comparing an element with itself
#         if my_list[i] + my_list[j] == target:
#             result_list.append([i, j])

            

# # Displaying the pairs in list format
# print("Pairs that sum up to the target:", result_list)



# def twoSum():

#     lst = []
#     target = 9
#     while True:
#         x = input("Enter any number in the list : ")

#         if (x.lower() == 'done'):
#             break

#         lst.append(int(x))

#     f_lst = []

#     for item in range(len(lst)):
#         for item2 in range(item+1, len(lst)):
#             if lst[item] + lst[item2] == target:
#                 f_lst.append(item)
#                 f_lst.append(item2)

#     print(f_lst)

# twoSum()

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []

        for item in range(len(nums)):
            for item2 in range(item+1, len(nums)):
                if nums[item] + nums[item2] == target:
                    result.append(item)
                    result.append(item2)
                    return result

solution = Solution()
nums = [3,4,7,8,1]
target = 9
print(solution.twoSum(nums, target))