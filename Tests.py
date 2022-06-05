import Transformer
import SentimentAnalysis

def callTests():
    # text tokenization
    sentence = "Alicia has a cat. A cat has got Alicia"
    tr = Transformer.transformers()
    print(tr.tokenize_many_texts(sentence))
    #   sentiment analysis
    classSentObject = SentimentAnalysis.sentimentAnalysis("The platform provides universal access to the world's best education, partnering with top universities and organizations to offer courses online. Fraud shall not take place. Universities enjoy it it.")
    print("zero")
    classSentObject.frequencyDistribution(3)
    print("one")
    classSentObject.analyzeSentiment_PatternAnalyzer()
    print("two")
    classSentObject.analyzePolarity_PatternAnalyzer()
    print("three")
    classSentObject.analyzePolarity_NaiveBayesAnalyzer()
    print("four")
    classSentObject.analyzeSentiment_NaiveBayesAnalyzer()
    print("five")
    classSentObject.frequencyDistribution(3)
    print("six")
    classSentObject.concordanceList("fraud")
    print("seven")
    classSentObject.NLTKSentiment()