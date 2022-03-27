import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

class IPGrabber extends StreamlitComponentBase{
  public state = {numClicks: 0, isFocused: false}
  
  public render = (): ReactNode => {
    return (
      <img src="https://raw.githubusercontent.com/alexng353/error-pages/main/1x1_%2300000000.png" onLoad={this.getIP} alt="">
      </img>
    )
  }

  private getIP = (): void => {
    const url = "https://api.ipify.org/?format=json"
    fetch(url)
      .then(response => response.json())
      .then(data => Streamlit.setComponentValue(data.ip));
  }
}
export default withStreamlitConnection(IPGrabber)