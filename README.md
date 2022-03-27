# Streamlit IP Grabber

This streamlit component grabs remote IPs from connections to [Streamlit](https://streamlit.io).

## Overview

This component is built in TypeScript and Python using REACT.js. 

Currently, the component uses [ipify](https://ipify.org) to fetch the user's public IP address.
* Install the component:

### [Download Latest from here](https://github.com/alexng353/streamlit-ip-grabber/releases)

- Download the .whl
- Open terminal and navigate to the directory with .whl in it

Then: `python3 -m pip install streamlit_ip_grabber-0.0.2-py3-none-any.whl`

#

### Use the component:
```python
import streamlit as st
from streamlit-ip-grabber import streamlit_ip_grabber

def getIP():
    if "ip" not in st.session_state:
        ip = streamlit_ip_grabber()
        if ip != 0:
            st.session_state["ip"]=ip
    if "ip" in st.session_state:
        # Put your code in here, an else: statement won't work
        st.write(st.session_state['ip'])
```

* This most likely will NOT work if the client has an adblocker or content blocker installed. We're working on that next.
## Quick Links

* [Streamlit Components documentation](https://docs.streamlit.io/library/components)
* [Streamlit Forums](https://discuss.streamlit.io/tag/custom-components)
* [Streamlit Components gallery](https://www.streamlit.io/components)
