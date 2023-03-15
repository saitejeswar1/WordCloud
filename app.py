import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import regex as re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


st.title('WordCloud Streamlit App')

st.markdown("""
This app performs Word Cloud
* **Python libraries:** streamlit, pandas, BeautifulSoup, wordcloud ......
* **Need to cantact: ** [Sai Tejeswar](https://github.com/saitejeswar1).
""")

st.set_option('deprecation.showPyplotGlobalUse', False)
#file_bytes = st.file_uploader("Upload a file", type="csv")

#if file_bytes is not None:
st.sidebar.header("Select Link") # change the links below with your own websites
links = ["https://annabyang.medium.com/whats-going-on-the-silicon-valley-bank-collapse-vs-the-2008-financial-crisis-8b5539995e63",
        "https://annabyang.medium.com/why-writers-should-care-about-ai-art-b859192776c9",
        "https://thisisyouth.medium.com/chatgpt-wont-kill-writing-but-it-will-kill-content-d3d2fe3af3cd",
        "https://towardsdatascience.com/a-decade-of-knowledge-graphs-in-natural-language-processing-5fdb15abc2b3",
        "https://towardsdatascience.com/beautifully-illustrated-nlp-models-from-rnn-to-transformer-80d69faf2109"]
URL = st.sidebar.selectbox('Link', links)
st.sidebar.header("Select No.of words you want to display")
words = st.sidebar.selectbox("No.of Words", range(10,1000,10))
if URL is not None:
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('div', attrs = {'id':'main-content'})
    text = table.text
    cleaned_text = re.sub('\t', "", text)
    cleaned_texts = re.split('\n', cleaned_text)
    cleaned_textss = "".join(cleaned_texts)
    #st.write(cleaned_textss)
    st.write("Word Cloud Plot")
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(background_color="white", max_words=words,
                          stopwords=stopwords).generate(cleaned_textss)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()



