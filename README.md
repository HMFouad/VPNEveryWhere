# VPNEveryWhere
VPNEveryWhere

Dans ce projet intitulé VPN EveryWhere, notre travail était de développer un logiciel facilitant la configuration du client OpenVPN
afin de simplifier l'utilisation aux différents utilisateurs quelques soit leurs niveaux en informatique, afin de pouvoir se 
connecter au serveur OpenVPN l'utilisateur devrait configurer le client installé sur sa machine à chaque connexion et cette tache 
n'est pas faisable pour le grand public.

Dans ce but on a rendu la configuration du client OpenVPN de FDN automatique en créant une interface, simple et facile à utiliser, 
il suffit juste de cliquer sur le bouton Connect et tout le travail nécessaire pour la configuration du client OpenVPN jusqu'au 
lancement de la connexion avec le serveur se fait automatiquement, et pour cela la bibliothèque scan qui contient les différents 
type de scan de ports(socket, avec et sans thread, en TCP et en UDP) récupère l'adresse du serveur à partir du fichier de 
configuration afin que scan des port se lance jusqu'à ce qu'il trouve un port ouvert ou non si tout les ports sont fermés, 
tout en commençant par le scan UDP et après on passe au scan TCP en respectant l'heuristique qu'on a mis en place en créant trois 
niveaux de priorité pour rendre le scan vite tout en dépendant du serveur et des ports ouverts en commençant par le niveau 1 qui 
contient les port les plus connus, après on passe au niveau 2 qui contient les ports qu'on a déjà trouvé ultérieurement et qui 
n'appartiennent pas au niveau 1 et qui se mis à jour à chaque fois où on tombe sur un port ouvert qui n'existe dans cette liste et 
après y a le niveau 3 qui contient tout les port possible.

Après avoir trouver un port ouvert le scan des port s'arrête et le fichier de configuration se mis à jour en écrivant le numéro de 
port ouvert trouvé et le protocole utilisé UDP ou TCP, et le client OpenVPN se lance automatiquement en prenant le fichier de 
configuration qui contient tout les informations nécessaire.
