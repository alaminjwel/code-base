# Docker Custom NGINX
# In the Bash script, write a program that creates a file named Dockerfile. The contents of the Dockerfile should have the following commands:

# 1. Set the base image to nginx:latest and expose port 80.

# 3. Copy a custom HTML file named index.html from the current directory to the container's /usr/share/nginx/html/ directory.

# 4. Copy a custom error page named error.html from the current directory to the container's /usr/share/nginx/html/ directory.

# 5. Replace the default Nginx configuration file (/etc/nginx/conf.d/default.conf) with a custom configuration file named nginx.conf from the current directory.

# 6. Set an environment variable named NGINX_ENV with the value custom.

# Print the contents of your Dockerfile at the end.
# =====================================================================================================================




#!/bin/bash

# Define the content of the Dockerfile
DOCKERFILE_CONTENT=$(cat <<EOF
FROM nginx:latest

EXPOSE 80

COPY index.html /usr/share/nginx/html/
COPY error.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf

ENV NGINX_ENV=custom
EOF
)

# Create a Dockerfile
echo "$DOCKERFILE_CONTENT" > Dockerfile

# Print the contents of the Dockerfile
cat Dockerfile