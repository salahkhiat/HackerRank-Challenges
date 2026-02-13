def timeConversion(s: str):

    pm_time = {
        '12':'12',
        '01':'13',
        '02':'14',
        '03':'15',
        '04':'16',
        '05':'17',
        '06':'18',
        '07':'19',
        '08':'20',
        '09':'21',
        '10':'22',
        '11':'23',
    }
    if s[-2:].lower() == "pm":
        return f"{pm_time[s[:2]]}{s[2:8]}" 
    
    elif s[-2:].lower() == "am" and s[:2] == "12":
        return f"00{s[2:8]}" 
    
    else :
        return s[:8]

t1 = "11:15:00PM"
t2 = "12:45:00PM"
print(timeConversion(t1))
print(timeConversion(t2))

