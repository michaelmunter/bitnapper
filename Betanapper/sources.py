# search_url        get from search page by excluding search term
# search_xpaths     get by inspecting search result in browser (must be in list)
# base_url          will be added to relative link of search result for absolute link to data - usually just the domain - i.e. https://www.[site].com
# table_xpaths      get by inspecting data table in browser
# char_remove       e.g. a '000 separator
# char_change       e.g. a decimal operator


sources = {
    # replace with your own sources
    "default": {
        "search_url": "https://www.proff.dk/branches%C3%B8g?q=",
        "search_xpaths": [
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div[1]/div[3]/div/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/span/h2/a',
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/span/h2/a'
        ],
        "base_url": "https://www.proff.dk",
        "table_xpaths": [
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/table',
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div/div[1]/div/div[5]/div[2]/div/div[1]/div/div[1]/div/table',
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/table'
        ],
        "char_remove": ".",
        "char_change": ","
    },

    # example source
    "proff.dk": {
        "search_url": "https://www.proff.dk/branches%C3%B8g?q=",
        "search_xpaths": [
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div[1]/div[3]/div/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/span/h2/a',
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/span/h2/a'
        ],
        "base_url": "https://www.proff.dk",
        "table_xpaths": [
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/table',
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div/div[1]/div/div[5]/div[2]/div/div[1]/div/div[1]/div/table',
            '//*[@id="scrollable-auto-tabpanel-0"]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div/div[1]/div/table'
        ],
        "char_remove": ".",
        "char_change": ","
    },

    # Add more sources here...
}
