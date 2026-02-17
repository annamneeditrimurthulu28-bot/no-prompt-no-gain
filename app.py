import streamlit as st

st.set_page_config(page_title="MarketMind", layout="centered")

# ======================
# GLOBAL CSS
# ======================
st.markdown("""
<style>
/* Hide Streamlit branding */
header {display:none;}
div[data-testid="stDecoration"] {display:none;}
footer {visibility:hidden;}
.block-container {padding-top: 1rem !important;}

/* Radio buttons as cards */
div[role="radiogroup"] label > div:first-child {
    display: none;
}

div[role="radiogroup"] label {
    width: 100%;
}

div[role="radiogroup"] label > div:last-child {
    padding: 18px 22px;
    border-radius: 14px;
    border: 2px solid #e5e7eb;
    margin-bottom: 16px;
    background: white;
    cursor: pointer;
    transition: all 0.25s ease;
    font-size: 16px;
}

div[role="radiogroup"] label:hover > div:last-child {
    border-color: #6366f1;
    background: #f5f7ff;
}

div[role="radiogroup"] label:has(input:checked) > div:last-child {
    border-color: #4f46e5;
    background: #e0e7ff;
    box-shadow: 0 0 0 4px rgba(79,70,229,0.25);
    font-weight: 700;
}

/* Output card */
.result-card {
    background: linear-gradient(135deg, #eef2ff, #ffffff);
    padding: 25px;
    border-radius: 16px;
    border-left: 6px solid #4f46e5;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown("## 📊 MarketMind")
st.markdown("Generative AI–Powered Sales & Marketing Intelligence")

# ======================
# INPUT SECTION
# ======================
task = st.radio(
    "Select Intelligence Type",
    [
        "Market Analysis",
        "Sales Strategy",
        "Customer Insights",
        "Marketing Campaign Ideas"
    ],
    index=0
)

user_input = st.text_area(
    "Enter your business / product / market details:",
    placeholder="Example: I am building an AI-powered fitness app for college students",
    height=120
)

generate = st.button("🚀 Generate Insight")

# ======================
# OUTPUT SECTION
# ======================
if generate:
    if not user_input.strip():
        st.error("❌ Please enter business / product / market details.")
    else:
        st.markdown("### ✅ AI Generated Insight")

        if task == "Market Analysis":
            insight_html = """
            <b>Market Overview:</b><br>
            Your idea addresses a real market need with measurable demand.<br><br>

            <b>Key Market Factors:</b>
            <ul>
                <li>Target customer demographics and purchasing behavior</li>
                <li>Existing competitors and differentiation opportunities</li>
                <li>Market size, growth rate, and pricing sensitivity</li>
            </ul>

            <b>Strategic Recommendation:</b><br>
            Conduct surveys, competitor benchmarking, and MVP testing before scaling.
            """

        elif task == "Sales Strategy":
            insight_html = """
            <b>Sales Objective:</b><br>
            Build a scalable and repeatable sales process.<br><br>

            <b>Recommended Actions:</b>
            <ul>
                <li>Clearly define your value proposition</li>
                <li>Select appropriate sales channels (online, partnerships, direct)</li>
                <li>Improve lead qualification and follow-up</li>
            </ul>

            <b>Expected Impact:</b><br>
            Higher conversion rates, predictable revenue, and stronger customer trust.
            """

        elif task == "Customer Insights":
            insight_html = """
            <b>Customer Understanding:</b><br>
            Customers expect personalized and relevant experiences.<br><br>

            <b>Insights Identified:</b>
            <ul>
                <li>Core customer pain points and motivations</li>
                <li>Behavior patterns and usage frequency</li>
                <li>Key drivers of satisfaction and churn</li>
            </ul>

            <b>Action Plan:</b><br>
            Segment customers and tailor messaging, pricing, and features accordingly.
            """

        elif task == "Marketing Campaign Ideas":
            insight_html = """
            <b>Campaign Goal:</b><br>
            Increase brand visibility and generate high-quality leads.<br><br>

            <b>Recommended Campaign Types:</b>
            <ul>
                <li>Social media ads targeting niche audiences</li>
                <li>Content marketing (blogs, reels, short-form videos)</li>
                <li>Influencer collaborations for trust-building</li>
                <li>Email campaigns for lead nurturing</li>
            </ul>

            <b>Expected Results:</b><br>
            Improved engagement, higher lead conversion, and stronger brand recall.
            """

        st.markdown(
            f"""
            <div class="result-card">
            <b>Selected Intelligence:</b> {task}<br><br>
            <b>Insight:</b><br>
            {insight_html}
            </div>
            """,
            unsafe_allow_html=True
        )
