from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import nltk
nltk.download('punkt')
import Transformer


class sentimentAnalysis:
    def __init__(self, text):
        self.text = text

        #polarity [-1;1] where -1 very negative, 1 very positive
        #subjectivity [0.0, 1.0] where 0 is objective sentence and 1 is subjective sentence



    def analyzeSentiment_PatternAnalyzer(self):
        analysis = TextBlob(self.text).sentiment
        print(analysis)
        return analysis

    def analyzePolarity_PatternAnalyzer(self):
        analysisPol = TextBlob(self.text).polarity
        analysisSub = TextBlob(self.text).subjectivity
        print(analysisPol)
        print(analysisSub)
        return (analysisPol, analysisSub)

    def analyzeSentiment_NaiveBayesAnalyzer(self):
        # Applying the NaiveBayesAnalyzer
        # Running sentiment analysis
        analysisPol = TextBlob(self.text, analyzer=NaiveBayesAnalyzer()).polarity
        analysisSub = TextBlob(self.text, analyzer=NaiveBayesAnalyzer()).subjectivity
        print("Sentiment(polarity=", analysisPol, ", subjectivity=",analysisSub,")")
        return("Sentiment(polarity=",analysisPol, ", subjectivity=",analysisSub,")")


    def analyzePolarity_NaiveBayesAnalyzer(self):
        analysisPol = TextBlob(self.text, analyzer=NaiveBayesAnalyzer()).polarity
        analysisSub = TextBlob(self.text, analyzer=NaiveBayesAnalyzer()).subjectivity
        print(analysisPol)
        print(analysisSub)
        return (analysisPol, analysisSub)

    def frequencyDistribution(self, number):
        tr = Transformer.transformers()
        t = tr.tokenize_many_texts(self.text)
        text = [word.lower() for word in t]
        text = [word for word in text if word.isalpha()]
        fd = nltk.FreqDist(text)
        print(fd.most_common(number))
        return fd.most_common(number)

    def concordanceList(self, word):
        text = nltk.Text(self.text)
        concordance_list = text.concordance_list(word, lines = 2)
        for entry in concordance_list:
            print(entry.line)

    def NLTKSentiment(self):
        from nltk.sentiment import SentimentIntensityAnalyzer
        nltk.download('vader_lexicon')
        sia = SentimentIntensityAnalyzer()
        results = sia.polarity_scores(self.text)
        print(results)
        return results

    #continue from this webpage https://realpython.com/python-nltk-sentiment-analysis/
    # TODO: freqanalysis of good an bad words separately
