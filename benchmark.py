import gensim

model_sogou = gensim.models.Word2Vec.load('data/Model/gensimWord2Vec.bin')
model_audio = gensim.models.Word2Vec.load('data/Model/gensimWord2Vec_audio.bin')

print('Benchmark:')
print('搜狗\t转写')
print(model_sogou.most_similar('车辆'))
print(model_audio.most_similar('车辆'))
print(model_sogou.most_similar('事故'))
print(model_audio.most_similar('事故'))
