class Node :
    def __init__(self):
        self.children = {}
        self.endHere = 0
        self.suggestions = []

class Trie :
    def __init__(self,maxSuggest):
        self.maxSuggest = maxSuggest
        self.root = Node()
        
    def addString(self,string):
        curr = self.root
        for k in string:
            if k not in curr.children :
                curr.children[k] = Node()
            curr = curr.children[k]
            self.addSuggestion(curr,string)     # add string as suggestion of curr char
        curr.endHere +=1
        
    def addSuggestion(self,node,word):
        if len(node.suggestions) < self.maxSuggest :
            node.suggestions.append(word)
        
    def searchSuggestions(self,string):
        res = [[] for _ in range(len(string))]
        curr = self.root
        for idx,k in enumerate(string):
            if k not in curr.children:
                break
            curr = curr.children[k]
            res[idx] = curr.suggestions
        return res
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
    
        maxSuggest = 3
        trie = Trie(maxSuggest)

        for product in products:
            trie.addString(product)
        res = trie.searchSuggestions(searchWord)
        return res