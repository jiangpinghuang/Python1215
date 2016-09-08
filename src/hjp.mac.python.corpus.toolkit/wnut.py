def tab2Spa(srcFile, tarFile):
    tar = open(tarFile, 'w')
    for line in open(srcFile, 'r'):
        print line.strip()
        str = line.strip().replace('\t', ' ')
        tar.write(str + '\n')

if __name__ == '__main__':
    srcFile = '../../../../../Workshop/Model/data/wnut/dev.txt'
    tarFile = '../../../../../Workshop/Model/data/tmp/wnut_dev.txt'
    tab2Spa(srcFile, tarFile)