import findWords
import basicSentimentAnalysis
import mainMethodsSentimentAnalysis
import transformers

if __name__ == '__main__':

    ##Settings
    listOfWords = ['company','court', 'lawsuit', 'fraud', 'suspicion', 'police', 'investigation']
    mainCatalog = 'd:/Crawler'
    dictionaryOfFirmNamesWithTickers = {"Tesla": ["TSLA", "Musk", "Elon Musk"], "Apple": ["AAPL", "Steve Jobs"], "Amazon": ["AMZN", "Jeff Besos"], "Meta": ["META"], "Toyota": ["TM"]}

    ##clear files with low number of occurrences of key words
    tr = transformers.transformers(mainCatalog, dictionaryOfFirmNamesWithTickers, 3)
    tr.iterateOverMainFolderAndRemoveTextsWithNotEnoughReferencesToACompany()


    ##create a list of subdirectories with which we will work
    fw = findWords.findWords(listOfWords, mainCatalog)
    catalogs = fw.listSubdirectories()

    ##iterate over every catalog and count word instances
    ##every catalog is another company
    ms = mainMethodsSentimentAnalysis.mainMethodsSentimentAnalysis(mainCatalog, listOfWords)
    wordOccurrences = ms.countWordOccurrences()

    ## analyze sentiment of joined texts on every company
    ms.runSentimentAnalysisForEveryCompany()





