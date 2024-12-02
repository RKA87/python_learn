import os

class Fileread:
    def __init__(self,filename:str):
        self.filename=filename
    
    def filepath(self):
        get_cwd=os.getcwd()
        file_path=os.path.join(get_cwd,self.filename)
        return file_path
    
    def data(self):
        try:
            with open(self.filepath(),'r',encoding="utf-16") as file:
                content=file.readlines()
                return content
        except Exception as E:
            print("Error:", E)

    def total_words_line_count(self):
        line_count=0
        words_count=0
        for line in self.data():
            line_count += 1
            strip_string=line.strip()
            words=strip_string.split(" ")
            words_count +=len(words)
        return (line_count, words_count)
    
    def word_search(self,word:str):
        word_count=0
        for line in self.data():
            x=line.strip().split(" ")
            word_count += x.count(word)
        return word_count


inst=Fileread("requirements.txt")
data=inst.data()
print(data)

(a,b)=inst.total_words_line_count()
print("Total No of lines:", a)
print("Total No of words:", b)

word="is"
result=inst.word_search(word)
print(f"The word '{word}' appears {result} times.")