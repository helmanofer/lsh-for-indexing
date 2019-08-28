import os

from lsh.random_projection import LshRandomProjection
import numpy as np
from lsh import ROOT_DIR

vector_dimension = 300
bucket_size = 3
num_of_buckets = 100
seed = 1
lsh = LshRandomProjection(vector_dimension, bucket_size, num_of_buckets, seed)
lsh.fit(20000000)

wds = []
vecs = []
with open(os.path.join(ROOT_DIR, "data" ,"cc.he.300.samp.vec"), encoding="utf-8") as f:
    for w in f:
        wds.append(w.split(" ")[0])
        vec = list(map(float, w.split(" ")[1:]))
        vecs.append(vec)

X = np.asarray(vecs)
ll = lsh.indexable_transform(X)

for ww, w in zip(ll, wds):
    print(w, len(set(ll[8]).intersection(ww)))