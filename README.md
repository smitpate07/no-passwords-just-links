
## Overview ##

In this repository, you'll learn how to securely share files or credentials by generating presigned URLs using n8n and AWS services. By using presigned URLs, you avoid the risky practice of sending sensitive information (like passwords) in emails, which can be intercepted by malicious actors.

Instead of exposing sensitive data in email bodies, presigned URLs allow recipients to access resources securely via time-limited links. This ensures that your files or credentials are shared only with authorized users, without compromising security.

## Why Use Presigned URLs? ##

**Security:** Presigned URLs ensure that sensitive information is not exposed directly in emails. Only users with the presigned link can access the resource, and the URL is valid for a limited time.

**Best Practice:** Avoid the common security risk of sharing passwords or private data through unencrypted email channels.

## High Level flow ##
<img width="903" height="326" alt="Overall_architecture" src="https://github.com/user-attachments/assets/8ca3fce3-68c7-4720-9c23-47669009b120" />


## Flow Steps ##

1. User uploads 
