import requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 将用户名（非必要）和 cookie（必要） 填写在下面字典中
userCookieDicts = {
    "userName": "your Cookie",
}

warnings.simplefilter('ignore', InsecureRequestWarning)

# 将要请求的 URL 替换 "your url"
url = "https://g8n.cn" + "your url"

for (key, value) in userCookieDicts.items():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090c0f) XWEB/11275 Flue",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": value.encode('utf-8').decode('latin-1'),
        "Referer": "https://g8n.cn/student/punchs/course/107772/2681383",
        "Origin": "https://g8n.cn",
    }

    data = {
        "lat": "your lat",  # 将 维度 填写在此处
        "lng": "your lng",  # 将 经度 填写在此处
        "acc": "253",
        "res": "",
        "gps_addr": "Fujian Province, Fuzhou",
    }

    response = requests.post(url, headers=headers, data=data, verify=False)

    if "我已签到过啦" in response.text:
        print(f"---- {key} 已经签到 ----")
    else:
        print(f"---- {key} 签到成功 ----")
