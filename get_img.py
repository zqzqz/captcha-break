import requests
from bs4 import BeautifulSoup



def download_img(img_name):

    res = requests.get(url, headers = header)
    page = BeautifulSoup(res.text, 'html.parser')
    # 获取验证码url
    img = "https://jaccount.sjtu.edu.cn/jaccount/"+page.select('div[class="input-control captcha-input"] img')[0]['src']
    data = requests.get(img)

    if data.status_code == requests.codes.ok:
        with open(u'D:/test/captcha-break/raw-img/%s.jpg'%(img_name), 'wb') as f:
            f.write(data.content)
            print("NO." + str(img_name) + " captcha downloaded")
            f.close()

if __name__ == "__main__":
    #上海交大官网邮箱jaccount登录
    url = "https://jaccount.sjtu.edu.cn/jaccount/jalogin?sid=jasjtumail&returl=CCs1OYRmOc6tQcPpePAYjBj4dB67gBdeiLlHyaQWtJQwju0O1oEPGC0A2JqGlj%2FS5RQzNttCyaqgpc6G11HtwG0%3D&se=CDswrjUq4G8kF098jEqdn5uXUgDmSXkK4OAlO5cMt%2BaVaw5ICPEdPu8%3D"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
    #下载100个验证码图片
    for i in range(300):
        img_name = str(i)
        download_img(img_name)
