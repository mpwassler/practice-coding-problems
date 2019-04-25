
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
