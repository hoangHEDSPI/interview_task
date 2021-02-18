class BloomFilter(set):
    def __init__(self, size, hash_count):
        super(BloomFilter, self).__init__()
        