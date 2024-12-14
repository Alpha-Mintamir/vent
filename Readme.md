# Data Preprocessing Scripts

This repository contains scripts for cleaning and preprocessing text data, including removing emojis, processing text to remove specific content, and filtering out non-English entries.

## Files

- `preprocessing.py`: Functions for text cleaning and preprocessing.
- `pre-processing.ipynb`: A Jupyter Notebook demonstrating how to use the preprocessing functions on a dataset.
- `data/`: A directory containing sample data files for testing the preprocessing functions.
- `emotion_feature.ipynb`: A Jupyter Notebook demonstrating how to extract emotion features from text data.
- `sentiment_feature.ipynb`: A Jupyter Notebook demonstrating how to extract sentiment features from text data.
- `vent_analysis.ipynb`: A Jupyter Notebook demonstrating how to perform vent analysis on text data.

## Features

- **Emoji Removal**: Clean text data by removing emojis.
- **Text Processing**: Modify text by removing unwanted sections.
- **Language Filtering**: Detect and remove non-English text entries.

## Usage

1. **Import the Functions**: Import the required functions from `preprocessing.py`.

2. **Load Your Data**: Read your dataset into a pandas DataFrame.

3. **Apply Preprocessing**:
    - Remove emojis from your text data.
    - Process the text to remove specific sentences or patterns.
    - Filter out non-English text entries.

4. **Save the Cleaned Data**: Export the processed DataFrame to a new file.

## Requirements

- Python 3.6 or higher
- pandas
- emoji
- langdetect

Install the required packages using:

```bash
pip install pandas emoji langdetect
```

## License

This project is licensed under the MIT License.