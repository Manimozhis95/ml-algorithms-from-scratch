import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding='latin-1')
    return df

ps = PorterStemmer()


stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text=str(text)
    text = text.lower()#lowercase
    text = re.sub(r"http\S+", "", text)#remove url
    text = re.sub(r"\d+", "", text)#remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))#remove punctuation

    words = text.split()#tokenize
    words = [word for word in words if word not in stop_words]  
    words = [ps.stem(word) for word in words]

    return " ".join(words)



def process_pipeline(file_path):
    df = load_data(file_path)
    
    #df = apply_preprocessing(df)
    return df