def search():
    def search():
    ###wikise***
        try:
            import wikipedia
            from googlesearch import search
            import emoji
            from emoji import emojize
            em = emojize(":backhand_index_pointing_right:") 
            search = input(f"{em}")
            query = search
            for i in search(query, tld= "co.in",num=10, stop=10, pause=2):
                print (i,"\n")
            result = wikipedia.page(a)
            print("\n",result.summary)
        except Exception as ex:
            print (ex)
    search()

search()