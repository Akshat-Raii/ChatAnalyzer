# Chat Analyzer

Welcome to the **Chat Analyzer**! This tool is designed to help you analyze and visualize statistics from your chat data. It provides insights into messaging patterns, user interactions, and more, using various visualizations and metrics.

## Features

- **Upload Chat Data**: Upload chat data in text format.
- **User Analysis**: View statistics for individual users or all users combined.
- **Statistics Overview**:
  - Total Messages
  - Total Words
  - Media Shared
  - Links Shared
- **Visualizations**:
  - Monthly and Daily Timelines
  - Activity Maps (Most Busy Days and Months)
  - Word Cloud
  - Most Common Words
  - Emoji Analysis

## Hosted Version

A hosted version of the Chat Analyzer is available at: [Chat Analyzer Dashboard](https://analyzer-chat.streamlit.app/)


## How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/chat-analyzer-dashboard.git
   cd ChatAnalyzer
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/chat-analyzer-dashboard.git
   cd ChatAnalyzer
4. **Prepare Chat Data.**

5. **Run the App**
   ```bash
   streamlit run app.py
5. **Upload and Analyze**:
   - Open your web browser and go to http://localhost:8501.
   - Navigate to the "Analyze Chat" section and upload your chat file.
   - Select a user from the dropdown menu to analyze specific data or choose "Overall" to see combined statistics.
   - Click "Show Analysis" to view the generated statistics and visualizations.

- **Project Structure**:
  - app.py: Main file for running the Streamlit app
  - process.py: Script for processing chat data and creating DataFrame.
  - fetcher.py: Contains functions for fetching and analyzing chat data.
  - requirements.txt: List of Python dependencies.
  - stop_hinglish.txt: File containing stop words used for text analysis.

- **Dependencies**:
  The project requires the following Python packages:
  - streamlit
  - pandas
  - matplotlib
  - seaborn
  - wordcloud
  - urlextract
  - emoji
    
  You can install all dependencies using the provided requirements.txt file.

## Contributing

1. **Fork the repository.**
   
2. **Create a new branch:**
   ```bash
   git checkout -b feature-branch

3. **Make your changes.**
   
4. **Commit your changes:**
   ```bash
   git commit -am 'Add new feature'

5. **Push to the branch:**
   ```bash
   git push origin feature-branch

6. **Open a pull request.**:
   

