import datetime
import time
import random
def randomdate(startDate,endDate):
    randomVal=random.random()
    dateFormat="%m/%d/%Y"
    extract_S_Date=time.strptime(startDate,dateFormat)
    extract_E_Date=time.strptime(endDate,dateFormat)
    
    startTime=time.mktime(extract_S_Date)
    endTime=time.mktime(extract_E_Date)
    
    randomTime=startTime+randomVal*(endTime-startTime)
    
    local_time=time.localtime(randomTime)
    
    randomDate=time.strftime(dateFormat,local_time)
    return randomDate
print("random date:",randomdate("10/12/2020","12/12/2023"))
    

