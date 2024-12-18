import os

class FileRead:
    """
    
    """
    def __init__(self,filename):
        """
        Initialize the filename and filepath exist is valid to execute in initialization itself
        """
        self.filename=filename
        self._data=None
        self.__filepath()
    
    def __filepath(self) ->str:
        """
        construct the full filepath and ensure the file exists

        Returns:
            str: The full file path

        Riases:
            FileNotFoundError - If the file not exist
        """
        filepath=os.path.join(os.getcwd(), self.filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {self.filename} does not exist")
        return filepath
    
    def _load_data(self):

        if self._data is None:
            try:
                with open(self.__filepath(), 'r') as file:
                    self._data=file.readlines()
            except Exception as E:
                raise Exception(f"Error raises while loading the data from file:{E}")
            
    def _get_data(self) ->list[str]:
        """
        Retrieve the cached file content.
        
        Returns:
            list[str]: The lines of the file as a list of strings.
        """
        self._load_data()
        return self._data
    
    def total_words_line_count(self):
        """
        Get the lines & words count        
        """
        lines=self._get_data()
        line_count=len(lines)
        word_count=0
        for line in lines:
            words=line.split()
            count=len(words)
            word_count += count
        word_count
        return (line_count, word_count)

    def word_frequency(self,word:str) -> int:
        lines=self._get_data()
        for line in lines:
            words_split=line.strip().split(" ") #every thing is string here, it got strip first and then split into lists outcome






        
    
# inst=FileRead("requirements.txt")
# data=inst._get_data()
# print(data)

# (result1,result2)=inst.total_words_line_count()
# print("line count:", result1, '\n',"word count:", result2)

# result3=inst.word_frequency("is")
# print(result3)


        

# inst=FileRead("requirements.txt")



lines=['Beautiful is better than ugly.\n', 'Explicit is better than implicit.\n', 'Simple is better than complex.\n', 'Complex is better than complicated.\n', 'Flat is better than nested.\n', 'Sparse is better than dense.\n', 'Readability counts.\n', "Special cases aren't special enough to break the rules.\n", 'Although practicality beats purity.\n', 'Errors should never pass silently.\n', 'Unless explicitly silenced.\n', 'In the face of ambiguity, refuse the temptation to guess.\n', 'There should be one-- and preferably only one --obvious way to do it.\n', "Although that way may not be obvious at first unless you're Dutch.\n", 'Now is better than never.\n', 'Although never is often better than *right* now.\n', "If the implementation is hard to explain, it's a bad idea.\n", 'If the implementation is easy to explain, it may be a good idea.\n', "Namespaces are one honking great idea -- let's do more of those!"]

for line in lines:
    x=line.strip()


months = (31,28,31,30,31,30,31,31,30,31,30,31)

number=int(input("enter number:"))

print(months[number-1])
