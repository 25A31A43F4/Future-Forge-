import streamlit as st
from recommender import recommend_careers

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="FutureForge",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- PROFESSIONAL DESIGN ----------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #eef2ff 0%,
        #fdf2f8 50%,
        #eff6ff 100%
    );
}

.main .block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1 {
    color: #4338ca;
    font-weight: 800 !important;
}

h2, h3 {
    color: #3730a3;
    font-weight: 700 !important;
}

div.stButton > button {
    background: linear-gradient(90deg, #4f46e5, #9333ea);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.65rem 1.2rem;
    font-weight: bold;
    min-height: 45px;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #3730a3, #7e22ce);
    color: white;
    border: none;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: rgba(255, 255, 255, 0.75);
    border-radius: 16px;
    border: 1px solid #ddd6fe;
    padding: 12px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

div[data-testid="stTextInput"] input {
    border-radius: 10px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    "<h1 style='text-align:center;'>🚀 FutureForge</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;color:#6d28d9;'>"
    "Explore. Learn. Build Your Future."
    "</h4>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>"
    "Discover your interests, explore careers, "
    "and plan your future with confidence."
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ----------------

st.sidebar.title("🚀 FutureForge")
st.sidebar.write("Your future starts here!")

student_type = st.sidebar.radio(
    "Choose Your Education Level",
    [
        "🏫 School Student",
        "🎓 Intermediate Student",
        "💻 College Student"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "Learn new skills, explore opportunities, "
    "and take the next step towards your goals."
)

# ---------------- SCHOOL STUDENTS ----------------

if student_type == "🏫 School Student":

    st.header("🏫 School Career Explorer")

    st.write(
        "Discover what you enjoy and explore different "
        "learning and career areas."
    )

    with st.container(border=True):

        name = st.text_input("👤 Enter your name")

        student_class = st.selectbox(
            "📚 Select your class",
            list(range(1, 11))
        )

        subjects = st.multiselect(
            "📖 Which subjects do you enjoy?",
            [
                "Mathematics",
                "Science",
                "English",
                "Social Studies",
                "Computers",
                "Arts",
                "Languages"
            ]
        )

        interests = st.multiselect(
            "💡 What activities do you enjoy?",
            [
                "Solving puzzles",
                "Drawing and designing",
                "Building things",
                "Helping people",
                "Exploring nature",
                "Using computers",
                "Reading and writing",
                "Doing experiments",
                "Business activities",
                "Sports and fitness"
            ]
        )

        explore_school = st.button(
            "✨ Explore My Interests",
            use_container_width=True
        )

    if explore_school:

        if not subjects and not interests:
            st.warning(
                "Please select at least one subject or activity."
            )

        else:

            st.success(
                f"Welcome, {name if name else 'Student'}!"
            )

            st.subheader("🌟 Your Exploration Results")

            recommendations = []

            if "Mathematics" in subjects:
                recommendations.extend([
                    "Engineering and Technology",
                    "Mathematics and Logical Thinking"
                ])

            if "Science" in subjects:
                recommendations.extend([
                    "Science and Research",
                    "Environmental Science"
                ])

            if "Computers" in subjects:
                recommendations.extend([
                    "Computer Science",
                    "Artificial Intelligence",
                    "Web Development"
                ])

            interest_map = {
                "Solving puzzles": [
                    "Logical Reasoning",
                    "Programming"
                ],
                "Drawing and designing": [
                    "Graphic Design",
                    "Animation"
                ],
                "Building things": [
                    "Engineering",
                    "Robotics"
                ],
                "Helping people": [
                    "Healthcare",
                    "Teaching",
                    "Social Service"
                ],
                "Exploring nature": [
                    "Environmental Science",
                    "Wildlife Studies"
                ],
                "Using computers": [
                    "Computer Science",
                    "Artificial Intelligence"
                ],
                "Reading and writing": [
                    "Journalism",
                    "Writing and Communication"
                ],
                "Doing experiments": [
                    "Scientific Research",
                    "Science and Technology"
                ],
                "Business activities": [
                    "Business Management",
                    "Entrepreneurship"
                ],
                "Sports and fitness": [
                    "Sports Science",
                    "Sports Management"
                ]
            }

            for interest_item in interests:
                recommendations.extend(
                    interest_map.get(interest_item, [])
                )

            recommendations = list(
                dict.fromkeys(recommendations)
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Your Class",
                    f"Class {student_class}"
                )

            with col2:
                st.metric(
                    "Interests Selected",
                    len(interests)
                )

            st.write("### 🎯 Areas You Can Explore")

            for item in recommendations:
                st.markdown(f"- ✨ {item}")

            st.write("### 📚 Suggested Next Steps")

            st.markdown("""
            - Explore beginner-friendly learning resources.
            - Try small educational projects.
            - Participate in school clubs and competitions.
            - Ask teachers about subjects you enjoy.
            """)

            st.info(
                "These suggestions help you explore possibilities. "
                "You do not need to decide your final career now."
            )

# ---------------- INTERMEDIATE STUDENTS ----------------

elif student_type == "🎓 Intermediate Student":

    st.header("🎓 Intermediate Career Planner")

    st.write(
        "Explore possible courses and career paths "
        "based on your Intermediate group."
    )

    with st.container(border=True):

        name = st.text_input("👤 Enter your name")

        stream = st.selectbox(
            "📚 Select your Intermediate group",
            ["MPC", "BiPC", "MEC", "CEC", "HEC"]
        )

        interests = st.multiselect(
            "💡 Select your interests",
            [
                "Technology",
                "Programming",
                "Medicine",
                "Biology",
                "Business",
                "Finance",
                "Law",
                "Government Services",
                "Teaching",
                "Design",
                "Research"
            ]
        )

        explore_intermediate = st.button(
            "🚀 Explore Career Options",
            use_container_width=True
        )

    stream_options = {
        "MPC": [
            "Engineering",
            "Computer Science",
            "Artificial Intelligence",
            "Data Science",
            "Architecture",
            "Physical Sciences"
        ],
        "BiPC": [
            "Medicine",
            "Biotechnology",
            "Pharmacy",
            "Nursing",
            "Agriculture",
            "Life Sciences"
        ],
        "MEC": [
            "Commerce",
            "Accounting",
            "Finance",
            "Economics",
            "Business Management"
        ],
        "CEC": [
            "Commerce",
            "Law",
            "Business Administration",
            "Economics",
            "Public Administration"
        ],
        "HEC": [
            "History and Social Sciences",
            "Law",
            "Teaching",
            "Journalism",
            "Civil Services Preparation"
        ]
    }

    interest_map = {
        "Technology": [
            "Computer Science",
            "Artificial Intelligence"
        ],
        "Programming": [
            "Software Development",
            "Web Development"
        ],
        "Medicine": [
            "Medicine",
            "Healthcare"
        ],
        "Biology": [
            "Biotechnology",
            "Life Sciences"
        ],
        "Business": [
            "Business Management",
            "Entrepreneurship"
        ],
        "Finance": [
            "Finance",
            "Accounting"
        ],
        "Law": [
            "Legal Studies"
        ],
        "Government Services": [
            "Civil Services"
        ],
        "Teaching": [
            "Education"
        ],
        "Design": [
            "Design and Digital Media"
        ],
        "Research": [
            "Scientific Research"
        ]
    }

    if explore_intermediate:

        st.success(
            f"Welcome, {name if name else 'Student'}!"
        )

        st.subheader(f"🌟 Career Options for {stream}")

        for career in stream_options[stream]:
            st.markdown(f"- 🎯 {career}")

        if interests:

            st.subheader("💡 Based on Your Interests")

            personalized = []

            for interest_item in interests:
                personalized.extend(
                    interest_map.get(interest_item, [])
                )

            personalized = list(dict.fromkeys(personalized))

            for career in personalized:
                st.markdown(f"- ✨ {career}")

        st.write("### 🗺️ Your Next Steps")

        st.markdown("""
        1. Research courses related to your interests.
        2. Check eligibility and entrance examinations.
        3. Compare course subjects and college options.
        4. Speak with teachers or career counsellors.
        """)

        st.info(
            "Career eligibility and admission requirements "
            "vary by course and institution. Verify them "
            "before making a decision."
        )

# ---------------- COLLEGE STUDENTS ----------------

else:

    st.header("💻 College Career Planner")

    st.write(
        "Find career options, identify skills to learn, "
        "and create a learning roadmap."
    )

    with st.container(border=True):

        name = st.text_input("👤 Enter your name")

        education = st.selectbox(
            "🎓 Select your current education",
            [
                "B.Tech 1st Year",
                "B.Tech 2nd Year",
                "B.Tech 3rd Year",
                "B.Tech 4th Year",
                "Other Degree"
            ]
        )

        branch = st.selectbox(
            "💻 Select your branch",
            [
                "CSE",
                "CSE (AI)",
                "CSE (AI & ML)",
                "IT",
                "ECE",
                "EEE",
                "Mechanical",
                "Civil",
                "Other"
            ]
        )

        skills = st.multiselect(
            "🛠️ Select your current skills",
            [
                "Python",
                "Java",
                "C",
                "C++",
                "HTML",
                "CSS",
                "JavaScript",
                "SQL",
                "Machine Learning",
                "Data Structures",
                "Communication"
            ]
        )

        interest = st.selectbox(
            "🎯 Choose your career interest",
            [
                "Artificial Intelligence",
                "Software Development",
                "Data Analytics",
                "Web Development",
                "Cybersecurity"
            ]
        )

        find_path = st.button(
            "🚀 Find My Career Path",
            use_container_width=True
        )

    roadmap = {
        "Artificial Intelligence": [
            "Python Programming",
            "Mathematics and Statistics",
            "Machine Learning",
            "Deep Learning",
            "Build AI Projects"
        ],
        "Software Development": [
            "Learn C++ or Java",
            "Practice Data Structures and Algorithms",
            "Learn Git and GitHub",
            "Develop Applications",
            "Prepare for Interviews"
        ],
        "Data Analytics": [
            "Learn Python",
            "Learn SQL",
            "Practice Pandas",
            "Create Data Visualizations",
            "Build Analytics Projects"
        ],
        "Web Development": [
            "Learn HTML and CSS",
            "Learn JavaScript",
            "Learn a Backend Framework",
            "Connect a Database",
            "Build and Deploy Websites"
        ],
        "Cybersecurity": [
            "Learn Networking Basics",
            "Understand Operating Systems",
            "Learn Python Fundamentals",
            "Study Security Concepts",
            "Practice in Legal Training Labs"
        ]
    }

    # Map the website's interest labels to the labels
    # used in the existing career_data.py file.
    interest_mapping = {
        "Artificial Intelligence": "Artificial Intelligence",
        "Software Development": "Software Development",
        "Data Analytics": "Data Analysis",
        "Web Development": "Web Development",
        "Cybersecurity": "Cybersecurity"
    }

    if find_path:

        st.divider()

        st.subheader("👤 Your Student Profile")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"**Name:** {name if name else 'Student'}")
            st.markdown(f"**Education:** {education}")

        with col2:
            st.markdown(f"**Branch:** {branch}")
            st.markdown(f"**Interest:** {interest}")

        st.divider()

        # CAREER RECOMMENDATIONS

        st.subheader("🎯 Recommended Careers")

        try:
            recommendations = recommend_careers(
                interest_mapping[interest],
                skills
            )

            for item in recommendations:

                with st.container(border=True):

                    st.markdown(
                        f"### 🚀 {item['Career']}"
                    )

                    score = item["Match Score"]

                    st.progress(
                        max(0, min(100, score)) / 100
                    )

                    st.write(f"**Match Score:** {score}%")

                    matching = item["Matching Skills"]
                    missing = item["Skills to Learn"]

                    st.write(
                        "**Matching Skills:** "
                        + (
                            ", ".join(matching)
                            if matching
                            else "Keep learning to build your skills"
                        )
                    )

                    st.write(
                        "**Skills to Learn:** "
                        + (
                            ", ".join(missing)
                            if missing
                            else "No additional listed skills"
                        )
                    )

        except Exception as error:
            st.warning(
                "Career recommendations could not be loaded. "
                "Please check recommender.py and career_data.py."
            )

        st.divider()

        # SKILL GAP ANALYSIS

        st.subheader("📊 Skill Gap Analysis")

        if skills:

            st.success(
                f"You selected {len(skills)} current skill(s)."
            )

            st.write("### Your Current Skills")

            for skill in skills:
                st.markdown(f"- ✅ {skill}")

        else:

            st.info(
                "No skills selected yet. Start with programming "
                "fundamentals and practise regularly."
            )

        required_skills = {
            "Artificial Intelligence": [
                "Python",
                "Machine Learning",
                "SQL"
            ],
            "Software Development": [
                "Python",
                "C++",
                "Java"
            ],
            "Data Analytics": [
                "Python",
                "SQL",
                "Excel"
            ],
            "Web Development": [
                "HTML",
                "CSS",
                "JavaScript"
            ],
            "Cybersecurity": [
                "Python",
                "SQL",
                "Networking"
            ]
        }

        target_skills = required_skills[interest]

        missing_skills = [
            skill for skill in target_skills
            if skill not in skills
        ]

        st.write(f"### Skills for {interest}")

        for skill in target_skills:

            if skill in skills:
                st.markdown(f"- ✅ {skill} — Selected")
            else:
                st.markdown(f"- 📘 {skill} — Learn next")

        if missing_skills:
            st.info(
                "Suggested learning priorities: "
                + ", ".join(missing_skills)
            )
        else:
            st.success(
                "You selected all the skills listed for this career. "
                "Continue practising and building projects."
            )

        st.divider()

        # PERSONALIZED LEARNING ROADMAP

        st.subheader("🗺️ Your Learning Roadmap")

        for index, step in enumerate(
            roadmap[interest],
            start=1
        ):

            st.markdown(
                f"**Step {index}** — {step}"
            )

        st.write("### 🏆 Recommended Actions")

        st.markdown("""
        - Practise coding regularly.
        - Build small projects using your skills.
        - Upload suitable projects to GitHub.
        - Participate in hackathons and coding contests.
        - Review your progress and keep learning.
        """)

        st.caption(
            "Match scores are estimates based on your selected "
            "interest and skills. They do not guarantee career success."
        )

# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    "<h4 style='text-align:center;color:#4338ca;'>"
    "🚀 FutureForge"
    "</h4>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:#6b7280;'>"
    "Explore. Learn. Build Your Future."
    "</p>",
    unsafe_allow_html=True
)