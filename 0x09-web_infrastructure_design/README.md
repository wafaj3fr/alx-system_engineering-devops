#0x09. Web infrastructure design
DevOps
SysAdmin
web infrastructure


Server:

A server is a powerful computer program or physical device dedicated to providing services and resources to other computers (clients) over a network.

Servers act as central repositories for data, applications, and other resources that clients can access and utilize.

Examples of server types include web servers, email servers, file servers, database servers, and application servers.

Domain Name:

A domain name is a human-readable text label (like "google.com") that acts as an alias for a website's underlying numerical address, known as an Internet Protocol (IP) address.

Domain names provide a memorable and user-friendly way to access websites instead of having to remember complex IP addresses.

Behind the scenes, a Domain Name System (DNS) translates domain names into their corresponding IP addresses, enabling users to access websites seamlessly.

Type of DNS record: www in www.foobar.com

The "www" in "www.foobar.com" is a subdomain, typically configured in a DNS A record to point to the web server hosting the website's content.

DNS A records map domain names or subdomains to IP addresses, allowing requests to be routed to the correct server.

While not strictly necessary, including "www" has been a longstanding convention, though website owners can choose to omit it and configure their domain's root directly as the web server's IP.

Web Server:

A web server is a specialized type of server that stores and delivers web pages and related content (images, CSS, JavaScript) to clients' web browsers upon request.

It acts as the front-end of a website, directly responding to HTTP (Hypertext Transfer Protocol) requests from users.

Common web servers include Apache, Nginx, and Microsoft IIS.

Application Server:

An application server is a software program that runs on a server and manages the execution of web applications or other complex software applications.

It provides an environment for application logic (code execution) and facilitates interaction with databases, external services, and the web server.

Examples of application servers include Tomcat, JBoss, and WebLogic Server.

Database:

A database is an organized collection of structured data that is electronically stored and managed.

Web applications often use databases to store and retrieve information (e.g., user accounts, product data, news articles).

Different types of databases exist, each with its own strengths and use cases (relational databases like MySQL, NoSQL databases like MongoDB).

Communication between servers and clients:

Servers use the TCP/IP (Transmission Control Protocol/Internet Protocol) suite to communicate with clients over the internet.

TCP ensures reliable data delivery, while IP provides the addressing mechanism for routing packets across the network.

HTTP, a protocol specifically designed for web communication, is built on top of TCP/IP for transmitting web pages and other web content.

### tasks:

## Simple web stack

## Distributed web infrastructure

## Secured and monitored web infrastructure
