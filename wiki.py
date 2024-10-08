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
    print("working on it.e..")
    start_time = time.time()
    
    queue = Queue()
    visited = set()
    parent = {}

    queue.put(start_page.title)
    visited.add(start_page.title)

print(start_page.links)

    #reconstruct path from target page to start page / everything below this line is in the 
    path = []
    page_title = target_page.title
    while page_title != start_page.title
        path.append(page_title)
        page_titile = parent[page_title]

    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print("this algorithm took", end_time - start_time, "seconds.")
    return path

# start and end pages for our wikipedia game solver
start_page = wiki.page("Pasadena High School (California)")
target_page = wiki.page("Rose Parade")    
path=wikipedi_game_solver(start_page,) target_page)
print(path)