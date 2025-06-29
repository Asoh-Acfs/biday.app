import streamlit as st
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: 
         linear-gradient(rgba(255,255,255,0.1), rgba(255,255,255,0.1)),
         
        url("https://i.postimg.cc/sXFhvNFd/28b4b66b94acdfb7f139bb1ed9ff6bf6.gif"),
        url("https://i.postimg.cc/0jSxrVq3/Screenshot-20250629-061325.jpg");
        url("https://i.postimg.cc/Z9S6BMdY/Screenshot-20250629-030117.jpg");
        
        background-size: cover, cover, cover;
        background-repeat: no-repeat, no-repeat, no-repeat;
        background-position: center, center, center;
    }

    .block-container { background-color: rgba(255, 255, 255, 0.0);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎀 Birthday content
st.title("🎀 Happy 22nd Birthday Chinenye, omoor, you're getting old oo 🎀")
st.image("https://i.postimg.cc/G2dW1h4N/Screenshot-20250629-033817.jpg", caption="I want cake 😭, tell Daddy to buy cake 👑", width=300)
st.image("https://i.postimg.cc/4Ytz3gnF/Screenshot-20250629-025200.jpg");
st.image("https://i.postimg.cc/Z9S6BMdY/Screenshot-20250629-030117.jpg");

st.subheader("💖 You are deeply loved and ANNOYING!!! 💖")

st.write("""
Dear Chinenye,

Wishing you a birthday as fabulous as your favorite color! 💅🏽💓  
You are annoying, irritating, a pain in my butt, and as extra as this app — and we LOVE that for you! 💄💝😒

May this year bring you all your heart's desires and more pink bags than Barbie.🎀 eyama 🤮🤢 

With all the love in the world,  
**Chidalu 💋**
""")

# Stretch the page so background shows fully
for _ in range(30):
    st.write("")

st.balloons()
