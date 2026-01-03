import requests

def fetch_posts():
    url = f"https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code != 200:
        return None 
    
    posts = response.json()
    processed_post = []

    for post in posts[:5]:
        processed_post.append ({
            "id": post ["id"],
            "title": post ["title"],
            "body":post ["body"]
        })

        return processed_post 
    
if __name__=="__main__":
    
    post_data_in = fetch_posts()

    if post_data_in:
        print ("\n Github repository Data :\n ")
    for post in post_data_in :
        print (post)
    else :
        print ("X Failed to fetch github data ")
