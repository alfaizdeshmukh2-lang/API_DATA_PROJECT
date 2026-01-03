import requests 

def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    repos = response.json()
    processed_data = []

    for repo in repos :
        processed_data.append({
            "name":repo["name"],
            "language":repo["language"],
            "stars":repo["stargazers_count"],
            "url":repo["html_url"]
        })
    return processed_data
if __name__=="__main__":
    username = "octocat"
    github_data = fetch_github_repos(username)

    if github_data:
        print ("\n Github repository Data :\n ")
    for repo in github_data :
        print (repo)
    else :
        print ("X Failed to fetch github data ")

    