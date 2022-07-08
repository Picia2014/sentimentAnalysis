# https://realpython.com/python-nltk-sentiment-analysis/#customizing-nltks-sentiment-analysis
# dictionaries for finance are described here https://termcoord.eu/2016/01/can-we-analyse-sentiments-within-financial-terminology/


import nltk
import transformers


# klasa tokenizuje tekst filtruje tekst i usuwa słowa nieistotne dla analizy tekstu
# klasa usuwa także zakończenia słów aby zostały trzony słów
# liczy słowa pozytywne i negatywne
# korzysta z biblioteki nltk

class customarySentimentAnalysis:

    def __init__(self, listOfDirectories):
        self.tr = transformers.transformers()
        self.listOfDirectories = listOfDirectories
        #polarity [-1;1] where -1 very negative, 1 very positive
        #subjectivity [0.0, 1.0] where 0 is objective sentence and 1 is subjective sentence
        self.unwanted = nltk.corpus.stopwords.words("english")
        self.unwanted.extend([w.lower() for w in nltk.corpus.names.words()])


    def skip_unwanted(pos_tuple):
        word, tag = pos_tuple
        if not word.isalpha() or word in unwanted:
            return False

        if tag.startswith("NN"):
            return False
        return True


        positive_words = [word for word, tag in filter(skip_unwanted, nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=["pos"])))]
        negative_words = [word for word, tag in filter( skip_unwanted, nltk.pos_tag(nltk.corpus.movie_reviews.words(categories=["neg"])))]
        positive_fd = nltk.FreqDist(positive_words)
        negative_fd = nltk.FreqDist(negative_words)

        common_set = set(positive_fd).intersection(negative_fd)

        for word in common_set:
            del positive_fd[word]
            del negative_fd[word]

        top_100_positive = {word for word, count in positive_fd.most_common(100)}
        top_100_negative = {word for word, count in negative_fd.most_common(100)}


        unwanted = nltk.corpus.stopwords.words("english")
        unwanted.extend([w.lower() for w in nltk.corpus.names.words()])

        positive_bigram_finder = nltk.collocations.BigramCollocationFinder.from_words([
        w for w in nltk.corpus.movie_reviews.words(categories=["pos"])
        if w.isalpha() and w not in unwanted
        ])

        negative_bigram_finder = nltk.collocations.BigramCollocationFinder.from_words([
            w for w in nltk.corpus.movie_reviews.words(categories=["neg"])
            if w.isalpha() and w not in unwanted
        ])


    def extract_features(text):
        features = dict()
        wordcount = 0
        compound_scores = list()
        positive_scores = list()

        for sentence in nltk.sent_tokenize(text):
            for word in nltk.word_tokenize(sentence):
                if word.lower() in top_100_positive:
                    wordcount += 1
            compound_scores.append(sia.polarity_scores(sentence)["compound"])
            positive_scores.append(sia.polarity_scores(sentence)["pos"])

        # Adding 1 to the final compound score to always have positive numbers
        # since some classifiers you'll use later don't work with negative numbers.
        features["mean_compound"] = mean(compound_scores) + 1
        features["mean_positive"] = mean(positive_scores)
        features["wordcount"] = wordcount

        return features

    features = [
        (extract_features(nltk.corpus.movie_reviews.raw(review)), "pos")
        for review in nltk.corpus.movie_reviews.fileids(categories=["pos"])
    ]

    features.extend([
        (extract_features(nltk.corpus.movie_reviews.raw(review)), "neg")
        for review in nltk.corpus.movie_reviews.fileids(categories=["neg"])
    ])


