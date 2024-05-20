import streamlit as st
from PIL import Image
from stock_function import Stock_function

st.set_page_config(page_title='Stock Price Integration', layout="wide", page_icon = 'Image1/a3.jpg', initial_sidebar_state = 'auto')

st.markdown("""
<style>
.big-font-1 {
    font-size:20px !important;
    text-align: center; 
    color: yellow
}
</style>
""", unsafe_allow_html=True)


def main(): 
    st.sidebar.markdown('<p class="big-font-1">Stock Price Integration</p>', unsafe_allow_html = True)
    
    st.sidebar.image("Image1/17.png")

    Stock_function()

    show_advanced_info_1 = st.sidebar.toggle(":blue[*Show Application Details*]", value = True)
    
    if show_advanced_info_1:
        st.sidebar.info("""
                    
                    **Generative AI application**
                    
                    - **About:** *Stock Price Integration*
                    
                    - **Model:** *Anthropic Tools - Claude backend*

                    - **Market Data:** *Yahoo Finance*
                    
                    - **Language:** *English*
                    
                    - **Release Date:** *April, 2024*
                    
                    """)
        
    show_advanced_info_2 = st.sidebar.toggle(":blue[*Show Developer Details*]", value = False)
    
    if show_advanced_info_2:
        st.sidebar.info("""
                    
                    *This appplication has been created by [:blue[Dipankar Porey]](https://www.linkedin.com/in/dipankar-porey-403320259/), 
                    Former Technology Consultant, Senior at Ernst & Young LLP.* 
                    
                    """)

       
if __name__ == '__main__':
    main()
