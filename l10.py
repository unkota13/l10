import streamlit as st
import time
import random

hours = st.slider("hour", min_value=0, max_value=24,value=0)
minutes = st.slider("minites", min_value=0, max_value=59,value=0)
seconds = st.slider("secouns", min_value=0, max_value=59,value=0)

total_seconds = hours * 3600 + minutes * 60 + seconds

if st.button("set up(タイマースタート)"):

    placeholder = st.empty()

    for t in range(int(total_seconds), -1, -1):
        h = t // 3600
        m = (t % 3600) // 60
        s = t % 60

        placeholder.write(f"残り{h}h{m}m{s}s")
        time.sleep(1)

    placeholder.write("time up!")