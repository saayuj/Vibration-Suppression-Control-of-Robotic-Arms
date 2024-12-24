import streamlit as st
import numpy as np
import time


if st.button("Generate Plot"):
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    if st.button("Terminate Plot"):
        pass
    else:
        for i in range(1, 501):
            new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
            chart.add_rows(new_rows)
            last_rows = new_rows
            time.sleep(0.001)
