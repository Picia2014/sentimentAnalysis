address = "d:/Crawler"
#address2 = "d:/Crawler/**/*.txt"

def listFiles():
    import os
    arr = os.listdir(address)
    print(arr)
    print("it Works")

def listFilesAndFolders():
    import glob
    for file_name in glob.iglob(address2, recursive=True):
        print(file_name)

def countWords(word):
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

def countManyWords(listOfWords, address2):
    # takes catalog and goes through all txt files in it
    # catalog has to end with /*.txt
    # it takes a list of words and
    import collections
    import glob
    import re
    listOfOccurrences = [0]*len(listOfWords)
    for file_name in glob.iglob(address2, recursive=True):
        try:
            sample_file = open(file_name, "r")
            file_contents = sample_file.read()
            #contents_as_list = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", file_contents).split())
            contents_as_list = file_contents.split()
        except:
            pass
        for word in listOfWords:
            position = listOfWords.index(word)
            occurrences = listOfOccurrences[position]
            occurrences = occurrences + contents_as_list.count(word)
            listOfOccurrences[position] = occurrences
    results = list(zip(listOfWords, listOfOccurrences))
    results.insert(0,address2)
    return results

def listSubdirectories(rootdir):
    import os
    results = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            results.append(d)
    return(results)