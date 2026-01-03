from github_api import fetch_github_repos
from post_api import fetch_posts
from utils import save_to_json, print_section

def main():

# Github api Data

    print_section("GITHUB API DATA")

    username = "octocat"
    github_data = fetch_github_repos(username)

    if github_data:
        for repo in github_data[:5]:
            print(repo)

        save_to_json("output/github_data.json", github_data)
    else:
        print("❌ Failed to fetch GitHub data")

    # post API data
    print_section("POST API DATA")

    post_data = fetch_posts()

    if post_data:
        for post in post_data:
            print(post)

        save_to_json("output/post_data.json", post_data)
    else:
        print("❌ Failed to fetch Post data")


if __name__ == "__main__":
    main()
