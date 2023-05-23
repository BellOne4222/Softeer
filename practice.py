ascending_set = set(range(1, 9))  # 1부터 8까지의 숫자 집합
print(ascending_set)
descending_set = {sorted(set(range(8, 0, -1)), reverse= True)}
print(descending_set)