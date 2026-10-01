# Optional interactive dashboard: pip install -r optional-requirements.txt && streamlit run src/dashboard.py
from pathlib import Path
import pandas as pd
import streamlit as st
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/sales.csv',parse_dates=['date'])
st.set_page_config(page_title='E-Commerce Analytics',layout='wide'); st.title('E-Commerce Analytics Dashboard')
c1,c2,c3,c4=st.columns(4); c1.metric('Revenue',f"${df.revenue.sum():,.0f}"); c2.metric('Profit',f"${df.profit.sum():,.0f}"); c3.metric('Orders',f"{df.order_id.nunique():,}"); c4.metric('Margin',f"{100*df.profit.sum()/df.revenue.sum():.1f}%")
st.subheader('Monthly Revenue'); st.line_chart(df.set_index('date').resample('MS')['revenue'].sum())
st.subheader('Category Performance'); st.bar_chart(df.groupby('category')['revenue'].sum().sort_values(ascending=False))
st.dataframe(df.sort_values('date',ascending=False).head(50),use_container_width=True)
