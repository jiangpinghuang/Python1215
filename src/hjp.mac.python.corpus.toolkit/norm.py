import string

def term2Norm(srcPath, srcFile, targFile):
    sentc = ''
    sentt = ''
    src = open(srcFile, 'w')
    tar = open(targFile, 'w')
    punc = string.punctuation
    for line in open(srcPath, 'r'):
        if len(line.strip()) > 1:
            str = line.strip().split('\t')
            if len(sentc) == 0:
                sentc = str[0]
                sentt = str[2]                
            else:
                if str[0] in punc:
                    sentc = sentc
                    sentt = sentt
                else:
                    sentc = sentc + " " + str[0]
                    sentt = sentt + " " + str[2]
        if len(line.strip()) == 0:
            #sentc = sentc.replace(' !!', '!!')
            #sentc = sentc.replace(' ..', '..')
            #sentc = sentc.replace(' ...', '...')
            #sentt = sentt.replace(' !!', '!!')
            #sentt = sentt.replace(' ..', '..')
            #sentt = sentt.replace(' ...', '...')
            print(sentc)
            print(sentt)
            src.write(sentc + ' \n')
            tar.write(sentt + ' \n')
            sentc = ''
            sentt = ''
        
if __name__ == '__main__':
    srcPath = '../../../../../Workshop/Model/data/norm/tweets_normalization_ner.txt'
    srcFile = '../../../../../Workshop/Model/data/tmp/tweets_normalization_ner_informal.txt'
    tarFile = '../../../../../Workshop/Model/data/tmp/tweets_normalization_ner_normalization.txt'
    term2Norm(srcPath, srcFile, tarFile)
