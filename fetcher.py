from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji


extractor=URLExtract()
def fetch_status(selected_user,df):
    if selected_user!="Overall":
        df=df[df["Users"]==selected_user]
    numMessages=df.shape[0]
    words=[]
    for message in df["Message"]:
        words.extend(message.split())
    media=df[df["Message"]=="<Media omitted>\n"].shape[0]
    urls=[]
    for message in df["Message"]:
        urls.extend(extractor.find_urls(message))
    return numMessages,len(words),media,len(urls)

def most_frequent_users(df):
    freq=df["Users"].value_counts().head()
    df=round((df["Users"].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={"Users":"Name","count":"Percent"})
    return freq,df

def create_wordcloud(selected_user,df):
    f=open("stop_hinglish.txt","r")
    stop_words=f.read()                       
    if selected_user!="Overall":
        df=df[df["Users"]==selected_user]

    word_df=df[df["Users"]!="Group Notification"]
    word_df=word_df[word_df["Message"]!="<Media omitted>\n"]
    def remove_stop_words(message):
        y=[]
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    wc=WordCloud(width=500,height=500,min_font_size=10,background_color="white")
    word_df["Message"]=word_df["Message"].apply(remove_stop_words)
    df_wc=wc.generate(word_df["Message"].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    f=open("stop_hinglish.txt","r")
    stop_words=f.read()
    if selected_user!="Overall":
        df=df[df["Users"]==selected_user]
    new_df=df[df["Users"]!="Group Notification"]
    new_df=new_df[new_df["Message"]!="<Media omitted>\n"]

    words=[]
    for message in new_df["Message"]:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    
    most_common_df=pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def numEmoji(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
        
    emojis = []
    
    for message in df["Message"]:
        emojis.extend([char for char in message if char in emoji.EMOJI_DATA])
    
    emoji_df = pd.DataFrame(Counter(emojis).most_common(), columns=['Emoji', 'Count'])
    return emoji_df

def monthly_timeline(selected_user,df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    
    timeline=df.groupby(["Year","month_num","Month"]).count()["Message"].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline["Month"][i]+"-"+str(timeline["Year"][i]))
    
    timeline["time"]=time
    
    return timeline

def daily_timeline(selected_user,df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    df["date"]=df["Dates"].dt.date
    daily_timeline=df.groupby("date").count()["Message"].reset_index()
    return daily_timeline

def week_activity(selected_user,df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    
    return df["day"].value_counts()

def month_activity(selected_user,df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]

    return df["Month"].value_counts()

def activity_map(selected_user,df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    
    user_map=df.pivot_table(index="day",columns="period",values="Message",aggfunc="count").fillna(0)
    return user_map
