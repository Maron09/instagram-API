
![9ffeb9de-f118-4fc1-8725-5ec2f075bf8e](https://github.com/Maron09/instagram-API/assets/107930543/43e09586-c841-4ec8-8b63-7e0eac67d82f)


# Instagram API

## Overview

Instagram API is a FastAPI-based application that provides various endpoints to interact with Instagram's functionalities, including user authentication, profile information retrieval, post metrics, and media details. The service incorporates middleware for timeout handling and authentication.

## Features

- **User Login:** Authenticate users using their Instagram credentials.
- **Profile Information:** Retrieve profile information for a given username.
- **User Posts:** Fetch post metrics for a specified user within optional date ranges.
- **Media Details:** Obtain details of a specific media post using its URL.
- **Media Likers:** Get the list of users who liked a particular media post.

## Endpoints

### 1. User Login
**URL:** `/v1/api/login`  
**Method:** `POST`  
**Description:** Authenticates a user with their Instagram credentials.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "message": "Login Successful",
  "username": "string"
}
```

### 2. Profile Information
**URL:** `/v1/api/profile`  
**Method:** `GET`  
**Description:** Retrieves profile information for a given username.

**Query Parameters:**
- `username` (required): The username of the profile to retrieve.

**Response:**
```json
{
  "profile_data": { /* Profile information */ }
}
```

### 3. User Posts
**URL:** `/v1/api/user_posts`  
**Method:** `GET`  
**Description:** Fetches post metrics for a specified user within optional date ranges.

**Query Parameters:**
- `username` (required): The username to retrieve posts for.
- `from_date` (optional): Start date for post retrieval (YYYY-MM-DD).
- `to_date` (optional): End date for post retrieval (YYYY-MM-DD).

**Response:**
```json
{
  "posts": [ /* List of posts */ ]
}
```

### 4. Media Details
**URL:** `/v1/api/media`  
**Method:** `GET`  
**Description:** Retrieves details of a specific media post using its URL.

**Query Parameters:**
- `url` (required): The URL of the media to retrieve details for.

**Response:**
```json
{
  "media_details": { /* Media details */ }
}
```

### 5. Media Likers
**URL:** `/v1/api/media_likers`  
**Method:** `GET`  
**Description:** Gets the list of users who liked a particular media post.

**Query Parameters:**
- `media_id` (required): The media ID in the format `{post_id}_{owner_id}`.
- `username` (required): The username of the logged-in user.

**Response:**
```json
{
  "likers": [ /* List of likers */ ]
}
```

## Middleware

### TimeoutMiddleware
Handles request timeouts. The timeout is set to 600 seconds.

### AuthenticationMiddleware
Handles authentication using the Instagram service.



## Packages Used
This project makes use of several third-party libraries:
* Instaloader: A tool to download pictures (or videos) along with their captions and other metadata from Instagram.
* Instagpy: An Instagram automation tool.
* Instagrapi: A fast and effective Instagram Private API wrapper (compatible with Python 3.7+).


## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/maron09/instagram-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd instagram-api
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   fastapi dev main.py
   ```

## Usage

Access the API endpoints at `http://127.0.0.1:8000`. Use tools like `curl`, Postman, or any HTTP client to interact with the endpoints.

## Author

**maron09**

GitHub: [maron09](https://github.com/maron09)
