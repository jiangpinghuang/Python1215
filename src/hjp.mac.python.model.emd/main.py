import gensim, pdb, sys, scipy.io as io, numpy as np, pickle, string, multiprocessing as mp
from emd import emd

def read_line_by_line(dataset_name, C, model, vec_size, stopwords):
    SW = set()
    for line in open(stopwords):
        line = line.strip()
        if line != '':
            SW.add(line)
    stop = list(SW)

    f = open(dataset_name)
    if len(C) == 0:
        C = np.array([], dtype=np.object)
    num_lines = sum(1 for line in open(dataset_name))
    y = np.zeros((num_lines,))
    X = np.zeros((num_lines,), dtype=np.object)
    BOW_X = np.zeros((num_lines,), dtype=np.object)
    count = 0
    remain = np.zeros((num_lines,), dtype=np.object)
    the_words = np.zeros((num_lines,), dtype=np.object)
    for line in f:
        line = line.strip()
        line = line.translate(string.maketrans("", ""), string.punctuation)
        T = line.split('\t')
        classID = T[0]
        if classID in C:
            IXC = np.where(C == classID)
            y[count] = IXC[0] + 1
        else:
            C = np.append(C, classID)
            y[count] = len(C)
        W = line.split()
        F = np.zeros((vec_size, len(W) - 1))
        inner = 0
        RC = np.zeros((len(W) - 1,), dtype=np.object)
        word_order = np.zeros((len(W) - 1), dtype=np.object)
        bow_x = np.zeros((len(W) - 1,))
        for word in W[1:len(W)]:
            try:
                test = model[word]
                if word in stop:
                    word_order[inner] = ''
                    continue
                if word in word_order:
                    IXW = np.where(word_order == word)
                    bow_x[IXW] += 1
                    word_order[inner] = ''
                else:
                    word_order[inner] = word
                    bow_x[inner] += 1
                    F[:, inner] = model[word]
            except KeyError, e:
                word_order[inner] = ''
            inner = inner + 1
        Fs = F.T[~np.all(F.T == 0, axis=1)]
        word_orders = word_order[word_order != '']
        bow_xs = bow_x[bow_x != 0]
        X[count] = Fs.T
        the_words[count] = word_orders
        BOW_X[count] = bow_xs
        count = count + 1;
    return (X, BOW_X, y, C, the_words)

def distance(x1,x2):
    return np.sqrt( np.sum((np.array(x1) - np.array(x2))**2) )

def main():
    model = gensim.models.Word2Vec.load_word2vec_format('/home/hjp/Workshop/Model/data/lib/GoogleNews-vectors-negative300.bin', binary=True)
    vec_size = 300

    stopwords = "/home/hjp/Workshop/Model/tmp/tmp/wmd/stop_words.txt"
    train_dataset = "/home/hjp/Workshop/Model/data/tmp/pit.train.txt"
    save_file = "/home/hjp/Workshop/Model/tmp/tmp/wmd/wmd_twitter.pk"

    (X, BOW_X, y, C, words) = read_line_by_line(train_dataset, [], model, vec_size, stopwords)

    n = np.shape(X)
    n = n[0]
    D = np.zeros((n, n))

    for i in xrange(n):
        bow_i = BOW_X[i]
        bow_i = bow_i / np.sum(bow_i)
        bow_i = bow_i.tolist()
        BOW_X[i] = bow_i
        X_i = X[i].T
        X_i = X_i.tolist()
        X[i] = X_i
        
    n = np.shape(X)
    n = n[0]

    Di = np.zeros((1, n/2))
    for i in range(n):
        if i % 2 == 0:
            j = i + 1
            Di[0,i/2] = emd( (X[i], BOW_X[i]), (X[j], BOW_X[j]), distance)
            print Di[0, i/2]
  
    with open(save_file, 'w') as f:
        pickle.dump(Di, f)

if __name__ == "__main__":
    main()                                                                                             
