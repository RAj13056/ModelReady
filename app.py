import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="ModelReady Lite",
    page_icon="📸",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}
.title {
    text-align: center;
    color: #d63384;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# APP TITLE
# --------------------------------------------------
st.markdown('<div class="title">📸 ModelReady Lite</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Fashion Model Portfolio Readiness Checker</div>',
    unsafe_allow_html=True
)

st.write(
    "Evaluate how prepared your modeling portfolio is for agency submissions."
)

st.divider()

# --------------------------------------------------
# EXPERIENCE LEVEL
# --------------------------------------------------
experience = st.selectbox(
    "Experience Level",
    ["Beginner", "Intermediate", "Professional"]
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

    # Dictionary of portfolio items
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

    # Small bonus for experience level
    if experience == "Intermediate":
        score += 5
    elif experience == "Professional":
        score += 10

    # Prevent score from exceeding 100
    score = min(score, 100)

    # Missing portfolio assets
    missing_items = [
        item for item, completed in items.items()
        if not completed
    ]

    # Determine status
    if score < 50:
        status = "❌ Not Ready"
    elif score < 80:
        status = "⚠️ Almost Ready"
    else:
        status = "✅ Ready"

    st.divider()

    st.subheader("Results")

    st.metric("Readiness Score", f"{score}%")
    st.progress(score / 100)

    st.markdown(f"### Status: {status}")

    # --------------------------------------------------
    # MISSING ITEMS
    # --------------------------------------------------
    st.subheader("Missing Items")

    if missing_items:
        for item in missing_items:
            st.write(f"• {item}")
    else:
        st.success("No missing items found. Great job!")

    # --------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------
    st.subheader("Recommendations")

    recommendations = []

    if not headshot:
        recommendations.append(
            "Add a professional headshot with natural lighting."
        )

    if not full_body:
        recommendations.append(
            "Include a full body image to showcase proportions."
        )

    if not digitals:
        recommendations.append(
            "Create clean digitals with minimal styling."
        )

    if not profile:
        recommendations.append(
            "Add a profile shot to highlight facial structure."
        )

    if not editorial:
        recommendations.append(
            "Include editorial images to demonstrate versatility."
        )

    if not commercial:
        recommendations.append(
            "Consider adding commercial-style portfolio images."
        )

    if not comp_card:
        recommendations.append(
            "Create a professional comp card for agency submissions."
        )

    if not measurements:
        recommendations.append(
            "Include accurate and updated body measurements."
        )

    if not contact:
        recommendations.append(
            "Ensure your contact information is clearly visible."
        )

    if recommendations:
        for rec in recommendations:
            st.write(f"✅ {rec}")
    else:
        st.success(
            "Excellent portfolio! Your portfolio appears ready for submission."
        )

    # --------------------------------------------------
    # FINAL MESSAGE
    # --------------------------------------------------
    if score >= 80:
        st.balloons()
        st.success(
            "Congratulations! Your portfolio is in strong shape for agency submissions."
        )