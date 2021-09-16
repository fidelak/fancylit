import pandas as pd
import altair as alt
import streamlit as st


def bar_chart(
    df: pd.DataFrame,
):
    """
    Purpose:
        Renders bar chart
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """

    x_col = st.selectbox("Select x axis for bar chart", df.columns)
    xcol_string = x_col + ":O"
    if st.checkbox("Show as continuous?", key="bar_chart_x_is_cont"):
        xcol_string = x_col + ":Q"
    y_col = st.selectbox("Select y axis for bar chart", df.columns)
    z_col = st.selectbox("Select z axis for bar chart", df.columns)

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(x=xcol_string, y=y_col, color=z_col, tooltip=list(df.columns))
        .interactive()
        .properties(title="Bar Chart for " + x_col + "," + y_col)
        .configure_title(fontSize=20)
        .configure_axis(labelFontSize=20, titleFontSize=20)
        .configure_legend(labelFontSize=20, titleFontSize=20)
    )

    st.altair_chart(chart, use_container_width=True)


def line_chart(
    df: pd.DataFrame,
):
    """
    Purpose:
        Renders line chart
    Args:
        df - Pandas dataframe
    Returns:
        N/A
    """
    interpol_kwds = (
        "linear",
        "linear-closed",
        "step",
        "step-before",
        "step-after",
        "basis",
        "basis-open",
        "cardinal",
        "cardinal-open",
        "bundle",
        "monotone",
    )
    x_col = st.selectbox("Select x axis for line chart", df.columns)
    y_col = st.selectbox("Select y axis for line chart", df.columns)
    interpol = st.selectbox("Interpolation options", interpol_kwds)
    x_col_string = x_col + ":O"
    if st.checkbox(
        "Show as continuous?", value=True, key="line_chart_x_is_cont"
    ):
        x_col_string = x_col + ":Q"
    encode_kwargs = {
        "x": x_col_string,
        "y": y_col,
        "tooltip": list(df.columns),
    }
    if st.checkbox("Multi series?", key="line_chart_is_multi-series"):
        z_col = st.selectbox("Series source", df.columns)
        encode_kwargs.update(color=z_col)
        encode_kwargs.update(strokeDash=z_col)
    else:
        encode_kwargs.pop("color", None)
        encode_kwargs.pop("strokeDash", None)
    show_points = st.checkbox("Show markers?", key="line_chart_display_markers")

    if st.checkbox("Fill area?", key="line_chart_fill_area"):
        chart = (
            alt.Chart(df)
            .mark_area(point=show_points, interpolate=interpol, line=True)
            .encode(**encode_kwargs)
            .interactive()
            .properties(title="Line Chart for " + x_col + "," + y_col)
            .configure_title(fontSize=20)
            .configure_axis(labelFontSize=20, titleFontSize=20)
            .configure_legend(labelFontSize=20, titleFontSize=20)
        )
    else:
        chart = (
            alt.Chart(df)
            .mark_line(point=show_points, interpolate=interpol)
            .encode(**encode_kwargs)
            .interactive()
            .properties(title="Line Chart for " + x_col + "," + y_col)
            .configure_title(fontSize=20)
            .configure_axis(labelFontSize=20, titleFontSize=20)
            .configure_legend(labelFontSize=20, titleFontSize=20)
        )

    st.altair_chart(chart, use_container_width=True)
