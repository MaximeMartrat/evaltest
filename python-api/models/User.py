import bcrypt

class User:
    def __init__(self, nom, prenom, pseudo, email, telephone, section):
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.telephone = telephone
        self.section = section
        self.password_hash = None

        def get_full_name(self):
            return f"{self.prenom} {self.nom}"

        def set_password(self, password):
            # Hasher le mot de passe et le stocker sous forme de hachage sécurisé
            self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        def check_password(self, password):
            # Vérifier si le mot de passe fourni correspond au mot de passe haché stocké
            return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
