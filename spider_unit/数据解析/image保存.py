import requests

if __name__ == "__main__":
    url = "https://img0.baidu.com/it/u=439116727,1655593570&fm=253&fmt=auto&app=138&f=JPEG?w=578&h=500"

    picture = requests.get(url=url).content

    with open("./冬奥会图片.jpg", "wb") as fp:
        fp.write(picture)

    print("over!!")
