# Base image
FROM alpine:3.8

# Copy root filesystem
COPY rootfs /

# Copy Python requirements file
COPY requirements.txt /tmp/

# ENV
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2
ENV VERSION="0.6.1"

# Build
RUN \
    apk add --no-cache \
    apache2-utils=2.4.35-r0 \
    apk-tools=2.10.1-r0 \
    bash=4.4.19-r1 \
    ca-certificates=20171114-r3 \
    curl=7.61.1-r1 \
    nginx=1.14.2-r0 \
    python3=3.6.6-r0 \
    \
    && pip3 install --no-cache-dir -r /tmp/requirements.txt \
    \
    && rm -f -r /tmp/* \
    \
    && curl -L -s https://github.com/just-containers/s6-overlay/releases/download/v1.21.7.0/s6-overlay-amd64.tar.gz \
        | tar xvzf - -C / \
    \
    && python3 /opt/store/setup.py install

# Entrypoint
ENTRYPOINT [ "/init" ]

# Arguments
ARG BUILD_DATE

# Labels
LABEL \
    maintainer="Joakim Sørensen @ludeeus <ludeeus@gmail.com>" \
    org.label-schema.description="Easy manage custom_components for Home Assistant." \
    org.label-schema.name="custom-component-store" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/ludeeus/custom-component-store" \
    org.label-schema.usage="https://github.com/ludeeus/custom-component-store/blob/master/README.md"