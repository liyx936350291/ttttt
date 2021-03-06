import pytest
import uri as uri
from Tools.scripts.make_ctype import method
from tools.api import request_tool
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
# json path，参数类型为列表 根据jsonpath提取响应正文中的数据
# json_path = [{"token": '$.data.token'}]
@pytest.mark.ok
def test_addProd(pub_data):
    pub_data["productCode"] = "自动生成 字符串 3,10 数字"
    # a = ["小米","耐克","LV","华为","匡威"]
    # b = rad
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"token": "$['data']['token']"}]
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '增加产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token" :"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "自动生成 字符串 2,15 数字 小米",
  "colors": [
    "黑色"
  ],
  "price": "自动生成 数字 2,15",
  "productCode": "${productCode}",
  "productName": "手机",
  "sizes": [
    "64G8G"
  ],
  "type": "手机"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,
                             expect=expect,feature=feature,story=story,title=title,json_data=json_data)

def test_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '下架'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    headers = {"token" :"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

