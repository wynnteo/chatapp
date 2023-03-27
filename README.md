# Chatapp with Django, React, and Channels

This is an example chat application built with Django, React, and Django Channels. The application uses websockets to enable real-time communication between clients.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker

### Installing

1. Clone the repository:

`git clone https://github.com/wynnteo/chatapp.git` <br/>
`cd chatapp`

2. Build the Docker images:

`docker-compose build`

3. Run the Docker containers:

`docker-compose up`

This will start the Django development server and the React development server.

4. Access the chatapp:

http://localhost <br/>
This will open the chatapp in your browser.

### Usage

Once you have the chatapp running, you can open multiple browser windows to simulate different clients. When you send a message from one client, all other clients that are connected to the same chatroom will receive the message in real-time.

### Author

Wynn Teo
