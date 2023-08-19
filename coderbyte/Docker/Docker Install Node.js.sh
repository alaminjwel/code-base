# Docker Install Node.js
# In the Bash script, write a program that creates a file named Dockerfile. The contents of the Dockerfile should have the following commands:

# First, the base image should install node:18-alpine. Then set the WORKDIR to be /app

# When you are in the working directory, run yarn install with a --production flag. Finally, use CMD with parameters ["node", "src/index.js"] and expose the container to port 3000.

# Print the contents of your Dockerfile at the end.
# ============================================================================================================


#!/bin/bash

# Define the content of the Dockerfile
DOCKERFILE_CONTENT=$(cat <<EOF
FROM node:18-alpine

WORKDIR /app

RUN yarn install --production

EXPOSE 3000

CMD ["node", "src/index.js"]
EOF
)

# Create a Dockerfile
echo "$DOCKERFILE_CONTENT" > Dockerfile

# Print the contents of the Dockerfile
cat Dockerfile



