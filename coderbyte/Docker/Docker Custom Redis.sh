# Docker Compose Rails Project
# In this project, you will be editing the docker-compose.yml file so that this application builds properly.

# First, the file should contain two services, db and web. The database service should contain the following directives with their corresponding values:

# image should be postgres, volumes should be set to ./tmp/db:/var/lib/postgresql/data, environment should contain POSTGRES_PASSWORD which is set to password123.

# Then the web service should contain the following directives with their corresponding values:

# build should be ., the command to start the application should be set to bundle exec rails s -p 3000 -b '0.0.0.0', ports should be set to "3000:3000", and finally depends_on should be set to db.

# Finally, print the contents of the docker-compose.yml.
#=================================================================================================================


#!/bin/bash

# Define the content of the Dockerfile
DOCKERFILE_CONTENT=$(cat <<EOF
FROM redis:7.0.11

EXPOSE 6379

COPY my_redis.conf /usr/local/etc/redis/redis.conf

ENV REDIS_ENV=custom

RUN mkdir /data && chown redis:redis /data

USER redis

CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
EOF
)

# Create a Dockerfile
echo "$DOCKERFILE_CONTENT" > Dockerfile

# Print the contents of the Dockerfile
cat Dockerfile
