# 导包
import requests


# 创建要封装的部门类
class DeptApi:
    def __init__(self):
        # 定义部门模块的url
        self.dept_url = "http://ihrm-test.itheima.net" + "/api/company/department"

    def add_dept(self, name, cod, headers):
        # 根据外部传入的name，code拼接成要发送的请求体数据
        jsonData = {"name": name, "code": cod,
                    "manager": "我", "introduce": "没有"}
        return requests.post(url=self.dept_url, json=jsonData, headers=headers)

    def query_dept(self, em_id, headers):
        # 拼接查询部门的url
        query_url = self.dept_url + "/" + em_id
        # 发送查询部门的接口请求，并返回结果
        return requests.get(url=query_url, headers=headers)

    def modify_dept(self, em_id, jsonData, headers):
        # 拼接修改部门的url
        modify_url = self.dept_url + "/" + em_id
        # 发送查询部门的接口请求，并返回结果
        return requests.put(url=modify_url, json=jsonData, headers=headers)

    def delete_dept(self, em_id, headers):
        # 拼接删除部门的url
        delete_url = self.dept_url + "/" + em_id
        # 发送查询部门的接口请求，并返回结果
        return requests.delete(url=delete_url, headers=headers)
