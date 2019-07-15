from TenAwsTSSvc import TenAwsTSSvc
from TenAwsTSSvc import PutRow

if __name__ == '__main__':
    o = TenAwsTSSvc("Key", "秘钥", '区域') # 这3个参数都需要替换成自己相对应的数据
    o.DoConnect()
    
    Item = {
            "Id": {
                    "S":"2"
            },
            "Arr": {
                "S": "2"
            }
        }
    putrow = PutRow(client, "Test", Item)
    b = putrow.DoPutRow()
    
