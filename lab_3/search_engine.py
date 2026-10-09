class ChainingHash:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size
        
    def insert(self, key, value):
        self.table[self._hash(key)].append((key, value))
        
    def search(self, key):
        probes = 0
        for k, v in self.table[self._hash(key)]:
            probes += 1
            if k == key: return True, probes
        return False, probes

class ProbingHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        
    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size
        
    def insert(self, key, value):
        idx = self._hash(key)
        while self.table[idx] is not None:
            idx = (idx + 1) % self.size
        self.table[idx] = (key, value)
        
    def search(self, key):
        idx = self._hash(key)
        start_idx = idx
        probes = 0
        while self.table[idx] is not None:
            probes += 1
            if self.table[idx][0] == key: return True, probes
            idx = (idx + 1) % self.size
            if idx == start_idx: break
        return False, probes

def binary_search_words(arr, target):
    low, high, comps = 0, len(arr) - 1, 0
    while low <= high:
        comps += 1
        mid = (low + high) // 2
        if arr[mid][0] == target: return True, comps
        elif arr[mid][0] < target: low = mid + 1
        else: high = mid - 1
    return False, comps

if __name__ == "__main__":
    words = [f"word{i}" for i in range(1, 31)]
    dataset = [(w, i) for i, w in enumerate(words)]
    dataset.sort() 
    
    chaining = ChainingHash(40)
    probing = ProbingHash(40)
    for k, v in dataset:
        chaining.insert(k, v)
        probing.insert(k, v)
        
    target = input("Enter a word to search (e.g., word15, word99): ")
    
    bs_found, bs_comps = binary_search_words(dataset, target)
    ch_found, ch_probes = chaining.search(target)
    pr_found, pr_probes = probing.search(target)
    
    print(f"\n--- Search Results for '{target}' ---")
    print(f"Binary Search    : Found={bs_found}, Comparisons={bs_comps}")
    print(f"Hash (Chaining)  : Found={ch_found}, Probes={ch_probes}")
    print(f"Hash (Probing)   : Found={pr_found}, Probes={pr_probes}")
  
