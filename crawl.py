import requests
from datetime import datetime

url="https://3g.dxy.cn/newh5/view/pneumonia?from=timeline&isappinstalled=0"

now = datetime.now()
time_now = now.strftime("%m%d%Y%H:%M:%S")
time_hour = now.strftime("%Y%m%d%H")
response = requests.get(url)
if response.status_code == 200:
    content = response.content
    time_file = "/tmp/wuhan"+time_hour+".html"
    with open(time_file, 'w') as file:
        file.write(str(content))
    print(time_file + " normal saved")  



