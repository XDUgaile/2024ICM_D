import random

# 设置随机数生成的范围
lower_bound = -0.05
upper_bound = 0.05

# 设置每组数据的数量
num_values = 100

# 生成三组数据
group1 = [round(random.uniform(lower_bound, upper_bound), 2) for _ in range(num_values)]
group2 = [round(random.uniform(lower_bound, upper_bound), 2) for _ in range(num_values)]
group3 = [round(random.uniform(lower_bound, upper_bound), 2) for _ in range(num_values)]

# 将数据转换为字符串格式并用逗号分隔
group1_str = ', '.join(map(str, group1))
group2_str = ', '.join(map(str, group2))
group3_str = ', '.join(map(str, group3))

# 打印结果
print("'Objective 1': [", group1_str)
print("\n'Objective 2': [", group2_str)
print("\n'Objective 3': [", group3_str)