import transformers
import basicSentimentAnalysis

class Tests:


    def __init__(self):
        # text tokenization
        self.sentence2 = "I am really concerned about Bitcoin prices. There is a lot of decreases in the market, investors do not seem to believe that it can maintain its value. Market prices crashed."
        self.sentence2 = "I hate Russia for what they did to Ukraine. I wish it was president Putin's children who died in this war. I can now see how Adolf Hitler raised to power and how he misused this power. Thousands of innocent people die because of his imperialistic ambitions."
        self.sentence = "Ukraine is fighting for survival. They managed to defend their country against stronger occupant for more than 3 months. Whole Europe supports Ukraine in their fight for freedom."
        self.listOfWords = ['company', 'court', 'lawsuit', 'fraud', 'suspicion', 'police', 'investigation']
        self.mainCatalog = 'd:/Crawler'
        self.dictionaryOfFirmNamesWithTickers = {"Tesla": ["TSLA", "Musk", "Elon Musk"], "Apple": ["AAPL", "Steve Jobs"],
                                            "Amazon": ["AMZN", "Jeff Besos"], "Meta": ["META"], "Toyota": ["TM"]}
        self.listOfDirectories = ["d:/Crawler/Amazon/", "d:/Crawler/Tesla/"]

        self.tr = transformers.transformers(self.mainCatalog, self.dictionaryOfFirmNamesWithTickers, threshold=3)
        self.bs = basicSentimentAnalysis.basicSentimentAnalysis(self.listOfDirectories, self.mainCatalog, self.dictionaryOfFirmNamesWithTickers, threshold=3)

    def callTests(self):
        print(self.tr.tokenize_many_texts(self.sentence))
        #   sentiment analysis
        self.bs.frequencyDistribution(3, self.sentence)
        print("one")
        self.bs.analyzeSentiment_PatternAnalyzer(self.sentence)
        print("two")
        self.bs.analyzePolarity_PatternAnalyzer(self.sentence)
        print("three")
        self.bs.analyzePolarity_NaiveBayesAnalyzer(self.sentence)
        print("four")
        self.bs.analyzeSentiment_NaiveBayesAnalyzer(self.sentence)
        print("five")
        self.bs.frequencyDistribution(3, self.sentence)
        print("six")
        self.bs.concordanceList("fraud", self.sentence)
        print("seven")
        self.bs.NLTKSentiment(self.sentence)