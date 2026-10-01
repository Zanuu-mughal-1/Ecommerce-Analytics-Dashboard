from pathlib import Path
import pandas as pd, matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
df=pd.read_csv(ROOT/'data/sales.csv',parse_dates=['date']); df['month']=df.date.dt.to_period('M').astype(str)
kpis=pd.DataFrame([{'Revenue':df.revenue.sum(),'Profit':df.profit.sum(),'Orders':df.order_id.nunique(),'Units':df.quantity.sum(),'AvgOrderValue':df.revenue.sum()/df.order_id.nunique(),'MarginPct':100*df.profit.sum()/df.revenue.sum()}]).round(2); kpis.to_csv(OUT/'kpis.csv',index=False)
monthly=df.groupby('month',as_index=False)[['revenue','profit']].sum(); monthly.to_csv(OUT/'monthly_performance.csv',index=False)
cat=df.groupby('category',as_index=False)[['revenue','profit']].sum().sort_values('revenue',ascending=False); cat.to_csv(OUT/'category_performance.csv',index=False)
country=df.groupby('country',as_index=False)['revenue'].sum().sort_values('revenue',ascending=False); country.to_csv(OUT/'country_revenue.csv',index=False)
plt.figure(figsize=(8,4)); plt.plot(monthly.month,monthly.revenue,marker='o',label='Revenue'); plt.plot(monthly.month,monthly.profit,marker='o',label='Profit'); plt.xticks(rotation=45); plt.legend(); plt.title('Monthly Revenue and Profit'); plt.tight_layout(); plt.savefig(OUT/'monthly_trend.png',dpi=160); plt.close()
plt.figure(figsize=(7,4)); plt.bar(cat.category,cat.revenue); plt.xticks(rotation=25); plt.title('Revenue by Category'); plt.tight_layout(); plt.savefig(OUT/'category_revenue.png',dpi=160); plt.close()
plt.figure(figsize=(7,4)); plt.bar(country.country,country.revenue); plt.title('Revenue by Country'); plt.tight_layout(); plt.savefig(OUT/'country_revenue.png',dpi=160); plt.close()
print(kpis.to_string(index=False))
