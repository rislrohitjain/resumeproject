from flask import Flask, render_template
import os

# Database Mock Logic
try:
    from database import increment_and_get_visitor_count
except ImportError:
    def increment_and_get_visitor_count():
        return 1240 

app = Flask(__name__)

@app.route('/')
def resume():
    # Centralized Configuration for Anshul Mathur
    config = {
        "name": "Anshul Mathur",
        "title": "Anshul Mathur | Business Analyst | Project Implementation",
        "email": "anshul.mathur@example.com",
        "location": "Jaipur, Rajasthan, India",
        "summary": (
            "Experienced Business Analyst with a demonstrated history of "
            "working in the information technology and services industry. Skilled "
            "in Microsoft Word, Android, Management, and Customer Service."
        ),
        "developername": "Rohit Jain",
        "skills": {
            "core": [
                "Client Interfacing",
                "Centralization",
                "Transparency",
                "Business Analysis"
            ],
            "technical": [
                "Jira Administration",
                "Microsoft Excel",
                "Microsoft PowerPoint",
                "Android"
            ],
            "methodology": [
                "Scrum Basics",
                "Project Lifecycle",
                "Requirement Gathering",
                "Documentation"
            ]
        },
        "experience": [
            {
                "role": "Analyst",
                "company": "Deloitte",
                "period": "Feb 2025 - Jan 2026",
                "desc": "Gathered project requirements, oversaw application releases, and collaborated with clients to ensure error-free delivery."
            },
            {
                "role": "Business Analyst",
                "company": "Dev Information Technology Limited",
                "period": "Dec 2019 - Oct 2024",
                "desc": "Managed business analysis workflows and stakeholder communications over a 5-year tenure in Jaipur."
            },
            {
                "role": "Business Analyst",
                "company": "Soncoya Solutions Pvt. Ltd.",
                "period": "Apr 2019 - Oct 2019",
                "desc": "Focused on requirement elicitation and business process mapping."
            },
            {
                "role": "Technical Support Engineer",
                "company": "IBM",
                "period": "Oct 2016 - Dec 2017",
                "desc": "Provided technical troubleshooting and system support within the Jaipur hub."
            }
        ],
        "education": "B.Tech in IT - Kautilya Institute of Tech. & Engg.",
        "socials": {
            "linkedin": "https://www.linkedin.com/in/anshulmathur-40186167",
            "github": "#",
            "mobile": "+91 94606 00426",
            "portfolio": "#"
        }
    }

    current_visitors = increment_and_get_visitor_count()
    return render_template('index.html', config=config, current_visitors=current_visitors)

if __name__ == '__main__':
    app.run(debug=True, port=5000)