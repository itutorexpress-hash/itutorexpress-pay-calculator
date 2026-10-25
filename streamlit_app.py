import streamlit as st

st.set_page_config(page_title="iTutorExpress | Tutor Pay Calculator", page_icon="📊", layout="centered")

st.markdown("""
<style>
.block-container {max-width: 960px; padding-top: 2.2rem;}
div[data-testid="stMetricValue"] {font-size: 2.15rem; font-weight: 750;}
div[data-testid="stMetricLabel"] {font-size: 1rem;}
</style>
""", unsafe_allow_html=True)

st.title("Explore the tutor pay")

students = st.segmented_control(
    "Students per pod", options=[3, 4, 5], default=3,
    format_func=lambda n: f"{n} students", label_visibility="collapsed"
)
if students is None:
    students = 3

recommended_pay = {3: 15, 4: 18, 5: 21}
if "last_students" not in st.session_state:
    st.session_state.last_students = students
    st.session_state.pay = recommended_pay[students]
if students != st.session_state.last_students:
    st.session_state.pay = recommended_pay[students]
    st.session_state.last_students = students

st.markdown(f"**Tutor pay per 30-minute session — ${st.session_state.pay}**")
pay = st.slider("Adjust tutor pay", min_value=12, max_value=25, step=1,
                key="pay", label_visibility="collapsed")

price_per_student = 450
sessions_per_week = 3
weeks = 12
sessions = sessions_per_week * weeks
revenue = students * price_per_student
tutor_cost = pay * sessions
profit = revenue - tutor_cost
margin = profit / revenue * 100 if revenue else 0

st.divider()
left, right = st.columns(2)
with left:
    st.metric("Revenue / 12 weeks", f"${revenue:,}")
    st.metric("Gross profit / pod", f"${profit:,}")
with right:
    st.metric("Tutor cost / 12 weeks", f"${tutor_cost:,}")
    st.metric("Gross margin", f"{margin:.1f}%")

st.caption("Before administrative, assessment, technology and other operating expenses. Assumes all students pay and all 36 sessions take place.")
st.caption("Initial reading pilot: 3 students per pod; 4 may be offered when appropriate. Five students is for financial comparison only. Daniela's existing one-hour pod remains $25 for 3 students.")
