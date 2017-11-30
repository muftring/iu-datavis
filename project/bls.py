#
# bls.py
#
# Bureau of Labor Statistics
#

import re

def init():
    loadCityTownData()
    loadStateCodes()

def code2month(code):
    month = "(unknown)"
    if code == "M01":
        month = "January"
    elif code == "M02":
        month = "February"
    elif code == "M03":
        month = "March"
    elif code == "M04":
        month = "April"
    elif code == "M05":
        month = "May"
    elif code == "M06":
        month = "June"
    elif code == "M07":
        month = "July"
    elif code == "M08":
        month = "August"
    elif code == "M09":
        month = "September"
    elif code == "M10":
        month = "October"
    elif code == "M11":
        month = "November"
    elif code == "M12":
        month = "December"
    return month

def month2number(month):
    number = "00"
    if month == "January":
        number = "01"
    elif month == "February":
        number = "02"
    elif month == "March":
        number = "03"
    elif month == "April":
        number = "04"
    elif month == "May":
        number = "05"
    elif month == "June":
        number = "06"
    elif month == "July":
        number = "07"
    elif month == "August":
        number = "08"
    elif month == "September":
        number = "09"
    elif month == "October":
        number = "10"
    elif month == "November":
        number = "11"
    elif month == "December":
        number = "12"
    return number

def dateFrom(year, month):
    return "{}/{}".format(year,month2number(month))



code2citytown = {}
citytown2code = {}

def loadCityTownData():
    file = open("bls-cities-and-towns.raw", "r")

    count = 0
    for line in file.readlines():
        count += 1
        #ignore, code, citytownstate = line.rstrip().split(">", 2)[1].split(" ",2)
        #citytown, state = citytownstate.split(",")
        #code2citytown[code]=citytown
        #citytown2code[citytown]=code
        #print("line: {} code: {} citytownstate: {}, citytown: {}, state: {}".format(count, code, citytownstate, citytown, state))

        ignore, code, citytownstate = line.rstrip().split(">", 2)[1].split(" ",2)
        a, b = citytownstate.split(",")
        citytown = a.lstrip().rstrip()
        state = b.lstrip().rstrip()

        try:
            select = citytown2code[state]
        except:
            select = {}
        newDict = {}
        for eCity in select:
            eCode = select[eCity]
            newDict[eCity] = eCode
        newDict[citytown] = code
        citytown2code[state] = newDict

        code2citytown[code]=citytown

    file.close()

def decodeCityTown(s):
    code = s[3:len(s)-2]
    return code2citytown[code]

def searchDictionary(d, city):
    #print("searching for:", city, "in", d)
    res = []
    for key in d.keys():
        if re.match(city, key):
            res.append(d[key])
    return res

def findCityTownCode(city, state):
    return searchDictionary(citytown2code[state], city)

def trimCityName(city):
    return city.replace(" city","").replace(" County/city","").replace(" town","").replace(" (consolidated)","")



code2state = {}

def loadStateCodes():
    file = open("bls-state-codes.raw", "r")

    count = 0
    for line in file.readlines():
        count += 1
        ignore, code, state = line.rstrip().split(">", 2)[1].split(" ",2)
        code2state[code]=state
        #print("line: {} code: {} state: {}".format(count, code, state))

    file.close()

def decodeState(s):
    code = s[5:7]
    return code2state[code]



code2measure = {
    "03" : "unemployment-rate",
    "04" : "unemployment",
    "05" : "employment",
    "06" : "labor-force"
}

measure2Code = {
    "unemployment-rate" : "03",
    "unemployment" : "04",
    "employment" : "05",
    "labor-force" : "06"
}

def findMeasureCode(s):
    return measure2Code[s]

def decodeMeasure(s):
    code = s[len(s)-2:]
    return code2measure[code]
