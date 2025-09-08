FROM kitware/trame:uv

# Set Python and Vue versions
ENV TRAME_PYTHON=3.13
ENV TRAME_CLIENT_TYPE=vue3

# Copy the local app and the deploy directory
COPY --chown=trame-user:trame-user . /local-app
COPY --chown=trame-user:trame-user ./bundles/docker /deploy

RUN /opt/trame/entrypoint.sh build
