import FindWords
import SentimentAnalysis
import Transformer

if __name__ == '__main__':
    #Settings
    listOfWords = ['company','court', 'lawsuit', 'fraud', 'suspicion', 'police', 'investigation']
    mainCatalog = 'd:/Crawler'

    #make a list of subfolders in a directory
    subFolders = FindWords.listSubdirectories(mainCatalog)
    listOfDirectories = []
    for adres in subFolders:
        adres = adres+'/*.txt'
        listOfDirectories.append(adres)

    #iterate over subdirectories and count occurrences of words from my list
    occurrencessOfWordsInSubfolders = []
    for subfolder in listOfDirectories:
        occurrencessOfWordsInSubfolders.append(FindWords.countManyWords(listOfWords, subfolder))
        print(occurrencessOfWordsInSubfolders)
    # results are as a list in occurrencessOfWordsInSubfolders

    #create a corpus of all texts in a particular folder for every company separately
    import Transformer
    listOfCorpuses = []
    tr = Transformer.transformers()
    for subfolder in listOfDirectories:
            joinedTextFilesForOneCompany = tr.joinManyTextsFromSubfolder(subfolder)
            listOfCorpuses.append([subfolder, joinedTextFilesForOneCompany])
    print(listOfCorpuses)

    # run sentiment analysis for every company
    for company in listOfCorpuses:
        se = SentimentAnalysis.sentimentAnalysis(company[1])
        print(se.analyzeSentiment_PatternAnalyzer())
        print(se.analyzeSentiment_NaiveBayesAnalyzer())
        print(se.NLTKSentiment())
