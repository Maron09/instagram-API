# Instagram API

This project provides an API for retrieving profile information and media details from Instagram. It's built using **FastAPI** framework, allowing for efficient and scalable web services. The API endpoints are designed to fetch profile information and media details based on usernames and URLs respectively.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/maron09/Instagram-API.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the server:
    ```bash
    fastapi dev <name_of_py_file>
    ```
    or:
    ```bash
    python <name_of_py_file>
    ```

## Endpoints

### 1. Profile Info
- **Endpoint:** `/v1/api/profile`
- **Method:** `GET`
- **Description:** Retrieves profile information for a given username.
- **Query Parameters:**
    - `username`: Username of the profile to retrieve.
- **Example:**
    ```bash
    GET /v1/api/profile?username=johndoe
    ```

### 2. Media Details
- **Endpoint:** `/v1/api/media`
- **Method:** `GET`
- **Description:** Retrieves details of media based on the provided URL.
- **Query Parameters:**
    - `url`: URL of the media to retrieve details for.
- **Example:**
    ```bash
    GET /v1/api/media?url=https://www.instagram.com/p/ABC123/
    ```

## Middleware

A custom middleware `TimeoutMiddleware` is included to set a global timeout of 60 seconds for requests. This helps in handling requests more efficiently, preventing potential bottlenecks or long-running processes.

## Usage

To use the API, simply make HTTP requests to the specified endpoints with appropriate parameters. The API will return JSON responses containing the requested data.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for any improvements or bug fixes.
