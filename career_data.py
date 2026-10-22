import pandas as pd

career_data = [
    {
        "Career": "AI/ML Engineer",
        "Interest": "Artificial Intelligence",
        "Skills": ["Python", "Machine Learning", "SQL"]
    },
    {
        "Career": "Software Developer",
        "Interest": "Software Development",
        "Skills": ["Python", "C++", "Java"]
    },
    {
        "Career": "Data Analyst",
        "Interest": "Data Analysis",
        "Skills": ["Python", "SQL", "Excel"]
    },
    {
        "Career": "Web Developer",
        "Interest": "Web Development",
        "Skills": ["HTML", "CSS", "JavaScript"]
    },
    {
        "Career": "Cybersecurity Analyst",
        "Interest": "Cybersecurity",
        "Skills": ["Python", "SQL", "Networking"]
    }
]

careers_df = pd.DataFrame(career_data)