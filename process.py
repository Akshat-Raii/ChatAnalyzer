import re
import pandas as pd
def process(data):
    pattern='\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages=re.split(pattern,data)[1:]
    dates=re.findall(pattern,data)
    df=pd.DataFrame({"Messages": messages, "Dates": dates})
    df["Dates"]=pd.to_datetime(df["Dates"], format="%d/%m/%y, %H:%M - ")
    users=[]
    messages=[]
    for message in df["Messages"]:
        entry=re.split("([\w\W]+?):\s",message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append("Group Notification")
            messages.append(entry[0])

    df["Users"]=users
    df["Message"]=messages
    df.drop(columns=["Messages"],inplace=True)
    df["date"]=df["Dates"].dt.date
    df["day"]=df["Dates"].dt.day_name()
    df["Year"]=df["Dates"].dt.year
    df["Year"] = df["Year"].astype(str).str.replace(',', '', regex=False)
    df["month_num"]=df["Dates"].dt.month
    df["Month"]=df["Dates"].dt.month_name()
    df["Day"]=df["Dates"].dt.day
    df["Hour"]=df["Dates"].dt.hour
    df["Minute"]=df["Dates"].dt.minute
    period = []
    for hour in df[["day","Hour"]]["Hour"]:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df

