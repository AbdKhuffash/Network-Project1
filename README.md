
## Overview
This rapsority contains a project aimed at network diagnostics and server-client interaction. It encompasses various functionalities including ping, trace route, name server lookup, and server-client communication. Below is a brief overview of the project parts:

### Part 1: Network Diagnostics
Ping: Measures the time it takes to transfer data between client and host.

Tracert (Trace Route): Shows the path packets take and the time taken.

Nslookup (Name Server Lookup): Retrieves DNS information for a domain or IP.

Telnet: Enables remote access to servers or devices over a network.

### Part 2: Server-Client Interaction
The server, written in Python using socket programming, listens on port 8855.

Clients send messages containing their names to the server every two seconds.

The server echoes the last received message and its timestamp to all clients.

### Part 3: Web Server
Implements a TCP server with defined port.

Responds to requests for specific HTML, CSS, image, or redirection files.

Handles various cases including serving localized content, redirection, and error handling.

## Usage
Detailed instructions on how to use each part of the project can be found within their respective sections.

