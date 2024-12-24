import streamlit as st
import time 
from streamlit_elements import elements, mui, html
# from injector import st_tweaker

# col1  = st.container()
# col2  = st.container()
# col3  = st.container()

if 'axis_type' not in st.session_state:
    st.session_state['axis_type'] = "auto"
    
AXIS_STATUS = {
        "timestamp" : time.time(),
        "axies" : {
            "pan" : {
                "firmware_version" : "1.0.0",
                "position" : 0,
            }
        }
    }

json_view = st.json(AXIS_STATUS)
    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def buttons():
    # local_css("./designs/style.css")
    cols = st.columns(2)
    with cols[0]:
        st.button(label="Full Test", on_click=full_test)
        st.button(label="Limit Switch", on_click=limit_switch_test)
        st.button(label="Qmode Speed", on_click=qmode_speed_test)
    with cols[1]:
        st.button(label="Hmode Speed", on_click=hmode_speed_test)
        st.button(label="Update Axis", on_click=update_axis)
        st.button(label="Refresh", on_click=refresh_axis)
    with st.expander("Modify Params"):
        st.text_input("Pan Speed", value="0.0")
        

def keys():
    # local_css("./designs/keys.css")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.button("Up", key="keys")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Left")
    with col3:
        st.button("Right")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.button("Down")
        
def _update_status():
    AXIS_STATUS["timestamp"] = time.time()
     
def full_test():
    print("Full Test")

def limit_switch_test():
    print("Limit Switch Test")

def qmode_speed_test():
    print("Qmode Speed Test") 

def hmode_speed_test():
    print("Hmode Speed Test")

def update_axis():
    print("Update Axis")

def refresh_axis():
    print("Refreshing", st.session_state['axis_type'])
    _update_status()

def side_bar():
    with st.sidebar:
        st.subheader("AXIBO TESTING APP v1.1.0")
        st.session_state['axis_type'] = st.selectbox("Select Test Type", ("auto", "pan", "tilt"))
        buttons()
        # st.json(AXIS_STATUS)
        keys()
    # with elements("callbacks_retrieve_data"):
    #     mui.Button("Button", color="primary", onClick=update_axis)

    while True:
        time.sleep(1.00)
        AXIS_STATUS["timestamp"] = time.time()
        json_view.json(AXIS_STATUS)

                
def main():
    side_bar()
    
            
if __name__ == "__main__":
    main()
