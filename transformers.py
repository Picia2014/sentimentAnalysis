from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk
#from nltk.corpus import stopwords
import pandas as pd
import os
import traceback

class transformers:

    # klasa przetwarza pliki w katalogu
    # klasa także usuwa komunikaty z niewystarczającą liczbą powtórzeń dla danej spółki

    def __init__(self, mainCatalog, dictionaryOfFirmNamesWithTickers, threshold):
        self.mainCatalog = mainCatalog
        self.dictionaryOfFirmNamesWithTickers = dictionaryOfFirmNamesWithTickers
        self.threshold = threshold


    def iterateOverMainFolderAndRemoveTextsWithNotEnoughReferencesToACompany(self):
        for root, subdirectories, files in os.walk(self.mainCatalog):
            for subdirectory in subdirectories:
                print("subdirectory", subdirectory, "--------------------------------------------------------")
                key = subdirectory
                synonyms = self.dictionaryOfFirmNamesWithTickers[subdirectory]
                print("subdirectory", subdirectory, "key", key, "synonyms", synonyms)
                subdirectoryFullAddress = os.path.join(root, subdirectory)
                self.__applyRemovalMethodOtoAllFilesInASubfolder(subdirectoryFullAddress, key, synonyms)


    # def __matchSubfolderWithKey(self, key):
        ##finds the subfolder inside mainCatalog which has the same name as a company we look for
        # for root, subdirectories, files in os.walk(self.mainCatalog):
        #     for subdirectory in subdirectories:
        #         if subdirectory.lower()==key.lower():
        #             return os.path.join(root, subdirectory)

    def __applyRemovalMethodOtoAllFilesInASubfolder(self, subdirectory, key, synonyms):
        ##takes a method and applies to all files
        ##intention is to apply check whether file contains more than 2 occurrences of company name or synonyms
        ## if not, method deletes the file
        for root, subdirectories, files in os.walk(subdirectory):
            for file in files:
                fileFullAddress = os.path.join(root, file)
                print("fileFullAddress", fileFullAddress)
                self.__removeFileIfLowNumberOfCompanyWords(fileFullAddress, key, synonyms)

    def __removeFileIfLowNumberOfCompanyWords(self, fileFullAddress, key, synonyms):
        #threshold defines how many occurrences of key words must be to keep the file
        ##function returns True/False about removal of the file
        occurrences = 0
        try:
            file = open(fileFullAddress, "r")
            text = file.read()
            occurrences = text.count(key)
            print("key occurrences", key, occurrences)
            for synonym in synonyms:
                occurrences = occurrences + text.count(synonym)
            print("synonyms occurrences", synonyms, occurrences-text.count(key))
            file.close()
            if occurrences < self.threshold:
                print(key, synonyms, occurrences)
                print("file to be removed:", file)
                #os.remove(file)
                return True
        except: traceback.print_exc()
        return False

    def joinManyTextsFromSubfolder(self, subfolder):
        text = ""
        import glob
        for filename in glob.iglob(subfolder, recursive=True):
            if filename.endswith(".txt"):
                try:
                    with open(filename) as f:
                        contents = f.read()
                        f.close()
                    text = text + contents
                    continue
                except:
                    pass
            else:
                continue
        return text

    def tokenize_one_text(self, text):
        stopwords = nltk.corpus.stopwords.words("english")
        #tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
        from nltk.tokenize import word_tokenize
        text_tokens = word_tokenize(text)
        text_tokens = [word.lower() for word in text_tokens if word.isalpha()]
        tokens_without_sw = [word for word in text_tokens if not word in stopwords]
        print(tokens_without_sw)
        # very good description how to remove stop words is here https://stackabuse.com/removing-stop-words-from-strings-in-python/
        return tokens_without_sw


    def tokenize_many_texts(self, allTextsToBeTransformed):
        result = []
        if type(allTextsToBeTransformed) == str:
            return self.tokenize_one_text(allTextsToBeTransformed)
        else:
            allTextsToBeTransformed = list(allTextsToBeTransformed)
            for text in allTextsToBeTransformed:
                result.append(self.tokenize_one_text(text))
            return result

    def countVectorize(self, corpus):
        # creates a list of words and counts in every string how many words of each element from the list there is there
        vectorizer = CountVectorizer(lowercase = True)
        count_matrix = vectorizer.fit_transform(corpus)
        count_array = count_matrix.toarray()
        df = pd.DataFrame(data=count_array, columns=vectorizer.get_feature_names())
        print(df)
        return df


    def tfidfVectorize(self, corpus):
        vectorizer = TfidfVectorizer(lowercase=True)
        vectorizer = vectorizer.fit_transform(corpus)
        X = vectorizer.fit_transform(corpus)
        df = pd.DataFrame(X.toarray())
        print(df)
        return df

    # spacy
    # empath
    # evaluate
    # bert
    # liwc
    # NLTK

    # def parts_of_speech():
    #    import spacy
    #
    #    spacy.prefer_gpu()
    #    import en_core_web_sm
    #    nlp = en_core_web_sm.load()
    #
    #    nlp = spacy.load("en_core_web_sm")
    #    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    #
    #    for token in doc:
    #        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #              token.shape_, token.is_alpha, token.is_stop)

    # def lemmatizer():
    #    import spacy
    #
    #    # English pipelines include a rule-based lemmatizer
    #    nlp = spacy.load("en_core_web_sm")
    #    lemmatizer = nlp.get_pipe("lemmatizer")
    #    print(lemmatizer.mode)  # 'rule'

    #    doc = nlp("I was reading the paper.")
    #    print([token.lemma_ for token in doc])
    #    # ['I', 'be', 'read', 'the', 'paper', '.']


