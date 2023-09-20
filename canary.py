import tkinter as tk
from tkinter import ttk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def create_gui():
    root = tk.Tk()
    root.title("Sentiment Analysis Tool")

    style = ttk.Style()
    style.configure("TButton", padding=6, font=("Arial", 12))
    style.configure("TLabel", padding=6, font=("Arial", 12))

    text_entry = create_text_entry(root)
    analyze_button = create_analyze_button(root, text_entry)
    create_clear_button(root, text_entry)
    result_label = create_result_label(root)
    score_label = create_score_label(root)
    create_sentiment_detail_labels(root, result_label, score_label)

    text_entry.bind("<KeyRelease>", lambda event: analyze_sentiment(event, text_entry, result_label, score_label))

    root.mainloop()

def create_text_entry(root):
    text_entry = tk.Text(root, height=5, width=40)
    text_entry.pack()
    return text_entry

def create_analyze_button(root, text_entry):
    analyze_button = ttk.Button(root, text="Analyze Sentiment", command=lambda: analyze_sentiment(None, text_entry))
    analyze_button.pack()
    return analyze_button

def create_clear_button(root, text_entry):
    def clear_text():
        text_entry.delete("1.0", "end")

    clear_button = ttk.Button(root, text="Clear Text", command=clear_text)
    clear_button.pack()
    return clear_button

def create_result_label(root):
    result_label = ttk.Label(root, text="", font=("Arial", 12))
    result_label.pack()
    return result_label

def create_score_label(root):
    score_label = ttk.Label(root, text="", font=("Arial", 12))
    score_label.pack()
    return score_label

def create_sentiment_detail_labels(root, result_label, score_label):
    global positive_label, negative_label, neutral_label
    positive_label = ttk.Label(root, text="", font=("Arial", 12))
    positive_label.pack()
    
    negative_label = ttk.Label(root, text="", font=("Arial", 12))
    negative_label.pack()
    
    neutral_label = ttk.Label(root, text="", font=("Arial", 12))
    neutral_label.pack()

def analyze_sentiment(event, text_entry, result_label, score_label):
    text = text_entry.get("1.0", "end-1c")
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)

    compound_score = sentiment_scores['compound']
    sentiment_label = get_sentiment_label(compound_score)

    result_label.config(text=f"Sentiment: {sentiment_label}")
    score_label.config(text=f"Compound Score: {compound_score:.2f}")

    positive_label.config(text=f"Positive: {sentiment_scores['pos']:.2f}")
    negative_label.config(text=f"Negative: {sentiment_scores['neg']:.2f}")
    neutral_label.config(text=f"Neutral: {sentiment_scores['neu']:.2f}")

def get_sentiment_label(compound_score):
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    create_gui()
