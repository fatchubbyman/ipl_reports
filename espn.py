from bs4 import BeautifulSoup as bs
import requests
# open the league link and find all the match report URLs and store them in a text file and find some way to open all of them together

urls = ['https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/indian-premier-league-2009-374163/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/indian-premier-league-2009-10-418064/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/indian-premier-league-2011-466304/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/indian-premier-league-2012-520932/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/indian-premier-league-2013-586733/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/pepsi-indian-premier-league-2014-695871/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/pepsi-indian-premier-league-2015-791129/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/ipl-2016-968923/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/ipl-2017-1078425/match-schedule-fixtures-and-results',
        'https://espncricinfo.com/series/ipl-2018-1131611/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/ipl-2019-1165643/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/ipl-2020-21-1210595/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/ipl-2021-1249214/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/match-schedule-fixtures-and-results',
        'https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results']

game_links = []

for url in urls :
    c=0
    opener = requests.get(url)
    soup = bs(opener.content,'lxml')
    all_matches = soup.find('div', class_ = 'ds-grow ds-px-0')
    #match = all_matches.find_all('div', class_ = 'ds-p-4 hover:ds-bg-ui-fill-translucent ds-border-none ds-border-t ds-border-line')
    for i in all_matches.children:
        game_links.append(i)
        c+=1
    print(c)

                 


print(len(game_links))