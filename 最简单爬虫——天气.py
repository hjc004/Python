import requests
import re


def get_weather(url):
    response = requests.get(url)
    response.encoding = 'utf-8'

	# 抓取当天气温（非实时）
    aim = re.findall('<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日(.*?)时 (.*?)  (.*?)  (.*?)"',
                     response.text, re.S)
    print("今日气温：%s" % aim[0][5])


if __name__ == "__main__":
    url_bj = "http://www.weather.com.cn/weather1d/101280701.shtml#input"
    get_weather(url_bj)
