class  CountVectorizer:
    def __init__(self, lowercase=True):
        self.lowercase = lowercase

    
    def fit_transform(self, info = None):
        self.wordbank = []
        self.transform = []
        for element in y:
            for j in element.lower().split():
                self.wordbank.append(j)
        for i in y:
            dct = dict.fromkeys(wordbank, 0)
            for line in element.lower().split():
                if line in self.wordbank:
                    dct[line] += 1
         
            self.transform.append(list(dct.values()))
        return self.transform
        
    def get_feature_names(self):
         return self.wordbank
    
