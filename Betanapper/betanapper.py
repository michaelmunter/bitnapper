from sources import sources
import os
import traceback
import requests
from lxml import html

# ------------------------- #
# -------- OPTIONS -------- #
# ------------------------- #
start_index = 0          # set to 0 to start run with first search term
end_index = 2         # set to None to run for all the rest
print_search_terms = True  # adds search term to output
print_header = True       # adds header to output
ignore_blanks = True
source = "default"       # choose source from sources.py
char_changed_into = "."  # changes char_change - e.g. new decimal operator
# ------------------------- #

# get source data
search_url = sources[source]["search_url"]
search_xpaths = sources[source]["search_xpaths"]
base_url = sources[source]["base_url"]
table_xpaths = sources[source]["table_xpaths"]
char_remove = sources[source]["char_remove"]
char_change = sources[source]["char_change"]


# get search_terms
with open('search_terms.txt') as f:
    search_terms = f.read().splitlines()


def fetch_data(search_term, get_header=False):  # get table data and convert to list
    try:
        # get search page
        url = f"{search_url}{search_term}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"searchUrl error: {search_term}")
        print(f"Fetching data for: {search_term}")
        search_tree = html.fromstring(response.content)

        # get data page link
        data_url = None

        for sx in search_xpaths:
            href_list = search_tree.xpath(sx + '/@href')
            if href_list:
                data_url = base_url + href_list[0]
                break

        if not data_url:
            print(f"dataUrl error: {search_term}")
            return [search_term]

        # get data page
        try:
            company_response = requests.get(data_url)
        except requests.exceptions.ConnectionError:
            print(f"ConnectionError: {search_term}")
            return [search_term]

        if company_response.status_code != 200:
            print(f"dataFetch error: {search_term}")
            return [search_term]
        company_tree = html.fromstring(company_response.content)

        # get table rows
        rows = None
        for tx in table_xpaths:
            href_list = company_tree.xpath(tx + '//tr')
            if href_list:
                rows = href_list
                break

        if not rows:
            print(f"data error (no rows): {search_term}")
            return [search_term]

        formatted_data = [search_term]

        # get headers and data rows
        if get_header:
            headerX = [cell.text for cell in rows[0].xpath('th')]
            headerY = [[cell.text for cell in row.xpath(
                'th')] for row in rows[1:-1]]
            formatted_data[0] = "Index"
        data_rows = [
            [cell.text for cell in row.xpath('td')] for row in rows[1:-1]]

        # transform headers or data to list & return
        for row in data_rows:
            for item in row:
                if get_header:
                    header_name = headerY[data_rows.index(
                        row)][0] + "|" + headerX[row.index(item)+1]
                    formatted_data.append(header_name)
                else:
                    formatted_data.append(item)
        return formatted_data

    # if error, return only search term
    except IndexError:
        print(f"IndexError: {search_term}")
        traceback.print_exc()
        return [search_term]


def format_for_tsv(row):
    formatted_row = []
    for item in row:
        try:
            item = item.replace(char_remove, "")
            item = item.replace(char_change, char_changed_into)
        except AttributeError:
            pass
        formatted_row.append(str(item))
    return "\t".join(formatted_row)


# FORMAT & WRITE TO FILE
cwd = os.path.dirname(os.path.realpath(__file__))
with open(f"{cwd}/output.txt", "w") as f:

    f.seek(0)
    f.truncate()
    if print_header:
        header = [fetch_data(search_terms[0], True)]
        formatted_header = format_for_tsv(header)
        f.write(f"{formatted_header}\n")
        print(formatted_header)
    for search_term in search_terms[start_index:end_index]:
        row = fetch_data(search_term)
        if (row[1:] == []) & ignore_blanks:  # skip if row is empty
            continue
        if not print_search_terms:
            row = row[1:]  # exclude the search term
        formatted_row = format_for_tsv(row)
        f.write(f"{formatted_row}\n")
        print(formatted_row)

print("\n --- FINISHED ---")
