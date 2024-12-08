# streamlit_app.py
import streamlit as st
from data_processing import (
    load_data, create_boxplot_activities, create_violinplot_sleep_duration,
    create_bar_study_time_vs_quality, create_violinplot_free_time,
    create_boxplot_caffeine_intake, create_line_physical_activity,
    create_line_screen_time, create_pairplot_study_screen,
    create_stacked_bar, create_correlation_heatmap
)


st.markdown("# Python project - Student Sleep Patterns")

st.markdown("### Hypothesis")
st.markdown("My assumption - the quality of sleep of students depends on students' hours of study, sleep duration, physical activity and screen time")

st.markdown("### Dataset")
st.markdown("Dataset is taken from - https://www.kaggle.com/datasets/arsalanjamal002/student-sleep-patterns/data")

st.markdown("### Describing the main details of dataset")
df = load_data()

st.write(df.head(10))
st.write("Data info:")
buffer = []
buffer.append("Number of rows: {}".format(df.shape[0]))
buffer.append("Number of columns: {}".format(df.shape[1]))
st.write("\n".join(buffer))

st.write("Data types:")
st.write(df.dtypes)
st.write("Check for NaN:")
st.write(df.isna().sum())

st.markdown("### Creation of plots")

st.markdown("#### Boxplot: Distribution of Activities")
fig_box = create_boxplot_activities()
st.pyplot(fig_box)

st.markdown("#### Violinplot: Sleep Duration vs Sleep Quality")
fig_violin_sleep = create_violinplot_sleep_duration()
st.pyplot(fig_violin_sleep)

st.markdown("#### Bar: Study Time vs Sleep Quality")
fig_bar_study = create_bar_study_time_vs_quality()
st.pyplot(fig_bar_study)

st.markdown("#### Violinplot: Free Time vs Sleep Quality")
fig_violin_free = create_violinplot_free_time()
st.pyplot(fig_violin_free)

st.markdown("#### Boxplot: Caffeine Intake vs Sleep Quality")
fig_caffeine = create_boxplot_caffeine_intake()
st.pyplot(fig_caffeine)

st.markdown("#### Lineplot: Physical Activity vs Sleep Quality")
fig_line_phys = create_line_physical_activity()
st.pyplot(fig_line_phys)

st.markdown("#### Lineplot: Screen Time vs Sleep Quality")
fig_line_screen = create_line_screen_time()
st.pyplot(fig_line_screen)

st.markdown("#### Pairplot: Study_Time, Sleep_Quality, and Screen_Time")
fig_pair = create_pairplot_study_screen()
st.pyplot(fig_pair)

st.markdown("#### Stacked Bar: Influence of different parameters with Sleep Quality")
fig_stacked = create_stacked_bar()
st.pyplot(fig_stacked)

st.markdown("#### Correlation Heatmap")
fig_corr = create_correlation_heatmap()
st.pyplot(fig_corr)

st.markdown("### Conclusion")
st.markdown("Our hypothesis is disproved, as there is not such a big correlation between factors and their relation to quality of sleep to make any decisions.")
