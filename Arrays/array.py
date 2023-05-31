# expemse = [['Jan',2200],['Feb',2350],['Mar',2600],['Apr',2130],['May',2190]]
# simple = [2200,2350,2600,2130,2190,2000]

# # 1 in Feb, how many dollarsyou spent extra compare to Jan?

# extra_exp = expemse[1][1] - expemse[0][1]
# print(f'The extra dollars spent in feb month is {extra_exp}')

# print()

# # 2 Find out your total expense in first quarter (first three months) of this year

# total_3_months = expemse[0][1] + expemse[1][1] + expemse[2][1]
# print(f'Total of first three months {total_3_months}')
# print()

# # 3 Find out if you spent exactly 2000$ in any months
# print(2000 in expemse)
        
        
# print()

# # 4 june month jus finished and your expense is 1980$ add this in your array


# expemse.insert(5,('Jun',1980))
# print(expemse)

# print()

# # 5 you returned an item that you bought in monts of april and got refund of 200$ 

# expemse[3][1] = expemse[3][1] - 200

# print(expemse)


# print()
# print('----------------------- Q2---------------------')

# heros = ['Spider-Man','Hulk','Thor','Iron Man','Captain America']

# # 1 length of list
# print(f'Length of list is: {len(heros)}')
# print()

# # 2 add balck panther in end of the list

# heros.append('Black Panther')
# print(heros)
# print()
# # 3 add black panther after a hulk
# heros.remove('Black Panther')
# heros.insert(1,'Black Panther')
# print(heros)
# print()

# # 4 remove hulk and thor and replace with dr strange
# heros[2:4] = 'Dr. Strange'
# print(heros)

# print()

# print('----------------Q 3----------------')

# num = int(input('enther '))

# list  = [i for i in range(1,num+1) if i%2 ==1]
# print(list)




# Advanced questions


# Given an unsorted integer array, find a pair with the given sum in it.

# list = [8,2,4,5,1,3,6]

# def pair_of_sum(list,target):
#     for i in range(len(list)-1):
#         for j in range(i+1,len(list)):
#             if list[i] + list[j] == target:
#                 return (list[i],list[j])
#     return 'Pairs are not found'


# print(pair_of_sum(list,14))



# Check if a subarray with 0 sum exists or not

# def sum_subarray(sets,m):
#     sets = set()
#     sum = 0
#     for i in range(m):
#         sum +=1
#         if sum == 0 | sets[sum] == True:
#             return True
#         sets[sum] = True
#     return False


# set = { 4, -6, 3, -1, 4, 2, 7}

# print(sum_subarray(set,6))




# def intersect(nums1, nums2):
#         cur1 = cur2 = 0
#         # sort nums1 and nums2
#         nums1.sort()
#         nums2.sort()
        
#         answer = []
        
#         # Repeat until one of the pointers gets to the end
#         while cur1!=len(nums1) and cur2!=len(nums2):
#             if nums1[cur1]==nums2[cur2]:
#                 answer.append(nums1[cur1])
#                 cur1+=1
#                 cur2+=1
#             else:
#                 if nums1[cur1]>nums2[cur2]:
#                     cur2+=1
#                 else:
#                     cur1+=1
#         return answer
    
    
# list1 = [1,2,2,1]
# list2 = [2,2]

# print(intersect(list1,list2))







def thirdMax( nums):

        nums.sort(reverse = True)
        count = 1
        previous = nums[0]

        for i in range(len(nums)):
            if nums[i] != previous:
                count = count + 1
                previous = nums[i]
            if count == 3:
                return nums[i]
        return nums[0]
    
    
nums = [10, 2, 4, 5, 6, 2, 9, 1, 7, 5, 4, 11, 30]
print(thirdMax(nums))