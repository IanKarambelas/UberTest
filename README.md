Email Service - Backend

I chose Backend because I have had limited experience with frontend and web applications as my education was in computer engineering.

I spent far too long trying to get Django up and running for a rudimentary frontend. As I had no prior knowledge, it consisted mostly of reading the specs and API. If I had to do it over again, I would have a lot better idea of what I need to do in order to get a simple web page to accept user entered data.

The relevant file you're looking for is emailservice/emailapp/email.py

I had trouble trying to get Apache/Django up and running on an Amazon EC2 instance, so the function that actual sends an email and falls back to a second service in case of failure (i.e. the backend) is the only thing functional. Most everything else is boilerplate, generated by the webframework, except where noted.
