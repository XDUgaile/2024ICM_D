import numpy as np

# 设置随机数生成的范围和数量
lower_bound = 0
upper_bound = 0.1
num_values = 500

# 生成第一组完全随机的数据
group1 = np.round(np.random.uniform(lower_bound, upper_bound, num_values), 3)

# 在第一组数据的基础上生成第二组数据，略为“改善”
group2 = np.round(group1 + np.random.uniform(0, 0.01, num_values), 3)
group2 = np.clip(group2, lower_bound, upper_bound)

# 在第二组数据的基础上生成第三组数据，进一步“改善”
group3 = np.round(group2 + np.random.uniform(0, 0.01, num_values), 3)
group3 = np.clip(group3, lower_bound, upper_bound)

# 将numpy数组转换为逗号分隔的字符串
group1_str = ', '.join(map(str, group1))
group2_str = ', '.join(map(str, group2))
group3_str = ', '.join(map(str, group3))

# 打印结果
print("'Objective 1': [", group1_str)
print("\n'Objective 2': [", group2_str)
print("\n'Objective 3': [", group3_str)