import requests
from datetime import datetime
import schedule
import time
url="https://3g.dxy.cn/newh5/view/pneumonia?from=timeline&isappinstalled=0"
from lxml import html

def analyse(content,time_hour):
    # 全国 确诊 1409 例 疑似 2032 例
    # 死亡 42 例 治愈 39 例
    tree = html.fromstring(content)
    try:
        c_confirm = tree.xpath('//*[@id="root"]/div/div[3]/div[1]/p[2]/span/span[1]/span/text()')        
        c_suspect = tree.xpath('//*[@id="root"]/div/div[3]/div[1]/p[2]/span/span[2]/span/text()')
        c_dead = tree.xpath('//*[@id="root"]/div/div[3]/div[1]/p[2]/span/span[3]/span/text()')
        c_heal = tree.xpath('//*[@id="root"]/div/div[3]/div[1]/p[2]/span/span[4]/span/text()')
        import csv
        nms = [time_hour,c_confirm[0],c_suspect[0],c_dead[0],c_heal[0]]
        print(nms)
        results=[[int(i) for i in nms]]
        f = open('numbers.csv', 'a+')
        with f:
            writer = csv.writer(f)
            writer.writerows(results)
    except:
        pass
    
    

def crawl_job():
    now = datetime.now()
    time_hour = now.strftime("%Y%m%d%H")
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        time_file = "/tmp/wuhan"+time_hour+".html"
        with open(time_file, 'w') as file:
            file.write(content.decode("utf-8"))
        print(time_file + " saved")  
        analyse(content, time_hour)

def main():
    crawl_job()
    schedule.every(1).hours.do(crawl_job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

