import random
import numpy as np
from Settings import generate_settings
import matplotlib.pyplot as plt

def generate_increasing_list(start_height, end_height, n):

    # 总跨度
    total_diff = end_height - start_height

    # 生成 (n-1) 个随机数，使用 uniform(0.15, 1.0) 确保每个增量 > 0
    increments = [random.uniform(0.15, 1.0) for _ in range(n - 1)]

    # 将这些增量缩放，使它们的和等于 total_diff
    sum_increments = sum(increments)
    normalized_increments = [inc * total_diff / sum_increments for inc in increments]

    # 逐步累加，生成单调递增序列
    result = [start_height]
    current_value = start_height
    for inc in normalized_increments:
        current_value += round(inc)
        # 这里无需再次检查“是否等于上一个值”，因为 inc > 0，必定严格递增
        result.append(current_value)

    return result

class DataList:

    def __init__(self,data_settings,data_type = "yuredian"):

        self.data_list = []
        self.append_list = []
        self.data_settings = data_settings
        self.data_type = data_type

        self.y_record = 0
        self.y_type = -1
        self.g_record = 0

    def show_data(self):

        # 自动生成 X 坐标
        x = list(range(len(self.data_list)))  # X 坐标为 [0, 1, 2, 3, 4]

        # 绘制普通的散点图
        plt.scatter(x, self.data_list, c='blue', s=100, alpha=0.7, edgecolors='black', label='Laser Points')

        # 特别标记的点
        plt.scatter(x[self.y_record], self.data_list[self.y_record], c='red', s=150, label=f'Preheat : {self.y_record}')

        # 添加标题和坐标轴标签
        plt.title(f"Preheat Point Value : {self.data_list[self.y_record]}")
        plt.xlabel('Index')
        plt.ylabel('Laser Value Sim')

        # 添加图例
        plt.legend()

        # 显示图表
        plt.show()

    def generate_y(self):

        # 一共几个点
        len_of_y = random.randint(self.data_settings["y_len"][0],self.data_settings["y_len"][1])

        # 预热点在列表中的起始位置
        start_of_y = random.randint(self.data_settings["y_start"][0],self.data_settings["y_start"][1])

        # 升高部分的持续范围
        range_of_y = random.randint(self.data_settings["y_range"][0],self.data_settings["y_range"][1])

        # 起始地面高度
        ground_h = random.randint(0,self.data_settings["base_g_floating"]) + self.data_settings["base_g"]

        # 起始板坯高度
        banpi_h = random.randint(0,self.data_settings["base_h_floating"]) + self.data_settings["base_h"]

        self.data_list.append(ground_h)

        # 若已经指定类型则pass
        if self.y_type != -1:
            pass
        else:
            self.y_type = random.randint(0,2)

        # 直角型
        if self.y_type == 0:

            for i in range(len_of_y):

                if i < start_of_y:

                    self.data_list.append(self.data_list[i] + random.randint(-1, 1))

                elif i == start_of_y:

                    self.append_list = generate_increasing_list(self.data_list[i], banpi_h, range_of_y)
                    self.data_list += self.append_list

                    self.y_record = i + range_of_y

                elif i > start_of_y + len(self.append_list):

                    if random.randint(0, 1):
                        self.data_list.append(self.data_list[i - 1] + random.randint(-1, 1))
                    else:
                        self.data_list.append(self.data_list[i - 1])

        # 圆弧形
        elif self.y_type == 1:

            pass

        elif self.y_type == 2:

            pass

    def generate_data_list(self):

        print(random.randint(1, 10))


#
# Excel_Data = DataList(generate_settings)
# Excel_Data.y_type = 0
# Excel_Data.generate_y()
# Excel_Data.show_data()
# print(Excel_Data.data_list)
#

import numpy as np

def generate_arc_list(start, end, length):
    """
    生成一个符合圆弧形且单调的列表
    :param start: 起始值
    :param end: 结束值
    :param length: 列表的长度
    :return: 圆弧形且单调的列表
    """
    # 生成角度，均匀分布在 0 到 π/2 之间
    # theta = np.random.uniform(0, np.pi / 2, length)

    # 随机生成角度（随机分布）
    theta = np.sort(np.random.uniform(0, np.pi / 2, length))  # 从 0 到 π/2 的随机角度
    # theta += np.random.uniform(-1, 1, length)  # 添加角度随机扰动
    theta = np.clip(theta, 0, np.pi / 2)  # 确保角度范围有效

    # 使用正弦函数生成圆弧形曲线
    arc_values = np.sin(theta)

    # 将生成的值映射到 [start, end]
    mapped_values = start + (end - start) * arc_values

    return mapped_values.tolist()

# 示例参数
start_value = 1000
end_value = 700
list_length = 20

# 生成圆弧形单调列表
result = generate_arc_list(start_value, end_value, list_length)

plt.plot(result, marker='o', label='Arc Curve')
plt.title('Arc-Shaped List')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()

# 打印结果
print(result)
