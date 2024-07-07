from wxauto import WeChat 
from datetime import datetime
import requests 
def get_weather(api_key, city='Beijing'):
    url =f'http://api.openweathermap.org/data/2.5/weather?q='+f'{city}'+'&appid='+f'{api_key}'
    response = requests.get(url)
    data = response.json()
    main = data['main']
    temperature = main['temp']
    humidity = main['humidity']
    wind = data['wind']['speed']
    weather = data['weather'][0]['description']
    print(url)
    return temperature,humidity,weather,wind

def get_time():
    curr_time =datetime.now()
    return curr_time.strftime("%Y-%m-%d %H:%M:%S")

def show_weather(api_key, city='Beijing'):
    weather_data = get_weather(api_key, city)
    return (f"当前 {city.upper()} 天气：{weather_data[2]}，温度：{round((weather_data[0]-273.15))}℃，湿度：{weather_data[1]}%, 风速：{weather_data[3]}")
    # print(f"当前时间：{get_time()}")

api_key = 'b63775f0a1ab48934bbc07cc2501a348'
city = 'Sydney'
# show_weather(api_key, city)

weather_forcast_msg = show_weather(api_key, city)
time_msg = f"当前时间：{get_time()}"

from wxauto import WeChat

wx = WeChat()

# 发送消息
who = 'Brenda'
for i in range(1):
    wx.SendMsg(time_msg, who)
    wx.SendMsg(weather_forcast_msg, who)
    
# # 获取当前聊天页面（文件传输助手）消息，并自动保存聊天图片
# msgs = wx.GetAllMessage(savepic=True)
# for msg in msgs:
#     print(f"{msg[0]}: {msg[1]}")