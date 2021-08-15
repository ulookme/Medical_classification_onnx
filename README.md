# Medical Image Classification Using the MedNIST Dataset

Using Pytorch and Flask
Contexte
L'entreprise a remporté un appel d'offre du CHRU de Nancy pour la réalisation d'un POC (Proof Of Concept) d'une solution IA capable de classer les images radios en six catégories.
L'objectif est de prouver les compétences techniques de votre start-up à mener à bien ce projet et faire adhérer le corps médical au projet Health Data Hub.
Le Health Data Hub étant en cours de mise en œuvre, l'entreprise utilise le dataset MedNIST.
Une première version a été développée en Pytorch (MedNet by NVIDIA) et Flask. Il s'agit d'une interface simple pour sélectionner une image en local et lancer le modèle pour prédire sa classe.
Nous avons comme mission d'améliorer le modèle MedNet (en modifiant ses paramètres ou en utilisant une autre architecture) et d'ajouter une fonctionnalité qui permet de sélectionner un ensemble d'images et de les classer dans le dossier approprié en utilisant le modèle amélioré.
L'utilisation de l'intelligence artificielle (IA), et des réseaux neuronaux convolutionnels profonds (RNC) en particulier, a conduit à des améliorations de la vitesse de traitement et de diagnostic des images radiologiques. Les algorithmes de pointe sont comparables à la norme de soins actuelle. Les meilleurs experts humains surpassent toujours l'IA, de sorte que les technologies en cours de développement servent de complément aux médecins et aux chercheurs, et non de remplacement.


## Requirements

Install them from `requirements.txt`:

    pip install -r requirements.txt


## Local Deployment

Run the server:

    python app.py


## License

The mighty MIT license. Please check `LICENSE` for more details.
