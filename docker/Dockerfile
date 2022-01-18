FROM vyahello/pypi-base:0.1.0
LABEL version=0.1.0 \
      metadata="The main image for fast weather api application" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
ARG VERSION
ENV CODE_DIR="/app" \
    IMAGE_REPO="vyahello/pypi" \
    SERVER_PORT=8080 \
    IMAGE_VERSION=${VERSION}
WORKDIR ${CODE_DIR}
COPY pypi pypi
COPY requirements.txt docker/entry.sh ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
ENTRYPOINT ["/app/entry.sh"]
