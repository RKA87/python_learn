from csv import reader

def read_csv(filepath="C:/Temp/all_games.csv"):
    with open(filepath, encoding="utf-8") as file:
        all_games = reader(file)
        all_games = list(all_games)
    return all_games

# Create dictionary of platforms

def platform_dict(all_games):
    platform_dict={}
    for game in all_games[1:]:  # Do not include the header
        name = game[0]
        platform = game[1]
        platform_dict[name] = platform
    
    platform_dict = {name: platform.strip() for name, platform in platform_dict.items()}
    return platform_dict

def create_lists(all_games):

    name = []
    platform = []
    date = []
    summary = []
    meta_score = []
    user_score = []

    # Iterate over columns and append values to lists
    for game in all_games[1:]:
        name.append(game[0])
        platform.append(game[1].replace(" ", ""))
        date.append(game[2])
        summary.append(game[3])
        meta_score.append(float(game[4]))
        user_score.append(float(game[5]))
    return name, platform, date, summary, meta_score, user_score

def year_dict(name_list, date_list):
    year_dict = {}

    for key, value in zip(name_list, date_list):
        year_dict[key] = value[-4:]

    return year_dict

#using conditional statements

# Video games released after 2014

def dict_by_year(name_list,date_list,year):
    after_year = {key: value[-4:] for key, value in zip(name_list, date_list) if int(value[-4:]) > year}
    return after_year


# Video games released between 2014 and 2018 (both inclusive)
def year_between(name_list,date_list,from_year,to_year):
    years_in_between = {key: value[-4:] for key, value in zip(name_list, date_list) if int(value[-4:]) >= from_year and int(value[-4:]) <= to_year}
    return years_in_between

# Games with meta score below 25 or above 97
def meta_in_between(name_list,meta_score_list,from_day,to_day):
    meta_in_between={
        key: value
        for key, value in zip(name_list, meta_score_list)
        if float(value) < from_day or float(value) > to_day
    }
    return meta_in_between

# Create a nested dictionary
def tile_platform_date(name_list,platform_list,date_list):
    tile_platform_date = {}
    for n, p, dt in zip(name_list, platform_list, date_list):
        tile_platform_date[n] = {"platform": p, "date": dt}
    return tile_platform_date

# Create another nested dictionary
def title_date(name_list,date_list):
    title_date = {}
    for n, dt in zip(name_list, date_list):
        title_date[n] = {"date": dt}
    return title_date

# Extract release years and transform them into integers inside the nested dictionary
def release_years(tile_platform_date):
    for (title, outer_value) in tile_platform_date.items():
        for (inner_key, date) in outer_value.items():
            try:
                outer_value.update({inner_key: int(date[-4:])})
            except:
                print(date)
    tile_platform_date.update({title: outer_value})
    return tile_platform_date

def main():
    result=read_csv()
    list_results=create_lists(result)
    print(list_results)

if __name__ == "__main__":
    main()