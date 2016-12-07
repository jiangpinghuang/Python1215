"Translating tweet tags to sentences."

import string

def tweet2sent(orifile, srcfile, tarfile):
    srcsent = ''
    tarsent = ''
    src = open(srcfile, 'w')
    tar = open(tarfile, 'w')
    pun = string.punctuation
    for line in open(orifile, 'r'):
        if len(line.strip()) > 0:
            str = line.strip().split('\t')
            if len(srcsent) == 0:
                srcsent = str[0]
                tarsent = str[2]
            else:
                if str[0] in pun:
                    srcsent = srcsent
                    tarsent = tarsent
                else:
                    srcsent = srcsent + " " + str[0]
                    tarsent = tarsent + " " + str[2]
        else:
            print srcsent
            print tarsent
            src.write(srcsent + '\n')
            tar.write(tarsent + '\n')
            srcsent = ''
            tarsent = ''
        
if __name__ == '__main__':
    origin = '/home/hjp/Workshop/Model/data/nom/tweets_normalization_ner.txt'
    source = '/home/hjp/Workshop/Model/data/tmp/tweets_normalization_ner_src.txt'
    target = '/home/hjp/Workshop/Model/data/tmp/tweets_normalization_ner_tar.txt'
    
    tweet2sent(origin, source, target)
    