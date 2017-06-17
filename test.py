

if __name__ == "__main__":
    query = input()
    query = query.replace("%20", " ")
    results = "escuchas.find({{'$text':{{'$search':'\\'{}\\\''}}}})".format(query)
    print(results)