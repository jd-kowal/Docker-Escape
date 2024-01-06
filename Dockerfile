FROM ubuntu:latest


RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
    mkdir -p /etc/secret && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    echo 'CTF{Jestem słaby w hakowanie: <Twoje_Imie_i_Nazwisko>}' > /etc/secret/secret.txt && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update && chmod 700 /etc/secret/secret.txt && apt-get install -y docker-ce python3 python3-pip




RUN echo 'root:3566bf5ea52fec6eaf5d8bc513ea7659' | chpasswd

RUN useradd -ms /bin/bash adam


COPY app/ /app

RUN chown root:root -R /app

RUN chmod 770 -R /app

RUN usermod -aG docker adam


RUN pip3 install -r /app/requrements.txt

RUN echo '#!/bin/sh\n\
    dockerd &\n\
    FLASK_APP=/app/app.py flask run --host=0.0.0.0\n' > /entrypoint.sh


RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]


# Build: docker build -t ubuntu-dind .
# Run: docker run -d -p 5000:5000 --privileged --hostname ubuntu-dind --name ubuntu-dind ubuntu-dind
# Enter: docker exec -itu adam ubuntu-dind bash
