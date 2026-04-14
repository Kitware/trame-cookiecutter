FROM kitware/trame:uv

# Set Python and Vue versions
ENV TRAME_PYTHON=3.12
ENV TRAME_CLIENT_TYPE=vue3

# -------------------------------------------------------------------
# !!! Using path from root diretory !!!
# -------------------------------------------------------------------
# Copy the local app and the deploy directory when using local
# directory (./setup/initialized.sh) instead of
# a published package (./setup/requirements.txt)
# => use one or the other
COPY --chown=trame-user:trame-user . /local-app
COPY --chown=trame-user:trame-user ./examples/docker/setup /deploy/setup
# -------------------------------------------------------------------

RUN /opt/trame/entrypoint.sh build
