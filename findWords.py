address = "d:/Crawler"
#address2 = "d:/Crawler/**/*.txt"

class findWords:

    # klasa liczy słowa dotyczące oszustw ile razy pojawiają się w danym komunikacie
    # klasa także przetwarza katalogi aby z nich stworzyć korpusy
    # czyli iteruje po podkatalogach i robi listę spółek

    def __init__(self, listOfWords, mainCatalog):
        self.listOfWords = listOfWords
        self.mainCatalog = mainCatalog

    def listFiles(self):
        import os
        arr = os.listdir(self.mainCatalog)
        print(arr)
        print("it Works")

    def listFilesAndFolders(self):
        import glob
        result = []
        for file_name in glob.iglob(self.mainCatalog, recursive=True):
            print(file_name)
            result.apppend(file_name)
        return result

    def __countWords(self, word, address2):
        import collections
        import glob
        occurrences = 0
        for file_name in glob.iglob(address2, recursive=True):
            try:
                sample_file = open(file_name,    "r")
                file_contents = sample_file. read()
                contents_as_list = file_contents. split()
                occurrences = occurrences + file_contents.count(word)
            except:
                pass
        return (word, occurrences)

    def countManyWords(self, listOfWords, address2):
        # takes catalog and goes through all txt files in it
        # catalog has to end with /*.txt
        # it takes a list of words and
        #import collections
        import glob
        #import re
        listOfOccurrences = [0]*len(listOfWords)
        for file_name in glob.iglob(address2, recursive=True):
            try:
                sample_file = open(file_name, "r")
                file_contents = sample_file.read()
                #contents_as_list = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", file_contents).split())
                contents_as_list = file_contents.split()
            except:
                pass
            for word in self.listOfWords:
                position = self.listOfWords.index(word)
                occurrences = listOfOccurrences[position]
                occurrences = occurrences + contents_as_list.count(word)
                listOfOccurrences[position] = occurrences
        results = list(zip(self.listOfWords, listOfOccurrences))
        results.insert(0,address2)
        return results

    def listSubdirectories(self):
        import os
        results = []
        #for file in os.walk(rootdir):
        #    if os.path.isdir(file[0]):
        #        #print("file", file[0])
        #        results.append(file[0])
        #return(results)

        for root, dirs, files in os.walk(self.mainCatalog, topdown=False):
            for name in dirs:
                print(os.path.join(root, name))
                fulladdress = root+"/"+name
                results.append(fulladdress)
        print("results", results)
        return results