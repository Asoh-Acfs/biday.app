import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background:
            url('https://i.postimg.cc/Z9S6BMdY/Screenshot-20250629-030117.jpg'),
            url('https://i.postimg.cc/4Ytz3gnF/Screenshot-20250629-025200.jpg');
        background-size: cover, cover;
        background-repeat: no-repeat, no-repeat;
        background-position: center center, center center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 💅🏽 Inject pink & glitter styles
st.markdown(
    """
    <style>
        .stApp {
            background-color: #ffe6f0;
            background-image: url("https://i.imgur.com/Rwh6r8W.gif"); /* glitter overlay */
            background-size: cover;
            color: #d63384;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ff4da6;
        }
        .stButton > button {
            background-color: #ff69b4;
            color: white;
            border-radius: 12px;
        }
        img {
            border: 5px solid #ffb6c1;
            border-radius: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎀 Birthday content
st.title("🎀 Happy 22nd Birthday Chinenye ,omoor, you're getting old oo🎀")
st.image("https://i.postimg.cc/G2dW1h4N/Screenshot-20250629-033817.jpg", caption="I want cake 😭, tell Daddy to buy cake👑", width=300)

st.subheader("💖 You are deeply loved  and ANNOYING!!!💖")

st.write("""
Dear Chinenye,

Wishing you a birthday as fabulous as your favorite color! 💅🏽💓  
You are annoying, irritating, a pain in my butt, and as extra as this app — and we LOVE that for you! 💄💝😒

May this year bring you all your heart's desires and more pink bags than Barbie. eyama 🤮🤢 🎀

With all the love in the world,  
**Chidalu💋**
""")

st.balloons()
