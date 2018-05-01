import gevent
from gevent import monkey
# 导入网络模块
import urllib.request
# 打补丁
monkey.patch_all()

def load_img(img_url, img_name):
    # 发送请求
    response = urllib.request.urlopen(img_url)
    f = open(img_name, "wb")
    while True:
        result = response.read(1024)
        if result:
            f.write(result)
        else:
            break
    f.close()
    print("%s图片下载完成" % img_name)

if __name__ == '__main__':
# 图片地址
    img_url1 = "http://a4.att.hudong.com/34/91/01300000249947122354919810631.jpg"
    img_url2 = "http://pic60.nipic.com/file/20150207/11284670_083602732000_2.jpg"
    img_url3 = "http://www.hsliuxue.com.cn/Files/image/3%2815%29.jpg"
    gevent.joinall([
        gevent.spawn(load_img, img_url1, "1.jpg"),
        gevent.spawn(load_img, img_url2, "2.jpg"),
        gevent.spawn(load_img, img_url3, "3.jpg")
    ])
