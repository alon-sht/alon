import streamlit as st

st.set_page_config(
    page_title="Contact Me",
    layout='centered',
    )
# %%
st.markdown(f"<h1 style='color:#38afff'>Hi :)</h1>",unsafe_allow_html=True)
st.markdown(f"#### My name is Alon Shtrikman")

st.markdown(f"#### If you found my suitcase, please contact me using the following links/details:")


def im(id):
    return "http://drive.google.com/uc?export=view&id="+str(id)

def mkdn(link,img):
    return f"""
            <a href="{link}">
            <img src="{img}" width="100" height="100" class="center"/>
            </a>
            """


col1, col2 = st.columns(2)
sp=st.markdown("---")
col3,col4 = st.columns(2)

wa_link=r"https://wa.me/972547592228?text=Hi%252C%20I%20found%20your%20suitcase"
wa_photo=im('1lbNxpJumlR-awz1Y51EApxcLQhwtuJ3w')
fb_link=r"https://m.me/alon.shtrikman"
fb_photo=im('1lTzhTaGFtLPOZS_AtCw6fPnu9RJZzcAi')
mail_link=r"mailto:alon.shtrikman@gmail.com"
mail_photo=im('1laYJYgcQIW_pp5OOrFZmpCh1G09MXr-F')
phone_link=r"tel:00972547592228"
phone_photo=im('1lVV0IU4AJhn5L2CXv7FaKQmc9DinZwD3')


col1.markdown(f"### [WhatsApp]({wa_link})",unsafe_allow_html=True)
col1.markdown(mkdn(wa_link,wa_photo),unsafe_allow_html=True)


col2.markdown(f"### [Facebook Messenger]({fb_link})",unsafe_allow_html=True)
col2.markdown(mkdn(fb_link,fb_photo),unsafe_allow_html=True)

col3.markdown(f"### [Email]({mail_link})",unsafe_allow_html=True)
col3.markdown(mkdn(mail_link,mail_photo),unsafe_allow_html=True)

col4.markdown(f"### [+972-54-7592228]({phone_link})",unsafe_allow_html=True)
col4.markdown(mkdn(phone_link,phone_photo),unsafe_allow_html=True)


