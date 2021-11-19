import pandas as pd
import numpy as np
import schedule as sc
def find_similars_days(f_list,s_list):
    list_days=[]
    for i in f_list:
        for j in s_list:
            if i==j:
                result=True
                list_days.append(i)
                #return result
    return list_days
def find_similars_hours(f_list,s_list):
    list_hours=[]
    for i in f_list:
        for j in s_list:
            if i==j:
                result=True
                list_hours.append(i)
                #continue
    return list_hours

    
class Client:
    tel_number=''
    lec_days=[]
    time_period=[]
    
    def __init__(self,tel_number,lec_days,time_period):
        self.tel_number = tel_number
        self.lec_days = lec_days
        self.time_period = time_period
    
    def set_tel_number(self,tel_number):
        self.tel_number = tel_number
        
    def set_lec_days(self,lec_days):
        self.lec_days = lec_days
        
    def set_time_period(self,time_period):
        self.time_period = time_period
    
    def get_tel_number(self):
        return self.tel_number
    
    def get_lec_days(self):
        return self.lec_days    
    
    def get_time_period(self):
        return self.time_period.strftime("%H:%M:%S").tolist()


                            
first_client=Client('380965217864',['Saturday','Sunday'],pd.date_range("18:00", "18:30", freq="30min"))
second_client=Client('380500397333',['Saturday','Sunday'],pd.date_range("12:00", "20:30", freq="30min"))
third_client=Client('380505878609',['Tuesday'],pd.date_range("18:00", "18:30", freq="30min"))
fourth_client=Client('380961623961',['Saturday','Sunday'],pd.date_range("17:00", "20:30", freq="30min"))
fifth_client=Client('380950858030',['Sunday'],pd.date_range("20:00", "20:30", freq="30min"))
sixth_client=Client('380930252818',['Monday','Tuesday','Wednesday','Thursday','Friday'],pd.date_range("13:14", "18:20", freq="30min"))
seventh_client=Client('380960828714',['Tuesday','Friday'],pd.date_range("09:00", "13:00", freq="30min"))
eight_client=Client('380955546535',['Sunday'],pd.date_range("18:00", "20:00", freq="30min"))
nineth_client=Client('380674867255',['Monday','Tuesday','Wednesday','Thursday','Friday'],pd.date_range("10:00", "16:30", freq="30min"))
tenth_client=Client('380976233984',['Saturday'],pd.date_range("13:00", "14:00", freq="30min"))
base={0:first_client,1:second_client,2:third_client,3:fourth_client,4:fifth_client,5:sixth_client,6:seventh_client,7:eight_client,8:nineth_client,9:tenth_client}

def set_schedule(f_client,s_client):
        f_condition=find_similars_days(f_client.get_lec_days(),s_client.get_lec_days())   
        s_condition=find_similars_hours(f_client.get_time_period(),s_client.get_time_period())
        if len(f_condition)!=0 and len(s_condition)!=0:
            schedule_clients=sc.Schedule(str(f_condition[0]),str(f_client.get_tel_number()),str(s_client.get_tel_number()),str(s_condition[0]))
            #print("Phone number of first client : "+str(f_client.get_tel_number())+" Phone number of second client : "+str(s_client.get_tel_number())+" days for practice: "+str(f_condition[0])+" hours for practice: "+str(s_condition[0]))
            scheduleString=str(f_condition[0])+'  '+str(f_client.get_tel_number())+"  "+str(s_client.get_tel_number())+'  ('+str(s_condition[0])+') |'
            return scheduleString

schStr=''
for i in range(0,len(base)-1):
    for j in range(0,len(base)-1):
        sch=set_schedule(base[i],base[j+1])
        if(sch!=None):
            schStr+=sch
            #print(sch)
list_sch=schStr.split("|")
#print(list_sch)
list_monday=[]
list_sunday=[]
list_tuesday=[]
list_saturday=[]
for i in list_sch:
    if 'Monday' in i:
        list_monday.append(i)
    elif 'Saturday' in i:
        list_saturday.append(i)
    elif 'Sunday' in i:
        list_sunday.append(i)
    elif 'Tuesday' in i:
        list_tuesday.append(i)
        
print('Monday:')
for i in list_monday:
    print(i.replace('Monday',' '))
print('Tuesday:')
for i in list_tuesday:
    print(i.replace('Tuesday',' '))  
print('Saturday:')
for i in list_saturday:
    print(i.replace('Saturday',' '))  
print('Sunday:')
for i in list_sunday:
    print(i.replace('Sunday',' '))      
        


    
     
    
#print(type(pd.date_range("11:00", "21:30", freq="30min")))
