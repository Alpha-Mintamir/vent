# Vent Here Dataset - Emotion and Sentiment Analysis

## Overview

This dataset contains sentiment and emotion analysis results of venting content scraped from the Ethiopian-based Telegram channel [Vent Here](https://t.me/vent_here). The dataset provides insight into the emotional expressions and sentiments of users in the channel. The text data has been processed and analyzed using state-of-the-art NLP techniques to extract emotion and sentiment labels.

## Dataset Details

- **Source**: The data was scraped from the Telegram channel [Vent Here](https://t.me/vent_here), a community space where users express their feelings and emotions.
- **Cleaning Process**: The raw data was pre-processed by:
    - Removing emojis
    - Removing text prefixes
    - Filtering out non-English language columns to focus on English text

## Columns

- **date**: The timestamp when the venting content was posted.
- **text**: The cleaned vent text content.
- **emotion_label**: The predicted emotion label for each vent based on a RoBERTa-based emotion classification model.
- **sentiment_label**: The sentiment label (positive, negative, neutral) predicted using a sentiment analysis pipeline.
- **sentiment_score**: The sentiment score, ranging from -1 (negative) to 1 (positive), based on sentiment analysis.

## Sentiment Analysis

The sentiment for each row was extracted using the Hugging Face `pipeline` for sentiment analysis:

```python
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis", truncation=True)
```

## Emotion Analysis

The emotion for each vent text was extracted using a RoBERTa-based model trained to predict various emotional labels from the text. This model categorizes text into different emotions such as joy, sadness, anger, and more.

## Example Data

| date        | text                                   | emotion_label | sentiment_label | sentiment_score |
|-------------|----------------------------------------|---------------|-----------------|-----------------|
| 2024-12-01  | "I'm feeling so overwhelmed lately"    | sadness       | negative        | -0.85           |
| 2024-12-02  | "I just had a great day with friends!" | happiness     | positive        | 0.92            |

## How to Use

Download the dataset from Kaggle.

Load the dataset into a Pandas DataFrame for analysis:

```python
import pandas as pd
df = pd.read_csv('Vent Dataset with emotion and sentiment.csv')
```

Explore the dataset and use it for your research or projects related to sentiment analysis, emotion classification, or natural language processing.

## Repository

For more information on the process of scraping, cleaning, and analyzing the data, you can check out the GitHub repository.

## License

This dataset is provided for research and educational purposes. Please ensure that you comply with the terms of service of Telegram and respect user privacy when using or sharing this dataset. The dataset is not intended for commercial use without proper authorization.

## Acknowledgements

Thanks to the creators and contributors of the Telegram channel Vent Here for their participation in the community, which made this dataset possible. The sentiment and emotion models used in this project are based on pre-trained models from Hugging Face and RoBERTa.

### Key Changes for Kaggle

- Added a section about how users can load and use the dataset, tailored to a Kaggle audience.
- The "License" section encourages proper use while keeping the dataset research-friendly.
- Included a note on the repository link for those who want to understand the scraping process in detail.

This version should fit well in Kaggle’s dataset section!