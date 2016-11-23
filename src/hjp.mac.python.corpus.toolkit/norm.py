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
    linux = '/home/hjp/Workshop/Model/'
    mac = '/Users/hjp/Workspace/Workshop/Model/'
    os = 'MAC' # MAC or LINUX
    if os == 'MAC':
        srcPath = mac + 'data/norm/test_set_2.txt'
        srcFile = mac + 'data/tmp/test_set_2_informal.txt'
        tarFile = mac + 'data/tmp/test_set_2_normalization.txt'
    else:
        srcPath = linux + 'data/norm/tweets_normalization_ner.txt'
        srcFile = linux + 'data/tmp/tweets_normalization_ner_informal.txt'
        tarFile = linux + 'data/tmp/tweets_normalization_ner_normalization.txt'   

    term2Norm(srcPath, srcFile, tarFile)
