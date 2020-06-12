import json
import app
import logging
from logging import handlers


# 编写初始化日志的代码
# 1 首先定义一个初始化日志的函数
def init_logging():
    # 2 在函数中，设置日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 设置控制台处理器
    sh = logging.StreamHandler()
    # 5 设置文件处理器（文件处理的作用是设置保存日志的文件地址的：需要使用项目根目录定位到日志文件）
    log_path = app.BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path,
                                                   when='M',
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding='utf-8')
    # 6 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 7 将格式化器添加到文件处理器和控制台处理当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 8 将文件处理器和控制台处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)


# 封装通用断言函数
def assert_common(self, http_code, success, code, message, response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


# 编写读取登录数据的函数
def read_login_data(filepath):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json格式的数据文件，并把数据处理成列表元组形式（[(),(),()]）添加到空列表中
        result_list = list()
        for login_data in jsonData:
            # 把每一组登录数据的所有values转化为元组形式，并添加到空列表当中
            result_list.append(tuple(login_data.values()))

    print("查看读取的登录数据为：", result_list)
    return result_list


# 编写读取部门模块的数据函数
def read_dept_data(filepath, interface_name):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 把数据文件加载成json格式
        jsonData = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        dept_data= jsonData.get(interface_name)  # type:dict
        # 把数据处理成列表元组对象，然后添加到空列表当中
        result_list = list()
        result_list.append(tuple(dept_data.values()))
        # 返回数据
    print("读取的{}部门数据为:{}".format(interface_name, result_list))
    return result_list
