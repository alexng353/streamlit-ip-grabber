import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

if not _RELEASE:
    _streamlit_ip_grabber = components.declare_component(
        "streamlit_ip_grabber",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _streamlit_ip_grabber = components.declare_component("streamlit_ipgrabber", path=build_dir)

def streamlit_ip_grabber(key=None):
    value = _streamlit_ip_grabber(key=key, default=0)
    return value
    
if not _RELEASE:
    import streamlit as st
    if "ip" not in st.session_state:
        ip = streamlit_ip_grabber()
        if ip != 0:
            st.session_state["ip"]=ip
            print("Got IP")
    if "ip" in st.session_state:
        st.write(st.session_state['ip'])