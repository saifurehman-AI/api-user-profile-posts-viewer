import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

while True:
    try:
        user_id = int(input("Enter User ID (1-10): "))

        if 1 <= user_id <= 10:
            break

        print("Invalid User ID. Please enter a number from 1 to 10.")

    except ValueError:
        print("Invalid input. Please enter a numeric User ID.")

url = f"{BASE_URL}/users/{user_id}"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    user_data = response.json()

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)
    raise SystemExit(1)

except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")
    raise SystemExit(1)

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    raise SystemExit(1)

except requests.exceptions.JSONDecodeError:
    print("Invalid JSON response received.")
    raise SystemExit(1)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
    raise SystemExit(1)

print("Status Code:", response.status_code)


print("Name:", user_data["name"])
print("Email:", user_data["email"])
print("City:", user_data["address"]["city"])

posts_url = f"{BASE_URL}/posts"

params = {"userId": user_id}

try:

    posts_response = requests.get(posts_url, params=params, timeout=10)
    posts_response.raise_for_status()

    posts_data = posts_response.json()

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)
    raise SystemExit(1)

except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")
    raise SystemExit(1)

except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
    raise SystemExit(1)

except requests.exceptions.JSONDecodeError:
    print("Invalid JSON response received.")
    raise SystemExit(1)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
    raise SystemExit(1)

print("Posts Status Code:", posts_response.status_code)
print("Total Posts:", len(posts_data))

if posts_data:
    print("First Post:", posts_data[0])

    print("\nAll Posts:")

    for post in posts_data:
        print("\nPost ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])
else:
    print("No posts found for this user.")
