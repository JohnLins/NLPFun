import gensim.downloader as api
wv = api.load('word2vec-google-news-300')


print("king", wv['king'])
print("kid", wv['kid'])
