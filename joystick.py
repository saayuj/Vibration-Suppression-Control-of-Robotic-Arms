import streamlit as st


def main():
    st.title("Joystick")

    x_axis_value = 0.0
    y_axis_value = 0.0

    x_axis_slider = st.slider("X-axis", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)
    y_axis_slider = st.slider("Y-axis", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)

    if x_axis_slider != x_axis_value or y_axis_slider != y_axis_value:
        x_axis_value = x_axis_slider
        y_axis_value = y_axis_slider
        st.text(f"X-axis value: {x_axis_value}")
        st.text(f"Y-axis value: {y_axis_value}")



if __name__ == "__main__":
    main()
