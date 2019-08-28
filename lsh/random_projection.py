import random
from itertools import zip_longest

import numpy as np
from scipy import sparse
from sklearn.random_projection import johnson_lindenstrauss_min_dim


class LshRandomProjection(object):
    def __init__(self, vector_dimension, bucket_size=3, num_of_buckets=None, seed=None):
        """
        :param vector_dimension: int
        :param bucket_size: int - the larger the less accurate but easier on the lucene index
        :param num_of_buckets: auto or int
        :param seed: int
        """
        self.vector_dimension = vector_dimension
        self.bucket_size = bucket_size
        self.num_of_buckets = num_of_buckets
        self.seed = seed
        if seed is None:
            self.seed = random.randint()
        self.projection = None

    def fit(self, n_samples=None):
        if not n_samples and not self.num_of_buckets:
            assert "Please provide either n_samples or num_of_buckets"
        if n_samples:
            n_components = self.auto_lsh_num_of_components(n_samples)
            self.num_of_buckets = n_components/self.bucket_size
        else:
            n_components = self.bucket_size * self.num_of_buckets
        density = 1 / np.sqrt(self.vector_dimension)
        self.projection = sparse.random(n_components, self.vector_dimension, density=density,
                                        data_rvs=np.random.randn, random_state=self.seed)

    @staticmethod
    def auto_lsh_num_of_components(n_samples, eps=0.1):
        return johnson_lindenstrauss_min_dim(n_samples=n_samples, eps=eps)

    @staticmethod
    def grouper(iterable, n, fillvalue=None):
        """Collect data into fixed-length chunks or blocks"""
        # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)

    def transform(self, X):
        return X * self.projection.T

    def _stringify(self, x):
        g = self.grouper("".join((x > 0).astype(int).astype(str)), self.bucket_size, '0')
        return ["%s_%s" % (ix, "".join(a)) for ix, a in enumerate(g)]

    def indexable(self, X):
        if X.ndim == 1:
            return self._stringify(X)
        indexable_list = []
        for x in X:
            indexable_list.append(self._stringify(x))
        return indexable_list

    def indexable_transform(self, X):
        X_new = self.transform(X)
        return self.indexable(X_new)

    # def save_model(self):


