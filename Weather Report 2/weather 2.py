# Prog-11: Weather report (EP.2)
# #6?3?????21 Name ?
import json
import math

def top_K_max_temp_by_region(data, K):
    regionTemp = {'C':{},'E':{},'N':{},'NE':{},'S':{},'W':{}}
    for i in data:
        for j in regionTemp:
            if j == data[i]['city']['region']:
                regionTemp[j][data[i]['city']['name']] = {}
                for k in range(len(data[i]['list'])):
                    regionTemp[j][data[i]['city']['name']][data[i]['list'][k]['dt_txt']] = data[i]['list'][k]['main']['temp']
                break
    print(regionTemp)
    # ---------------------------------------------------------------------------------
    topKMax = {}
    for i in regionTemp:
        allTemp = []
        for j in regionTemp[i]:
            for k in regionTemp[i][j]:
                if regionTemp[i][j][k] not in allTemp:
                    allTemp.append(regionTemp[i][j][k])
        allTemp.sort(reverse=True)
        maxTemp = []
        for j in range(len(allTemp)):
            if j == K:
                break
            for k in regionTemp[i]:
                subMaxTemp = []
                for l in regionTemp[i][k]:
                    if regionTemp[i][k][l] == allTemp[j]:
                        subMaxTemp.append((allTemp[j],k,l))
                if subMaxTemp != []:
                    subMaxTemp.sort(key=lambda x:x[1])
                    for m in subMaxTemp:
                        maxTemp.append(m)
        topKMax[i] = maxTemp
    return topKMax

def average_temp_by_date(data, region):
    regionTemp = {'C':{},'E':{},'N':{},'NE':{},'S':{},'W':{}}
    for i in data:
        for j in regionTemp:
            if j == data[i]['city']['region']:
                regionTemp[j][data[i]['city']['name']] = {}
                for k in range(len(data[i]['list'])):
                    regionTemp[j][data[i]['city']['name']][data[i]['list'][k]['dt_txt']] = data[i]['list'][k]['main']['temp']

                break
    # ---------------------------------------------------------------------------------
    if region == "ALL":
        date = []
        for i in regionTemp:
            for j in regionTemp[i]:
                for k in regionTemp[i][j]:
                    d = k.split()
                    if d[0] not in date:
                        date.append(d[0])
        avgTemp = []
        for d in date:
            resTemp = 0
            n = 0
            for i in regionTemp:
                for j in regionTemp[i]:
                    for k in regionTemp[i][j]:
                        if d in k.split():
                            resTemp += regionTemp[i][j][k]
                            n += 1
            avgTemp.append((d,resTemp/n))
        return avgTemp
    else:
        date = []
        for i in regionTemp[region]:
            for j in regionTemp[region][i]:
                d = j.split()
                if d[0] not in date:
                    date.append(d[0])
        avgTemp = []
        for i in date:
            resTemp = 0
            n = 0
            for j in regionTemp[region]:
                for k in regionTemp[region][j]:
                    if i in k.split():
                        resTemp += regionTemp[region][j][k]
                        n += 1
            avgTemp.append((i,resTemp/n))
        return avgTemp

def max_rain_in_3h_periods(data, region, date):
    timeRain = {
         0: [0,0],
         3: [0,0],
         6: [0,0],
         9: [0,0],
        12: [0,0],
        15: [0,0],
        18: [0,0],
        21: [0,0]
    }

    if region == "ALL":
        for i in data:
            for j in range(len(data[i]['list'])):
                if data[i]['list'][j]['dt_txt'].split()[0] == date:
                    for k in data[i]['list'][j]:
                        if k == "rain":
                            timeRain[int(data[i]['list'][j]["dt_txt"].split()[1][:2])][0] += data[i]['list'][j]['rain']['3h']
                            timeRain[int(data[i]['list'][j]["dt_txt"].split()[1][:2])][1] += 1
        for i in timeRain:
            timeRain[i] = timeRain[i][0]/timeRain[i][1]
        print(timeRain)

def AM_PM_weather_description_by_region(data, date):
    regionWeather = {'C':{'AM':{},'PM':{}},'E':{'AM':{},'PM':{}},'N':{'AM':{},'PM':{}},'NE':{'AM':{},'PM':{}},'S':{'AM':{},'PM':{}},'W':{'AM':{},'PM':{}}}
    for i in data:
        for j in range(len(data[i]['list'])):
            dt = data[i]['list'][j]['dt_txt'].split()
            if dt[0] == date:
                noon = "PM"
                if dt[1] < "12:00:00":
                    noon = "AM"
                if data[i]['list'][j]['weather'][0]['description'] not in regionWeather[data[i]['city']['region']][noon]:
                    regionWeather[data[i]['city']['region']][noon][data[i]['list'][j]['weather'][0]['description']] = 1
                else:
                    regionWeather[data[i]['city']['region']][noon][data[i]['list'][j]['weather'][0]['description']] += 1
    # ---------------------------------------------------------------------------------
    topWeatherDes = {}
    for i in regionWeather:
        topWeatherDes[i] = {}
        for j in regionWeather[i]:
            topWeather = ["",0]
            for k in regionWeather[i][j]:
                if regionWeather[i][j][k] > topWeather[1]:
                    topWeather[1] = regionWeather[i][j][k]
                    topWeather[0] = k
            topWeatherDes[i][j] = topWeather[0]
    return topWeatherDes

def most_varied_weather_provinces(data):
    cityWeather = {}
    for i in data:
        weatherDes = []
        for j in range(len(data[i]['list'])):
           wd = data[i]['list'][j]['weather'][0]['description']
           if wd not in weatherDes:
               weatherDes.append(wd)
        cityWeather[data[i]['city']['name']] = len(weatherDes)
    # -----------------------------------------------------------------
    mostWeatherDes = max([cityWeather[i] for i in cityWeather])
    city = set({})
    for i in cityWeather:
        if cityWeather[i] == mostWeatherDes:
            city.add(i)
    return city

def main():
    with open("th_weather.json") as f:
        data = json.load(f)
    x = int(input("ไปทำให้มันดีกว่านี้เอง <ใส่ 1-5>: "))
    if x == 1:
        print(top_K_max_temp_by_region(data,5))
    if x == 2:
        print(average_temp_by_date(data,"C")) 
    if x == 3:
        print(max_rain_in_3h_periods(data,'ALL','2021-04-07'))
    if x == 4:
        print(AM_PM_weather_description_by_region(data,'2021-04-09'))
    if x == 5:
        print(most_varied_weather_provinces(data))

main()
