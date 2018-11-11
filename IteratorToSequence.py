#instead of iterating over iterators and iterables,they can be converted to sequences
#this program converts an iterator to a list using the list constructor
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti=TestIterator()
print(list(ti))