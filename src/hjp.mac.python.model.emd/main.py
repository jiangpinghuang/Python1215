import gensim, pdb, sys, scipy.io as io, numpy as np, pickle, string, multiprocessing as mp
from emd import emd

# read data sets line by line
def read_line_by_line(dataset_name, C, model, vec_size, stopwords):
    # get stop words (except for twitter!)
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
        print '%d out of %d' % (count + 1, num_lines)
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
                # print 'Key error: "%s"' % str(e)
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

def get_wmd(ix):
    n = np.shape(X)
    n = n[0]
    Di = np.zeros((1,n))
    i = ix
    print '%d out of %d' % (i, n)
    for j in xrange(i):
        Di[0,j] = emd( (X[i], BOW_X[i]), (X[j], BOW_X[j]), distance)
        print Di[0,j]
    return Di

def main():
    # load pre-trained word vector.
    model = gensim.models.Word2Vec.load_word2vec_format('/home/hjp/Workshop/Model/data/lib/GoogleNews-vectors-negative300.bin', binary=True)
    vec_size = 300

    # set path of stop words, train_dataset, save_file and save_file_mat.
    stopwords = "/home/hjp/Downloads/wmd/stopwords.txt"
    train_dataset = "/home/hjp/Downloads/wmd/all_twitter_by_line.txt"
    save_file_mat = "/home/hjp/Downloads/wmd/demo_twitter.mat"
    save_file = "/home/hjp/Downloads/wmd/dist_twitter.pk"

    # read document by line.
    (X, BOW_X, y, C, words) = read_line_by_line(train_dataset, [], model, vec_size, stopwords)

    # save pickle of extracted variables.
    # with open(load_file, 'w') as f:
    #    pickle.dump([X, BOW_X, y, C, words], f)

    # save a Matlab format .mat file (optional). 
    # io.savemat(save_file_mat, mdict={'X': X, 'BOW_X': BOW_X, 'y': y, 'C': C, 'words': words})
    
    # with open(load_file) as f:
    #    [X, BOW_X, y, C, words] = pickle.load(f)
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
    pool = mp.Pool(processes=8)

    pool_outputs = pool.map(get_wmd, list(range(n)))
    pool.close()
    pool.join()

    WMD_D = np.zeros((n,n))
    for i in xrange(n):
        WMD_D[:,i] = pool_outputs[i]

    with open(save_file, 'w') as f:
        pickle.dump(WMD_D, f)

if __name__ == "__main__":
    main()                                                                                             
