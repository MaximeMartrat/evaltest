from models.User import User
import bcrypt

class Apprenant(User):
    def __init__(self, nom, prenom, pseudo, adresse, rib, secu, email, telephone, formation, section):
        super().__init__(nom, prenom, pseudo, email, telephone, section)
        self.adresse = adresse
        self.rib = rib
        self.secu = secu
        self.formation = formation
        self.password_hash = None

    def set_password(self, password):
        # Hasher le mot de passe et le stocker sous forme de hachage sécurisé
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        # Vérifier si le mot de passe fourni correspond au mot de passe haché stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
