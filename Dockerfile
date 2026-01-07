FROM dorowu/ubuntu-desktop-lxde-vnc

RUN rm -f /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-tk && \
    pip3 install --no-cache-dir customtkinter pillow tkcalendar && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app/

COPY fintrack.conf /etc/supervisor/conf.d/

RUN chmod -R 777 /app
