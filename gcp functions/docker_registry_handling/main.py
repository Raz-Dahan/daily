import requests

DOCKER_USERNAME="***"
DOCKER_PASSWORD="***"

def delete_oldest_tags(data, context):
    repository = "razdahan31/gha-pipeline"
    url = f"https://hub.docker.com/v2/repositories/{repository}/tags"
    tags = []
    while url:
        response = requests.get(url)
        data = response.json()
        if "results" in data:
            page_tags = [tag['name'] for tag in data["results"]]
            tags.extend(page_tags)
            url = data.get("next")
    if len(tags) > 20:
        headers = {
            "Content-Type": "application/json"
        }
        
        # Authenticate and get the JWT token
        auth_response = requests.post(
            "https://hub.docker.com/v2/users/login/",
            json={"username": DOCKER_USERNAME, "password": DOCKER_PASSWORD},
            headers=headers
        )
        auth_data = auth_response.json()
        if "token" in auth_data:
            token = auth_data["token"]
            headers["Authorization"] = f"JWT {token}"
        else:
            print("Authentication failed")
            return
        
        tags_to_delete = tags[10:]
        for tag in tags_to_delete:
            delete_url = f"https://hub.docker.com/v2/repositories/{repository}/tags/{tag}/"
            delete_response = requests.delete(delete_url, headers=headers)
            if delete_response.status_code == 204:
                print(f"Successfully deleted {tag}")
            else:
                print(f"Failed to delete {tag}")
        
        return "Tags deletion complete."
    else:
        return "No tags to delete."
