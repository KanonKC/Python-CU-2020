# Prog-11: Weather report (EP.2)
# #6?3?????21 Name ?
import json
import math

with open("th_weather.json") as f:
    data = json.load(f)

def top_K_max_temp_by_region(data, K):
    maxTemp = {
        'C':[],
        'E':[],
        'N':[],
        'NE':[],
        'S':[],
        'W':[]
    }

    tempList = {
        'C':[],
        'E':[],
        'N':[],
        'NE':[],
        'S':[],
        'W':[]
    }

    for i in data:
        for j in range(len(data[i]['list'])):
            tempList[data[i]['city']['region']].append((data[i]['list'][j]['main']['temp'],data[i]['city']['name'],data[i]['list'][j]['dt_txt']) )

    for i in tempList:
        tempList[i].sort(key=lambda x:x[0],reverse=True)

    for i in maxTemp:
        for j in range(K):
            maxTemp[i].append(tempList[i][j])

    return maxTemp
        
def average_temp_by_date(data, region):
    date = []
    for i in data:
        for j in range(len(data[i]['list'])):
            dt = data[i]['list'][j]['dt_txt'].split()
            if dt[0] not in date:
                date.append(dt[0])
    
    if region == "ALL":
        avgTemp = [[i,[0,0]] for i in date]

        for a in range(len(avgTemp)):
            for i in data:
                for j in range(len(data[i]['list'])):
                    dt = data[i]['list'][j]['dt_txt'].split()
                    if dt[0] == avgTemp[a][0]:
                        avgTemp[a][1][0] += data[i]['list'][j]['main']['temp']
                        avgTemp[a][1][1] += 1
        
        for a in range(len(avgTemp)):
            avgTemp[a][1] = avgTemp[a][1][0]/avgTemp[a][1][1]

        return [(i[0],i[1]) for i in avgTemp]
    elif region in ['C','E','N','NE','S','W']:
        avgTemp = [[i,[0,0]] for i in date]
        
        for a in range(len(avgTemp)):
            for i in data:
                if data[i]['city']['region'] == region:
                    for j in range(len(data[i]['list'])):
                        dt = data[i]['list'][j]['dt_txt'].split()
                        if dt[0] == avgTemp[a][0]:
                            avgTemp[a][1][0] += data[i]['list'][j]['main']['temp']
                            avgTemp[a][1][1] += 1
        
        for a in range(len(avgTemp)):
            avgTemp[a][1] = avgTemp[a][1][0]/avgTemp[a][1][1]

        
        return [(i[0],i[1]) for i in avgTemp]
    else:
        return []    

def max_rain_in_3h_periods(data, region, date):

    a = {
        0 : 0,
        3 : 0,
        6 : 0,
        9 : 0,
        12 : 0,
        15 : 0,
        18 : 0,
        21 : 0
    }

    if region == "ALL":
        for i in data :
            for j in range(len(data[i]['list'])):
                dt = data[i]['list'][j]['dt_txt'].split()
                # print(dt)
                if dt[0] == date:
                    for k in data[i]['list'][j]:
                        if k == 'rain': # 09
                            if data[i]['list'][j]['rain']['3h'] > a[int(dt[1][:2])]:
                                a[int(dt[1][:2])] = data[i]['list'][j]['rain']['3h']
    
    else:
        for i in data :
            if data[i]['city']['region'] == region:
                for j in range(len(data[i]['list'])):
                    dt = data[i]['list'][j]['dt_txt'].split()
                    # print(dt)
                    if dt[0] == date:
                        for k in data[i]['list'][j]:
                            if k == 'rain': # 09
                                if data[i]['list'][j]['rain']['3h'] > a[int(dt[1][:2])]:
                                    a[int(dt[1][:2])] = data[i]['list'][j]['rain']['3h']
            

    return [(i,a[i]) for i in a]

def AM_PM_weather_description_by_region(data, date):

    w = {
        'C': {'AM':{},'PM':{}},
        'E': {'AM':{},'PM':{}},
        'N': {'AM':{},'PM':{}},
        'NE': {'AM':{},'PM':{}},
        'S': {'AM':{},'PM':{}},
        'W': {'AM':{},'PM':{}}
    }

    for i in data:
        for j in range(len(data[i]['list'])):
            dt = data[i]['list'][j]['dt_txt'].split()
            if dt[0] == date:
                timeZone = "PM"
                if dt[1] < '12:00:00':
                    timeZone = "AM"
                
                if data[i]['list'][j]['weather'][0]['description'] in w[data[i]['city']['region']][timeZone]:
                    w[data[i]['city']['region']][timeZone][data[i]['list'][j]['weather'][0]['description']] += 1
                else:
                    w[data[i]['city']['region']][timeZone][data[i]['list'][j]['weather'][0]['description']] = 1
                
    for i in w:
        for j in w[i]:
            mostWeatherName = ""
            mostWeatherValue = 0
            for k in w[i][j]:
                if w[i][j][k] > mostWeatherValue:
                    mostWeatherValue = w[i][j][k]
                    mostWeatherName = k
            w[i][j] = mostWeatherName
    
    return w


def most_varied_weather_provinces(data):
    w = {}

    for i in data:
        manyWeather = []
        for j in range(len(data[i]['list'])):
            if data[i]['list'][j]['weather'][0]['description'] not in manyWeather:
                manyWeather.append(data[i]['list'][j]['weather'][0]['description'])
        w[data[i]['city']['name']] = len(manyWeather)

    mostWeatherValue = 0
    for i in w:
        if w[i] > mostWeatherValue:
            mostWeatherValue = w[i]

    return ({i for i in w if w[i]==mostWeatherValue})



def main():
    pass

main()

# top_K_max_temp_by_region(data, 2)
# print(average_temp_by_date(data,'C'))
# most_varied_weather_provinces(data)
# print(max_rain_in_3h_periods(data, 'C', '2021-04-07'))
# AM_PM_weather_description_by_region(data, '2021-04-09')
# most_varied_weather_provinces(data)