import requests
from datetime import datetime
import schedule
import time
url="https://3g.dxy.cn/newh5/view/pneumonia?from=timeline&isappinstalled=0"

def crawl_job():
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

def main():
    schedule.every(1).hours.do(crawl_job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

