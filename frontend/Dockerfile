FROM ubuntu:20.10 as builder
RUN apt update && apt install -y curl git unzip xz-utils zip libglu1-mesa openjdk-8-jdk wget


# Configurez l'environnement Flutter
ENV ANDROID_SDK_ROOT /opt/android-sdk
ENV PATH $PATH:$ANDROID_SDK_ROOT/platform-tools:$ANDROID_SDK_ROOT/tools/bin

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

# Exécutez la compilation du projet Flutter
RUN flutter build apk

# Exécutez le serveur de développement Flutter
CMD ["flutter", "run"]