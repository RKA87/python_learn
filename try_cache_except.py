file_path='C:/Temp/all_games.csv'
try:
    all_games=open(file_path,'r')
    print(list(all_games))
except (UnicodeError, UnicodeEncodeError, UnicodeDecodeError, AttributeError) as E:
    print ("Error Message:", E)