

### 关于类的方法
~~~
# 初始化数据类
Excel_Data = DataList(generate_settings)

# 设置预热点生成类型为:直角型
Excel_Data.y_type = 0
Excel_Data.generate_y()

# 开启画图
Excel_Data.show_data()

# 获得当前列表
print(Excel_Data.data_list)