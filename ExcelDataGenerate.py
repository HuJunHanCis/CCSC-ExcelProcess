import random
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

    def __init__(self,data_settings,data_type):

        self.data_list = []
        self.append_list = []
        self.data_settings = data_settings
        self.data_type = data_type

        self.y_record = 0
        self.g_record = 0

    def show_data(self):

        # 自动生成 X 坐标
        x = list(range(len(self.data_list)))  # X 坐标为 [0, 1, 2, 3, 4]

        # 绘制散点图
        plt.scatter(x, self.data_list, c='blue', s=100, alpha=0.7, edgecolors='black')

        # 添加标题和坐标轴标签
        plt.title('Scatter Plot with Single List (Y-axis)')
        plt.xlabel('Index')
        plt.ylabel('Value')

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

        if random.randint(0,2) == 0:

            for i in range(len_of_y):

                if i < start_of_y:

                    self.data_list.append(self.data_list[i] + random.randint(-1, 1))

                elif i == start_of_y:

                    self.append_list = generate_increasing_list(self.data_list[i], banpi_h, range_of_y)
                    self.data_list += self.append_list

                    self.y_record = i

                elif i > start_of_y + len(self.append_list):

                    if random.randint(0, 1):
                        self.data_list.append(self.data_list[i - 1] + random.randint(-1, 1))
                    else:
                        self.data_list.append(self.data_list[i - 1])



    def generate_data_list(self):

        print(random.randint(1, 10))



Excel_Data = DataList(generate_settings,"yuredian")
Excel_Data.generate_y()
Excel_Data.show_data()

# DataList(generate_settings,"goucao")



