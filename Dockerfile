# Arguments
ARG VERSION
ARG BUILD_FROM=python:3.7-slim

FROM ${BUILD_FROM}

# Set working dir
WORKDIR /app

# Gather all the files.
COPY . /app

# Build
RUN \
  pip install --trusted-host pypi.python.org -r requirements.txt

# Entrypoint
CMD ["python", "-u", "server.py"]

# Arguments
ARG BUILD_DATE

# Labels
LABEL \
    maintainer="Joakim Sørensen @ludeeus <ludeeus@gmail.com>" \
    org.label-schema.description="Easy manage custom_components for Home Assistant." \
    org.label-schema.name="custom-component-store" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/ludeeus/custom-component-store" \
    org.label-schema.usage="https://github.com/ludeeus/custom-component-store/blob/master/README.md" \