import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


lowerWindowWidth = 1
upperWindowWidth = 1
heightThreshold = 10
std_threshold = 1.5

# data = pd.read_excel('Laser_20250114100605.xlsx', header=0)
data = pd.read_excel('Laser_20250116110305.xlsx', header=0)


count = data.shape[0]
x = np.linspace(0, count, count)

distance_col = data["Distance"]

noise = np.random.normal(0, 1, count)  # 均值为 0，标准差为 1 的正态分布噪声

# 将噪声添加到 Distance 列
# distance_col = distance_col + noise

xyz_mat = data[["X","Y","Z"]].to_numpy()


def fallDetection(start):
    j = -1
    k = -1
    for i in range (start,count):
        # if i > 180:
            # x = i

        # j = (idx for idx, s in enumerate(distance_col[i+1:], start=i+1) 
        #   if distance(s,distance_col[i]) >= lowerWindowWidth)
        end = min(i + 701, count)
        for idx in range(i+1,end):
            if distance(xyz_mat[i,:],xyz_mat[idx,:]) >= lowerWindowWidth:
                j = idx
                break
        if j == -1:
            continue

        di = np.median([x for x in distance_col[i:j]])
        # k = np.argmax(distance_col)
        # if i>=k:
        #     continue;
        # mode_result = stats.mode(distance_col[i:k])
        # mode_value = mode_result.mode
        # smallest_index = distance_col[i:k].to_list().index(mode_value) + i
        # di = distance_col[smallest_index]

        for idx2 in range(j, end):
            if distance(xyz_mat[idx2,:],xyz_mat[j,:]) >= upperWindowWidth:
                k = idx2
                break
        if k == -1:
            continue
        flag1 = True
        for j3 in range(0, idx2 + 1 - j):  # 循环条件：j3 + j < index3 + 1
            dj3 = distance_col[j+j3]
            flag1 = flag1 and (dj3 - di >= heightThreshold)
            if not flag1:
                break

        if flag1:
            index = j
            break
    # print(dj3)
    # print(di)
    return index

def riseDetection(start):
    j = -1
    k = -1

    for i in range (start,count):
        if i > 180:
            x = i

        # j = (idx for idx, s in enumerate(distance_col[i+1:], start=i+1) 
        #   if distance(s,distance_col[i]) >= lowerWindowWidth)
        end = min(i + 701, count)

        for idx in range(i+1,end):
            if distance(xyz_mat[i,:],xyz_mat[idx,:]) >= lowerWindowWidth:
                j = idx
                break
        if j == -1:
            continue
        di = np.median([x for x in distance_col[i:j]])
        # k = np.argmax(distance_col)
        # if i>=k:
        #     continue;
        # mode_result = stats.mode(distance_col[i:k])
        # mode_value = mode_result.mode
        # smallest_index = distance_col[i:k].to_list().index(mode_value) + i
        # di = distance_col[smallest_index]
        for idx2 in range(j, end):
            if distance(xyz_mat[idx2,:],xyz_mat[j,:]) >= upperWindowWidth:
                k = idx2
                break
        if k == -1:
            continue
        flag1 = True
        for j3 in range(0, idx2 + 1 - j):  # 循环条件：j3 + j < index3 + 1
            dj3 = distance_col[j+j3]
            flag1 = flag1 and (di - dj3 >= heightThreshold)
            if not flag1:
                break

        if flag1:
            index = j
            break
    # print(dj3)
    # print(di)
    return index

def distance(target1, target):
    # print(np.linalg.norm(target1 - target))
    return np.linalg.norm(target1 - target)




rise_idx = riseDetection(0)
if rise_idx >= 0:
        plt.figure(figsize=(10, 6))
        plt.scatter(x, distance_col, label='Data')
        # plt.plot(x, predictions, color='red', label='Piecewise Linear Regression')
        # for bp in breakpoints[1:-1]:  # 跳过起点和终点
        end = min(rise_idx + 700, count)
        rise_max = np.argmin(distance_col[rise_idx:end])
        plt.axvline(x[rise_max+rise_idx], color='green', linestyle='--')
        for l in range(rise_idx, end):
            subset = distance_col[l:l +10]
            std_v = subset.std()
            print(std_v)
            if std_v < std_threshold:
                print("找到目标预热点")
                plt.axvline(x[l], color='blue', linestyle='--')
                break

        plt.legend()
        plt.show()


fall_idx = fallDetection(0)

print(fall_idx)
if fall_idx >= 0:
    rise_idx = riseDetection(fall_idx)
    print(rise_idx)
    if rise_idx >= 0:
        print("检测到槽")

        # 绘图
        plt.figure(figsize=(10, 6))
        plt.scatter(x, distance_col, label='Data')
        # plt.plot(x, predictions, color='red', label='Piecewise Linear Regression')
        # for bp in breakpoints[1:-1]:  # 跳过起点和终点
        end = min(rise_idx + 700, count)
        rise_max = np.argmin(distance_col[rise_idx:end])
        plt.axvline(x[rise_max+rise_idx], color='green', linestyle='--')
        for l in range(rise_idx, end):
            subset = distance_col[l:l +10]
            std_v = subset.std()
            print(std_v)
            if std_v < std_threshold:
                print("找到目标预热点")
                plt.axvline(x[l], color='blue', linestyle='--')
                break

        plt.legend()
        plt.show()
        print(1)

else:
    rise_idx = riseDetection(0)
    print(rise_idx)
    if rise_idx >= 0:
        print("检测到上升点")
        
# a = distance(xyz_mat[0,:],xyz_mat[count-1,:])
# print(a)
