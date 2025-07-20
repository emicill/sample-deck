import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Coca-Cola: Smart & Sustainable",
    page_icon="🥤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Coca-Cola Branding CSS ---
st.markdown('''
<style>
body, [data-testid="stAppViewContainer"] {
    background: #fff !important; 
    body, [data-testid="stAppViewContainer"], .block-container, .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6, div {
    color: #000 !important;
}
.hero-bg {
    background: #E4002B;
    border-radius: 0 0 32px 32px;
    padding: 2.5rem 1rem 2rem 1rem;
    margin-bottom: 2.5rem;
    text-align: center;
    box-shadow: 0 4px 24px rgba(228,0,43,0.08);
}
.coke-logo {
    width: 180px;
    margin-bottom: 1.2rem;
}
.coke-title {
    font-size: 2.6rem;
    color: #fff;
    font-weight: bold;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
}
.coke-slogan {
    font-size: 1.3rem;
    color: #fff;
    font-weight: 500;
    margin-bottom: 0.5rem;
}
.coke-section {
    background: #fff;
    border-radius: 18px;
    box-shadow: 0 2px 12px rgba(28,28,28,0.07);
    padding: 2rem 1.5rem 2rem 1.5rem;
    margin-bottom: 2rem;
    max-width: 1100px;
    margin-left: auto;
    margin-right: auto;
}
.coke-section-title {
    color: #E4002B;
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 1rem;
    margin-top: 0.5rem;
}
.coke-article-btn {
    background: #E4002B;
    color: #fff;
    border-radius: 8px;
    padding: 0.7rem 1.5rem;
    font-size: 1.1rem;
    border: none;
    font-weight: bold;
    margin-top: 1rem;
    box-shadow: 0 2px 8px rgba(228,0,43,0.13);
    cursor: pointer;
    transition: background 0.2s, color 0.2s;
    display: inline-block;
    text-decoration: none;
}
.coke-article-btn:hover {
    background: #b71c1c;
    color: #fff;
}
.coke-article-title {
    color: #E4002B;
    font-size: 1.2rem;
    font-weight: bold;
    margin-top: 0.7rem;
    margin-bottom: 0.3rem;
}
.coke-article-desc {
    color: #1C1C1C;
    font-size: 1rem;
    margin-bottom: 0.5rem;
}
@media (max-width: 900px) {
    .coke-title {font-size: 1.5rem;}
    .coke-section-title {font-size: 1.2rem;}
    .coke-section {padding: 1rem;}
}
</style>
''', unsafe_allow_html=True)

# --- Hero Section ---
with st.container():
    st.markdown('<div class="hero-bg">', unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Coca-Cola_logo.svg/1024px-Coca-Cola_logo.svg.png")
    st.markdown('<div class="coke-title">Coca-Cola: Smart & Sustainable</div>', unsafe_allow_html=True)
    st.markdown('<div class="coke-slogan">Packaging a Better Future, Backed by Science</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Tabs Navigation ---
tabs = st.tabs([
    "Home",
    "Sustainability",
    "Packaging Facts",
    "Science Behind Coke",
    "Our Impact",
    "Contact"
])

# --- Home Tab ---
with tabs[0]:
    with st.container():
        st.markdown('<div class="coke-section">', unsafe_allow_html=True)
        st.markdown('<div class="coke-section-title">Featured Article</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.image("https://freepnglogo.com/images/all_img/coke-logo-2017-76d1.png", use_container_width=True)
        with col2:
            st.markdown("### Why Coca-Cola Believes in Smart, Sustainable Packaging")
            st.markdown("""
            **Discover how Coca-Cola is rethinking packaging, using more recycled materials, and investing in a circular economy for a cleaner planet.**
            
            Coca-Cola is committed to reducing its environmental impact by making all packaging 100% recyclable and increasing the use of recycled content. Learn how science and innovation are driving a more sustainable future for your favorite drink.
            """)
            st.markdown('<a href="#" class="coke-article-btn">Read More</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.write("")
    with st.container():
        st.markdown('<div class="coke-section">', unsafe_allow_html=True)
        st.markdown('<div class="coke-section-title">Latest Sustainability Stories</div>', unsafe_allow_html=True)
        grid_cols = st.columns(3, gap="large")
        articles = [
            {
                "img": "https://jbecotex.com/wp-content/uploads/2025/05/rPET-bottle-manufacturing.png",
                "title": "Are PET Bottles Sustainable?",
                "desc": "A deep dive into the science and lifecycle of PET bottles, and why they can be a smart choice for the environment."
            },
            {
                "img": "https://preview.redd.it/what-cools-the-fastest-glass-bottles-or-aluminium-cans-v0-xg217tfgmq5d1.jpeg?auto=webp&s=e445b83c21f48d558c32bf2d44cad04b951dfa9a",
                "title": "Cans vs Glass: The True Environmental Cost",
                "desc": "Comparing the carbon footprint, recyclability, and real-world impact of cans, glass, and plastic bottles."
            },
            {
                "img": "https://mir-s3-cdn-cf.behance.net/project_modules/hd/ae257423433081.56047f8c5846d.jpg",
                "title": "Recycling Innovation at Coca-Cola",
                "desc": "How Coke is investing in new recycling technologies and making it easier for consumers to close the loop."
            }
        ]
        for i, article in enumerate(articles):
            with grid_cols[i]:
                st.image(article["img"], use_container_width=True)
                st.markdown(f"**{article['title']}**")
                st.markdown(article["desc"])
                st.markdown('<a href="#" class="coke-article-btn">Read More</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- Sustainability Tab ---
with tabs[1]:
    with st.container():
        st.markdown('<div class="coke-section">', unsafe_allow_html=True)
        st.markdown('## Our Sustainability Commitment')
        st.markdown('''
**Coca-Cola is committed to a world without waste.**

- Using more recycled content in our packaging
- Reducing plastic use and investing in plant-based materials
- Supporting community recycling initiatives
- Making all packaging 100% recyclable by 2025
        ''')
        st.image("https://www.coca-cola.com/content/dam/onexp/ph/en/brands/coca-cola/sustainability/What%20happens%20when%20you%20recycle%20me_updated.png", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- Packaging Facts Tab ---
with tabs[2]:
    with st.container():
        st.markdown('<div class="coke-section">', unsafe_allow_html=True)
        st.markdown('## Packaging Facts')
        st.markdown('''
- **PET Bottles:** Lightweight, shatterproof, and 100% recyclable. Many Coke bottles now use up to 50% recycled PET (rPET).
- **Aluminum Cans:** Infinitely recyclable, with a global recycling rate of ~69%.
- **PlantBottle™:** Some bottles use up to 30% plant-based materials.
- **Lightweighting:** Coke has reduced the weight of its bottles and cans, cutting carbon emissions in transport.
        ''')
        st.image("https://thedrum-media.imgix.net//thedrum-prod/s3/news/tmp/684567/coca-cola_x_merlin_2.jpg?w=1280&ar=default&fit=crop&crop=faces&auto=format", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- Science Behind Coke Tab ---
with tabs[3]:
    with st.container():
        st.markdown('<div class="coke-section">', unsafe_allow_html=True)
        st.markdown('## The Science Behind Coke Packaging')
        st.markdown('''
Scientific studies show that PET bottles have a lower carbon footprint than glass, especially when recycled. Aluminum cans are highly recyclable and save 95% of the energy compared to new production. Our R&D teams are constantly innovating to make packaging even more sustainable.
        ''')
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzAqJfdr52E2kTXLeSX6GhKZsnsnzeXUEU9g&s", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- Our Impact Tab ---
with tabs[4]:
    with st.container():
        st.markdown('<div class="coke-section">', unsafe_allow_html=True)
        st.markdown('## Our Impact')
        st.markdown('''
- **Community Recycling:** Supporting local recycling programs worldwide.
- **Water Stewardship:** Returning more water to communities than we use in our drinks.
- **Climate Action:** Reducing emissions across our value chain.
        ''')
        st.image("https://s3.amazonaws.com/media.mediapost.com/dam/cropped/2024/12/09/cokepackaging_U77MysV.png", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- Contact Tab ---
with tabs[5]:
    with st.container():
        st.markdown('<div class="coke-section">', unsafe_allow_html=True)
        st.markdown('## Contact Us')
        st.markdown('''
Have questions or want to partner with us on sustainability?
- Email: sustainability@coca-cola.com
- Phone: +1-800-GET-COKE
- [Coca-Cola Sustainability Site](https://www.coca-colacompany.com/sustainability)
        ''')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Coca-Cola_logo.svg/1024px-Coca-Cola_logo.svg.png", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
---
<div style="text-align:center; color:#888; font-size:1rem; margin-top:2rem;">
    <p>Inspired by <a href='https://www.coca-colacompany.com/' target='_blank' style='color:#E4002B; text-decoration:underline;'>Coca-Cola.com</a> | Powered by science, inspired by sustainability.<br>Not affiliated with The Coca-Cola Company.</p>
</div>
""", unsafe_allow_html=True) 
