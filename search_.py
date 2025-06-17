import webbrowser

x = 1
query_count = 0

while (x == 1):
    if (query_count > 0):
        query = input("What Else Would You Like to Find ?: ")
        if (query == "exit"):
            x = 0
            break
        else:
            url = "google.com/search?q="
            adjusted_query = query.replace(" ", "+")
            print(adjusted_query)
            search_string = url + adjusted_query
            webbrowser.open_new_tab(search_string)
            query = ""
            query_count = query_count + 1
    else:
        query = input("What Do You Want to Search ?: ")
        if (query == "exit"):
            x = 0
            break
        else:
            url = "google.com/search?q="
            adjusted_query = query.replace(" ", "+")
            print(adjusted_query)
            search_string = url + adjusted_query
            webbrowser.open(search_string)
            query = ""
            query_count = query_count + 1