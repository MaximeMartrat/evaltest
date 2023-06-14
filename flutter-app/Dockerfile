FROM ubuntu:latest

# Installer les dépendances nécessaires pour Flutter
RUN apt-get update
RUN apt-get install -y curl git wget unzip libgconf-2-4 gdb libstdc++6 libglu1-mesa fonts-droid-fallback lib32stdc++6 python3 sed
RUN apt-get clean

# Installer Flutter
RUN git clone https://github.com/flutter/flutter.git /usr/local/flutter
ENV PATH="/usr/local/flutter/bin:${PATH}"

# Activer Flutter Web
RUN flutter channel beta
RUN flutter upgrade
RUN flutter config --enable-web

WORKDIR /app
