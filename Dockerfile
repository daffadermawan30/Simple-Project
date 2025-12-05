FROM dorowu/ubuntu-desktop-lxde-vnc

# Hapus repo Chrome yang broken (penyebab apt-get update gagal)
RUN rm -f /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-tk && \
    pip3 install customtkinter pillow tkcalendar

WORKDIR /app
COPY BetaFintrack.py /app/

CMD ["python3", "BetaFintrack.py"]
