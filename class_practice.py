import typing as t
from math import log


----------------------------------------
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
                
        for element in info:
            dct = dict.fromkeys(self.wordbank, 0)
            for word in element.lower().split():
                if word in self.wordbank:
                    dct[word] += 1
         
            self.transform.append(list(dct.values()))
        return self.transform

      
    def get_feature_names(self):
         return set(self.wordbank)
        
    def tf_transform(self):
        self.tf = self.fit_transform()
        for sentence in self.tf:
            for word in sentence:
                word = word/len(sentence)
        return self.tf
 ----------------------------------------


# Реализуем функцию tf_transform. Пробегаемся по вложенным списка, подающейся на вход матрицы
# и оцениваем вес каждого элемента вложенного списка
def tf_transform(count_matrix: t.List[t.List[int]]) -> t.List[t.List[int]]:
    result = list()

    for sentence in count_matrix:
        all_words = sum(sentence)
        result_row = [round(word / all_words, 3) for word in sentence]
        result.append(result_row)

    return result


# Реализуем функцию idf_transform. Пробегаемся по вложенным списка, подающейся на вход матрицы
# и оценим вес каждого слова с использованием логарифма
def idf_transform(count_matrix: t.List[t.List[int]]) -> t.List[t.List[int]]:
    result = list()
    documemt_amount = len(count_matrix) + 1
    
    for col in range(len(count_matrix[0])):
        wrdn = 0
        for row in count_matrix:
            if row[col] != 0:
                wrdn += 1
                
        result.append(round(log(documemt_amount / (wrdn + 1)), 1)  + 1)
    
    return result
  
  
  
# Класс, в котором будет метод tf*idf, алогритмы которых мы уже получили
class TfidfTransformer:
    def __init__(self):
        pass
    
    def fit_transform(self, count_matrix):
        tf = tf_transform(count_matrix)
        idf = idf_transform(count_matrix)
        
        tf_idf = list()
        for txt in tf:
            tf_idf.append([round(a * b, 3) for a, b in zip(txt, idf)])
        
        return tf_idf
      
      
      
# Реализум класс TfidfVectorizer, который будет наследоваться от Count_vectorizer.
class CountVectorizer:
    def __init__(self):
        pass
   
    def fit_transform(self, corpus):
        pass
  
    def get_feature_mames(self):
        pass
    
class TfIdfVectorizer(CountVectorizer):
    def __init__ (self):
        super().__init__(self)
        self._tfidf_transformer = TfIdfTransformer()
      
    def fit_transform(self, corpus):
        count_matrix = super(self).fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)

      
if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again',
                'Pasta Pomodoro Fresh ingredients Parmesan to taste'
            ]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
