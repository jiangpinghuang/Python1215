import os
import glob
import math
import random

tokFiles = []

def trainDev(path, wpath, flag):
    index = 0
    f = open(wpath, 'w')
    f.write("pair_ID\tsentence_A\tsentence_B\trelatedness_score\tparaphrase_judgment\n")
    for line in open(path, 'r'):
        index += 1
        sents = ""
        print line
        strs = line.split('\t')
        for i in range(len(strs)):
            print strs[i]
        if strs[4].strip() == '(0, 5)':
            print '0.0000'
            print 'non-paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.0") + "\t" + "0"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0, 0.1), 2)) + "\t" + "0"
        if strs[4].strip() == '(1, 4)':
            print '0.2000'
            print 'non-paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.2") + "\t" + "0"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.1, 0.3), 2)) + "\t" + "0"
        if strs[4].strip() == '(2, 3)':
            print '0.4000'
            print 'debatable'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.4") + "\t" + "2"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.3, 0.5), 2)) + "\t" + "2"
        if strs[4].strip() == '(3, 2)':
            print '0.6000'  
            print 'paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.6") + "\t" + "1"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.5, 0.7), 2)) + "\t" + "1"
        if strs[4].strip() == '(4, 1)':
            print '0.8000'  
            print 'paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("0.8") + "\t" + "1"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.7, 0.9), 2)) + "\t" + "1"
        if strs[4].strip() == '(5, 0)':
            print '1.0000' 
            print 'paraphrases'
            if flag:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str("1.0") + "\t" + "1"
            else:
                sents = str(index) + "\t" + strs[2] + "\t" + strs[3] + "\t" + str(round(random.uniform(0.9, 1.0), 2)) + "\t" + "1" 
        print sents
        f.write(sents + '\n')
    f.close()        
 
def testData(path, wlabel, wpath, flag):
    index = 0
    f = open(wpath, 'w')
    f.write("pair_ID\tsentence_A\tsentence_B\trelatedness_score\tparaphrase_judgment\n")
    sent = []
    label = []
    for line in open(path, 'r'):        
        print line
        strs = line.split('\t')
        print(len(strs))
        print(index)
        sent.append(strs[2] + "\t" + strs[3])    
    print wlabel
    for lines in open(wlabel, 'r'):        
        print lines
        strs = lines.split('\t')        
        if strs[1].strip() == '0.0000':
            print '0.0000'
            print 'non-paraphrases'
            if flag:
                label.append(str("0.0") + "\t" + "0")
            else:
                label.append(str(round(random.uniform(0, 0.1), 2)) + "\t" + "0")
        if strs[1].strip() == '0.2000':
            print '0.2000'
            print 'non-paraphrases'
            if flag:
                label.append(str("0.2") + "\t" + "0")
            else:
                label.append(str(round(random.uniform(0.1, 0.3), 2)) + "\t" + "0")
        if strs[1].strip() == '0.4000':
            print '0.4000'
            print 'non-paraphrases'
            if flag:
                label.append(str("0.4") + "\t" + "0")
            else:
                label.append(str(round(random.uniform(0.3, 0.5), 2)) + "\t" + "0")          
        if strs[1].strip() == '0.6000':
            print '0.6000'  
            print 'debatable'
            if flag:
                label.append(str("0.6") + "\t" + "2")
            else:       
                label.append(str(round(random.uniform(0.5, 0.7), 2)) + "\t" + "2")           
        if strs[1].strip() == '0.8000':
            print '0.8000'  
            print 'paraphrases'
            if flag:
                label.append(str("0.8") + "\t" + "1") 
            else:
                label.append(str(round(random.uniform(0.7, 0.9), 2)) + "\t" + "1")            
        if strs[1].strip() == '1.0000':
            print '1.0000' 
            print 'paraphrases'
            if flag:
                label.append(str("1.0") + "\t" + "1") 
            else:
                label.append(str(round(random.uniform(0.9, 1.0), 2)) + "\t" + "1")            
        index += 1
    for i in range(index):
        f.write(str(i + 1) + "\t" + sent[i] + "\t" + label[i] + "\n")
    f.close()

def sentLength(path):
    for line in open(path, 'r'):
        strs = line.split("\t")
        str1 = strs[2].split(" ")
        str2 = strs[3].split(" ")
        step = abs(len(str1) - len(str2))
        if step > 10:
            print 'sent1: ', strs[2]
            print 'sent2: ', strs[3]
            print line

def sentSplit(filepath, dist):
    with open(filepath) as datafile, \
         open(dist + 'id.txt', 'w') as idfile, \
         open(dist + 'ls.tok', 'w') as lsfile, \
         open(dist + 'rs.tok', 'w') as rsfile, \
         open(dist + 'sim.txt', 'w') as simfile, \
         open(dist + 'pi.txt', 'w') as pifile:
            datafile.readline()
            for line in datafile:
                print line
                id, ls, rs, sim, pi = line.strip().split('\t')
                idfile.write(id + '\n')
                lsfile.write(ls + '\n')
                rsfile.write(rs + '\n')
                simfile.write(sim + '\n')
                pifile.write(pi + '\n')
                
def fileExt(file):
    return  os.path.splitext(file)[1]

def dirPath(dir):
    for file in glob.glob(dir + os.sep + '*'):
        if os.path.isdir(file):
            dirPath(file)
        else:
            if fileExt(file) == '.tok':
                tokFiles.append(file)

def buildVocab(filePaths, distPath, lowerCase=True):
    vocab = set()
    dirPath(filePaths)
    for file in tokFiles:
        with open(file) as f:
            for line in f:
                if lowerCase:
                    line = line.lower()
                vocab |= set(line.split())
    with open(distPath, 'w') as f:
        for w in sorted(vocab):
            f.write(w + '\n')
            
def extractSentence(srcFile, distFile):
    f = open(distFile, 'w')
    sents = []
    for line in open(srcFile, 'r'):
        print line
        sent = line.split('\t')
        print sent[2]
        print sent[3]
        if sent[2] not in sents:
            sents.append(sent[2])
        if sent[3] not in sents:
            sents.append(sent[3])
    for i in range(len(sents)):
        f.write(sents[i] + " \n")
      
if __name__ == '__main__':
    train = '../Workshop/Model/data/pit/pit_train.txt'
    wtrain = '../Workshop/Model/data/tmp/pit_train.txt'
    dev = '../Workshop/Model/data/pit/pit_dev.txt'
    wdev = '../Workshop/Model/data/tmp/pit_dev.txt'
    test = '../Workshop/Model/data/pit/pit_test.txt'
    label = '../Workshop/Model/data/pit/pit_test_label.txt'
    wtest = '../Workshop/Model/data/tmp/pit_test.txt'
    strain = '../Workshop/Model/data/tmp/train/'
    sdev = '../Workshop/Model/data/tmp/dev/'
    stest = '../Workshop/Model/data/tmp/test/'
    pit = '../Workshop/Model/data/tmp/'

    trainDev(train, wtrain, True) 
    trainDev(dev, wdev, True) 
    testData(test, label, wtest, True)
    sentSplit(wtrain, strain)
    sentSplit(wdev, sdev)
    sentSplit(wtest, stest)
    buildVocab(pit, pit + 'vocab.txt', True)
    buildVocab(pit, pit + 'vocabs.txt', False)
    extractSentence(dev, wdev)  
