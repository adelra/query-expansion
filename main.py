from hazm import *
import pickle
listt = [
"تلفات جاده آمار",
"انرژي هسته قوانين",
"مربي فوتبال ايران",
"تحريم اقتصادي ايران",
"باغباني گل آموزش"
]
for x in listt:
    input_query = x
    pkl_file = open('data.pkl', 'rb')
    dic = pickle.load(pkl_file)
    pkl_file.close()
    normalizer = Normalizer()
    normalized = normalizer.normalize(input_query)
    stemmer = Stemmer()
    stemmed = stemmer.stem(normalized)
    tokens = word_tokenize(stemmed)
    list_of_synonyms = {}
    for x in tokens:
        try:
            tokens_synonyms = word_tokenize(dic[x])
            for y in tokens_synonyms:
                list_of_synonyms[x] = y

        except:
            pass
            list_of_synonyms[x] = x
    values = list_of_synonyms.values()
    print(' '.join(values))
