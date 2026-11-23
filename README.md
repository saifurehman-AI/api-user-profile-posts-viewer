# API User Profile & Posts Viewer

A Python project that uses the Requests library to retrieve user profiles and their associated posts from a REST API.

## Features

- Accepts User ID from the user.
- Validates User ID (1-10).
- Retrieves user profile information.
- Displays user's name, email, and city.
- Retrieves posts using query parameters.
- Displays post IDs, titles, and bodies.
- Handles HTTP errors.
- Handles timeout errors.
- Handles connection errors.
- Handles invalid JSON responses.
- Handles empty posts lists.

## Technologies Used

- Python
- Requests Library
- REST API
- JSON

## API Used

JSONPlaceholder

https://jsonplaceholder.typicode.com

## Project Structure

```text
api_user-posts-viewer/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

First, install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Run the Python file using:

```bash
python main.py
```

Enter a User ID between 1 and 10 when prompted.

## API Endpoints

### 1. User Profile

HTTP Method: GET

```text
https://jsonplaceholder.typicode.com/users/{user_id}
```

Retrieves the selected user's profile information.

### 2. User Posts

HTTP Method: GET

```text
https://jsonplaceholder.typicode.com/posts?userId={user_id}
```

Retrieves all posts associated with the selected user.

## Example

Input:

```text
Enter User ID (1-10): 2
```

Output:

```text
Status Code: 200
Name: Ervin Howell
Email: Shanna@melissa.tv
City: Wisokyburgh

Posts Status Code: 200
Total Posts: 10
```

The program also displays the titles and bodies of all retrieved posts.

## Error Handling

The project handles the following errors:

- HTTP errors (4xx and 5xx).
- Request timeout.
- Connection errors.
- Invalid JSON responses.
- Invalid user input.
- Empty posts responses.

## Project Status

Core project implementation and API testing completed.