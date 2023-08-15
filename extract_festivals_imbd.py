import requests
import pprint
import parsel

url = 'https://www.imdb.com/event/all/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)

print(response.text)
selector = parsel.Selector(response.text)
# 获取所有li标签‘#__next > main > div > section > div > section > div > div.sc-c7c3a435-1.NixYx.ipc-page-grid__item.ipc-page-grid__item--span-2 > section > a:nth-child(1928)’
lis = selector.css('#__next > main > div > section > div > section > div > div.sc-c7c3a435-1.NixYx.ipc-page-grid__item.ipc-page-grid__item--span-2 > section > a')
print(len(lis))
festivals = []
# 遍历出每个li标签内容
for a in lis:
    a = a.css('a::text')
    # 获取电影标题 hd 类属性 下面的 a 标签下面的 第一个span标签里面的文本数据 get()输出形式是 字符串获取一个  getall() 输出形式是列表获取所有
    # title = li.css('.hd a span:nth-child(1)::text').get()   # get()输出形式是 字符串
    # movie_list = li.css('.bd p:nth-child(1)::text').getall()     # getall() 输出形式是列表
    # star = movie_list[0].strip().replace('\xa0\xa0\xa0', '').replace('/...', '')
    # movie_info = movie_list[1].strip().split('\xa0/\xa0')   # ['1994', '美国', '犯罪 剧情']
    # movie_time = movie_info[0]  # 电影上映时间
    # movie_country = movie_info[1]   # 哪个国家的电影
    # movie_type = movie_info[2]     # 什么类型的电影
    # rating_num = li.css('.rating_num::text').get()   # 电影评分
    # people = li.css('.star span:nth-child(4)::text').get()   # 评价人数
    # summary = li.css('.inq::text').get()   # 一句话概述
    # dit = {
    #     '电影名字': title,
    #     '参演人员': star,
    #     '上映时间': movie_time,
    #     '拍摄国家': movie_country,
    #     '电影类型': movie_type,
    #     '电影评分': rating_num,
    #     '评价人数': people,
    #     '电影概述': summary,
    # }
    # # pprint 格式化输出模块
    # pprint.pprint(dit)
    festivals.append(a.get())
