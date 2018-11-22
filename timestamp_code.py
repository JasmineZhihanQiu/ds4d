import re
import datetime as dt
import time
import calendar

def timeconvert(time):
    timelist=[]
    for a in time:
        zero = re.compile(',0')
        new_zero = zero.sub(',',a)
        slash = re.compile('/')
        new_slach = slash.sub(',',new_zero)
        colon = re.compile(':')
        new_colon = colon.sub(',',new_slach)
        space = re.compile(' ')
        new_space = space.sub(',',new_colon)

        if int(new_space[0])>0:
            newlist = new_space
        else:
            newlist = new_space[1:]
            
        timelist.append(newlist)
    timeSer = pd.Series(timelist)
    return timeSer

a = measured_data['starttime']
measured_data.loc[:,'starttime'] = timeconvert(a)
b = measured_data['endtime']
measured_data.loc[:,'endtime'] = timeconvert(b)

def timestamp(time):
    timelist=[]
    for a in time:
        format = '%d,%m,%Y,%H,%M'
        date = dt.datetime.strptime(a,format) 
        ts = calendar.timegm(date.timetuple())
        timelist.append(ts)
    timestamp = pd.Series(timelist)
    return timestamp

a = measured_data['starttime']
measured_data.loc[:,'starttime'] = timestamp(a)
b = measured_data['endtime']
measured_data.loc[:,'endtime'] = timestamp(b)


a = home_data['stdinstalltime']
home_data.loc[:,'stdinstalltime'] = timeconvert(a)
b = home_data['studyperiod_end_time']
home_data.loc[:,'studyperiod_end_time'] = timeconvert(b)

a = home_data['stdinstalltime']
home_data.loc[:,'stdinstalltime'] = timestamp(a)
b = home_data['studyperiod_end_time']
home_data.loc[:,'studyperiod_end_time'] = timestamp(b)