# (1)
nums = list()
for n in range(3):
    data = int(input(f'{n + 1}個目の整数を入力して下さい >>')) 
    nums.append(data)
print(max(nums))
