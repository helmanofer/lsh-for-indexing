## LSH for indexing

This package helps search engines to index and easily search on vector using Local sensitivity hashing (LSH)

#### Installation
    pip install -i https://test.pypi.org/simple/ lsh-for-indexing

#### Usage example
    from lsh import random_projection
    import numpy as np
    
    my_vectors_dimentions = 6
    rp = andom_projection.LshRandomProjection(vector_dimension=6, bucket_size=3, num_of_buckets=2, seed=1)
    vec = np.asarray([1,0,1,1,0,0])
    rp.fit()
    rp.indexable_transform(vec)
    >> ['0_010', '1_000']
    
if you know your collection size and you want an optimal number of bucket_size
    
    rp.fit(sample_size=2000)