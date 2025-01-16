import random

random.seed(22327)

settings = {

    # 地面高度
    "base_g" : 1000,
    "base_g_floating" : 15,

    # 板坯高度
    "base_h" : 700,
    "base_h_floating" : 30,

    # 点的个数
    "base_l" : 1000,

    # 随机种子
    "random" : 22327,

    "floating" : 2,

    # "stride" :

    "goucao" : {

        "start_position" : (50,150),

    },

    "yuredian" : {

        "start_position" : (400,600),

    }
}

class DataList:

    def __init__(self,data_settings,data_type):

        self.data_list = []

    def growing(self, data_list):

        print(random.randint(1, 10))

