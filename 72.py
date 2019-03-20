import webbrowser
search_term = input("Enter the search term: ")
url = "https://www.google.com/search?q={}".format(search_term)
webbrowser.open(url)