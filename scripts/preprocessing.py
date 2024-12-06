import re
import nltk
import pandas as pd
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

import emoji

def remove_emojis(df, text_column):
    def remove_emojis_from_text(text):
        if not isinstance(text, str):
            return text
        return emoji.replace_emoji(text, replace='')

    # Apply the function to the specified column
    df[text_column] = df[text_column].apply(remove_emojis_from_text)
    return df






def process_text(input_text):
    second_newline_index = input_text.find('\n', input_text.find('\n') + 1)
    if second_newline_index != -1:
        return input_text[second_newline_index + 1:]
    return input_text


def remove_non_english_rows(df, text_column):
    DetectorFactory.seed = 0  

    def is_mostly_english(text):
        if not isinstance(text, str): 
            return False
        try:
            return detect(text) == 'en'
        except LangDetectException:
            return False

    # Drop NaN values in the text column and convert non-strings to strings
    df[text_column] = df[text_column].fillna("").astype(str)

    # Filter rows where the text is predominantly English
    df = df[df[text_column].apply(is_mostly_english)]
    return df
    
