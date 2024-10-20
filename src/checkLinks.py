'''
This code is for checking the links in the readme file
'''

import re
import requests

def extract_links_from_readme(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        readme_content = file.read()

    link_pattern = re.compile(r'href="(.*?)"')
    links = link_pattern.findall(readme_content)
    
    return links


def check_links(links):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    for link in links:
        try:
            response = requests.get(link, allow_redirects=True,
                                    headers=headers)
            if response.status_code == 404:
                print(f" ** 404 Not Found: {link}")
            else:
                None  # Link is OK, return None
        except requests.RequestException as e:
            print(f" ** Error checking {link}: {e}")


def check_for_duplicates(links):
    duplicated_links = [
        'https://arxiv.org/abs/1811.02629',
        'https://academic.oup.com/gigascience/article/7/6/giy065/5026175',
        'https://pubs.rsna.org/doi/10.1148/radiol.2021203957',
        'https://ieeexplore.ieee.org/document/6975210',
        'https://ieeexplore.ieee.org/document/8458220',
        'https://pubs.rsna.org/doi/10.1148/radiol.12111607',
        'https://www.cell.com/cell/fulltext/S0092-8674(18)30154-5',
    ] #List of links that relate to some datasets
    
    seen_links = {}
    for link in links:
        if link in duplicated_links:
            pass
        elif link in seen_links:
            seen_links[link] += 1
        else:
            seen_links[link] = 1
    
    duplicates_found = False
    for link, count in seen_links.items():
        if count > 1:
            if not duplicates_found:
                print(" ** Duplicate links found:")
                duplicates_found = True
            print(f" ** {link} appears {count} times")

    if not duplicates_found:
        print(" ** No duplicate links found")



file_path = './README.md'
links = extract_links_from_readme(file_path)
check_links(links)
check_for_duplicates(links)
