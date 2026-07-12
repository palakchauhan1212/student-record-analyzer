frequency = {}
repeated = {}
unique = set()
class Para:
    def __init__(self):
        str = input('Enter the paragraph:')
        new_str = str.lower()
        str1 = ''
        for i in new_str:
            if i=="." or i=="," or i=="!" or i=="-" or i=="_" :
                str1 = str1 + ''
            else:
                str1 = str1 + i
        str2 = str1.split()
        print('Paragraph with no punctuation and in lower case:',str1)
        self.info(str2)
    def info(self,str2):
        word = ''
        max = 0
        for i in str2:
            a=0
            for j in str2:
                if i==j:
                    a+=1
            frequency[i] = a
            unique.add(i)
        for i in frequency.items():
            if i[1]>=max:
                max=i[1]
                name=i[0]
        repeated[name] = max
obj = Para()
print('Frequency of each word:',frequency)
print('Most repeated word:',repeated)
print('Set of unique words:',unique)