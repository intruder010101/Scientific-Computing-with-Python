def add_time(start_time, duration, day=""):
    time = start_time.split()[0]
    AM_PM = start_time.split()[1]
    st_hours = int(time.split(":")[0])
    st_minutes = int(time.split(":")[1])
    
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])
    
    total_minutes = (st_hours + duration_hours)*60 + st_minutes + duration_minutes 
    hoursfromtotal = int(total_minutes/60)
    left_minutes = total_minutes%60
    
    if hoursfromtotal%12: end_time_hours = hoursfromtotal%12 
    else: end_time_hours = 12
    if left_minutes < 10: end_time_minutes = "0" + str(left_minutes)
    else: end_time_minutes = left_minutes
    
    if AM_PM == "AM":
        n = int(hoursfromtotal/24) #n_days_later
        if st_hours != 12:
            if (int(hoursfromtotal/12) %2) == 0: end_AM_PM = " AM"
            else: end_AM_PM = " PM"
        else:
            if (int((hoursfromtotal-12)/12) %2) == 0: end_AM_PM = " AM"
            else: end_AM_PM = " PM"
    else:
        if st_hours != 12:
            n = int((hoursfromtotal+12)/24)
            if (int(hoursfromtotal/12) %2) == 0: end_AM_PM = " PM"
            else: end_AM_PM = " AM"
        else:
            n = int((hoursfromtotal)/24)
            if (int((hoursfromtotal-12)/12) % 2) == 0: end_AM_PM = " PM"
            else: end_AM_PM = " AM"
    
    if n == 0: 
        n_days = ""
    elif n == 1:
        n_days = "(next day)"
    else:
        n_days = "({} days later)".format(n)
    
    if day != "":
        days = {1:"Monday", 2:"Tuesday", 3:"Thursday", 4:"Wednesday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
        day_lowercase = day.lower()
        day = day[0].upper() + day_lowercase[1:]
        for key,value in days.items():
            if value == day:
                new_day_value = (key + n) % 7
                day = days.get(new_day_value)       
                break
        string_for_print = str(end_time_hours) + ":" + str(end_time_minutes) + end_AM_PM + ", " + day + " " + n_days + " " 
        return string_for_print
    
    string_for_print = str(end_time_hours) + ":" + str(end_time_minutes) + end_AM_PM + " " + n_days + " "
    return string_for_print 

          

#main
start_time = input("Start time: ")
duration = input("Duration: ")
print(add_time(start_time, duration, "mOnDaY"))

