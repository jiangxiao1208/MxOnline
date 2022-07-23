from apps.utils.random_str import generate_random
import json

def send_single_sms(code, mobile):
    #发送单条短信
    # ver_code = generate_random(4, 0)
    res = {"code": 0, "mobile": mobile, "msg" : "..."}

    return res


if __name__ == "__main__":
    res = send_single_sms(0, mobile=123456789)
    msg = res["msg"]
    if res["code"] == 0:
        print("发送成功")
    else:
        print("发送失败: {}".format(msg))

    print(res)