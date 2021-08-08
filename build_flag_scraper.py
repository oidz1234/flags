from autoscraper import AutoScraper

url = 'https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags'

wanted_list = ['Flag of Albania', 'https://en.wikipedia.org/wiki/File:Flag_of_Albania.svg']

scraper = AutoScraper()
scraper.build(url, wanted_list)

result = scraper.get_result_similar('https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags', group_by_alias=True)


for f in result['']:
    if 'svg' in f:
        print(f)
# that gets the list of all flags
# now for each of those we need the "original file" link then we can include that in webapges
# or just download them all.






scraper.save('flags_scraper')




