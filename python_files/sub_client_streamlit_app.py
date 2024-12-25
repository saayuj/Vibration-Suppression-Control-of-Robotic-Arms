import streamlit as st
import pandas as pd
import numpy as np
import time
import sys
import zmq


port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)


context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://localhost:%s" % port)


if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)


topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)


df = pd.DataFrame({'data': [0]}, index=[0.000])


if st.button("Generate Plot"):
    chart = st.line_chart(df)

    if st.button("Terminate Plot"):
        pass
    else:
        for i in range(5000):
            string = socket.recv()
            topic, messagedata = string.split()
            df.loc[0.001 * (i + 1)] = int(messagedata)
            chart.add_rows(df)
            time.sleep(0.001)
