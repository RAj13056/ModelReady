"""MODELREADY — The Portfolio Issue.

Run: streamlit run app.py
All original portfolio checklist items, weights, grades, advice, agencies and trends retained.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="MODELREADY — The Portfolio Issue",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CSS_FILE = Path(__file__).resolve().parent / "styles" / "style.css"
st.markdown(f"<style>{CSS_FILE.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def html(fragment: str) -> None:
    st.markdown(fragment, unsafe_allow_html=True)


def clear_result() -> None:
    st.session_state["evaluation_visible"] = False


# Photography: Unsplash-hosted editorial images. The layout remains functional
# without the images (the CSS provides luxurious dark image fallbacks).
HERO_PHOTO = (
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb"
    "?auto=format&fit=crop&w=1050&q=85"
)
# Original editorial photograph bundled with MODELREADY (works without photo hosting).
# Encode the bundled photograph so Streamlit can display it without
# .streamlit/config.toml or enableStaticServing.
photo_path = Path(__file__).resolve().parent / "static" / "one_to_watch_editorial.jpg"
AGENCY_PHOTO = (
    "https://images.unsplash.com/photo-1539109136881-3be0616acf4b"
    "?auto=format&fit=crop&w=1000&q=85"
)

# ----------------------------------------------------
# THE COVER / HERO
# ----------------------------------------------------
html("""
<div class="masthead">
  <div class="wordmark">MODEL<span>READY</span><b>.</b></div>
  <div class="masthead-right">THE PORTFOLIO ISSUE <span class="masthead-dot">✦</span> 2026 EDITION</div>
</div>
<div class="microbar">
  <span>MODEL PORTFOLIO INTELLIGENCE</span>
  <span>THE ART OF BEING SEEN</span>
  <span>INDEPENDENT PORTFOLIO REVIEW</span>
</div>
""")

html(f"""
<section class="cover">
  <div class="cover-photo" aria-hidden="true" style="background-image:linear-gradient(90deg,#0d0d0c 1%,rgba(13,13,12,.26) 48%,rgba(13,13,12,.08)),url('{HERO_PHOTO}')"></div>
  <div class="cover-scrim" aria-hidden="true"></div>
  <div class="cover-topline"><span>AGENCY PORTFOLIO INTELLIGENCE</span><span>VOL. 01 / MODELREADY</span></div>
  <div class="cover-content">
     <div class="cover-kicker">THE MODEL PORTFOLIO REVIEW</div>
     <h1>READY FOR<br><em>REPRESENTATION?</em></h1>
     <p>Agency-level portfolio analysis for aspiring fashion models. Evaluate your portfolio against international standards and prepare for professional representation with confidence.</p>
     <div class="cover-bottomline"><span>YOUR CAREER. YOUR NEXT CHAPTER.</span><span class="cover-cross">✦</span></div>
  </div>
  <div class="cover-vertical">MODELREADY / EDITION 001</div>
</section>
""")

html("""
<div class="editorial-stats">
  <div class="editorial-stat"><span class="stat-no">01 /</span><strong>15</strong><span class="stat-label">LEADING AGENCIES</span></div>
  <div class="editorial-stat"><span class="stat-no">02 /</span><strong>09</strong><span class="stat-label">PORTFOLIO ASSETS EVALUATED</span></div>
  <div class="editorial-stat"><span class="stat-no">03 /</span><strong>05</strong><span class="stat-label">MODEL CATEGORIES</span></div>
  <div class="editorial-stat"><span class="stat-no">04 /</span><strong class="stat-elite">ELITE</strong><span class="stat-label">INDUSTRY BENCHMARK</span></div>
</div>
<div class="editor-note"><span>THE STANDARD</span><p>Professional portfolio evaluation inspired by international agency standards.</p><span class="editor-note-mark">✦</span></div>
""")

# ----------------------------------------------------
# THE ASSESSMENT / SAME ORIGINAL CONTENT
# ----------------------------------------------------
html("""
<div class="section-topline"><span>THE ASSESSMENT</span><span>01 — 03</span></div>
<div class="feature-heading">
  <div><div class="section-kicker">01 / THE PROFILE</div><h2>Your next chapter<br><em>starts here.</em></h2></div>
  <div class="feature-heading-aside">BEGIN YOUR ASSESSMENT <span>↘</span><p>Select your modeling category and experience level.</p></div>
</div>
""")

profile_left, profile_right = st.columns([1.18, 1], gap="large")
with profile_left:
    html('<div class="control-title">01 — MODELING CATEGORY</div>')
    model_type = st.radio(
        "Modeling Category",
        ["Fashion", "Commercial", "Fitness", "Runway", "Lifestyle"],
        horizontal=True,
        label_visibility="collapsed",
        key="modeling_category",
        on_change=clear_result,
    )
with profile_right:
    html('<div class="control-title">02 — EXPERIENCE LEVEL</div>')
    experience = st.radio(
        "Experience Level",
        ["Beginner", "Intermediate", "Professional"],
        horizontal=True,
        label_visibility="collapsed",
        key="experience_level",
        on_change=clear_result,
    )

html("""
<div class="section-topline assets-topline"><span>THE PORTFOLIO</span><span>02 — 03</span></div>
<div class="feature-heading assets-feature">
  <div><div class="section-kicker">02 / THE ESSENTIALS</div><h2>The portfolio<br><em>checklist.</em></h2></div>
  <div class="feature-heading-aside">NINE ELEMENTS. ONE IMPRESSION.<p>Choose every asset already included in your professional portfolio.</p></div>
</div>
<div class="asset-head"><span>YOUR MATERIALS</span><span>SELECT WHAT YOU HAVE ↘</span></div>
""")

col_a, col_b = st.columns(2, gap="large")
with col_a:
    headshot = st.checkbox("Professional Headshot", help="Professional beauty image with strong lighting", key="headshot", on_change=clear_result)
    digitals = st.checkbox("Agency Digitals", help="Natural digitals with minimal styling", key="digitals", on_change=clear_result)
    editorial = st.checkbox("Editorial Portfolio", help="High-fashion editorial imagery", key="editorial", on_change=clear_result)
    comp_card = st.checkbox("Comp Card", help="Industry-standard submission card", key="comp_card", on_change=clear_result)
    measurements = st.checkbox("Measurements Included", help="Current professional model measurements", key="measurements", on_change=clear_result)
with col_b:
    full_body = st.checkbox("Full Body Shot", help="Showcases proportions and silhouette", key="full_body", on_change=clear_result)
    profile = st.checkbox("Profile Shot", help="Displays profile and facial structure", key="profile", on_change=clear_result)
    commercial = st.checkbox("Commercial Portfolio", help="Commercial and lifestyle images", key="commercial", on_change=clear_result)
    contact = st.checkbox("Contact Information", help="Professional contact information", key="contact", on_change=clear_result)

items = {
    "Professional Headshot": headshot,
    "Full Body Shot": full_body,
    "Digitals": digitals,
    "Profile Shot": profile,
    "Editorial Photo": editorial,
    "Commercial Photo": commercial,
    "Comp Card": comp_card,
    "Contact Information": contact,
    "Measurements Included": measurements,
}
asset_count = sum(items.values())
completion = int(asset_count / 9 * 100)

html(f"""
<div class="progress-spread">
  <div class="progress-copy"><span>YOUR PORTFOLIO / PROGRESS</span><h3>Portfolio<br><em>completion.</em></h3></div>
  <div class="progress-number"><strong>{completion}</strong><span>%</span><div>{asset_count:02d} OF 09 ASSETS INCLUDED</div></div>
  <div class="progress-track"><div style="width:{completion}%"></div></div>
</div>
""")

# A native Streamlit action button preserves the original scoring interaction.
evaluate = st.button("REVEAL MY PORTFOLIO ASSESSMENT  ↗", use_container_width=True, type="primary")
if evaluate:
    st.session_state["evaluation_visible"] = True

# ----------------------------------------------------
# THE REPORT / SAME ORIGINAL WEIGHTS & ADVICE
# ----------------------------------------------------
if st.session_state.get("evaluation_visible", False):
    weights = {
        "Professional Headshot": 15,
        "Full Body Shot": 15,
        "Digitals": 15,
        "Profile Shot": 10,
        "Editorial Photo": 10,
        "Commercial Photo": 10,
        "Comp Card": 10,
        "Contact Information": 10,
        "Measurements Included": 5,
    }
    score = sum(weights[item] for item, selected in items.items() if selected)
    if experience == "Intermediate":
        score += 5
    elif experience == "Professional":
        score += 10
    score = min(score, 100)

    status = "Not Ready" if score < 50 else "Almost Ready" if score < 80 else "Ready"
    grade = "A+" if score >= 90 else "A" if score >= 80 else "B" if score >= 70 else "C" if score >= 60 else "Needs Improvement"
    badge = "Agency Ready" if score >= 85 else "Nearly Ready" if score >= 70 else "Portfolio In Progress"
    missing_items = [item for item, selected in items.items() if not selected]

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

    recommendations = []
    if not headshot:
        recommendations.append("Add a professional headshot with clean lighting and minimal editing.")
    if not full_body:
        recommendations.append("Include a full body image to showcase proportions.")
    if not digitals:
        recommendations.append("Create agency-standard digitals with minimal styling.")
    if not profile:
        recommendations.append("Add a profile shot to show facial structure.")
    if not editorial:
        recommendations.append("Add editorial work to show versatility.")
    if not commercial:
        recommendations.append("Include commercial images to demonstrate market appeal.")
    if not comp_card:
        recommendations.append("Create a professional comp card.")
    if not measurements:
        recommendations.append("Include accurate and updated measurements.")
    if not contact:
        recommendations.append("Add professional contact information.")
    if model_type == "Runway" and not full_body:
        recommendations.append("Runway models should prioritize full-body imagery.")
    if model_type == "Fitness" and not commercial:
        recommendations.append("Fitness portfolios benefit from athletic and commercial-style content.")
    if model_type == "Fashion" and not editorial:
        recommendations.append("Fashion portfolios should include editorial imagery.")

    if score < 50:
        next_steps = ["Build a complete modeling portfolio.", "Schedule a professional photoshoot.", "Create industry-standard digitals.", "Add measurements and contact information."]
    elif score < 80:
        next_steps = ["Fill missing portfolio gaps.", "Improve portfolio variety.", "Update your comp card.", "Begin researching modeling agencies."]
    else:
        next_steps = ["Prepare agency submissions.", "Continue updating your portfolio.", "Network with photographers and agencies.", "Maintain current measurements and digitals."]

    strength_html = "".join(f'<li><span>✦</span>{escape(s)}</li>' for s in strengths) or '<li><span>—</span>No major strengths identified yet.</li>'
    missing_html = "".join(f'<li><span>○</span>{escape(s)}</li>' for s in missing_items) or '<li><span>✦</span>Your portfolio includes all recommended assets.</li>'
    rec_html = "".join(f'<li><span>↗</span>{escape(s)}</li>' for s in recommendations) or '<li><span>✦</span>Excellent! Your portfolio appears ready for agency submission.</li>'
    steps_html = "".join(f'<li><span>{n:02d}</span>{escape(s)}</li>' for n, s in enumerate(next_steps, 1))
    submission_assets = [
        ("Professional Photos", headshot and full_body),
        ("Contact Information", contact),
        ("Measurements", measurements),
        ("Comp Card", comp_card),
        ("Digitals", digitals),
    ]
    submission_html = "".join(
        f'<div class="submission-entry"><span class="{"complete" if done else "incomplete"}">{"✓" if done else "○"}</span>{escape(item)}</div>'
        for item, done in submission_assets
    )

    html(f"""
<section class="report">
  <div class="report-top"><span>THE PORTFOLIO REPORT</span><span>03 / YOUR PERSONAL REVIEW</span></div>
  <div class="report-title"><div><span class="section-kicker">THE EVALUATION</span><h2>Your portfolio,<br><em>under review.</em></h2></div><span class="report-stamp">MODELREADY<br>ISSUE NO. 001</span></div>
  <div class="report-score-grid">
    <div class="report-score"><span class="report-metric-label">READINESS SCORE</span><div class="report-big-number">{score}<span>%</span></div><div class="metric-foot">AGENCY SUBMISSION READINESS</div><div class="report-bar"><div style="width:{score}%"></div></div></div>
    <div class="report-grade"><span class="report-metric-label">PORTFOLIO GRADE</span><div class="report-big-grade {'long-grade' if len(grade) > 3 else ''}">{escape(grade)}</div><div class="metric-foot">OVERALL PORTFOLIO ASSESSMENT</div></div>
    <div class="report-status"><span class="report-metric-label">SUBMISSION STATUS</span><div class="report-status-heading">{escape(badge)}</div><div class="metric-foot">CURRENT STANDING / {escape(status)}</div><div class="report-seal">✳</div></div>
  </div>
  <div class="report-two-col">
    <div class="report-list"><div class="report-list-kicker">01 / THE HIGHLIGHTS</div><h3>Portfolio <em>strengths.</em></h3><ul>{strength_html}</ul></div>
    <div class="report-list"><div class="report-list-kicker">02 / THE OPPORTUNITIES</div><h3>What's <em>missing.</em></h3><ul>{missing_html}</ul></div>
  </div>
  <div class="report-advice"><div class="report-advice-heading"><div class="report-list-kicker">03 / THE EXPERT EDIT</div><h3>Recommendations.</h3><p>What your portfolio could benefit from next.</p></div><ul>{rec_html}</ul></div>
  <div class="report-two-col report-final-grid">
    <div class="report-list"><div class="report-list-kicker">04 / YOUR ACTION PLAN</div><h3>Next <em>steps.</em></h3><ol class="steps-list">{steps_html}</ol></div>
    <div class="report-list"><div class="report-list-kicker">05 / BEFORE YOU SUBMIT</div><h3>Agency <em>checklist.</em></h3><div class="submission-list">{submission_html}</div></div>
  </div>
  <div class="report-footer"><span>MODELREADY / PRIVATE PORTFOLIO REVIEW</span><span>END OF ASSESSMENT ✦</span></div>
</section>
""")

# ----------------------------------------------------
# INDUSTRY PERSPECTIVE / ONE TO WATCH
# ----------------------------------------------------
html('<div class="industry-border"><span>THE INDUSTRY EDIT</span><span>04 — 05</span></div>')
# Native Streamlit image: displays the JPG directly from disk, without
# CSS background/data URLs/static-server configuration.
with st.container(key="one_to_watch"):
    watch_image, watch_text = st.columns([0.93, 1.07], gap="small", vertical_alignment="top")
    with watch_image:
        if photo_path.is_file():
            st.image(str(photo_path), use_container_width=True)
            html('<div class="one-watch-photo-credit">MODELREADY / THE INDUSTRY EDIT &nbsp; · &nbsp; 01</div>')
        else:
            st.error(f"One to Watch image missing: {photo_path}")
    with watch_text:
        html("""
        <div class="watch-copy watch-copy-native">
          <span class="section-kicker">04 / INDUSTRY PERSPECTIVE</span>
          <h2>One to<br><em>watch.</em></h2>
          <div class="watch-rule"></div>
          <div class="watch-quote-kicker">WORDS FROM THE ARCHIVE / ALEXANDER MCQUEEN</div>
          <blockquote>“There is no better designer than nature.”</blockquote>
          <div class="watch-quote-credit"><span class="credit-rule"></span> ALEXANDER MCQUEEN <span class="credit-role">/ BRITISH FASHION DESIGNER</span></div>
          <div class="watch-footer">THE FASHION INDUSTRY / A CLOSER LOOK <span>↗</span></div>
        </div>
        """)

AGENCIES = {
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
    "Nomad Management": "https://www.nomadmgmt.com",
}
agency_rows = "".join(
    f'<a class="agency-row" href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer"><span class="agency-n">{index:02d}</span><span class="agency-title">{escape(name)}</span><span class="agency-out">↗</span></a>'
    for index, (name, url) in enumerate(AGENCIES.items(), 1)
)

html(f"""
<section class="agency-section">
   <div class="agency-top"><span class="section-kicker">05 / THE INTERNATIONAL DIRECTORY</span><span>YOUR INDUSTRY REFERENCES / 15 AGENCIES</span></div>
   <h2>Global agency<br><em>watchlist.</em></h2>
   <div class="agency-layout">
     <div class="agency-feature-photo" style="background-image:linear-gradient(0deg,rgba(0,0,0,.65),transparent 50%),url('{AGENCY_PHOTO}')">
        <div class="agency-photo-caption"><span>THE INDUSTRY INDEX</span><p>Know the agencies.<br><em>Know the standard.</em></p><small>INTERNATIONAL REPRESENTATION / 001</small></div>
     </div>
     <div class="agency-index"><div class="agency-index-heading"><span>THE INDEX</span><span>EXPLORE ↗</span></div><div class="agency-grid">{agency_rows}</div></div>
   </div>
</section>
""")

TRENDS = [
    "Strong digitals",
    "Editorial versatility",
    "Commercial versatility",
    "Natural skin presentation",
    "Strong branding",
    "Professional online presence",
    "Confidence and consistency",
]
trend_rows = "".join(
    f'<div class="trend-row"><span>{i:02d}</span><strong>{escape(trend)}</strong><span class="trend-star">✦</span></div>'
    for i, trend in enumerate(TRENDS, 1)
)
html(f"""
<section class="trends-section">
  <div class="trends-header"><div class="section-kicker">THE INDUSTRY NOTES</div><h2>What matters<br><em>right now.</em></h2><p>Industry trends</p></div>
  <div class="trends-rows">{trend_rows}</div>
</section>
<footer class="closing-footer">
  <div class="footer-overline">AN EDITORIAL NOTE ON AMBITION, IMAGE & IDENTITY</div>
  <div class="closing-quote">The art of<br><em>being seen.</em></div>
  <div class="footer-bottom"><span class="footer-logo">MODELREADY<span>.</span></span><span>LUXURY PORTFOLIO INTELLIGENCE PLATFORM</span><span>BUILT WITH PYTHON & STREAMLIT</span></div>
</footer>
""")
