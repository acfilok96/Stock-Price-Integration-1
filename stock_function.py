from PIL import Image
from excuses import Excuses
import streamlit as st
from streamlit_chat import message
from prompts import PromptCls
from model_description import run_tool_interaction


def Stock_function():
    
    #################################################
    col1, col2 = st.columns((1, 2.5))

    original = Image.open("Image1/tony.jpg")
    col1.image(original, use_column_width=True)
    col1.info(":blue[Hey, I'm a stock expert! Happy to help you!] 😊")
    container_11 = col2.container(height = 350, border = False)
    
    ################################################
        
    if "messages_temp_F" not in st.session_state:
        st.session_state.messages_temp_F = []


    k = 1
    with container_11:

        for message_s in st.session_state.messages_temp_F:
            if message_s["role"] == "Dipankaruser":
                message(message_s["content"], is_user = True, key = str(k) + '_user', avatar_style = "initials", seed = "Dipankar Porey")
            elif message_s["role"] == "Stockassistant":
                message(message_s["content"], key = str(k), avatar_style = "initials", seed = "Tony", allow_html = True)
            k += 1

    def clear_chat_history():
        
        st.session_state.messages_temp_F = []
        
    st.sidebar.button(':green[*Clear Chat History*]', on_click = clear_chat_history)
            
    if prompt := st.chat_input("Ask me !"):
        
        with container_11:
            
            st.session_state.messages_temp_F.append({"role": str("Dipankar")+"user", "content": prompt})
            

            message(prompt, is_user = True, key = str(k) + '_user', avatar_style = "initials", seed = "Dipankar Porey")

            k += 1
            full_response = ""
            with st.spinner(":green[Thinking . . .]"):
                try: 

                    prompt_prompt = PromptCls.StockPromptStyleVanilla(prompt)
                    full_response = run_tool_interaction(prompt_prompt)
                    message(full_response , key = str(k), avatar_style = "initials", seed = "Tony", allow_html=True)
                
                except Exception as e:
                    
                    full_response = Excuses.listofExcuses()
                    message(full_response, key = str(k), avatar_style = "initials", seed = "Tony", allow_html=True)
                
            st.session_state.messages_temp_F.append({"role": str("Stock")+"assistant", "content": full_response})
