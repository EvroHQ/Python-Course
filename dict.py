employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            
### Patrick est partit
del employes["id03"]

### Julie a maintenant 26 ans
employes["id02"]["age"] = 26

### Paul fêtera son anniversaire la semaine prochaine (on récupère son âge)
age_paul = employes["id01"]["age"]