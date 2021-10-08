
def smallest(plist):
    if len(plist) == 1:
        return int(plist[0])
    if plist[0] < plist[1]:
        plist[1] = plist[0]
    return smallest(plist[1:])
            

def linearSearchValueIndexEqual(plist):
    if not plist:
        return []
    final = []
    count = 0
    for i in plist:
        if i == count:
            final.append(i)
        count += 1
    return final
            

def binarySearchValueIndexEqual(plist):
    if not plist:
        return []
    final = []
    for index in range(len(plist)):
        left = 0
        right = len(plist) - 1
        while left <= right:
            middle = (right - left) // 2 + left     
            if plist[middle] == index:
                if index == plist[index]:           
                    final.append(middle)
                break
            elif index < plist[middle]:
                right = middle - 1              
            else:                               
                left = middle + 1
    return final



class Hashtable:
    def __init__(self, items):
        self.bucketsize = len(items)
        self.buckets = [[] for i in range(self.bucketsize)]
        self.assign_buckets(items)

    def assign_buckets(self, items):
        for element in items:
            hash_code = hash(element)
            index = hash_code % self.bucketsize
            self.buckets[index].append((items))



def anonymousLetter(book, letter):
    group = (book, letter)
    hashtable = Hashtable(group)
    for ch in letter:
        if ch not in book:
            return False
        elif letter.count(ch) > book.count(ch):
            return False
    return True

