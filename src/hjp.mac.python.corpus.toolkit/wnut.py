from apt_inst import TarFile
def tab2Spa(srcFile, tarFile):
    tar = open(tarFile, 'w')
    for line in open(srcFile, 'r'):
        print line.strip()
        str = line.strip().replace('\t', ' ')
        tar.write(str + '\n')

def test2Term(srcFile, tarFile):
    tar = open(tarFile, 'w')
    for line in open(srcFile, 'r'):
        if len(line.strip()) >0:
            if len(line.strip()) > 30:
                str = "UNK O"
            else:
                str = line.strip() + " O"
        else:
            str = ""
        tar.write(str + '\n')
            
def term2Token(srcFile, tarFile):
    tar = open(tarFile, 'w')
    for line in open(srcFile, 'r'):
        if len(line.strip()) > 0:
            str = line.strip()
            tok = str.split(' ')
            print tok[2]
            term = tok[2]
        else:
            term = ""
        tar.write(term + '\n')
        
def comToken(srcFile, tarFile):  
    count = 1
    with open(srcFile, 'r') as fp1, open(tarFile, 'r') as fp2:
        for i in fp1:
            j = fp2.readlines()
            if i != '\r\n' and j =='\r\n':
                print count
            count = count + 1
               
 

if __name__ == '__main__':
    #srcFile = '../../../../../Workshop/Model/data/wnut/wnut_test.txt'
    #tarFile = '../../../../../Workshop/Model/data/tmp/wnut_test.txt'
    #tab2Spa(srcFile, tarFile)
    #test2Term(srcFile, tarFile)
    #srcFile = '/home/hjp/Downloads/test21'
    #tarFile = '/home/hjp/Downloads/whu.txt'
    #term2Token(srcFile, tarFile)
    srcFile = '/home/hjp/Downloads/test17.txt'
    tarFile = '/home/hjp/Downloads/test.txt'
    term2Token(srcFile, tarFile)