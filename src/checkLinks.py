import re
import requests

def extract_links_from_readme(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        readme_content = file.read()

    link_pattern = re.compile(r'href="(.*?)"')
    links = link_pattern.findall(readme_content)
    
    return links


def check_links(links):
    for link in links:
        try:
            response = requests.head(link, allow_redirects=True)
            if response.status_code == 404:
                print(f"404 Not Found: {link}")
            else:
                None  # Link is OK, return None
        except requests.RequestException as e:
            print(f"Error checking {link}: {e}")



file_path = './README.md'
links = extract_links_from_readme(file_path)
check_links(links)
