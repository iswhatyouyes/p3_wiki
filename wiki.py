import wikipediaapi
import time

user_agent = "p3_wiki (07kalebg@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = prage.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    links = fetch_links(start_page)

    #make a loop that checks every item in links and prints out a message 



# start and end pages for our wikipedia game solver
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("Rose Parade")

print(start_page.links)z