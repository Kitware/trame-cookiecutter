FROM kitware/trame

# Create the /deploy directory with trame-user as the owner
RUN install -d -o trame-user -g trame-user /deploy

# Copy the server directory
COPY --chown=trame-user:trame-user ./server /deploy/server
