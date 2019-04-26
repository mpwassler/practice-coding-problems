import bisect
# 1.1 Get product of all other elements

# Original
# def multiply_array_items(arr):
#   new_arr = []
#   for index, num in enumerate(arr):
#     product = None
#     for inner_index, inner_num in enumerate(arr):
#       if inner_index != index:
#         if not product:
#           product = inner_num
#         else:
#           product = inner_num * product
#     new_arr.append(product)
#   return new_arr

# O(n) solution
def multiply_array_items(nums):

  prefix_products = []
  for num in nums:
    if prefix_products:
      prefix_products.append(prefix_products[-1] * num)
    else:
      prefix_products.append(num)

  suffix_products = []

  for num in reversed(nums):
    if suffix_products:
      suffix_products.append(suffix_products[-1] * num)
    else:
      suffix_products.append(num)

  suffix_products = list(reversed(suffix_products))

  result = []
  for i in range(len(nums)):
    if i == 0:
      result.append(suffix_products[i + 1])
    elif i == len(nums) - 1:
      result.append(prefix_products[i - 1])
    else:
      result.append(
        prefix_products[i - 1] * suffix_products[i + 1]
      )

  return result

# 1.2 Locate smallest window to be sorted
# Original
# def window(nums):
#   unsorted_nums = nums
#   sorted_nums = sorted(nums)
#   sort_start = None
#   sort_end = None

#   for i in range(len(nums)):
#     if unsorted_nums[i] != sorted_nums[i]:
#       if sort_start == None:
#         sort_start = i

#   for i in reversed(range(len(nums))):
#     if unsorted_nums[i] != sorted_nums[i]:
#       if sort_end == None:
#         sort_end = i

#   return (sort_start,sort_end)

  # O(n)
def window(nums):
  left, right = None, None
  n = len(nums)
  max_seen, min_seen = -float("inf"), float("inf")
  for i in range(n):
    max_seen = max(max_seen, nums[i])
    if nums[i] < max_seen:
      right = i
  for i in range(n - 1, -1, -1):
    min_seen = min(min_seen, nums[i])
    if nums[i] > min_seen:
      left = i
  return left, right

# 1.3 Calculate maximum subarray sum
# first
# def sub_array_sum(nums):
#   totals = []
#   reverse_totals = []
#   n = len(nums)
#   last_highest = 0
#   for i in range(n):
#     number = nums[i]
#     if totals and i < n:
#       number_to_add = number + totals[i - 1]
#       totals.append(number + totals[i - 1] )
#     else:
#       number_to_add = number
#       totals.append(number)
#     if number_to_add > last_highest:
#       last_highest = number_to_add
#   for i in range(n - 1, -1, -1):
#     number = nums[i]
#     length = len(reverse_totals)
#     if length and i > 0:
#       number_to_add = number + reverse_totals[length - 1]
#       reverse_totals.append(number + reverse_totals[length - 1] )
#     else:
#       number_to_add = number
#       reverse_totals.append(number)
#     if number_to_add > last_highest:
#       last_highest = number_to_add
#   if last_highest > 0:
#     return last_highest
#   else:
#     return 0

# Better
def sub_array_sum(nums):
  max_ending_here = max_so_far = 0
  for x in nums:
    max_ending_here = max(x, max_ending_here + x)
    max_so_far = max(max_so_far, max_ending_here)
  return max_so_far


# def smaller_counts(nums):
#   smaller_nums = []
#   checked_nums = []
#   previus_number = 0
#   n = len(nums)
#   for i in range(n - 1, -1, -1):
#     number = nums[i]
#     if not smaller_nums:
#       smaller_nums.append(0)
#     else:
#       prev = len(smaller_nums) - 1
#       if previus_number < number:
#         smaller_nums.append(smaller_nums[prev] + 1)
#       else:

#         smaller_ammount = 0
#         for i in reversed(checked_nums):
#           if i < number:
#             smaller_ammount += 1
#         smaller_nums.append(smaller_ammount)
#       previus_number = number
#     checked_nums.append(number)
#   smaller_nums.reverse()
#   return smaller_nums

# prettier
def smaller_counts(nums):
  result = []
  seen = []

  for num in reversed(nums):
    i = bisect.bisect_left(seen, num)
    result.append(i)
    bisect.insort(seen, num)
  return list(reversed(result))


