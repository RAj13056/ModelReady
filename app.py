import streamlit as st

def load_css():
    with open("styles/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="MODELREADY",
    page_icon="✨",
    layout="wide"
)

load_css()

# --------------------------------------------------
# TITLE
st.markdown("""
<div class="hero-box">

<div class="hero-title">
DISCOVER YOUR POTENTIAL
</div>

<div class="hero-subtitle">
Evaluate your portfolio against international agency standards,
identify opportunities for professional growth,
and build a portfolio worthy of the world's leading agencies.
</div>

</div>
""", unsafe_allow_html=True)# --------------------------------------------------
st.markdown(
    '<div class="title">MODELREADY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Luxury Portfolio Intelligence For Future Models</div>',
    unsafe_allow_html=True
)

st.write(
    "Evaluate how prepared your modeling portfolio is for agency submissions."
)

st.divider()

# --------------------------------------------------
# MODEL TYPE
# --------------------------------------------------
model_type = st.selectbox(
    "Modeling Category",
    [
        "Fashion",
        "Commercial",
        "Fitness",
        "Runway",
        "Lifestyle"
    ]
)

# --------------------------------------------------
# EXPERIENCE LEVEL
# --------------------------------------------------
experience = st.selectbox(
    "Experience Level",
    [
        "Beginner",
        "Intermediate",
        "Professional"
    ]
)

# --------------------------------------------------
# PORTFOLIO CHECKLIST
# --------------------------------------------------
st.subheader("Portfolio Checklist")

headshot = st.checkbox("Professional Headshot")
full_body = st.checkbox("Full Body Shot")
digitals = st.checkbox("Digitals")
profile = st.checkbox("Profile Shot")
editorial = st.checkbox("Editorial Photo")
commercial = st.checkbox("Commercial Photo")
comp_card = st.checkbox("Comp Card")
contact = st.checkbox("Contact Information")
measurements = st.checkbox("Measurements Included")

# --------------------------------------------------
# EVALUATE BUTTON
# --------------------------------------------------
if st.button("Evaluate Portfolio"):

    items = {
        "Professional Headshot": headshot,
        "Full Body Shot": full_body,
        "Digitals": digitals,
        "Profile Shot": profile,
        "Editorial Photo": editorial,
        "Commercial Photo": commercial,
        "Comp Card": comp_card,
        "Contact Information": contact,
        "Measurements Included": measurements
    }

    # --------------------------------------------------
    # WEIGHTED SCORING
    # --------------------------------------------------
    weights = {
        "Professional Headshot": 15,
        "Full Body Shot": 15,
        "Digitals": 15,
        "Profile Shot": 10,
        "Editorial Photo": 10,
        "Commercial Photo": 10,
        "Comp Card": 10,
        "Contact Information": 10,
        "Measurements Included": 5
    }

    score = 0

    for item, checked in items.items():
        if checked:
            score += weights[item]

    if experience == "Intermediate":
        score += 5
    elif experience == "Professional":
        score += 10

    score = min(score, 100)

    # --------------------------------------------------
    # STATUS
    # --------------------------------------------------
    if score < 50:
        status = "❌ Not Ready"
    elif score < 80:
        status = "⚠️ Almost Ready"
    else:
        status = "✅ Ready"

    # --------------------------------------------------
    # PORTFOLIO GRADE
    # --------------------------------------------------
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "Needs Improvement"

    # --------------------------------------------------
    # AGENCY BADGE
    # --------------------------------------------------
    if score >= 85:
        badge = "🏆 Agency Ready"
    elif score >= 70:
        badge = "⭐ Nearly Ready"
    else:
        badge = "📋 Portfolio In Progress"

    # --------------------------------------------------
    # MISSING ITEMS
    # --------------------------------------------------
    missing_items = [
        item for item, checked in items.items()
        if not checked
    ]

    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------
    st.divider()

    st.header("Portfolio Evaluation Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Readiness Score", f"{score}%")

    with col2:
        st.metric("Portfolio Grade", grade)

    st.progress(score / 100)

    st.success(f"Submission Status: {badge}")

    st.markdown(f"### Status: {status}")

    # --------------------------------------------------
    # STRENGTHS
    # --------------------------------------------------
    st.subheader("Portfolio Strengths")

    strengths = []

    if headshot:
        strengths.append("Strong professional presentation")

    if editorial:
        strengths.append("Showcases creative versatility")

    if commercial:
        strengths.append("Demonstrates marketability for commercial work")

    if digitals:
        strengths.append("Agency-friendly digitals included")

    if contact:
        strengths.append("Professional contact information provided")

    if strengths:
        for strength in strengths:
            st.write(f"✅ {strength}")
    else:
        st.write("No major strengths identified yet.")

    # --------------------------------------------------
    # MISSING ITEMS
    # --------------------------------------------------
    st.subheader("Missing Portfolio Assets")

    if missing_items:
        for item in missing_items:
            st.write(f"❌ {item}")
    else:
        st.success("Your portfolio includes all recommended assets.")

    # --------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------
    st.subheader("Recommendations")

    recommendations = []

    if not headshot:
        recommendations.append(
            "Add a professional headshot with clean lighting and minimal editing."
        )

    if not full_body:
        recommendations.append(
            "Include a full body image to showcase proportions."
        )

    if not digitals:
        recommendations.append(
            "Create agency-standard digitals with minimal styling."
        )

    if not profile:
        recommendations.append(
            "Add a profile shot to show facial structure."
        )

    if not editorial:
        recommendations.append(
            "Add editorial work to show versatility."
        )

    if not commercial:
        recommendations.append(
            "Include commercial images to demonstrate market appeal."
        )

    if not comp_card:
        recommendations.append(
            "Create a professional comp card."
        )

    if not measurements:
        recommendations.append(
            "Include accurate and updated measurements."
        )

    if not contact:
        recommendations.append(
            "Add professional contact information."
        )

    # Category-specific recommendations
    if model_type == "Runway" and not full_body:
        recommendations.append(
            "Runway models should prioritize full-body imagery."
        )

    if model_type == "Fitness" and not commercial:
        recommendations.append(
            "Fitness portfolios benefit from athletic and commercial-style content."
        )

    if model_type == "Fashion" and not editorial:
        recommendations.append(
            "Fashion portfolios should include editorial imagery."
        )

    if recommendations:
        for rec in recommendations:
            st.write(f"👉 {rec}")
    else:
        st.success(
            "Excellent! Your portfolio appears ready for agency submission."
        )

    # --------------------------------------------------
    # NEXT STEPS
    # --------------------------------------------------
    st.subheader("Next Steps")

    if score < 50:
        st.write("1. Build a complete modeling portfolio.")
        st.write("2. Schedule a professional photoshoot.")
        st.write("3. Create industry-standard digitals.")
        st.write("4. Add measurements and contact information.")

    elif score < 80:
        st.write("1. Fill missing portfolio gaps.")
        st.write("2. Improve portfolio variety.")
        st.write("3. Update your comp card.")
        st.write("4. Begin researching modeling agencies.")

    else:
        st.write("1. Prepare agency submissions.")
        st.write("2. Continue updating your portfolio.")
        st.write("3. Network with photographers and agencies.")
        st.write("4. Maintain current measurements and digitals.")

    # --------------------------------------------------
    # AGENCY SUBMISSION CHECKLIST
    # --------------------------------------------------
    st.subheader("Agency Submission Checklist")

    st.write("✅ Professional Photos")
    st.write("✅ Contact Information")
    st.write("✅ Measurements")
    st.write("✅ Comp Card")
    st.write("✅ Digitals")

    # --------------------------------------------------
    # SUCCESS ANIMATION
    # --------------------------------------------------
    if score >= 80:
        st.balloons()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
# --------------------------------------------------
# ONE TO WATCH
# --------------------------------------------------

st.divider()

st.header("🌟 One To Watch")

st.info("""
The world's leading models constantly study agency boards to understand
industry standards, portfolio quality, digitals, posing styles, and
the type of talent currently being represented globally.
""")

st.subheader("Global Agency Watchlist")

agencies = {
    "Wilhelmina Models": "https://www.wilhelmina.com",
    "IMG Models": "https://www.imgmodels.com",
    "Next Management": "https://www.nextmanagement.com",
    "Elite Model Management": "https://www.elitemodelmanagement.com",
    "Ford Models": "https://www.fordmodels.com",
    "Storm Management": "https://www.stormmanagement.com",
    "The Society Management": "https://www.thesocietymanagement.com",
    "Women Management": "https://www.womenmanagement.com",
    "DNA Model Management": "https://www.dnamodels.com",
    "Premier Model Management": "https://www.premiermodelmanagement.com",
    "Select Model Management": "https://www.selectmodel.com",
    "Viva Models": "https://www.viva-paris.com",
    "Major Model Management": "https://www.majormodel.com",
    "Freedom Models": "https://www.freedommodels.com",
    "Nomad Management": "https://www.nomadmgmt.com"
}

for agency, url in agencies.items():
    st.markdown(f"**{agency}**")
    st.write(url)

st.subheader("Industry Trends")

st.success("""
✓ Strong digitals

✓ Editorial versatility

✓ Commercial versatility

✓ Natural skin presentation

✓ Strong branding

✓ Professional online presence

✓ Confidence and consistency
""")

st.markdown("""
<div class="quote">
Fashion Changes. Style Endures.
</div>

<div class="quote-author">
MODELREADY
</div>
""", unsafe_allow_html=True)
st.divider()

st.caption(
    "MODELREADY | Luxury Portfolio Intelligence Platform | Built with Python, Streamlit and AI-Assisted Development"
)