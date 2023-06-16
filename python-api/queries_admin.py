insert_admin_formateur_false = "INSERT INTO administrateur (nomAdmin, prenomAdmin, pseudoAdmin, emailAdmin, telephoneAdmin, passwordAdmin,  id_section_FK) values (%s, %s, %s, %s, %s, %s, %s)"

insert_admin_formateur_true = "INSERT INTO administrateur (nomAdmin, prenomAdmin, pseudoAdmin, emailAdmin, telephoneAdmin, passwordAdmin, id_formateur_FK, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s, %s)"
