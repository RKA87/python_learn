# Optimized program of task1
import os

class FileRead:
    def __init__(self,filename):
        self.filename=filename
        self._filepath=self._filepath()

    def _filepath(self):
        cwd=os.getcwd()
        filepath=os.path.join(cwd, self.filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Specified '{self.filename}' is not exist in defined path")
        else:
            return filepath
    
    def _get_data(self):
        try:
            with open(self._filepath(),'r',encoding="utf16") as file:
                data=file.readlines()
                return data
        except Exception as E:
            return Exception("Data Load Error:", E)
    
    def load_data(self):
        return self._get_data()
    
filename="requirement"

try:
    inst1=FileRead(filename)
    result=inst1._filepath()
    print(result)
except Exception as e:
    print(e)

