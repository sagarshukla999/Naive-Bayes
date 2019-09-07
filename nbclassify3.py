import sys
import os
import re
import ast
import math
import glob
testing_data = sys.argv[1]

model_file = "nbmodel.txt"
output_file = "nboutput.txt"

items = []
with open(model_file, 'r') as i:
    line = i.readline()
    while line:
        items.append(line)
        # print(line)
        line = i.readline()
dictTP = {}
dictTN = {}
dictDP = {}
dictDN = {}
for item in items:
    value = item.split("=")
    if value[0] == "dictTP":
        dictTP = ast.literal_eval(value[1])
    elif value[0] == "dictTN":
        dictTN = ast.literal_eval(value[1])
    elif value[0] == "dictDP":
        dictDP = ast.literal_eval(value[1])
    elif value[0] == "dictDN":
        dictDN = ast.literal_eval(value[1])
    elif value[0] == "denominatiorTP":
        denominatiorTP = int(value[1])
    elif value[0] == "denominatiorTN":
        denominatiorTN = int(value[1])
    elif value[0] == "denominatiorDP":
        denominatiorDP = int(value[1])
    elif value[0] == "denominatiorDN":
        denominatiorDN = int(value[1])
    elif value[0] == "TPfiles":
        TPfiles = int(value[1])
    elif value[0] == "TNfiles":
        TNfiles = int(value[1])
    elif value[0] == "DPfiles":
        DPfiles = int(value[1])
    elif value[0] == "DNfiles":
        DNfiles = int(value[1])
    elif value[0] == "v":
        v = int(value[1])
    else:
        print("Error")
        
#print(dictDP)        


total = DPfiles+DNfiles+TPfiles+TNfiles
stopwords = [
    "i", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

allpaths = glob.glob(os.path.join(testing_data, '*/*/*/*.txt'))


for paths in allpaths:
    with open(paths, 'r') as i:
        line = i.readline()
    line = line.lower()
    newsent = re.sub(r"[^a-zA-Z0-9]+", ' ', line)
    arr = newsent.split()
    arr1 = [x for x in arr if x not in stopwords]
    probTP = 0
    for i in arr1:
        # if i not in stopwords:
        if i in dictTP:
            probTP += math.log(dictTP[i]+1)-math.log(denominatiorTP+v)
        else:
            probTP += math.log(1)-math.log(denominatiorTP+v)

    probTP += math.log(TPfiles)-math.log(total)

    probTN = 0
    for i in arr1:
        # if i not in stopwords:
        if i in dictTN:
            probTN += math.log(dictTN[i]+1)-math.log(denominatiorTN+v)
        else:
            probTN += math.log(1)-math.log(denominatiorTN+v)

    probTN += math.log(TNfiles)-math.log(total)

    probDP = 0
    for i in arr1:
        # if i not in stopwords:
        if i in dictDP:
            probDP += math.log(dictDP[i]+1)-math.log(denominatiorDP+v)
        else:
            probDP += math.log(1)-math.log(denominatiorDP+v)

    probDP += math.log(DPfiles)-math.log(total)

    probDN = 0
    for i in arr1:
        # if i not in stopwords:
        if i in dictDN:
            probDN += math.log(dictDN[i]+1)-math.log(denominatiorDN+v)
        else:
            probDN += math.log(1)-math.log(denominatiorDN+v)

    probDN += math.log(DNfiles)-math.log(total)

    if probDN > probDP and probDN > probTP and probDN > probTN:
        ans = "deceptive negative "+paths
    elif probDP > probDN and probDP > probTP and probDP > probTN:
        ans = "deceptive positive "+paths
    elif probTP > probDP and probTP > probDN and probTP > probTN:
        ans = "truthful positive "+paths
    else:
        ans = "truthful negative "+paths

    #print(ans)
    with open(output_file, 'a') as f:
        f.write(ans+"\n")
