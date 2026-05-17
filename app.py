import streamlit as st
from groq import Groq
import random

# ── API Setup ─────────────────────────────────────────────
client = Groq(api_key="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")  # ← Paste your gsk_ key here

# ── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="AceAI | Interview Practice",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Global CSS ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
* { font-family: 'Inter', sans-serif !important; box-sizing: border-box; }
.stApp { background: #0d0b12 !important; color: #e7e0ed !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* NAVBAR */
.navbar {
    background: rgba(13,11,18,0.9); backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(208,188,255,0.1);
    padding: 1rem 4rem; display: flex;
    align-items: center; justify-content: space-between;
}
.nav-logo { font-size: 1.5rem; font-weight: 900; color: #d0bcff; }
.nav-logo span { color: #a855f7; }

/* HERO */
.hero {
    min-height: 90vh;
    background: radial-gradient(ellipse at 50% 0%, rgba(124,58,237,0.18) 0%, transparent 70%), #0d0b12;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center; padding: 6rem 2rem 4rem;
}
.hero-badge {
    background: rgba(208,188,255,0.1); border: 1px solid rgba(208,188,255,0.2);
    color: #d0bcff; font-size: 0.8rem; font-weight: 600;
    padding: 0.4rem 1.2rem; border-radius: 20px; margin-bottom: 1.5rem; display: inline-block;
}
.hero-title {
    font-size: 3.8rem; font-weight: 900; line-height: 1.1;
    letter-spacing: -0.03em; margin-bottom: 1.2rem; color: #e7e0ed;
}
.gradient-text {
    background: linear-gradient(135deg, #d0bcff, #a855f7, #6366f1);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-sub { font-size: 1.1rem; color: #958ea0; max-width: 580px; line-height: 1.7; margin: 0 auto 2.5rem; }

/* STATS */
.stats-section {
    background: rgba(29,26,35,0.5);
    border-top: 1px solid rgba(73,68,84,0.3); border-bottom: 1px solid rgba(73,68,84,0.3);
    padding: 2rem 4rem; display: flex; justify-content: center; gap: 4rem; flex-wrap: wrap;
}
.stat-num { font-size: 2rem; font-weight: 900; color: #d0bcff; }
.stat-desc { font-size: 0.8rem; color: #958ea0; margin-top: 0.2rem; }

/* SECTION */
.section { padding: 5rem 4rem; max-width: 1200px; margin: 0 auto; }
.section-tag { color: #a855f7; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.6rem; }
.section-title { font-size: 2.4rem; font-weight: 800; color: #e7e0ed; letter-spacing: -0.02em; margin-bottom: 1rem; line-height: 1.2; }
.section-sub { font-size: 0.95rem; color: #958ea0; max-width: 500px; line-height: 1.7; }

/* FEATURE CARDS */
.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 1.2rem; margin-top: 2.5rem; }
.feature-card {
    background: #1d1a23; border: 1px solid #494454; border-radius: 16px; padding: 1.6rem; transition: all 0.3s;
}
.feature-card:hover { border-color: rgba(208,188,255,0.4); transform: translateY(-3px); }
.feature-icon { font-size: 1.8rem; margin-bottom: 1rem; }
.feature-title { font-size: 0.95rem; font-weight: 700; color: #e7e0ed; margin-bottom: 0.4rem; }
.feature-desc { font-size: 0.82rem; color: #958ea0; line-height: 1.6; }

/* STEPS */
.steps-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.2rem; margin-top: 2.5rem; }
.step-card { background: #1d1a23; border: 1px solid #494454; border-radius: 16px; padding: 2rem 1.5rem; text-align: center; }
.step-num {
    width: 44px; height: 44px; background: linear-gradient(135deg, #7c3aed, #6366f1);
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; font-weight: 800; color: white; margin: 0 auto 1rem;
}
.step-title { font-size: 0.95rem; font-weight: 700; color: #e7e0ed; margin-bottom: 0.4rem; }
.step-desc { font-size: 0.82rem; color: #958ea0; line-height: 1.6; }

/* COMPANIES STRIP */
.companies-strip { padding: 2.5rem 4rem; background: rgba(29,26,35,0.3); border-top: 1px solid rgba(73,68,84,0.3); border-bottom: 1px solid rgba(73,68,84,0.3); text-align: center; }
.companies-title { font-size: 0.8rem; color: #958ea0; margin-bottom: 1.2rem; text-transform: uppercase; letter-spacing: 0.08em; }
.companies-list { display: flex; justify-content: center; flex-wrap: wrap; gap: 0.8rem; }
.company-pill { background: #2c2832; border: 1px solid #494454; color: #cbc3d7; padding: 0.35rem 0.9rem; border-radius: 20px; font-size: 0.82rem; font-weight: 500; }

/* ABOUT */
.about-grid { display: grid; grid-template-columns: 1fr 1.4fr; gap: 3rem; align-items: start; margin-top: 2.5rem; }
.about-img { background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(99,102,241,0.08)); border: 1px solid rgba(208,188,255,0.12); border-radius: 20px; padding: 2.5rem; text-align: center; }
.about-icon { font-size: 4rem; margin-bottom: 1rem; }
.about-img-title { font-size: 1.1rem; font-weight: 700; color: #d0bcff; margin-bottom: 0.4rem; }
.about-img-sub { font-size: 0.82rem; color: #958ea0; line-height: 1.6; }
.about-text p { color: #cbc3d7; line-height: 1.8; margin-bottom: 0.8rem; font-size: 0.9rem; }
.value-item { display: flex; gap: 0.8rem; align-items: flex-start; margin-bottom: 1rem; }
.value-icon { font-size: 1.2rem; }
.value-title { font-size: 0.88rem; font-weight: 700; color: #d0bcff; }
.value-desc { font-size: 0.8rem; color: #958ea0; line-height: 1.5; }

/* CONTACT */
.contact-grid { display: grid; grid-template-columns: 1fr 1.5fr; gap: 2.5rem; margin-top: 2.5rem; }
.contact-card { background: #1d1a23; border: 1px solid #494454; border-radius: 14px; padding: 1.2rem; display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 0.8rem; }
.contact-icon { width: 42px; height: 42px; min-width: 42px; background: rgba(124,58,237,0.2); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; }
.contact-label { font-size: 0.7rem; color: #958ea0; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.2rem; }
.contact-value { font-size: 0.88rem; font-weight: 600; color: #e7e0ed; }
.contact-form { background: #1d1a23; border: 1px solid #494454; border-radius: 16px; padding: 1.8rem; }
.form-title { font-size: 1rem; font-weight: 700; color: #e7e0ed; margin-bottom: 1.2rem; }

/* FOOTER */
.footer { background: #0a0810; border-top: 1px solid rgba(73,68,84,0.4); padding: 3rem 4rem 1.5rem; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 2.5rem; margin-bottom: 2rem; }
.footer-brand-name { font-size: 1.2rem; font-weight: 900; color: #d0bcff; margin-bottom: 0.6rem; }
.footer-brand-desc { font-size: 0.8rem; color: #958ea0; line-height: 1.6; }
.footer-heading { font-size: 0.75rem; font-weight: 700; color: #e7e0ed; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.8rem; }
.footer-link { display: block; font-size: 0.8rem; color: #958ea0; margin-bottom: 0.5rem; }
.footer-bottom { border-top: 1px solid rgba(73,68,84,0.3); padding-top: 1.2rem; display: flex; justify-content: space-between; align-items: center; }
.footer-copy { font-size: 0.75rem; color: #494454; }
.footer-made { font-size: 0.75rem; color: #494454; }
.footer-made span { color: #d0bcff; }

/* LOGIN */
.login-wrap { min-height: 100vh; background: radial-gradient(ellipse at 30% 50%, rgba(124,58,237,0.15) 0%, transparent 60%), #0d0b12; display: flex; align-items: center; justify-content: center; padding: 2rem; }
.login-card { background: #1d1a23; border: 1px solid #494454; border-radius: 20px; padding: 2.5rem; width: 100%; max-width: 420px; }
.login-logo { text-align: center; margin-bottom: 1.5rem; }
.login-logo-icon { font-size: 2.5rem; }
.login-logo-title { font-size: 1.8rem; font-weight: 900; color: #d0bcff; }
.login-title { font-size: 1.2rem; font-weight: 700; color: #e7e0ed; margin-bottom: 0.3rem; }
.login-sub { font-size: 0.82rem; color: #958ea0; margin-bottom: 1.5rem; }

/* DASHBOARD */
.dash-header {
    background: rgba(13,11,18,0.85); backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(73,68,84,0.3);
    padding: 0.8rem 2rem; display: flex;
    align-items: center; justify-content: space-between;
    position: sticky; top: 0; z-index: 100;
}
.dash-logo { font-size: 1.2rem; font-weight: 900; color: #d0bcff; }
.dash-user { display: flex; align-items: center; gap: 0.7rem; background: #2c2832; border: 1px solid #494454; border-radius: 10px; padding: 0.4rem 0.8rem; }
.dash-user-name { font-size: 0.82rem; font-weight: 600; color: #e7e0ed; }
.dash-user-role { font-size: 0.68rem; color: #958ea0; }
.dash-nav-label { font-size: 0.62rem; font-weight: 700; color: #494454; letter-spacing: 0.1em; text-transform: uppercase; padding: 0.6rem 0.2rem 0.3rem; }

/* QUESTION */
.question-card { background: #1d1a23; border: 1px solid #494454; border-top: 2px solid #d0bcff; border-radius: 16px; padding: 1.6rem; margin-bottom: 1rem; }
.q-meta { display: flex; gap: 0.4rem; margin-bottom: 0.8rem; flex-wrap: wrap; }
.q-badge { padding: 0.18rem 0.6rem; border-radius: 20px; font-size: 0.68rem; font-weight: 600; }
.q-badge-company { background: rgba(208,188,255,0.1); color: #d0bcff; border: 1px solid rgba(208,188,255,0.2); }
.q-badge-topic { background: rgba(99,102,241,0.1); color: #a5b4fc; border: 1px solid rgba(99,102,241,0.2); }
.q-badge-pyq { background: rgba(34,197,94,0.1); color: #4ade80; border: 1px solid rgba(34,197,94,0.2); }
.q-badge-ai { background: rgba(168,85,247,0.1); color: #c084fc; border: 1px solid rgba(168,85,247,0.2); }
.q-text { font-size: 1rem; font-weight: 600; color: #e7e0ed; line-height: 1.5; }

/* SCORE */
.score-card { background: #1d1a23; border: 1px solid #494454; border-radius: 14px; padding: 1.3rem; text-align: center; margin-bottom: 1rem; }
.score-num { font-size: 2.5rem; font-weight: 900; color: #d0bcff; line-height: 1; }
.score-bar { height: 5px; background: #2c2832; border-radius: 3px; margin: 0.7rem 0; overflow: hidden; }
.score-fill { height: 100%; background: linear-gradient(90deg, #7c3aed, #d0bcff); border-radius: 3px; }

/* FEEDBACK */
.feedback-card { background: #1d1a23; border: 1px solid #494454; border-radius: 14px; overflow: hidden; }
.feedback-header { padding: 0.8rem 1.1rem; border-bottom: 1px solid rgba(73,68,84,0.4); display: flex; justify-content: space-between; align-items: center; }
.feedback-title { font-size: 0.82rem; font-weight: 700; color: #e7e0ed; }
.live-badge { background: rgba(208,188,255,0.1); color: #d0bcff; font-size: 0.6rem; font-weight: 700; padding: 0.15rem 0.5rem; border-radius: 4px; }
.feedback-body { padding: 1.1rem; }
.feedback-item { background: rgba(29,26,35,0.5); border-radius: 7px; padding: 0.5rem 0.7rem; font-size: 0.78rem; color: #cbc3d7; line-height: 1.5; margin-bottom: 0.3rem; }
.feedback-item.good { border-left: 3px solid #4ade80; }
.feedback-item.improve { border-left: 3px solid #f87171; }
.feedback-section-title { font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin: 0.8rem 0 0.4rem; display: flex; align-items: center; gap: 0.3rem; }

/* Streamlit overrides */
div.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #6366f1) !important;
    color: white !important; border: none !important; border-radius: 10px !important;
    font-weight: 600 !important; font-size: 0.88rem !important; width: 100% !important;
    box-shadow: 0 4px 15px rgba(124,58,237,0.25) !important; transition: all 0.2s !important;
}
div.stButton > button:hover { opacity: 0.88 !important; }
div.stTextInput > div > div > input, div.stTextArea > div > div > textarea, div.stSelectbox > div > div {
    background: #15121b !important; border: 1px solid #494454 !important; color: #e7e0ed !important; border-radius: 10px !important;
}
div.stTextInput > div > div > input:focus, div.stTextArea > div > div > textarea:focus { border-color: #d0bcff !important; }
label { color: #cbc3d7 !important; font-size: 0.82rem !important; font-weight: 500 !important; }
div[data-testid="stMetric"] { background: #1d1a23; border: 1px solid #494454; border-radius: 12px; padding: 0.8rem !important; }
div[data-testid="stMetricValue"] { color: #d0bcff !important; font-weight: 800 !important; }
div[data-testid="stMetricLabel"] { color: #958ea0 !important; font-size: 0.75rem !important; }
hr { border-color: rgba(73,68,84,0.4) !important; }
</style>
""", unsafe_allow_html=True)

# ── PYQ Database ──────────────────────────────────────────
PYQ_DATABASE = {
    "TCS": {
        "Python Programming": ["What is the difference between a list and a tuple in Python?","Explain the concept of decorators in Python with an example.","What is the difference between deep copy and shallow copy?","How does Python manage memory? Explain garbage collection.","What are *args and **kwargs in Python?","Explain exception handling in Python with try, except, finally.","What is a lambda function in Python? Give an example.","What is the difference between append() and extend()?","Explain the concept of generators in Python.","What is the difference between '==' and 'is' operators?"],
        "SQL & Databases": ["What is the difference between DELETE, DROP and TRUNCATE?","Explain the difference between INNER JOIN and OUTER JOIN.","Write a query to find the second highest salary from Employee table.","What is normalization? Explain 1NF, 2NF, 3NF.","What is the difference between WHERE and HAVING clause?","Explain ACID properties in database transactions.","What is the difference between UNION and UNION ALL?","Write a SQL query to find duplicate records in a table.","What are indexes in SQL and why are they used?","What is the difference between a primary key and foreign key?"],
        "HR & Behavioral": ["Tell me about yourself.","Why do you want to join TCS?","Where do you see yourself in 5 years?","What are your strengths and weaknesses?","Are you willing to relocate?","How do you handle pressure and tight deadlines?","Why should we hire you over other candidates?","What do you know about TCS as a company?","Tell me about a time you worked in a team.","Are you comfortable with bond/service agreement?"],
        "DSA & Problem Solving": ["What is the difference between stack and queue?","Explain binary search and its time complexity.","What is a linked list? What are its types?","Explain bubble sort with an example.","What is recursion? Write a recursive function for factorial.","What is the difference between BFS and DFS?","Write a program to check if a string is a palindrome.","What is the time complexity of quicksort?","Explain what a hash table is.","What is dynamic programming? Give an example."],
        "Artificial Intelligence & Machine Learning": ["What is the difference between supervised and unsupervised learning?","Explain overfitting and how to prevent it.","What is a confusion matrix?","What is the difference between classification and regression?","Explain gradient descent in simple terms.","What is the difference between AI, ML, and Deep Learning?","Explain the bias-variance tradeoff.","What is a neural network? Explain its basic structure.","What is feature engineering?","What is cross-validation and why is it used?"],
        "Object Oriented Programming": ["What are the four pillars of OOP?","Explain the difference between abstraction and encapsulation.","What is polymorphism? Give an example.","What is the difference between a class and an object?","Explain inheritance with an example.","What is method overloading and method overriding?","What is an abstract class?","What is a constructor? What are its types?","Explain the concept of multiple inheritance.","What is the difference between compile-time and runtime polymorphism?"],
        "General Aptitude & Reasoning": ["A train travels 60 km/hr. How long to cover 180 km?","If 6 workers complete a task in 8 days, how many days for 4 workers?","What comes next: 2, 6, 12, 20, 30, ?","A shopkeeper sells at 20% profit. CP is Rs 500, find SP.","Two numbers are in ratio 3:5. Sum is 48. Find the numbers.","If today is Monday, what day after 100 days?","Simplify: 15% of 200 + 25% of 400.","Find the odd one out: Cat, Dog, Cow, Eagle, Horse.","What is the next term: 1, 4, 9, 16, 25, ?","Two pipes fill a tank in 20 and 30 min. Together how long?"],
        "Computer Networks": ["What is the difference between TCP and UDP?","Explain the OSI model and its 7 layers.","What is DNS and how does it work?","What is the difference between IPv4 and IPv6?","Explain the three-way handshake in TCP.","What is the difference between a hub, switch, and router?","What is a subnet mask?","What is the difference between HTTP and HTTPS?","What is a MAC address?","What is a firewall?"],
        "Operating Systems": ["What is the difference between a process and a thread?","Explain deadlock and its four necessary conditions.","What is virtual memory and how does it work?","Explain different CPU scheduling algorithms.","What is a context switch?","What is thrashing in operating systems?","Explain the producer-consumer problem.","What is the difference between paging and segmentation?","What is a semaphore?","What is the difference between internal and external fragmentation?"],
        "Data Science & Analytics": ["What is exploratory data analysis (EDA)?","How do you handle missing data in a dataset?","What is data normalization?","What is correlation? How do you calculate it?","What is the difference between population and sample?","Explain the concept of feature selection.","What is the difference between a histogram and a bar chart?","What is a data pipeline?","What tools do you use for data visualization?","What is the difference between supervised and unsupervised learning?"],
    },
    "Infosys": {
        "Python Programming": ["What is the difference between mutable and immutable objects?","Explain list comprehension in Python.","What are Python modules and packages?","What is pickling and unpickling?","Explain iterators and iterables in Python.","How do you handle file operations in Python?","What are Python virtual environments?","What is the difference between class methods and static methods?","What is Python's GIL?","Explain the difference between range() and xrange()."],
        "SQL & Databases": ["What is the difference between SQL and NoSQL?","Explain different types of SQL joins.","What is a stored procedure?","What is a view in SQL?","Explain triggers in SQL.","Write a query to find top 5 highest paid employees.","What is a subquery? Give an example.","What is denormalization?","What is the difference between clustered and non-clustered indexes?","What are different types of database relationships?"],
        "HR & Behavioral": ["Tell me about yourself.","Why do you want to work at Infosys?","How do you prioritize tasks with multiple deadlines?","Tell me about a time you failed and what you learned.","How would your friends describe you in 3 words?","How do you keep updated with new technologies?","What are your salary expectations?","Do you have any questions for us?","Describe a challenging project you worked on.","How do you handle working under pressure?"],
        "DSA & Problem Solving": ["Write a program to reverse a linked list.","Explain the difference between a tree and a graph.","What is a binary search tree?","Write a program to find if two strings are anagrams.","Explain the merge sort algorithm.","What is the difference between a min-heap and max-heap?","Write a program to find all prime numbers up to N.","Write a program to find the longest common subsequence.","What is memoization?","Write a program to check if a number is Armstrong."],
        "Artificial Intelligence & Machine Learning": ["What is K-Nearest Neighbors algorithm?","What is regularization in ML? Explain L1 and L2.","What is a decision tree?","What is ensemble learning?","What is the ROC curve and AUC score?","What is the difference between bagging and boosting?","What is NLP? Give 3 real-world applications.","Explain Random Forest algorithm.","What is transfer learning?","What is the difference between parametric and non-parametric models?"],
        "Object Oriented Programming": ["What is the SOLID principle?","What is the difference between composition and inheritance?","What is a singleton class?","What is operator overloading?","What is the difference between pass by value and pass by reference?","What is an interface?","Explain the concept of friend functions.","What is the difference between early and late binding?","What are design patterns? Name 3 common ones.","Explain the factory design pattern."],
        "General Aptitude & Reasoning": ["A car covers 400 km in 5 hours. Average speed?","If 12 men build a wall in 10 days, how many days for 8 men?","Find missing: 1, 4, 9, 16, 25, ?","CP is Rs 800. Sold at 15% profit. Find SP.","What is 30% of 450?","A boat goes upstream 10 km/hr, downstream 14 km/hr. Speed of stream?","Complete: Book is to Reading as Fork is to ?","If 5 cats catch 5 mice in 5 min, how many cats for 100 mice in 100 min?","Rearrange: ATINOUC = ?","What is the probability of getting a head when a coin is tossed?"],
        "Computer Networks": ["What is the OSI model?","Difference between TCP and UDP.","What is IP addressing?","What is NAT?","How does DHCP work?","What is a VPN?","Difference between LAN, WAN, MAN.","What is ARP?","What is a protocol?","What is bandwidth?"],
        "Operating Systems": ["What are CPU scheduling algorithms?","Explain memory management in OS.","What is a semaphore?","What is external fragmentation?","What is mutual exclusion?","How can deadlock be prevented?","What are page replacement algorithms?","What is spooling?","What is a zombie process?","What is demand paging?"],
        "Data Science & Analytics": ["What is PCA?","What is A/B testing?","What is the Central Limit Theorem?","How do you detect outliers?","What is the difference between correlation and causation?","What is the p-value?","How do you deal with imbalanced datasets?","What is feature engineering?","What is data cleaning?","What is ETL?"],
    },
    "Google": {
        "Artificial Intelligence & Machine Learning": ["Explain the attention mechanism in transformers.","What is the difference between GPT and BERT?","How does backpropagation work?","What is batch normalization?","Explain word embeddings.","What is reinforcement learning?","Explain the vanishing gradient problem.","What is the difference between CNN and RNN?","What is the difference between online and batch learning?","Explain how a recommendation system works."],
        "Python Programming": ["How would you optimize a slow Python program?","What are context managers in Python?","Explain multiprocessing vs multithreading.","How does Python's async/await work?","What is the difference between __str__ and __repr__?","What are metaclasses?","How do you profile Python code?","Explain Python descriptors.","What is monkey patching?","What is duck typing?"],
        "DSA & Problem Solving": ["Given an array, find two numbers that add up to a target.","How would you detect a cycle in a linked list?","Implement a LRU cache.","Find the longest substring without repeating characters.","Given a binary tree, find its maximum depth.","Implement a queue using two stacks.","Find the kth largest element in an array.","Find all permutations of a given string.","Find the number of islands in a 2D grid.","Check if a binary tree is a valid BST."],
        "SQL & Databases": ["How would you optimize a slow SQL query?","Difference between OLTP and OLAP.","What is database sharding?","Explain CAP theorem.","How do you handle N+1 query problem?","Explain database isolation levels.","What is eventual consistency?","How would you design a DB for a social media app?","What is connection pooling?","What is a materialized view?"],
        "HR & Behavioral": ["Tell me about a time you solved a very difficult problem.","How do you approach learning a new technology?","Describe a disagreement with your team and how you handled it.","How do you handle ambiguous requirements?","How do you balance quality and speed?","Tell me about your most impactful project.","How do you handle feedback and criticism?","What is your biggest technical achievement?","Tell me about a time you mentored someone.","How do you make decisions with incomplete information?"],
        "Data Science & Analytics": ["How would you handle missing values?","Explain the difference between mean, median, mode.","What is A/B testing?","Explain PCA.","What is the Central Limit Theorem?","How do you detect outliers?","What is the difference between correlation and causation?","Explain p-value in hypothesis testing.","How would you deal with imbalanced datasets?","What metrics for evaluating a recommendation system?"],
        "Object Oriented Programming": ["Explain design patterns. Name 3.","Difference between composition and inheritance.","What is a singleton class?","Explain the factory design pattern.","What is the SOLID principle?","What is dependency injection?","Explain the observer design pattern.","What is the adapter pattern?","What is a proxy pattern?","What is the command pattern?"],
        "Computer Networks": ["How does HTTPS work?","What is load balancing?","Explain the concept of CDN.","Difference between REST and GraphQL.","How does DNS resolution work?","What is WebSocket?","Explain microservices vs monolithic.","What is rate limiting?","What is OAuth 2.0?","What is gRPC?"],
        "Operating Systems": ["How does a modern OS handle memory?","Difference between process and thread.","How do file systems work?","What is inter-process communication?","How does OS handle I/O?","What is a system call?","Explain virtual memory benefits.","What is the purpose of a kernel?","What is containerization?","What is the difference between VM and container?"],
        "General Aptitude & Reasoning": ["A train 150m long passes a pole in 10 seconds. Speed?","Next term: 3, 7, 15, 31, 63, ?","Two pipes fill tank in 20 and 30 min. Together?","Probability of head when coin tossed?","If APPLE = 50, what is MANGO?","Area of a circle with radius 7 cm?","Simplify: (15 × 4 - 20) ÷ (3 + 7)","A can do work in 10 days, B in 15. Together?","What angle between clock hands at 3:15?","Find next Fibonacci: 1, 1, 2, 3, 5, 8, 13, ?"],
    },
    "Amazon": {
        "HR & Behavioral": ["Tell me about a time you took ownership of a project.","Describe a decision with limited data.","Tell me about a time you disagreed with a manager.","Give an example of setting an extremely high bar for quality.","Tell me about a time you innovated.","Describe a time you learned something new quickly.","Tell me about earning trust with a difficult stakeholder.","Give an example of going above and beyond for a customer.","Describe a time you delivered results despite obstacles.","Tell me about simplifying a complex process."],
        "DSA & Problem Solving": ["Find the maximum subarray sum (Kadane's Algorithm).","Rotate a matrix 90 degrees clockwise.","Find the number of islands in a 2D grid.","Implement a min stack with getMin() in O(1).","Find the longest palindromic substring.","Check if a binary tree is a valid BST.","Find the meeting point of two linked lists.","Merge overlapping intervals.","Find the shortest path in an unweighted graph.","Count ways to climb n stairs (1 or 2 steps)."],
        "Python Programming": ["Implement a thread-safe singleton in Python.","Explain Python's asyncio library.","Implement custom exceptions in Python.","Implement a priority queue in Python.","Difference between map(), filter(), reduce().","How to implement memoization in Python?","How to parse a large JSON file efficiently?","What is the purpose of __slots__?","How would you implement a rate limiter?","What is the difference between deepcopy and copy?"],
        "SQL & Databases": ["Query to find customers who never placed an order.","Calculate running totals using window functions.","Find the Nth highest salary.","Write a query using CTE.","How to handle slow query with millions of records?","Pivot rows into columns.","What is a deadlock? How to prevent it?","What is partitioning?","Difference between optimistic and pessimistic locking.","Write a recursive CTE."],
        "Artificial Intelligence & Machine Learning": ["How does Alexa understand natural language?","Explain how a recommendation engine works.","Difference between collaborative and content-based filtering.","How would you build a fraud detection system?","How does sentiment analysis work?","How to handle real-time ML predictions at scale?","What is model drift?","What is the difference between online and batch learning?","What is AutoML?","How does AWS SageMaker help in ML deployment?"],
        "Object Oriented Programming": ["What is the strategy design pattern?","What is the decorator design pattern?","Explain the MVC architecture pattern.","What is dependency injection?","What is the repository pattern?","Explain event-driven programming.","What is the command design pattern?","Explain microservices architecture.","What is the saga pattern?","What is a circuit breaker pattern?"],
        "Computer Networks": ["How does Amazon AWS ensure high availability?","Difference between vertical and horizontal scaling.","What is a message queue?","What is eventual consistency?","How does caching work at scale?","What is a reverse proxy?","What is service mesh?","How does CDN work?","What is API gateway?","What is blue-green deployment?"],
        "Operating Systems": ["What is containerization?","Difference between VM and container.","How does Kubernetes manage containers?","What is serverless computing?","Difference between stateful and stateless.","How does log aggregation work?","What is a health check in microservices?","What is CI/CD pipeline?","What is auto-scaling?","What is a load balancer?"],
        "Data Science & Analytics": ["How to measure success of a recommendation system?","What is cohort analysis?","Explain customer lifetime value.","How do you detect anomalies in time-series data?","What is funnel analysis?","How to design an A/B test for checkout?","Difference between precision and recall.","How to handle seasonality in forecasting?","What is RFM analysis?","What is market basket analysis?"],
        "General Aptitude & Reasoning": ["If cost of 5 pens is Rs 75, cost of 8 pens?","A can work in 10 days, B in 15. Together?","What is the next: 3, 7, 15, 31, 63, ?","Area of rectangle with length 12 and width 8.","What percent is 60 of 240?","If A=1, B=2... Z=26, value of INDIA?","Ratio of boys to girls 3:2. Total 50 students. Find boys.","A shopkeeper gives 10% discount. MRP Rs 500. Find SP.","Two trains 200m and 150m cross each other in 20s. Same direction speed?","The average of 5 numbers is 40. Four are 30,35,45,50. Find fifth."],
    },
    "Microsoft": {
        "DSA & Problem Solving": ["Implement a stack using queues.","Find all subsets of a given set.","Remove the Nth node from the end of a linked list.","Serialize and deserialize a binary tree.","Find median of two sorted arrays.","Find if word exists in a board (Word Search).","Find number of ways to make change.","Find the majority element.","Implement a basic calculator.","Find the longest increasing subsequence."],
        "Python Programming": ["Explain Python's data model and magic methods.","Difference between __new__ and __init__.","Implement a custom iterator in Python.","What is duck typing?","What are abstract base classes?","How to implement MRO?","What is the purpose of __all__?","How to make a Python class hashable?","Explain Python's import system.","What is the difference between deep and shallow equality?"],
        "HR & Behavioral": ["Tell me about a project you're most proud of.","How do you stay updated with technology?","Describe working with a difficult team member.","What is your approach to debugging?","Tell me about improving a process significantly.","How do you handle multiple competing priorities?","Tell me about receiving critical feedback.","Why do you want to work at Microsoft?","Describe explaining a technical concept to non-technical person.","What do you do when you're stuck on a problem?"],
        "Artificial Intelligence & Machine Learning": ["What is Azure Cognitive Services?","Explain how GPT models generate text.","What is prompt engineering?","Explain RAG (Retrieval Augmented Generation).","Difference between zero-shot and few-shot learning.","What is the role of RLHF?","How does Copilot use AI?","Difference between language model and chat model.","How would you fine-tune a pre-trained model?","What is DALL-E?"],
        "SQL & Databases": ["Difference between clustered and non-clustered index.","Window functions in SQL with examples.","What is a recursive CTE?","How to handle hierarchical data in SQL?","Difference between OLAP and OLTP.","What is database replication?","What is a columnstore index?","How to implement full-text search?","What is a materialized view?","How to handle slow queries?"],
        "Object Oriented Programming": ["Explain SOLID principles.","Difference between composition and inheritance.","What is the factory method pattern?","Explain the proxy design pattern.","What is the adapter design pattern?","Explain the facade design pattern.","What is the template method pattern?","Explain loose coupling and high cohesion.","What is the observer pattern?","What is dependency injection?"],
        "Computer Networks": ["How does Azure networking work?","What is a virtual network?","How does SSL certificate work?","What is CDN?","How do WebSockets work?","What is gRPC?","What is service mesh?","How does OAuth 2.0 work?","What is API rate limiting?","What is load balancing?"],
        "Operating Systems": ["How does Windows handle process scheduling?","What is the Windows Registry?","How does NTFS file system work?","What is Active Directory?","What is WSL?","How does Windows manage memory?","What is a Windows service?","How does Group Policy work?","What is containerization?","Difference between VM and container?"],
        "Data Science & Analytics": ["How does Power BI connect to data sources?","What is DAX?","What is data lineage?","Difference between data lake and data warehouse.","How does Azure Machine Learning work?","What is MLOps?","What are feature stores?","What is data governance?","What is ETL pipeline?","What is a data catalog?"],
        "General Aptitude & Reasoning": ["If 3 typists type 3 pages in 3 min, pages in 1 hour for 9 typists?","Ball dropped from 64m, bounces half each time. Total distance?","Angle between clock hands at 3:15?","Next Fibonacci: 1, 1, 2, 3, 5, 8, 13, ?","If FACE=15, what is BEAD?","Person walks 5km north, 3km right, 5km right. Distance from start?","60% passed English, 70% Math, 40% both. % failed both?","Find the next: 1, 8, 27, 64, ?","What is 15% of 200?","If CODING = 111514497, DATA = ?"],
    },
    "Wipro": {
        "Python Programming": ["Difference between set and frozenset?","How does Python's threading module work?","How to implement binary search in Python?","What is Python's collections module?","How to connect to a database using Python?","Difference between JSON and Pickle?","Difference between os.path and pathlib?","What is MRO in Python?","What is the difference between sort() and sorted()?","What is the map() function?"],
        "SQL & Databases": ["Difference between natural join and equi-join?","Write query: employees who earn more than their manager.","What is a correlated subquery?","Query: department with highest average salary.","What is a composite key?","Explain database constraints.","Query: every alternate row from a table.","What is referential integrity?","What is a cross join?","Difference between REPLACE and UPDATE?"],
        "HR & Behavioral": ["Introduce yourself briefly.","Why did you choose computer science?","What are your technical skills?","Have you done any projects or internships?","Are you a team player?","How do you handle criticism from seniors?","Are you open to working night shifts?","How soon can you join if selected?","What is your biggest achievement in college?","What are your hobbies?"],
        "DSA & Problem Solving": ["Implement a queue using arrays.","Difference between linear and binary search.","Find the GCD of two numbers.","What is a circular linked list?","Explain insertion sort.","Count vowels in a string.","Print Fibonacci series up to N terms.","Swap two numbers without third variable.","What is a sparse matrix?","Write a program to find factorial."],
        "Artificial Intelligence & Machine Learning": ["Difference between AI and automation.","How is AI used in software testing?","What is generative AI?","Difference between rule-based and ML-based systems.","How does AI help in data analysis?","What is responsible AI?","What is a chatbot?","How would you explain ML to a non-technical person?","What is computer vision?","What is NLP?"],
        "Object Oriented Programming": ["What are the 4 pillars of OOP?","Polymorphism with real-world example.","Difference between overloading and overriding.","What is encapsulation?","Explain the concept of an interface.","Difference between class and structure.","What is multiple inheritance?","What is a destructor?","What is a virtual function?","What is an abstract class?"],
        "Computer Networks": ["What is a firewall?","Difference between HTTP and FTP.","What is a proxy server?","What is network topology?","Difference between unicast, multicast, broadcast.","What is ICMP?","What is network segmentation?","What is a VLAN?","What is bandwidth?","What is latency?"],
        "Operating Systems": ["Difference between preemptive and non-preemptive scheduling.","What is a critical section?","Types of operating systems.","What is demand paging?","Difference between logical and physical address.","File permissions in Linux.","What is a zombie process?","What are memory leaks?","What is a context switch?","What is thrashing?"],
        "Data Science & Analytics": ["What is data cleaning?","Difference between structured and unstructured data.","What is ETL?","What is a pivot table?","What is time series analysis?","Difference between classification and clustering.","What is data warehousing?","What is business intelligence?","What is big data?","What are the 3 Vs of big data?"],
        "General Aptitude & Reasoning": ["Next term: 5, 10, 20, 40, ?","Train 100m long passes bridge 150m in 25 sec. Speed?","15 men complete work in 20 days. Men needed for 10 days?","Average of 5 numbers is 40. Four are 30,35,45,50. Fifth?","If ROAD = 52, GATE = ?","Different: 17, 23, 37, 45, 53?","Number increased by 20% then decreased by 20%. Net change?","Clock shows 3:00. Angle at 3:45?","Rearrange: NATIOC = ?","Complete: 1, 8, 27, 64, ?"],
    },
    "Accenture": {
        "HR & Behavioral": ["Tell me about yourself.","Why do you want to join Accenture?","What do you know about Accenture's services?","How do you handle tight deadlines?","Tell me about a time you took initiative.","Are you comfortable with client-facing roles?","How do you manage time with multiple projects?","What value will you bring to Accenture?","Tell me about a time you showed leadership.","How do you adapt to new work environments?"],
        "Python Programming": ["Find factorial of a number in Python.","What is string formatting? Explain f-strings.","Count word frequency in a sentence.","Find all duplicates in a list.","What is dictionary comprehension?","Explain scope in Python (LEGB rule).","Sort a list without built-in sort.","Explain type conversion in Python.","What is the zip() function?","Write a program to check if a number is prime."],
        "SQL & Databases": ["What is DDL vs DML vs DCL?","Count employees in each department.","Difference between IN and EXISTS.","Find employees whose name starts with 'A'.","What is a self-join?","Average salary by department.","What is a database transaction?","What is COALESCE?","What is referential integrity?","What is the difference between CHAR and VARCHAR?"],
        "Artificial Intelligence & Machine Learning": ["Difference between AI and automation.","How is AI used in consulting?","What is generative AI? Give 3 business use cases.","What is a chatbot?","What is responsible AI?","How does AI help in customer service?","Difference between structured and unstructured data.","How would you explain ML to a non-technical client?","What is NLP?","What is computer vision?"],
        "DSA & Problem Solving": ["Reverse a string.","Find the second largest element.","Check if two strings are anagrams.","Find missing number in array 1 to N.","Implement a stack using arrays.","Remove duplicates from an array.","Find the intersection of two arrays.","Check if a number is Armstrong.","What is Big O notation?","Difference between array and linked list."],
        "Object Oriented Programming": ["What are the 4 pillars of OOP?","Explain inheritance with example.","What is encapsulation?","What is polymorphism?","What is abstraction?","What is a constructor and destructor?","What is method overriding?","Explain access modifiers.","What is multiple inheritance?","What is an abstract class?"],
        "Computer Networks": ["What is client-server architecture?","Explain HTTP request/response cycle.","What is REST API?","What is JSON?","Difference between GET and POST.","What is an API endpoint?","What is CORS?","What do SSL/TLS certificates do?","What is a protocol?","What is IP addressing?"],
        "Operating Systems": ["What is an OS? Main functions?","What is a process? What are its states?","What is multitasking vs multithreading?","What is RAM vs ROM?","What is a file system?","Difference between 32-bit and 64-bit OS.","What is a batch processing system?","What is the boot process?","What is virtual memory?","What is a device driver?"],
        "Data Science & Analytics": ["What is data analytics and its types?","Difference between data analytics and data science.","What is Excel VLOOKUP?","What are KPIs?","What is data visualization? Name 3 tools.","Difference between descriptive and predictive analytics.","What is a BI dashboard?","What is big data? Explain 3 Vs.","What is Python Pandas?","What is data preprocessing?"],
        "General Aptitude & Reasoning": ["Cost of 5 pens Rs 75. Cost of 8?","A and B work together. A in 10 days, B in 15. Together?","Next: 3, 7, 15, 31, 63, ?","CP Rs 800, 15% profit. Find SP.","30% of 450?","Two pipes fill tank in 20 and 30 min. Together?","Probability of head when coin tossed?","Rearrange: ATINOUC = ?","If today Monday, day after 100 days?","Simplify: 15% of 200 + 25% of 400."],
    },
    "Cognizant": {
        "HR & Behavioral": ["Tell me about yourself.","Why Cognizant over others?","What do you know about Cognizant?","How do you deal with tight deadlines?","Tell me about a time you took initiative.","Biggest weakness and how working on it?","How do you handle failure?","Willing to travel for client projects?","What value will you bring?","How do you keep up with technology?"],
        "Python Programming": ["Python's built-in data types?","Check if a number is prime.","Flatten a nested list.","What is zip() function?","Read and write CSV files.","Find most frequent element in a list.","Difference between sort() and sorted().","Explain default mutable arguments.","What are Python's logical operators?","Difference between is and == in Python."],
        "SQL & Databases": ["Display current date in SQL.","Find employees hired in last 6 months.","What is NULL in SQL?","Explain GROUP BY with example.","Find total sales per month.","Aggregate functions in SQL. Name 5.","Delete duplicate rows from a table.","Difference between left and right join.","What is COALESCE?","Write a query to find second highest salary."],
        "Artificial Intelligence & Machine Learning": ["What is machine learning? Give 3 examples.","Difference between AI, ML, Deep Learning.","What is training vs test dataset?","What is overfitting?","What is feature engineering?","Difference between classification and regression.","What is a neural network?","What is NLP?","What is computer vision?","What is a recommendation system?"],
        "DSA & Problem Solving": ["What is time complexity? Big O notation.","Difference between array and linked list.","Find factorial recursively.","What is a stack? Real-world example.","Find largest and smallest in array.","What is binary search?","What is a hash map?","Print all even numbers from 1 to 100.","What is DFS vs BFS?","Check if a number is palindrome."],
        "Object Oriented Programming": ["What is OOP and why important?","Give real-world example of each OOP pillar.","Difference between class and object.","What is method overloading?","What is super() function?","Static method vs instance method.","What is encapsulation in Python?","What is multiple inheritance?","What is a constructor?","What is abstraction?"],
        "Computer Networks": ["Difference between TCP and UDP.","What is an IP address?","Difference between LAN and WAN.","What is a router?","What is the OSI model?","What is HTTP status code 404?","Difference between IPv4 and IPv6.","What is bandwidth?","What is DNS?","What is a MAC address?"],
        "Operating Systems": ["Main functions of OS.","What is multitasking?","What is a thread?","What is deadlock?","Difference between primary and secondary memory.","What is a shell?","Difference between Windows and Linux.","What is a device driver?","What is virtual memory?","What is a file system?"],
        "Data Science & Analytics": ["What is data science?","Difference between data science and analytics.","Programming languages used in data science.","What is Pandas?","What is NumPy?","What is data preprocessing?","What is a DataFrame?","What is matplotlib?","What is machine learning?","What is data visualization?"],
        "General Aptitude & Reasoning": ["6 workers in 8 days. 4 workers in how many days?","Next: 2, 6, 12, 20, 30, ?","20% profit on Rs 500 CP. Find SP.","Odd one out: Cat, Dog, Cow, Eagle, Horse.","What day after 100 days if today Monday?","3:5 ratio, sum 48. Find numbers.","15% of 200 + 25% of 400.","Train travels 60 km/hr. Time for 180 km?","What is 30% of 450?","Find the odd number: 2, 3, 5, 7, 9, 11."],
    },
    "HCL": {
        "HR & Behavioral": ["Walk me through your resume.","Why do you want to work at HCL?","How do you handle disagreements?","Tell me about a technical challenge you overcame.","Comfortable with rotational shifts?","Expectations from this role?","Tell me about your final year project.","How do you handle not knowing the answer?","What is your biggest strength?","How do you manage your time?"],
        "Python Programming": ["Inheritance in Python with example.","Reverse a string without reverse().","Class variable vs instance variable.","What is enumerate()?","How does with statement work?","Generate random number 1 to 100.","Difference between readline() and readlines().","Python's string methods. Name 5.","What is the difference between list and tuple?","What is a lambda function?"],
        "SQL & Databases": ["Difference between primary key and unique key.","Fetch last 3 records from a table.","What does foreign key constraint do?","Find employees with the same salary.","What is an alias in SQL?","Difference between BETWEEN and IN.","Update salary of all employees by 10%.","Types of SQL commands.","What is a cross join?","What is referential integrity?"],
        "Artificial Intelligence & Machine Learning": ["What is artificial intelligence?","5 real-world applications of AI.","Difference between AI and machine learning.","What is deep learning?","What is computer vision?","What is a recommendation system?","What is speech recognition?","What is the Turing Test?","What is NLP?","What is generative AI?"],
        "DSA & Problem Solving": ["What is a data structure?","Difference between array and list.","Sum of digits of a number.","What is a binary tree?","Find largest element in a list.","What is a queue?","Difference between DFS and BFS.","Check if a number is palindrome.","What is a stack?","What is recursion?"],
        "Object Oriented Programming": ["What is OOP?","What is a class?","What is an object?","What is inheritance?","What is polymorphism?","What is encapsulation?","What is abstraction?","Difference between public and private.","What is a constructor?","What is method overriding?"],
        "Computer Networks": ["What is a computer network?","What is the internet?","What is an IP address?","What is DNS?","What is a MAC address?","Difference between wired and wireless.","What is a protocol?","What is bandwidth and latency?","What is a firewall?","What is HTTP?"],
        "Operating Systems": ["What is an OS?","5 popular operating systems.","What is multitasking?","What is a file system?","What is RAM?","Difference between 32-bit and 64-bit.","What is a process?","What is a thread?","What is virtual memory?","What is deadlock?"],
        "Data Science & Analytics": ["What is data science?","What is big data?","What is data mining?","What is machine learning?","What is data visualization?","Name 3 data science tools.","What is Python used for in data science?","Difference between data analyst and scientist.","What is SQL used for?","What is data preprocessing?"],
        "General Aptitude & Reasoning": ["400 km in 5 hours. Average speed?","12 men in 10 days. 8 men in how many days?","Missing: 1, 4, 9, 16, 25, ?","CP Rs 800, 15% profit. Find SP.","30% of 450?","Odd number: 2, 3, 5, 7, 9, 11.","Rearrange: NATIOC = ?","Complete: 1, 8, 27, 64, ?","Two pipes 20 and 30 min. Together?","Probability of head when coin tossed?"],
    },
    "Capgemini": {
        "HR & Behavioral": ["Tell me something not on your resume.","Why Capgemini?","How do you approach learning new things?","Tell me about going above and beyond.","How do you ensure quality in your work?","Tell me about your final year project.","Where do you see IT industry in 5 years?","How do you handle constructive criticism?","What is your greatest achievement?","How do you deal with tight deadlines?"],
        "Python Programming": ["Difference between while and for loop.","Find Armstrong numbers between 1 and 1000.","Use of break and continue.","Implement a simple calculator.","Print a pattern of stars.","Convert a string to a list.","Python's comparison operators.","Check if a string is palindrome.","What is recursion?","What is a list comprehension?"],
        "SQL & Databases": ["What is SQL? Types of commands?","Find employees in a specific department.","Purpose of ORDER BY clause.","Subquery to find above-average salaries.","What is an ER diagram?","Write a query to join three tables.","Difference between local and global temp table.","What is a database cursor?","What is normalization?","What is a primary key?"],
        "Artificial Intelligence & Machine Learning": ["What is AI? Give 5 applications.","What is machine learning?","Difference between AI and automation.","What is a chatbot?","What is NLP?","What is image recognition?","What is predictive analytics?","Role of AI in healthcare.","What is deep learning?","What is computer vision?"],
        "DSA & Problem Solving": ["What is an algorithm?","What is time complexity?","What is a stack?","What is a queue?","What is a linked list?","Name 3 sorting algorithms.","Explain linear and binary search.","What is recursion?","What is BFS and DFS?","What is dynamic programming?"],
        "Object Oriented Programming": ["What is OOP?","What are the 4 pillars of OOP?","What is a class and object?","Inheritance with example.","What is polymorphism?","What is encapsulation?","What is a constructor?","What is method overriding?","What is abstraction?","What is multiple inheritance?"],
        "Computer Networks": ["What is a network?","What is TCP/IP?","What is an IP address?","What is DNS?","What is a firewall?","Difference between HTTP and HTTPS.","What is WiFi?","What is a router?","What is bandwidth?","What is the OSI model?"],
        "Operating Systems": ["What is an OS?","What is a process?","What is a thread?","What is deadlock?","What is virtual memory?","What is a file system?","Difference between RAM and ROM.","What is context switching?","What is multitasking?","What is demand paging?"],
        "Data Science & Analytics": ["What is data analytics?","What is Python?","What is SQL?","What is Excel?","What is data visualization?","What is a dashboard?","Difference between data and information.","What is business intelligence?","What is big data?","What is data mining?"],
        "General Aptitude & Reasoning": ["5 pens cost Rs 75. Cost of 8?","A in 10 days, B in 15. Together?","Next: 3, 7, 15, 31, 63, ?","Train 150m passes pole in 10 sec. Speed?","30% of 450?","Two pipes 20 and 30 min. Together?","Probability of head?","If CODING = 111514497, DATA = ?","What is 15% of 200?","Find next: 2, 6, 12, 20, 30, ?"],
    },
    "Tech Mahindra": {
        "HR & Behavioral": ["Tell me about yourself.","Why Tech Mahindra?","What do you know about Tech Mahindra?","Learn from a mistake?","Deal with a difficult coworker?","Tell me about your project experience.","Open to telecom or IT services domain?","How do you manage stress?","What is your biggest strength?","Are you a team player?"],
        "Python Programming": ["Check if a year is a leap year.","Difference between tuple and list.","Find the largest element in a list.","What is string slicing?","How do Python dictionaries work?","Merge two dictionaries.","What is the map() function?","Remove all whitespace from a string.","What is a lambda function?","What is list comprehension?"],
        "SQL & Databases": ["Purpose of ORDER BY clause.","Find employees in specific department.","Difference between table and view.","Subquery to find above-average salaries.","What is an ER diagram?","Write query to join three tables.","Explain cascading updates.","What is a database cursor?","What is normalization?","What is referential integrity?"],
        "Artificial Intelligence & Machine Learning": ["What is artificial intelligence?","Types of machine learning.","What is deep learning?","5 applications of AI in telecom.","What is NLP?","What is computer vision?","Difference between AI and ML.","What is a recommendation system?","What is chatbot?","What is generative AI?"],
        "DSA & Problem Solving": ["What is a data structure?","What is an array?","What is a linked list?","What is a stack?","What is a queue?","What is a tree?","What is a graph?","Name 3 sorting algorithms.","What is recursion?","What is binary search?"],
        "Object Oriented Programming": ["4 pillars of OOP.","Inheritance with example.","What is polymorphism?","What is encapsulation?","What is abstraction?","What is a class?","What is an object?","What is a constructor?","What is method overriding?","What is multiple inheritance?"],
        "Computer Networks": ["What is a computer network?","What is TCP/IP?","What is an IP address?","What is DNS?","What is a firewall?","What is WiFi?","What is 5G?","What is the OSI model?","What is bandwidth?","What is HTTP?"],
        "Operating Systems": ["What is an OS?","What is a process?","What is multitasking?","What is a file system?","What is RAM?","What is virtual memory?","What is a thread?","What is deadlock?","What is context switching?","What is demand paging?"],
        "Data Science & Analytics": ["What is data science?","What is big data?","What is Python used for in data science?","What is machine learning?","What is data visualization?","What is SQL used for?","What is data cleaning?","Difference between data analyst and scientist.","What is data preprocessing?","What is business intelligence?"],
        "General Aptitude & Reasoning": ["Next: 5, 10, 20, 40, ?","Train 100m passes bridge 150m in 25 sec. Speed?","15 men in 20 days. Men for 10 days?","Average of 5 numbers is 40. Four are 30,35,45,50. Fifth?","ROAD = 52, GATE = ?","Different: 17, 23, 37, 45, 53?","Number +20% then -20%. Net change?","Clock at 3:00. Angle at 3:45?","Rearrange: ATINOUC = ?","Complete: 1, 8, 27, 64, ?"],
    },
    "Flipkart": {
        "DSA & Problem Solving": ["Design system for flash sales with millions of users.","Implement autocomplete for search bar.","Find minimum coins to make change.","Design a shopping cart data structure.","Implement a rate limiter for API calls.","Find optimal delivery route for multiple locations.","Find most popular product in search history.","Design a notification system for order updates.","Find products frequently bought together.","Implement inventory management with low-stock alerts."],
        "Python Programming": ["Python class for shopping cart with add/remove/total.","Validate Indian PIN codes.","Handle concurrent requests in Python.","Calculate delivery charges based on distance.","Implement search with filters in Python.","Detect fraudulent transactions.","Design scalable product catalog.","Parse and process product review data.","Implement a coupon discount system.","Handle payment gateway integration."],
        "SQL & Databases": ["Top 10 best-selling products this month.","Customers who bought A but not B.","Calculate customer lifetime value.","Find abandoned carts in last 7 days.","Find most returned products.","Design flash sale DB to prevent overselling.","Design DB for e-commerce platform.","Find products with rating above 4.","Find customers who never purchased.","Monthly revenue trend query."],
        "HR & Behavioral": ["Tell me about yourself.","Why do you want to work at Flipkart?","What do you know about Flipkart's business?","Tell me about solving a challenging problem.","How do you stay updated with e-commerce trends?","Describe working under pressure.","Tell me about building a project from scratch.","Where do you see yourself in 3 years?","How do you handle failure?","Tell me about a time you exceeded expectations."],
        "Artificial Intelligence & Machine Learning": ["How does Flipkart's recommendation system work?","How would you build a product search ranking system?","What is demand forecasting with ML?","How would you detect fake reviews using AI?","What is dynamic pricing with ML?","How to personalize homepage using ML?","What is customer churn prediction?","How to build a chatbot for customer support?","What is market basket analysis?","How would you build a fraud detection system?"],
        "Object Oriented Programming": ["Design class hierarchy for e-commerce product catalog.","Design a payment processing system.","Design a class for shopping cart.","Implement discount system using OOP.","Design an order management system.","Model a user authentication system.","Design a review and rating system.","Implement a search filter system.","Design notification service.","Design inventory management system."],
        "Computer Networks": ["How does Flipkart handle millions of concurrent users?","What is CDN and how does Flipkart use it?","How does payment gateway integration work?","What is API rate limiting?","How does Flipkart handle DDoS attacks?","What is geo-distribution of servers?","How does real-time inventory tracking work?","Role of message queues in e-commerce.","What is a reverse proxy?","What is load balancing?"],
        "Operating Systems": ["What is containerization?","Difference between VM and container.","What is Kubernetes?","What is auto-scaling?","What is a load balancer?","What is high availability?","What is disaster recovery?","What is CI/CD pipeline?","What is serverless computing?","What is microservices architecture?"],
        "Data Science & Analytics": ["Metrics to track for e-commerce platform.","How to measure success of a sale event.","What is cart abandonment rate?","How to segment customers for marketing.","What is RFM analysis?","How to forecast demand for Big Billion Day.","What is market basket analysis.","How to measure customer satisfaction.","What is cohort analysis?","What is funnel analysis?"],
        "General Aptitude & Reasoning": ["5 pens cost Rs 75. Cost of 8?","A in 10 days, B in 15. Together?","Next: 3, 7, 15, 31, 63, ?","Train 150m passes pole in 10 sec. Speed?","30% of 450?","Two pipes 20 and 30 min. Together?","Probability of head?","Odd: 2, 3, 5, 7, 9, 11.","If ROAD=52, GATE=?","Find next: 1, 8, 27, 64, ?"],
    },
}

# ── Session State ─────────────────────────────────────────
defaults = {"page":"home","logged_in":False,"user_name":"","question":"","feedback":"","score":0,"history":[],"question_count":0,"current_company":"","current_topic":"","question_type":"","used_pyqs":[]}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def nav_to(page):
    st.session_state.page = page
    st.rerun()

def get_pyq(company, topic):
    comp = company if company != "🏢 Any Company" else random.choice(list(PYQ_DATABASE.keys()))
    if comp in PYQ_DATABASE and topic in PYQ_DATABASE[comp]:
        questions = PYQ_DATABASE[comp][topic]
        unused = [q for q in questions if q not in st.session_state.used_pyqs]
        if not unused:
            st.session_state.used_pyqs = []
            unused = questions
        q = random.choice(unused)
        st.session_state.used_pyqs.append(q)
        return q
    return None

def gen_ai_question(company, topic, difficulty):
    comp = company.replace("🏢 Any Company", "a top tech company")
    prompt = f"""You are an expert interviewer for {comp} campus placement drives.
Generate ONE {difficulty} level interview question about: {topic}
Only return the question. No numbering, no extra text."""
    r = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"user","content":prompt}], temperature=0.8)
    return r.choices[0].message.content.strip()

def analyze(question, answer, language, company):
    comp = company.replace("🏢 Any Company","a top tech company")
    lang = "Respond in Hinglish (mix of Hindi and English)" if language == "Hinglish" else "Respond in simple clear English"
    prompt = f"""You are a friendly AI interview coach helping an Indian fresher prepare for {comp}.
Interview Question: {question}
Student Answer: {answer}
{lang}
Give feedback in this EXACT format:
SCORE: X/10
✅ WHAT YOU DID WELL:
• Point 1
• Point 2
❌ WHAT TO IMPROVE:
• Point 1
• Point 2
💡 BETTER ANSWER EXAMPLE:
Write a strong sample answer here
🏢 COMPANY TIP:
What this company specifically looks for
🧘 CONFIDENCE TIP:
One tip to reduce nervousness
Be encouraging and kind. Keep language simple."""
    r = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"user","content":prompt}], temperature=0.7)
    return r.choices[0].message.content.strip()

def extract_score(fb):
    try:
        for line in fb.split('\n'):
            if 'SCORE' in line.upper():
                for w in line.split():
                    w = w.replace('/10','').strip()
                    if w.isdigit():
                        return min(int(w), 10)
    except: pass
    return 5

# ══════════════════════════════════════════════════════════
# HOME PAGE
# ══════════════════════════════════════════════════════════
def page_home():
    st.markdown("""
    <div class="navbar">
        <div class="nav-logo">Ace<span>AI</span></div>
        <div style="display:flex;gap:1rem;align-items:center;">
            <span style="color:#958ea0;font-size:0.88rem;font-weight:500;">Features</span>
            <span style="color:#958ea0;font-size:0.88rem;font-weight:500;">Companies</span>
            <span style="color:#958ea0;font-size:0.88rem;font-weight:500;">About</span>
            <span style="color:#958ea0;font-size:0.88rem;font-weight:500;">Contact</span>
        </div>
    </div>
    <div class="hero">
        <div class="hero-badge">⚡ 500+ Real PYQs from 12 Top Companies</div>
        <h1 class="hero-title">Crack Your Dream<br><span class="gradient-text">Campus Interview</span></h1>
        <p class="hero-sub">India's smartest AI-powered interview coach. Practice real PYQs, get instant AI feedback, and build interview confidence — completely free.</p>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    with c1:
        if st.button("🚀 Start Practicing Free", key="h1"): nav_to("login")
    with c2:
        if st.button("ℹ️ About Us", key="h2"): nav_to("about")
    with c3:
        if st.button("📬 Contact Us", key="h3"): nav_to("contact")
    with c4:
        if st.button("🔑 Login", key="h4"): nav_to("login")

    st.markdown("""
    <div class="stats-section">
        <div><div class="stat-num">500+</div><div class="stat-desc">Real PYQs</div></div>
        <div><div class="stat-num">12</div><div class="stat-desc">Top Companies</div></div>
        <div><div class="stat-num">10</div><div class="stat-desc">Topics Covered</div></div>
        <div><div class="stat-num">AI</div><div class="stat-desc">Powered Feedback</div></div>
        <div><div class="stat-num">🇮🇳</div><div class="stat-desc">Built for India</div></div>
    </div>
    <div style="max-width:1200px;margin:0 auto;">
    <div class="section">
        <div class="section-tag">FEATURES</div>
        <div class="section-title">Everything to Crack Campus Drives</div>
        <p class="section-sub">From real PYQs to AI-powered feedback — AceAI covers every aspect of interview prep.</p>
        <div class="features-grid">
            <div class="feature-card"><div class="feature-icon">📚</div><div class="feature-title">Real PYQs from Top Companies</div><div class="feature-desc">Practice actual questions asked by TCS, Infosys, Google, Amazon & 8 more companies in their campus drives.</div></div>
            <div class="feature-card"><div class="feature-icon">🤖</div><div class="feature-title">AI-Powered Answer Analysis</div><div class="feature-desc">Get instant feedback — score out of 10, strengths, improvements, and a sample ideal answer.</div></div>
            <div class="feature-card"><div class="feature-icon">🏢</div><div class="feature-title">Company-Specific Prep</div><div class="feature-desc">Each company has different interview styles. Our AI knows exactly what TCS, Google, Amazon look for.</div></div>
            <div class="feature-card"><div class="feature-icon">🧘</div><div class="feature-title">Confidence Coach</div><div class="feature-desc">Specifically designed for Indian students who struggle with English communication and nervousness.</div></div>
            <div class="feature-card"><div class="feature-icon">🌐</div><div class="feature-title">Hinglish Support</div><div class="feature-desc">Get feedback in Hinglish — a friendly mix of Hindi and English — so you learn faster.</div></div>
            <div class="feature-card"><div class="feature-icon">📊</div><div class="feature-title">Progress Tracking</div><div class="feature-desc">Track your score history, see improvement over time, and identify weak topics.</div></div>
        </div>
    </div>
    </div>
    <div style="background:rgba(29,26,35,0.4);border-top:1px solid rgba(73,68,84,0.3);border-bottom:1px solid rgba(73,68,84,0.3);padding:4rem;">
    <div style="max-width:1200px;margin:0 auto;">
        <div class="section-tag">HOW IT WORKS</div>
        <div class="section-title">Start in 3 Simple Steps</div>
        <div class="steps-grid">
            <div class="step-card"><div class="step-num">1</div><div class="step-title">Choose Company & Topic</div><div class="step-desc">Select from 12 top companies and 10 interview topics based on which company you're targeting.</div></div>
            <div class="step-card"><div class="step-num">2</div><div class="step-title">Answer the Question</div><div class="step-desc">Get a real PYQ or AI-generated question. Type your answer just as you would speak in a real interview.</div></div>
            <div class="step-card"><div class="step-num">3</div><div class="step-title">Get AI Feedback</div><div class="step-desc">Receive a score, detailed analysis, a better answer, and company-specific tips.</div></div>
            <div class="step-card"><div class="step-num">4</div><div class="step-title">Track & Improve</div><div class="step-desc">Monitor your progress, identify weak areas, and keep practicing until interview-ready.</div></div>
        </div>
    </div>
    </div>
    <div class="companies-strip">
        <div class="companies-title">Practice for these top companies</div>
        <div class="companies-list">
            <span class="company-pill">TCS</span><span class="company-pill">Infosys</span><span class="company-pill">Wipro</span><span class="company-pill">HCL</span><span class="company-pill">Accenture</span><span class="company-pill">Cognizant</span><span class="company-pill">Capgemini</span><span class="company-pill">Tech Mahindra</span><span class="company-pill">Amazon</span><span class="company-pill">Google</span><span class="company-pill">Microsoft</span><span class="company-pill">Flipkart</span>
        </div>
    </div>
    <div class="footer">
        <div class="footer-grid">
            <div><div class="footer-brand-name">⚡ AceAI</div><div class="footer-brand-desc">India's smartest AI interview coach for campus placement preparation. Built specifically for Indian students by someone who faced the same challenges.</div></div>
            <div><div class="footer-heading">Product</div><span class="footer-link">Practice</span><span class="footer-link">PYQ Bank</span><span class="footer-link">Companies</span><span class="footer-link">Topics</span></div>
            <div><div class="footer-heading">Company</div><span class="footer-link">About Us</span><span class="footer-link">Contact</span><span class="footer-link">Privacy Policy</span><span class="footer-link">Terms of Use</span></div>
            <div><div class="footer-heading">Contact</div><span class="footer-link">📧 abhishekkatiyar2430686@gmail.com</span><span class="footer-link">📱 +91-8810939237</span><span class="footer-link">📍 Kanpur, Uttar Pradesh</span><span class="footer-link">🇮🇳 Made in India</span></div>
        </div>
        <div class="footer-bottom">
            <div class="footer-copy">© 2026 AceAI. All rights reserved.</div>
            <div class="footer-made">Made with ❤️ by <span>Abhishek Katiyar</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# LOGIN PAGE
# ══════════════════════════════════════════════════════════
def page_login():
    st.markdown("""
    <div style="min-height:100vh;background:radial-gradient(ellipse at 30% 50%, rgba(124,58,237,0.15) 0%, transparent 60%), #0d0b12;display:flex;align-items:center;justify-content:center;padding:2rem;">
    <div style="text-align:center;margin-bottom:2rem;">
        <div style="font-size:3rem;">⚡</div>
        <div style="font-size:2rem;font-weight:900;color:#d0bcff;">AceAI</div>
        <div style="font-size:1rem;font-weight:700;color:#e7e0ed;margin-top:1rem;">Welcome back!</div>
        <div style="font-size:0.82rem;color:#958ea0;">Login to start practicing interviews</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,1.2,1])
    with col2:
        st.markdown("<br>"*3, unsafe_allow_html=True)
        name = st.text_input("👤 Your Name", placeholder="e.g. Abhishek Katiyar")
        target = st.selectbox("🎯 Target Company", ["TCS","Infosys","Wipro","HCL","Accenture","Cognizant","Capgemini","Tech Mahindra","Amazon","Google","Microsoft","Flipkart"])
        if st.button("⚡ Enter AceAI", key="login_btn"):
            if name.strip():
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip()
                nav_to("dashboard")
            else:
                st.error("Please enter your name!")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Home", key="login_back"):
            nav_to("home")

# ══════════════════════════════════════════════════════════
# ABOUT PAGE
# ══════════════════════════════════════════════════════════
def page_about():
    st.markdown("""
    <div style="padding:4rem;max-width:1200px;margin:0 auto;">
        <div class="section-tag">ABOUT US</div>
        <div class="section-title">Built by a Student,<br>for Students</div>
        <div class="about-grid">
            <div class="about-img">
                <div class="about-icon">👨‍💻</div>
                <div class="about-img-title">Abhishek Katiyar</div>
                <div class="about-img-sub">BCA Student | PSIT College of Higher Education, Kanpur<br><br>AI Engineer Aspirant<br>Google AI Essentials Certified<br>BCG X GenAI Certified<br>Anthropic AI Fluency Certified</div>
            </div>
            <div class="about-text">
                <p>Hi! I'm <strong style="color:#d0bcff;">Abhishek Katiyar</strong>, a BCA student at PSIT College of Higher Education, Kanpur. I built AceAI because I faced the exact same problem — I could clear technical rounds but struggled with verbal communication and nervousness in interviews.</p>
                <p>I noticed most interview prep tools are either too expensive, English-only, or don't understand what Indian campus drives are really like. So I built something specifically for students like me.</p>
                <p>AceAI is powered by cutting-edge AI (Groq LLaMA 3.3), designed with Google Stitch AI, and built with Python & Streamlit. It's 100% free and made with ❤️ for Indian students.</p>
                <div style="margin-top:1.5rem;">
                    <div class="value-item"><div class="value-icon">🎯</div><div><div class="value-title">Our Mission</div><div class="value-desc">Make quality interview preparation accessible to every Indian student, regardless of college tier or English proficiency.</div></div></div>
                    <div class="value-item"><div class="value-icon">💡</div><div><div class="value-title">Our Vision</div><div class="value-desc">Help 1 million Indian students crack their dream campus placements using AI-powered personalized coaching.</div></div></div>
                    <div class="value-item"><div class="value-icon">🤝</div><div><div class="value-title">Our Values</div><div class="value-desc">Accessible, honest, encouraging, and always improving — just like the students we serve.</div></div></div>
                </div>
            </div>
        </div>
    </div>
    <div style="background:rgba(29,26,35,0.3);border-top:1px solid rgba(73,68,84,0.3);padding:3rem 4rem;">
    <div style="max-width:1200px;margin:0 auto;">
        <div class="section-tag">TECH STACK</div>
        <div class="section-title" style="font-size:1.8rem;">Built with Modern Technologies</div>
        <div class="features-grid" style="margin-top:1.5rem;">
            <div class="feature-card"><div class="feature-icon">🐍</div><div class="feature-title">Python</div><div class="feature-desc">Core programming language powering all backend logic and AI integrations.</div></div>
            <div class="feature-card"><div class="feature-icon">🎨</div><div class="feature-title">Streamlit</div><div class="feature-desc">Web framework for building the interactive user interface rapidly.</div></div>
            <div class="feature-card"><div class="feature-icon">🧠</div><div class="feature-title">Groq + LLaMA 3.3</div><div class="feature-desc">Ultra-fast AI inference for generating questions and analyzing answers in real-time.</div></div>
            <div class="feature-card"><div class="feature-icon">🎭</div><div class="feature-title">Google Stitch AI</div><div class="feature-desc">AI-powered UI design tool used to create the professional interface design.</div></div>
        </div>
    </div>
    </div>
    <div style="padding:3rem 4rem;max-width:1200px;margin:0 auto;">
        <div class="section-tag">CERTIFICATIONS</div>
        <div class="section-title" style="font-size:1.8rem;">Developer's Credentials</div>
        <div class="features-grid" style="margin-top:1.5rem;">
            <div class="feature-card"><div class="feature-icon">🔵</div><div class="feature-title">Google AI Essentials</div><div class="feature-desc">Specialization (5 courses) — Google / Coursera, May 2026</div></div>
            <div class="feature-card"><div class="feature-icon">🟣</div><div class="feature-title">AI Fluency: Framework & Foundations</div><div class="feature-desc">Anthropic — 2026</div></div>
            <div class="feature-card"><div class="feature-icon">🟢</div><div class="feature-title">GenAI Job Simulation</div><div class="feature-desc">BCG X / Forage — AI-Powered Financial Chatbot, March 2026</div></div>
            <div class="feature-card"><div class="feature-icon">🔷</div><div class="feature-title">Python Programming</div><div class="feature-desc">Infosys Springboard — October 2025</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("🚀 Start Practicing", key="ab1"): nav_to("login")
    with c2:
        if st.button("📬 Contact Us", key="ab2"): nav_to("contact")
    with c3:
        if st.button("🏠 Back to Home", key="ab3"): nav_to("home")

# ══════════════════════════════════════════════════════════
# CONTACT PAGE
# ══════════════════════════════════════════════════════════
def page_contact():
    st.markdown("""
    <div style="padding:4rem;max-width:1200px;margin:0 auto;">
        <div class="section-tag">CONTACT US</div>
        <div class="section-title">Get in Touch</div>
        <p class="section-sub">Have questions, feedback, or suggestions? We'd love to hear from you!</p>
        <div class="contact-grid">
            <div>
                <div class="contact-card"><div class="contact-icon">📧</div><div><div class="contact-label">Email</div><div class="contact-value">abhishekkatiyar2430686@gmail.com</div></div></div>
                <div class="contact-card"><div class="contact-icon">📱</div><div><div class="contact-label">Phone</div><div class="contact-value">+91-8810939237</div></div></div>
                <div class="contact-card"><div class="contact-icon">📍</div><div><div class="contact-label">Location</div><div class="contact-value">Kanpur, Uttar Pradesh, India</div></div></div>
                <div class="contact-card"><div class="contact-icon">💼</div><div><div class="contact-label">LinkedIn</div><div class="contact-value">linkedin.com/in/abhishek-katiyar-8148bb324</div></div></div>
                <div class="contact-card"><div class="contact-icon">⏰</div><div><div class="contact-label">Response Time</div><div class="contact-value">Within 24-48 hours</div></div></div>
            </div>
            <div class="contact-form">
                <div class="form-title">📬 Send us a Message</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<br>"*6, unsafe_allow_html=True)
        name = st.text_input("👤 Your Name", placeholder="Enter your name", key="c_name")
        email = st.text_input("📧 Your Email", placeholder="Enter your email", key="c_email")
        subject = st.selectbox("📋 Subject", ["General Question","Bug Report","Feature Request","Partnership","Feedback","Other"], key="c_sub")
        message = st.text_area("💬 Message", placeholder="Write your message here...", height=120, key="c_msg")
        if st.button("📬 Send Message", key="c_send"):
            if name.strip() and email.strip() and message.strip():
                st.success("✅ Message sent! We'll get back to you within 24-48 hours.")
            else:
                st.error("Please fill all fields!")

    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("🚀 Start Practicing", key="ct1"): nav_to("login")
    with c2:
        if st.button("ℹ️ About Us", key="ct2"): nav_to("about")
    with c3:
        if st.button("🏠 Back to Home", key="ct3"): nav_to("home")

# ══════════════════════════════════════════════════════════
# DASHBOARD PAGE
# ══════════════════════════════════════════════════════════
def page_dashboard():
    if not st.session_state.logged_in:
        nav_to("login")
        return

    COMPANIES = ["🏢 Any Company","TCS","Infosys","Wipro","HCL","Accenture","Cognizant","Capgemini","Tech Mahindra","Amazon","Google","Microsoft","Flipkart"]
    TOPICS = ["Artificial Intelligence & Machine Learning","Python Programming","SQL & Databases","Data Science & Analytics","HR & Behavioral","DSA & Problem Solving","Computer Networks","Operating Systems","Object Oriented Programming","General Aptitude & Reasoning"]

    st.markdown(f"""
    <div class="dash-header">
        <div class="dash-logo">⚡ AceAI</div>
        <div class="dash-user">
            <div><div class="dash-user-name">{st.session_state.user_name}</div><div class="dash-user-role">Fresher</div></div>
            <span>👤</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    s_col, m_col, f_col = st.columns([1, 2.2, 1.2])

    with s_col:
        st.markdown('<div class="dash-nav-label">NAVIGATION</div>', unsafe_allow_html=True)
        if st.button("🏠 Home", key="d_home"): nav_to("home")
        if st.button("ℹ️ About", key="d_about"): nav_to("about")
        if st.button("📬 Contact", key="d_contact"): nav_to("contact")
        st.markdown("---")
        st.markdown('<div class="dash-nav-label">PRACTICE SETTINGS</div>', unsafe_allow_html=True)
        company = st.selectbox("🏢 Company", COMPANIES, key="d_comp")
        topic = st.selectbox("📚 Topic", TOPICS, key="d_topic")
        difficulty = st.selectbox("🎯 Level", ["Fresher","Intermediate","Advanced"], key="d_diff")
        language = st.selectbox("🌐 Language", ["English","Hinglish"], key="d_lang")
        st.markdown("---")
        if st.button("🔄 Reset Session", key="d_reset"):
            for k in ["question","feedback","score","history","question_count","used_pyqs","current_company","current_topic","question_type"]:
                st.session_state[k] = [] if k in ["history","used_pyqs"] else 0 if k in ["score","question_count"] else ""
            st.rerun()
        if st.button("🚪 Logout", key="d_logout"):
            st.session_state.logged_in = False
            st.session_state.user_name = ""
            nav_to("home")

    with m_col:
        # Metrics
        c1,c2,c3 = st.columns(3)
        with c1: st.metric("Questions Done", st.session_state.question_count)
        with c2:
            avg = sum(st.session_state.history)/len(st.session_state.history) if st.session_state.history else 0
            st.metric("Avg Score", f"{avg:.1f}/10" if avg else "—")
        with c3:
            best = max(st.session_state.history) if st.session_state.history else 0
            st.metric("Best Score", f"{best}/10" if best else "—")

        st.markdown("<br>", unsafe_allow_html=True)

        # Question display
        if st.session_state.question:
            badge = "q-badge-pyq" if st.session_state.question_type == "PYQ" else "q-badge-ai"
            label = "✅ Real PYQ" if st.session_state.question_type == "PYQ" else "🤖 AI Generated"
            st.markdown(f"""
            <div class="question-card">
                <div class="q-meta">
                    <span class="q-badge q-badge-company">🏢 {st.session_state.current_company}</span>
                    <span class="q-badge q-badge-topic">📚 {st.session_state.current_topic}</span>
                    <span class="q-badge {badge}">{label}</span>
                </div>
                <div class="q-text">{st.session_state.question}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="question-card" style="text-align:center;padding:2.5rem;">
                <div style="font-size:3rem;margin-bottom:0.8rem;">🎯</div>
                <div style="font-size:1rem;color:#e7e0ed;font-weight:600;margin-bottom:0.4rem;">Ready to Practice?</div>
                <div style="font-size:0.82rem;color:#958ea0;">Select company & topic from sidebar, then click a button below!</div>
            </div>
            """, unsafe_allow_html=True)

        # Buttons
        b1,b2,b3 = st.columns(3)
        with b1:
            if st.button("📚 PYQ Question", key="d_pyq"):
                q = get_pyq(company, topic)
                if q:
                    st.session_state.question = q
                    st.session_state.current_company = company
                    st.session_state.current_topic = topic
                    st.session_state.question_type = "PYQ"
                    st.session_state.feedback = ""
                    st.session_state.score = 0
                    st.rerun()
                else:
                    st.warning("No PYQs for this combo. Try AI Question!")
        with b2:
            if st.button("🤖 AI Question", key="d_ai"):
                with st.spinner("Generating..."):
                    st.session_state.question = gen_ai_question(company, topic, difficulty)
                    st.session_state.current_company = company
                    st.session_state.current_topic = topic
                    st.session_state.question_type = "AI Generated"
                    st.session_state.feedback = ""
                    st.session_state.score = 0
                    st.rerun()
        with b3:
            if st.button("⏭️ Skip", key="d_skip"):
                q = get_pyq(company, topic)
                if q:
                    st.session_state.question = q
                    st.session_state.current_company = company
                    st.session_state.current_topic = topic
                    st.session_state.question_type = "PYQ"
                    st.session_state.feedback = ""
                    st.session_state.score = 0
                    st.rerun()

        # Answer area
        if st.session_state.question:
            answer = st.text_area("✍️ Your Answer", placeholder="Type your answer naturally... Don't worry about perfect English. Just write as you would speak in a real interview. AI will help you improve! 💪", height=180, key="d_ans")
            wc = len(answer.split()) if answer.strip() else 0
            color = "#4ade80" if wc >= 30 else "#facc15" if wc >= 10 else "#f87171"
            st.markdown(f"<p style='font-size:0.72rem;color:{color};margin-top:0.2rem;'>Words: {wc} {'✅ Good!' if wc >= 30 else '⚠️ Write more' if wc >= 5 else ''}</p>", unsafe_allow_html=True)

            a1,a2 = st.columns([3,1])
            with a1:
                if st.button("🤖 Submit for AI Review", key="d_submit"):
                    if answer.strip() and len(answer.split()) >= 5:
                        with st.spinner("🤖 Analyzing your answer..."):
                            st.session_state.feedback = analyze(st.session_state.question, answer, language, st.session_state.current_company)
                            st.session_state.score = extract_score(st.session_state.feedback)
                            st.session_state.history.append(st.session_state.score)
                            st.session_state.question_count += 1
                            st.rerun()
                    else:
                        st.warning("⚠️ Please write at least 2-3 sentences!")
            with a2:
                if st.button("➡️ Next Q", key="d_next"):
                    q = get_pyq(company, topic)
                    if q:
                        st.session_state.question = q
                        st.session_state.question_type = "PYQ"
                    else:
                        with st.spinner("Generating..."):
                            st.session_state.question = gen_ai_question(company, topic, difficulty)
                            st.session_state.question_type = "AI Generated"
                    st.session_state.current_company = company
                    st.session_state.current_topic = topic
                    st.session_state.feedback = ""
                    st.session_state.score = 0
                    st.rerun()

    with f_col:
        # Score card
        if st.session_state.history:
            sc = st.session_state.score
            pct = sc * 10
            status = "Strong ✅" if sc >= 7 else "Average ⚠️" if sc >= 5 else "Needs Work ❌"
            scolor = "#4ade80" if sc >= 7 else "#facc15" if sc >= 5 else "#f87171"
            avg = sum(st.session_state.history)/len(st.session_state.history)
            st.markdown(f"""
            <div class="score-card">
                <div style="font-size:0.7rem;color:#958ea0;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.5rem;">Session Score</div>
                <div class="score-num">{sc}<span style="font-size:1rem;color:#958ea0;">/10</span></div>
                <div style="font-size:0.85rem;font-weight:700;color:{scolor};margin:0.3rem 0;">{status}</div>
                <div class="score-bar"><div class="score-fill" style="width:{pct}%;"></div></div>
                <div style="font-size:0.72rem;color:#958ea0;">Avg: {avg:.1f}/10 over {len(st.session_state.history)} Q's</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown('<div style="font-size:0.7rem;color:#494454;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.4rem;">SCORE HISTORY</div>', unsafe_allow_html=True)
            for i, s in enumerate(st.session_state.history[-5:]):
                c = "#4ade80" if s >= 7 else "#facc15" if s >= 5 else "#f87171"
                st.markdown(f"""
                <div style="margin-bottom:0.4rem;">
                    <div style="display:flex;justify-content:space-between;font-size:0.68rem;color:#958ea0;margin-bottom:2px;"><span>Q{i+1}</span><span style="color:{c};">{s}/10</span></div>
                    <div style="height:4px;background:#2c2832;border-radius:2px;overflow:hidden;"><div style="width:{s*10}%;height:100%;background:{c};border-radius:2px;"></div></div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="score-card">
                <div style="font-size:2.5rem;">📊</div>
                <div style="font-size:0.8rem;color:#958ea0;margin-top:0.5rem;">Your scores appear here after answering!</div>
            </div>
            """, unsafe_allow_html=True)

        # Feedback card
        if st.session_state.feedback:
            fb = st.session_state.feedback
            lines = fb.split('\n')
            in_section = None
            output = '<div class="feedback-card"><div class="feedback-header"><span class="feedback-title">🤖 AI Feedback</span><span class="live-badge">LIVE</span></div><div class="feedback-body">'

            for line in lines:
                line = line.strip()
                if not line: continue
                if '✅' in line and 'WELL' in line.upper():
                    output += '<div class="feedback-section-title" style="color:#4ade80;">✅ What You Did Well</div>'
                    in_section = 'good'
                elif '❌' in line and 'IMPROVE' in line.upper():
                    output += '<div class="feedback-section-title" style="color:#f87171;">❌ What to Improve</div>'
                    in_section = 'improve'
                elif '💡' in line and 'BETTER' in line.upper():
                    output += '<div class="feedback-section-title" style="color:#d0bcff;">💡 Better Answer</div>'
                    in_section = 'better'
                elif '🏢' in line and 'TIP' in line.upper():
                    output += '<div class="feedback-section-title" style="color:#60a5fa;">🏢 Company Tip</div>'
                    in_section = 'company'
                elif '🧘' in line and 'CONFIDENCE' in line.upper():
                    output += '<div class="feedback-section-title" style="color:#c084fc;">🧘 Confidence Tip</div>'
                    in_section = 'confidence'
                elif 'SCORE' in line.upper():
                    continue
                elif line.startswith('•') or line.startswith('-'):
                    cls = 'good' if in_section == 'good' else 'improve' if in_section == 'improve' else ''
                    output += f'<div class="feedback-item {cls}">{line[1:].strip()}</div>'
                elif in_section in ['better','company','confidence'] and line:
                    output += f'<div class="feedback-item">{line}</div>'

            output += '</div></div>'
            st.markdown(output, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="feedback-card">
                <div class="feedback-header"><span class="feedback-title">AI Feedback Panel</span><span class="live-badge">READY</span></div>
                <div class="feedback-body" style="text-align:center;padding:1.5rem;">
                    <div style="font-size:2rem;margin-bottom:0.8rem;">🤖</div>
                    <div style="font-size:0.78rem;color:#958ea0;line-height:1.7;">
                        Answer a question to get:<br>
                        ✅ Score out of 10<br>
                        ✅ Strengths<br>
                        ✅ Areas to improve<br>
                        ✅ Better answer example<br>
                        ✅ Company-specific tips<br>
                        ✅ Confidence tips
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# ROUTER
# ══════════════════════════════════════════════════════════
page = st.session_state.page
if page == "home": page_home()
elif page == "login": page_login()
elif page == "dashboard": page_dashboard()
elif page == "about": page_about()
elif page == "contact": page_contact()
else: page_home()