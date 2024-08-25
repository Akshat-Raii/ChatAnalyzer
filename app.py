import streamlit as st
import process,fetcher
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Chat Analyzer",
    page_icon="Images\graph.png",  
)


st.sidebar.title("Dashboard")
app_mode=st.sidebar.selectbox("Select Page",["Home","Analyze Chat"])

if(app_mode=="Home"):
    st.title("Chat Analyzer")
    st.header("Welcome to the Chat Analyzer Dashboard!")
    image_path="Images/496fcdd0116e93963c9737c16662e204.gif"
    st.image(image_path,use_column_width=True) 
    

    st.markdown("""
    **Chat Analyzer** is your go-to tool for analyzing and visualizing chat data. This app helps you gain insights into your messaging patterns, user interactions, and more. Here’s how you can make the most out of it:

    ## Features
    - **Upload Your Chat Data**: Upload a chat file in text format to start analyzing.
    - **User-Specific Analysis**: Select any user or view statistics for all users combined.
    - **Comprehensive Statistics**:
        - Total Messages
        - Word Count
        - Media and Links Shared
    - **Visualizations**:
        - Monthly and Daily Timelines: Track messaging activity over time.
        - Activity Maps: Identify the busiest days and months.
        - Word Cloud: See the most frequently used words.
        - Common Words: Detailed breakdown of frequent words and their occurrences.
        - Emoji Analysis: Understand emoji usage patterns.

    ## How to Use the App

    1. **Upload Your Chat Data**:
       - Go to the "Analyze Chat" section from the sidebar.
       - Click on "Upload your Chat" to select and upload your chat file.

    2. **Select a User**:
       - After uploading, choose a user from the dropdown list. To analyze all users combined, select "Overall".

    3. **View Analysis**:
       - Click "Show Analysis" to generate and display various statistics and visualizations.

    4. **Explore Visualizations**:
       - **Timelines**: View daily and monthly messaging patterns.
       - **Activity Maps**: Discover the most active days and months.
       - **Word Cloud**: Explore frequently used words visually.
       - **Common Words**: Examine a list of common words and their frequencies.
       - **Emoji Analysis**: Review the most used emojis in the chat.

    """)


elif(app_mode=="Analyze Chat"):
    uploaded_file=st.sidebar.file_uploader("Upload your Chat")
    if uploaded_file is not None:
        with st.spinner('Processing file... Please wait.'):
            bytes_data = uploaded_file.getvalue()
            data = bytes_data.decode("utf-8")
            df = process.process(data)

        

        # Getting names of all users
        usernames=df["Users"].unique().tolist()
        usernames.remove("Group Notification")
        usernames.sort()
        usernames.insert(0,"Overall")
        selected_user=st.sidebar.selectbox("Show analysis of",usernames)
        if st.sidebar.button("Show Analysis"):
            st.title("Chat Statistics")
            totalMessages,words,media,urls=fetcher.fetch_status(selected_user,df)
            col1,col2,col3,col4=st.columns(4)
            with col1:
                st.header("Total Messages")
                st.title(totalMessages)

            with col2:
                st.header("Total Words")
                st.title(words)
            
            with col3:
                st.header("Media Shared")
                st.title(media)

            with col4:
                st.header("Links Shared")
                st.title(urls)

            st.title("Monthly Timeline")
           
            timeline=fetcher.monthly_timeline(selected_user,df)
            fig,ax=plt.subplots()
            plt.plot(timeline["time"],timeline["Message"],color="black")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

            st.title("Daily Timeline")
            daily_timeline=fetcher.daily_timeline(selected_user,df)
            fig,ax=plt.subplots()
            ax.plot(daily_timeline["date"],daily_timeline["Message"],color="black")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

            st.title("Activity Map")
            col1,col2=st.columns(2)
            with col1:
                st.header("Most Busy Days")
                busy_day=fetcher.week_activity(selected_user,df)
                fig,ax=plt.subplots()
                ax.bar(busy_day.index,busy_day.values,color="orange")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)

            with col2:
                st.header("Most Busy Months")
                busy_month=fetcher.month_activity(selected_user,df)
                fig,ax=plt.subplots()
                ax.bar(busy_month.index,busy_month.values,color="orange")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)

            st.title("Weekly Activity Map")
            user_map=fetcher.activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax=sns.heatmap(user_map)
            st.pyplot(fig)
            # Finding the most frequent users
            if selected_user=="Overall":
                st.title("Most Frequent Users")
                freq,new_df=fetcher.most_frequent_users(df)
                fig,ax=plt.subplots()
                
                
                col1,col2=st.columns(2)

                with col1:
                    ax.barh(freq.index,freq.values,color="aqua")
                    plt.xticks(rotation="vertical")
                    st.pyplot(fig)
                
                with col2:
                    st.dataframe(new_df)

            st.title("Word Cloud")
            df_wc=fetcher.create_wordcloud(selected_user,df)
            fig,ax=plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)


            st.title("Most Common Words")
            col1,col2=st.columns(2)
            most_common_df=fetcher.most_common_words(selected_user,df)
            
            with col1:
                most_common_df=most_common_df.rename(columns={0:"Words",1:"Frequency"})
                st.dataframe(most_common_df)

            with col2:
                fig,ax=plt.subplots()
                ax.barh(most_common_df["Words"],most_common_df["Frequency"])
                st.pyplot(fig)
                plt.xticks(rotation="vertical")

            st.title("Emoji Analysis")
            col1,col2=st.columns(2)
            emoji_df=fetcher.numEmoji(selected_user,df)
            
            st.dataframe(emoji_df)

            
            


        
