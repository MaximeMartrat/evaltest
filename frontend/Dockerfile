FROM debian:latest AS build-env
# Install flutter dependencies
RUN apt-get update
RUN apt-get install -y curl git wget unzip libgconf-2-4 gdb libstdc++6 libglu1-mesa fonts-droid-fallback lib32stdc++6 python3 sed
RUN apt-get clean


# Configurez l'environnement Flutter
ENV ANDROID_SDK_ROOT /opt/android-sdk
ENV PATH $PATH:$ANDROID_SDK_ROOT/platform-tools:$ANDROID_SDK_ROOT/tools/bin

# Fixer les autorisations du répertoire Flutter
RUN mkdir -p /opt/flutter
RUN chown -R flutteruser:flutteruser /opt/flutter

# Téléchargez et installez Flutter
RUN git clone https://github.com/flutter/flutter.git /opt/flutter
ENV PATH $PATH:/opt/flutter/bin

# Acceptez les licences Android SDK
RUN yes | flutter doctor --android-licenses

# Exécutez Flutter doctor pour vérifier l'installation
RUN flutter doctor

# Clonez votre projet GitHub
RUN git clone https://github.com/MaximeMartrat/evaltestfrontend /app

# Accédez au répertoire du projet
WORKDIR /app

# Créez un nouvel utilisateur pour exécuter Flutter
RUN adduser --disabled-password --gecos '' flutteruser
RUN chown -R flutteruser:flutteruser /app

# Définissez l'utilisateur nouvellement créé comme utilisateur actif
USER flutteruser

RUN flutter build apk
# Exécutez le serveur de développement Flutter
CMD ["flutter", "run"]