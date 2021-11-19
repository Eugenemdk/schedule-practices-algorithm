class Schedule:
    day='' 
    first_tel_number=''
    second_tel_number=''
    time_hours_lec=''
    
    def __init__(self,day,first_tel_number,second_tel,time_hours_lec):
        self.day = day
        self.first_tel_number = first_tel_number
        self.second_tel=second_tel
        self.time_hours_lec = time_hours_lec
    
    def set_day(self,day):
        self.day = day
        
    def set_first_tel_number(self,first_tel_number):
        self.first_tel_number = first_tel_number
        
    def set_second_tel_number(self,second_tel_number):
        self.second_tel_number = second_tel_number
    
    def set_time_hours_lec(self,time_hours_lec):
        self.time_hours_lec = time_hours_lec
        
    def get_day(self):
        return self.day    
    def get_first_tel_number(self):
        return self.first_tel_number
    def get_second_tel_number(self):
        return self.second_tel_number
    def get_time_hours_lec(self):
        return self.time_hours_lec  
