import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def remove_html(self, text: str) -> str:
        return re.sub(r"<.*?>", " ", text)

    def remove_urls(self, text: str) -> str:
        return re.sub(r"http\S+|www\S+", " ", text)

    def remove_emails(self, text: str) -> str:
        return re.sub(r"\S+@\S+", " ", text)

    def remove_special_characters(self, text: str) -> str:
        return re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    def normalize_whitespace(self, text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()

    def preprocess(self, text: str) -> str:
        if not isinstance(text, str):
            return "[EMPTY]"

        text = text.lower()
        text = self.remove_html(text)
        text = self.remove_urls(text)
        text = self.remove_emails(text)
        text = self.remove_special_characters(text)
        text = self.normalize_whitespace(text)

        tokens = text.split()

        tokens = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
            if word not in self.stop_words and len(word) > 2
        ]

        processed_text = " ".join(tokens)

        if processed_text == "":
            return "[EMPTY]"

        return processed_text