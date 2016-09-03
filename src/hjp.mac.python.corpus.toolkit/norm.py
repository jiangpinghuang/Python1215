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
                    sentc = sentc + str[0]
                    sentt = sentt + str[2]
                else:
                    sentc = sentc + " " + str[0]
                    sentt = sentt + " " + str[2]
        if len(line.strip()) == 0:
            sentc = sentc.replace(' !!', '!!')
            sentc = sentc.replace(' ..', '..')
            sentc = sentc.replace(' ...', '...')
            sentt = sentt.replace(' !!', '!!')
            sentt = sentt.replace(' ..', '..')
            sentt = sentt.replace(' ...', '...')
            print(sentc)
            print(sentt)
            src.write(sentc + '\n')
            tar.write(sentt + '\n')
            sentc = ''
            sentt = ''
        
if __name__ == '__main__':
    srcPath = '../../../../../Workshop/Model/data/norm/Normalization_POS_test_set_2.txt'
    srcFile = '../../../../../Workshop/Model/data/tmp/Normalization_POS_test_set_2_informal.txt'
    tarFile = '../../../../../Workshop/Model/data/tmp/Normalization_POS_test_set_2_normalization.txt'
    term2Norm(srcPath, srcFile, tarFile)
