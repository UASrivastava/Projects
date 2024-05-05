import streamlit as st
import pandas as pd
import plotly.express as px
import os
st.title("My Dashboard")

file = st.file_uploader("Upload file",type=({"csv","xlsx"}))

dir = os.chdir(r"C:\Users\anand\archive")
if file is not None:
    st.write("Selected file Name:"+file.name)
    df=pd.read_csv(file.name,encoding="ISO-8859-1")
    st.write(df)
else:
    df=pd.read_csv(r"C:\Users\anand\archive\Superstore.csv",encoding="ISO-8859-1")
    st.write(df)    

# col1,col2 = st.coloumns((2))

# df["Order Date"]=pd.to_datetime(df["Order Date"],format="mixed")

# date1=pd.to_datetime(df["Order Date"]).min()
# date2=pd.to_datetime(df["Order Date"]).min()
# st.write(date1)
# st.write(date2)
# with col1:
#     startTime=pd.to_datetime(st.date_input("Start date"),date1)

# with col2:
#     endTime=pd.to_datetime(st.date_input("End date"),date2)

fig=px.pie(df.head(100),names='Region',color="Sales")
st.plotly_chart(fig)

fig=px.bar(df.head(20),x="Customer Name",y="Quantity",color='Profit',hover_data=['Discount','Category'],width=700,height=600,title="Order Count of categories Sub-Category")
st.plotly_chart(fig)


