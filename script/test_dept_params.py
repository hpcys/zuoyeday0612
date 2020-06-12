# 导包
import unittest, logging
from api.login_api import LoginApi
from api.dept_api import DeptApi
import app
from parameterized import parameterized
from utils import assert_common, read_dept_data


# 创建测试类
class TestIhrmDept(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化部门
        self.dept_api = DeptApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app.HEADERS))

        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 定义部门模块的文件路径
    dept_filepath = app.BASE_DIR + "/data/dept_data.json"

    # 参数化
    @parameterized.expand(read_dept_data(dept_filepath, 'add_dept'))
    def test02_add_dept(self, name, cod, success, code, message, http_code):
        logging.info("app.HEADERS的值是：{}".format(app.HEADERS))
        # 发送添加部门的接口请求
        response = self.dept_api.add_dept(name, cod, app.HEADERS)
        # 打印添加部门的结果
        logging.info("添加部门的结果为：{}".format(response.json()))
        # 提取部门中的令牌并把部门令牌保存到全局变量中
        app.EM_ID = response.json().get("data").get("id")
        # 打印保存的部门ID
        logging.info("保存到全局变量的部门的ID为：{}".format(app.EM_ID))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dept_data(dept_filepath, "query_dept"))
    def test03_query_dept(self, success, code, message, http_code):
        # 发送查询部门的接口请求:
        response = self.dept_api.query_dept(app.EM_ID, app.HEADERS)
        # 打印查询部门的数据
        logging.info("查询部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dept_data(dept_filepath, "modify_dept"))
    def test04_modify_dept(self, name, success, code, message, http_code):
        # 调用封装的修改部门接口，发送接口请求
        response = self.dept_api.modify_dept(app.EM_ID, {"name": name},
                                             app.HEADERS)
        # 打印数据
        logging.info("修改部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_dept_data(dept_filepath, "delete_dept"))
    def test05_delete_dept(self, success, code, message, http_code):
        # 调用封装的删除部门接口，发送接口请求
        response = self.dept_api.delete_dept(app.EM_ID, app.HEADERS)
        # 打印删除部门的结果为
        logging.info("删除部门的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)
