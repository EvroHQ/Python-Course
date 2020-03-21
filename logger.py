import logging

logging.basicConfig(level=logging.WARNING,
                    filename="app.log",
                    filemode="w",
                    format='%(asctime)s | %(levelname)s : %(message)s')

logging.debug("La fonction a bien été exécutée.")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivee")
logging.critical("Erreur critique")