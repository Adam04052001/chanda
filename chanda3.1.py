class  CountVectorizer:
    def __init__(self, lowercase=True):
        self.lowercase = lowercase

# Создадим список, который посчитает нам количество слов, которое встретились в каждой строке. Также  сделаем, что вхождения будут тольк ос маленькой буквы. 
# Cделем список, в котором содержатся все слова из поступивших предложений. Превратим этот список в словарь, где слова будут ключами.
# Пробежимся по спискам, чтобы понять сколько раз слово встречается в них    
    def fit_transform(self, info = None):
        self.wordbank = []
        self.transform = []
        for element in info:
            for word in element.lower().split():
                self.wordbank.append(word)
                
        for i in info:
            dct = dict.fromkeys(wordbank, 0)
            for word in element.lower().split():
                if word in self.wordbank:
                    dct[word] += 1
         
            self.transform.append(list(dct.values()))
        return self.transform

      
    def get_feature_names(self):
         return self.wordbank
      
