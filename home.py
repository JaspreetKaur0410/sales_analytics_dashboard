from turtle import color
from altair import Orientation
import streamlit as st
import pandas as pd
import plotly.express as px
import time
from streamlit_option_menu import option_menu
from numerize.numerize import numerize

st.set_page_config(page_title="Analytical_Dashboard", page_icon="🔔", layout="wide")


from query import *


st.subheader("Insurance Descriptive Analytics")
st.markdown("##")

results=view_all_data()
df=pd.DataFrame(results)
print(df)
st.dataframe(df)

#side bar
st.sidebar.image("pictures/logo1.png", caption="online Analytics")

#switcher
st.sidebar.header("Please filter")
region=st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())
location=st.sidebar.multiselect("Select Location", options=df["Location"].unique(), default=df["Location"].unique())
construction=st.sidebar.multiselect("Select Construction", options=df["Construction"].unique(), default=df["Construction"].unique())

df_selection=df.query("Region==@region & Location==@location & Construction==@construction")
st.dataframe(df_selection)

def Home():
    with st.expander("Tabular"):
        showData=st.multiselect('Filter: ', df_selection.columns, default=[])
        st.write(df_selection[showData])
    total_investment=float((df_selection["Investment"]).sum())
    investment_mode=float((df_selection["Investment"]).mode())
    investment_mean=float((df_selection["Investment"]).mean())
    investement_median=float((df_selection["Investment"]).median())
    rating=float((df_selection["Rating"]).sum())

    total1,total2,total3,total4,total5=st.columns(5,gap='small')
    with total1:
        st.info('Total Investment', icon="📈")
        st.metric("Sum TZS", value=f"{total_investment:,.0f}")
        
    with total2:
        st.info('Most frequent', icon="📈")
        st.metric("Mode TZS", value=f"{investment_mode:,.0f}")

    
    with total3:
        st.info('Average', icon="📈")
        st.metric("Mean TZS", value=f"{investment_mean:,.0f}")
        
    with total4:
        st.info('Median', icon="📈")
        st.metric("Median TZS", value=f"{investement_median:,.0f}")
        
    with total5:
        st.info('Rating', icon="📈")
        st.metric("Rating TZS", value=f"{rating:,.0f}")


# GRAPHS

def graphs():

    investment_by_business_type=(df_selection.groupby(by=["BusinessType"]).count()[["Investment"]].sort_values(by="Investment"))
    fig_investment_business_type=px.bar(
        investment_by_business_type,
        x="Investment",
        y=investment_by_business_type.index,
        orientation="h",
        title="<b> Investment by Business Type </b>",
        color_discrete_sequence=["#0083b8"]*len(investment_by_business_type),
        template="plotly_white"
    )
    
    fig_investment_business_type.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )

    investment_by_state=(df_selection.groupby(by=["State"]).count()[["Investment"]])
    fig_investment_state=px.line(
        investment_by_state,
        x=investment_by_state.index,
        y="Investment",
        orientation="v",
        title="<b> Investment by State </b>",
        color_discrete_sequence=["#0083b8"]*len(investment_by_state),
        template="plotly_white"
    )

    fig_investment_state.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False))
    )

    left,right=st.columns(2)
    left.plotly_chart(fig_investment_state, use_container_width=True)
    right.plotly_chart(fig_investment_business_type, use_container_width=True)

def progressBar():
    st.markdown("""<style>.stProgress > div > div > div > 
                div { background-image: linear-gradient(to right, #99ff99 , #FFFF00)}</style>""",unsafe_allow_html=True,)
    
    target=3000000000
    current=df_selection["Investment"].sum()
    percent=round((current/target*100))
    mybar=st.progress(0)
    
    if(percent>100):
        st.subheader("Target done! ")
    else:
        st.write("you have ",percent,"% ", "of ",(format(target,'d'),"TZS"))
        for percent_complete in range(percent):
            time.sleep(0.1)
            mybar.progress(percent_complete+1,text=" Target Percentage")


def sideBar():
    with st.sidebar:
        selected=option_menu(
        menu_title="Main Menu",
        options=["Home","Progress"],
        icons=["house","eye"],
        menu_icon="cast",
        default_index=0
    )
    if selected=="Home":
        #st.subheader(f"Page: {selected}")
        Home()
        graphs()
    if selected=="Progress":
        progressBar()
        graphs()
    
sideBar()

#theme
hide_st_style=""" 

<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""



