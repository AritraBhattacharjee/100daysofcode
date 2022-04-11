import requests
from tkinter import *
# from newsapi import NewsApiClient
import apikey
root = Tk()
root.title("News App")
root.geometry("900x800")
# url ="https://newsapi.org/v2/everything"
category = 'sports'
url=f"http://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={apikey.api_key}"
T= Text(root,height=50,width=52,font=('comicsansms',16))
# query_params = {
#         "source":"bbc-news",
#         "sortBy":"top",
#         "apiKey":""

# }
mylabel = Label(root,text="News from the Sports Category: ",font=('comicsansms',16))
mylabel.grid(row=2,column=2)

try:
        # res = requests.get(url,params=query_params)
        res = requests.get(url)
        page = res.json()
        article = page['articles']
        # print(article)
        # print(res.json)
        results = []
        
        for ar in article:
                results.append(ar["title"])
                
        for i in range(len(results)):
                
                # printing all trending news
                # print(i + 1, results[i])
                # mylabel.config(text=f"{i+1} ) {results[i]}\n")

                mylabel.pack()
                T.insert(END,f"{i+1}) {results[i]}\n")
                T.pack(fill=X)
        print(res.status_code)
except Exception as e:
        print(e)


root.mainloop()