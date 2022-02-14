FROM alpine

RUN apk update && \
    apk add --no-cache build-base \
        python3-dev \
        python3 \
        libc-dev \
        libffi-dev \
        chromium \
        chromium-chromedriver \
        curl \ 
        bash && \
    python3 -m ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    pip3 install --upgrade pip wheel selenium && \
    rm -r /root/.cache

WORKDIR /usr/src/app
COPY . .
RUN chmod 0775 wait.sh 
