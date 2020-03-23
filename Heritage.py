projects = ["pr_Financials", "FrontEnd", "BackEnd", "pr_credits"]

class admin:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"User {self.nom} {self.prenom}"

    def show_projects(self):
        for project in projects:
            print(project)

class user(admin):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
    
    def show_projects(self):
        for project in projects:
            if not project.startswith("pr_"):
                print(project)

Chris = user("Chris", "Kirk")
Chris.show_projects()