import findWords
import transformers
import basicSentimentAnalysis
import pandas as pd
import thread
import xlsxwriter


class mainMethodsSentimentAnalysis:
    #class takes as the argument the address of the main catalog with investors opinions
    #class takes as the argument list of words which signal possibility of a fraud

    def __init__(self, mainCatalog, listOfWords):
        self.mainCatalog = mainCatalog # we will iterate over it to find all subfolders, each subfolder is 1 company
        self.listOfWords = listOfWords # which word we will be looking for
        # make a list of subfolders in a directory
        self.fw = findWords.findWords(self.listOfWords, self.mainCatalog)
        self.subFolders = self.fw.listSubdirectories()
        self.listOfDirectories = []
        for address in self.subFolders:
            address = address +'/*.txt'
            self.listOfDirectories.append(address)
        print("list of directories" ,self.listOfDirectories)
        self.listOfCorpuses = [] # we will keep here joined texts
        self.tr = transformers.transformers()
        self.bs = basicSentimentAnalysis.basicSentimentAnalysis(self.listOfDirectories)
        self.sentimentForEveryCompany = []


    def countWordOccurrences(self):
        #uses the list of subfolders
        # iterates over subdirectories and counts occurrences of words from list of words
        #in other words for every company it counts occurrences of words from the list of words
        occurrencessOfWordsInSubfolders = []
        for subfolder in self.listOfDirectories:
            occurrencessOfWordsInSubfolders.append(self.fw.countManyWords(self.listOfWords, subfolder))
        print(occurrencessOfWordsInSubfolders)
        # results are as a list in occurrencessOfWordsInSubfolders
        df = pd.DataFrame(occurrencessOfWordsInSubfolders)
        writer = pd.ExcelWriter('wordOccurrences.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='welcome', index=False)
        writer.save()
        return occurrencessOfWordsInSubfolders

    def __joinTextsForCompanies(self):
        # creates a corpus of all texts in a particular folder for every company separately
        #import transformers
        #we use class object listOfCorpuses because we want to save it, it takes ages to process it
        # self.listOfCorpuses = [] - I changed into class object
        counter = 1
        for subfolder in self.listOfDirectories:
                def metoda():
                    print("subfolder" ,subfolder)
                    joinedTextFilesForOneCompany = self.tr.joinManyTextsFromSubfolder(subfolder)
                    self.listOfCorpuses.append([subfolder, joinedTextFilesForOneCompany])
                watek = thread.myThread(counter, subfolder, metoda)
                print(watek, "started")
                watek.start()
                watek.join()
                counter = counter + 1
                print("next run of the loop")
        print("Wszystkie wątki zakończyly pracę")
        print("list of corpuses")
        print(self.listOfCorpuses)
        return self.listOfCorpuses

    def runSentimentAnalysisForEveryCompany(self):
        # takes AGES to run it
        #on the other hand, can work in a background, takes only 10% of CPU
        # run sentiment analysis for every company
        results = []
        self.listOfCorpuses = self.__joinTextsForCompanies()
        for company in self.listOfCorpuses:
            se = self.bs.sentimentAnalysis(company[1])
            sent1 = se.analyzeSentiment_PatternAnalyzer()
            sent2 = se.analyzeSentiment_NaiveBayesAnalyzer()
            sent3 = se.NLTKSentiment()
            print(sent1)
            print(sent2)
            print(sent3)
            results.append([company, "PatternAnalyzer", sent1, "NaiveBayes", sent2, "NLTK", sent3])
            del se
        df = pd.DataFrame(results)
        writer = pd.ExcelWriter('sentiment.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='welcome', index=False)
        writer.save()
        return results
        #this is an example of the results for 1 company for thousands of texts
        # Sentiment(polarity=0.10612503249695336, subjectivity=0.3598489694494145)
        # Sentiment(polarity=0.10612503249695336, subjectivity=0.3598489694494145)
        # Sentiment(polarity= 0.10612503249695336 , subjectivity= 0.3598489694494145 )
        # ('Sentiment(polarity=', 0.10612503249695336, ', subjectivity=', 0.3598489694494145, ')')

    def runSentimentAnalysisEachDocumentSeparatelyForAllCompanies(self):
        results = []
        for companyFolder in self.listOfDirectories:
            for file in companyFolder:
                se = self.bs.sentimentAnalysis(file)
                sent1 = se.analyzeSentiment_PatternAnalyzer()
                sent2 = se.analyzeSentiment_NaiveBayesAnalyzer()
                sent3 = se.NLTKSentiment()
                results.append([companyFolder, sent1, sent2, sent3])
                del se
        df = pd.DataFrame(results)
        writer = pd.ExcelWriter('sentimentSeparatelyFiles.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='welcome', index=False)
        writer.save()
        return results