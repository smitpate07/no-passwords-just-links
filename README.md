
## Overview ##

In this repository, you'll learn how to securely share files or credentials by generating presigned URLs using n8n and AWS services. By using presigned URLs, you avoid the risky practice of sending sensitive information (like passwords) in emails, which can be intercepted by malicious actors.

Instead of exposing sensitive data in email bodies, presigned URLs allow recipients to access resources securely via time-limited links. This ensures that your files or credentials are shared only with authorized users, without compromising security.

## Why Use Presigned URLs? ##

**Security:** Presigned URLs ensure that sensitive information is not exposed directly in emails. Only users with the presigned link can access the resource, and the URL is valid for a limited time.

**Best Practice:** Avoid the common security risk of sharing passwords or private data through unencrypted email channels.

## High Level flow ##
<img width="903" height="326" alt="Overall_architecture" src="https://github.com/user-attachments/assets/8ca3fce3-68c7-4720-9c23-47669009b120" />


## Flow Steps ##

1. User upload file to AWS S3 bucket.
2. AWS S3 bucket send S3 events to AWS EventBridge.
3. Based on the rules and target set in AWS Eventbridge notification is trigerred.
4. AWS EventBridge notifies N8N Webook of file arrival in AWS S3.
5. N8N Webhook trigger HTTP request.
6. N8N HTTP node sends request to AWS Lambda to generate Presigned URL with expiration time set for 1hr. AWS Lambda exposes Presigned URL to AWS API Gateway. AWS API Gateway reverts Presigend URL to N8N HTTP Node.
7. URL Generation timestamp, Expiration and URL links are set using N8N Edit Field node. Email Notification is send to the user. Generated URL Link, creation time and expiration time is saved into MongoDB database.
   
## Screenshot of data in MongoDB  ##
<img width="1018" height="229" alt="image" src="https://github.com/user-attachments/assets/02bc9cbe-50bd-418b-9c62-0e0059284b0c" />

   
