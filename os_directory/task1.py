import os

class Fileread:
    def __init__(self,filename:str):
        self.filename=filename
    
    def filepath(self):
        get_cwd=os.getcwd()
        file_path=os.path.join(get_cwd,self.filename)
        if os.path.exists(file_path):
            return file_path
        else:
            return "FileNotExist"
    
    def get_data(self):
        try:
            with open(self.filepath(),'r',encoding="utf-16") as file:
                content=file.readlines()
                return content
        except Exception as E:
            print("Error:", E)

    def total_words_line_count(self):
        line_count=0
        words_count=0
        for line in self.get_data():
            line_count += 1
            strip_string=line.strip()
            words=strip_string.split(" ")
            words_count +=len(words)
        return (line_count, words_count)
    
    def word_search(self,word:str):
        word_count=0
        frequency_word_count=0
        for line in self.get_data():
            x=line.strip().split(" ")
            word_count += x.count(word)
            if word in x:
                frequency_word_count += 1        
        return (word_count, frequency_word_count)
    

inst=Fileread("requirements.txt")
filepath=inst.filepath()
print("FilePath:",filepath)

data=inst.get_data()
print(data)

(a,b)=inst.total_words_line_count()
print("Total No of lines:", a)
print("Total No of words:", b)

word="is"
(result1,result2)=inst.word_search(word)
print(f"The word '{word}' appears {result1} times.")
print(f"Frequency Word Count of '{word}' is:",result2)


class Listttofile:
    def __init__(self,list):
        self.list=list

    def list_to_file(self):
        import os            
        cwd=os.getcwd()
        filename=input("Enter the filename:")
        os.path.join(cwd, filename)
        with open(filename, 'w') as file:
            for item in self.list:
                file.writelines(str(item)+'\n')

            file.close()
        print("List to file copied in directory")

list=[1,2,3,4,5,6,7,8,9]
inst=Listttofile(list)
result=inst.list_to_file()
print(result)