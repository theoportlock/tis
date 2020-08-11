FROM archlinux
COPY . /app
RUN pacman -Syu
RUN pacman -S python3
