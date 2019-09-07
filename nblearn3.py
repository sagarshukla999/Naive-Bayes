
import sys
import os
import re
import glob
from collections import Counter
path = 'op_spam_training_data'

pathsDN = []
pathsDP = []
pathsTN = []
pathsTP = []

allpaths = glob.glob(os.path.join(sys.argv[1], '*/*/*/*.txt'))
# print(allpaths)
for i in allpaths:
    # print(i)
    if "deceptive_from_MTurk" in i:
        if "negative_polarity" in i:
            pathsDN.append(i)

        else:
            pathsDP.append(i)
    else:
        if "negative_polarity" in i:

            pathsTN.append(i)
        else:
            pathsTP.append(i)

# print(pathsTruthful)
stopwords = [
    "i", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

dictDN = Counter()
for paths in pathsDN:
    with open(paths, 'r') as i:
        lines = i.read()
    lines = lines.lower()
    lines = re.sub(r"[^a-zA-Z]+", ' ', lines)
    arr = lines.split()
    #totalwordsDN += len(arr)
    arr1 = [x for x in arr if x not in stopwords]
    count = Counter(arr1)
    dictDN += count
denominatiorDN = sum(dictDN.values())

dictDP = Counter()
for paths in pathsDP:
    with open(paths, 'r') as i:
        lines = i.read()
    lines = lines.lower()
    lines = re.sub(r"[^a-zA-Z]+", ' ', lines)
    arr = lines.split()
    arr1 = [x for x in arr if x not in stopwords]
    count = Counter(arr1)
    dictDP += count
denominatiorDP = sum(dictDP.values())

dictTN = Counter()
for paths in pathsTN:
    with open(paths, 'r') as i:
        lines = i.read()
    lines = lines.lower()
    lines = re.sub(r"[^a-zA-Z]+", ' ', lines)
    arr = lines.split()
    arr1 = [x for x in arr if x not in stopwords]
    count = Counter(arr1)
    dictTN += count
denominatiorTN = sum(dictTN.values())

dictTP = Counter()
for paths in pathsTP:
    with open(paths, 'r') as i:
        lines = i.read()
    lines = lines.lower()
    lines = re.sub(r"[^a-zA-Z]+", ' ', lines)
    arr = lines.split()
    arr1 = [x for x in arr if x not in stopwords]
    count = Counter(arr1)
    dictTP += count
denominatiorTP = sum(dictTP.values())

V = dictTP+dictTN+dictDP+dictDN
v = len(V)


with open("nbmodel.txt", 'w') as f:
    f.write("dictTP="+str(dict(dictTP))+"\n")
    f.write("dictTN="+str(dict(dictTN))+"\n")
    f.write("dictDP="+str(dict(dictDP))+"\n")
    f.write("dictDN="+str(dict(dictDN))+"\n")
    f.write("denominatiorTP="+str(denominatiorTP)+"\n")
    f.write("denominatiorTN="+str(denominatiorTN)+"\n")
    f.write("denominatiorDP="+str(denominatiorDP)+"\n")
    f.write("denominatiorDN="+str(denominatiorDN)+"\n")
    f.write("TPfiles="+str(len(pathsTP))+"\n")
    f.write("TNfiles="+str(len(pathsTN))+"\n")
    f.write("DPfiles="+str(len(pathsDP))+"\n")
    f.write("DNfiles="+str(len(pathsDN))+"\n")
    f.write("v="+str(v)+"\n")

