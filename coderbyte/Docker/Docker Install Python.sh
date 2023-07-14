# In the Bash script, write a program that creates a file named Dockerfile. The contents of the Dockerfile should have the following commands:

# First, the base image should install python3 via the FROM command. Then the rest of the Dockerfile should look like the following:

# RUN pip install {{MODULES}}
# CMD ["python", {{FILENAME}}]

# {{MODULES}} should be replaced with the modules: numpy, scipy, and pandas all on one line. {{FILENAME}} should be replaced with ./main.py

# Then your bash script should print the SHA1 hash of the contents of Dockerfile so that the output looks something like: HASH_OUTPUT Dockerfile
# ==============================================================================================================================





#!/bin/bash

# Define the content of the Dockerfile
DOCKERFILE_CONTENT=$(cat <<EOF
FROM python:3
RUN pip install numpy scipy pandas
CMD ["python", "./main.py"]
EOF
)

# Create a Dockerfile
echo "$DOCKERFILE_CONTENT" > Dockerfile

# Compute the SHA1 hash of the Dockerfile
HASH_OUTPUT=$(sha1sum Dockerfile)

echo "$HASH_OUTPUT"
