# HTTP Request Inspector (Python)

A simple Python-based HTTP request inspector built using raw sockets.
This tool captures incoming HTTP requests and displays their structure such as method, path, headers, and body.

The purpose of this project is to help beginners understand how HTTP works internally without relying on frameworks like Flask or Django.

This project is also designed as a learning step toward building web security tools.

---

# Features

* Capture raw HTTP requests
* Display request method (GET, POST, etc.)
* Display request path
* Display HTTP headers
* Show raw request data
* Identify client IP address

---

# Technologies Used

* Python 3
* socket (TCP networking)
* basic HTTP protocol parsing

---

# How It Works

The script acts as a simple TCP server that listens for incoming HTTP connections.

Workflow:

Client (Browser / curl)
↓
TCP connection established
↓
Python socket server receives request
↓
Server reads raw HTTP data
↓
Server parses request line and headers
↓
Request information is printed to terminal

The server does not process the request like a normal web server.
Instead, it focuses on **inspecting and analyzing the request structure**.

---

# Installation

Clone this repository:

```
git clone https://github.com/yourusername/http-request-inspector.git
cd http-request-inspector
```

Make sure Python is installed:

```
python --version
```

---

# Usage

Run the script:

```
python main.py
```

The server will start listening:

```
Listening on port 8080
```

---

# Testing the Inspector

You can test the inspector using curl.

Example GET request:

```
curl http://localhost:8080/test
```

Example POST request:

```
curl -X POST http://localhost:8080/login -d "username=admin&password=123"
```

---

# Example Output

```
Connection from ('127.0.0.1', 52312)

----- RAW REQUEST -----
POST /login HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.88
Content-Length: 27
Content-Type: application/x-www-form-urlencoded

username=admin&password=123

----- PARSED DATA -----
Method: POST
Path: /login
HTTP Version: HTTP/1.1

Headers:
Host: localhost:8080
User-Agent: curl/7.88
Content-Type: application/x-www-form-urlencoded
```

---

# Project Structure

```
http-request-inspector
│
├── main.py
└── README.md
```

---

# Limitations (Current Version)

This project is intentionally simple and has several limitations:

* Only reads the first 4096 bytes of a request
* No concurrency (handles one connection at a time)
* No structured request logging
* No request body parsing
* No security detection

These limitations are intentional to keep the first version focused on understanding HTTP basics.

---

# Future Development

This project will evolve into a more advanced HTTP inspection and security analysis tool.

Planned features:

### 1. HTTP Request Parser

Convert headers and request body into structured data (dictionary / JSON).

### 2. Request Logging System

Store requests into log files with timestamps and IP addresses.

### 3. Attack Detection

Detect common attack patterns such as:

* SQL Injection
* Cross-Site Scripting (XSS)
* Path Traversal

### 4. Web Dashboard

Create a simple monitoring interface using Flask to visualize incoming requests.

### 5. Request Replay Tool

Allow users to resend captured requests for testing purposes.

### 6. Traffic Analytics

Analyze traffic patterns such as:

* most active IPs
* most requested endpoints
* suspicious behavior

---

# Learning Goals

This project helps developers understand:

* how HTTP requests work internally
* how TCP socket servers operate
* how web security tools analyze traffic
* the fundamentals behind tools like Burp Suite and request interceptors

---

# Educational Purpose

This project is built for educational purposes to help students and beginners explore networking and web security concepts.

---

# License

MIT License
