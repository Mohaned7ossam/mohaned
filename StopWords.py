import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  
    
    words = re.findall(r'\b\w+\b', text)
    
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    
    word_freq = Counter(filtered_words)
    
    return word_freq

def print_frequency_table(word_freq):
    max_word_length = max(len(word) for word in word_freq.keys())  # Find the length of the longest word
    print("Word".ljust(max_word_length + 5), "Frequency")  # Adjust spacing for the word column
    print("-" * (max_word_length + 15))  # Adjust the line length
    for word, freq in word_freq.items():
        print(word.ljust(max_word_length + 5), freq)  # Adjust spacing for the word column

file_path = './paragraphs.txt'

word_freq = process_text(file_path)

print_frequency_table(word_freq)
