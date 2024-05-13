from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cabinet_info = {
        "nom": "TriPhD Consulting",
        "adresse": "123 Rue de la Science, 75000 Paris, France",
        "telephone": "+33 1 23 45 67 89",
        "email": "contact@triphdconsulting.com",
        "site_web": "www.triphdconsulting.com",
        "services": [
            {
                "nom": "Consultation économique avancée",
                "description": "Analyse économique approfondie des marchés, des tendances et des opportunités. Modélisation économique pour prédire les impacts des politiques, des investissements et des changements de marché. Conseils stratégiques pour les entreprises, les gouvernements et les organisations à but non lucratif."
            },
            {
                "nom": "Services de communication spécialisés",
                "description": "Rédaction professionnelle et éditoriale en anglais pour une variété de documents, y compris les rapports, les présentations et les publications académiques. Traduction de documents techniques et commerciaux dans et depuis l'anglais. Formation à la communication professionnelle et à la rédaction académique."
            },
            {
                "nom": "Développement de logiciels sur mesure",
                "description": "Conception, développement et maintenance de logiciels personnalisés pour répondre aux besoins spécifiques des entreprises. Analyse et optimisation de systèmes logiciels existants. Conseils en architecture logicielle et en technologies émergentes."
            },
            {
                "nom": "Intégration de données et analyse avancée",
                "description": "Intégration de données à grande échelle à partir de sources multiples pour fournir des insights approfondis. Analyse statistique avancée et modélisation prédictive pour prendre des décisions informées. Visualisation de données interactives pour présenter les résultats de manière claire et compréhensible."
            },
            {
                "nom": "Formation spécialisée",
                "description": "Cours et ateliers sur l'économie, l'anglais professionnel et le génie logiciel pour les professionnels et les étudiants. Coaching personnalisé pour améliorer les compétences dans ces domaines spécifiques."
            }
        ]
    }
    return render_template('index.html', cabinet=cabinet_info)

if __name__ == '__main__':
    app.run(debug=True)
