from career_data import careers_df


def recommend_careers(student_interest, student_skills):

    results = []

    for _, career in careers_df.iterrows():

        score = 0

        # Interest matching
        if student_interest == career["Interest"]:
            score += 60

        # Skill matching
        required_skills = career["Skills"]

        matching_skills = set(student_skills).intersection(
            required_skills
        )

        if required_skills:
            score += (
                len(matching_skills) / len(required_skills)
            ) * 40

        results.append({
            "Career": career["Career"],
            "Match Score": round(score),
            "Matching Skills": list(matching_skills),
            "Skills to Learn": [
                skill for skill in required_skills
                if skill not in student_skills
            ]
        })

    results.sort(
        key=lambda item: item["Match Score"],
        reverse=True
    )

    return results[:3]