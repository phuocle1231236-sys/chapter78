import numpy as np
import pandas as pd
from scipy import stats
covid_data = pd.read_csv('covid_data.csv')
covid_data=covid_data[['iso_code','continent','location','date','total_cases','new_cases']]
covid_data.head(5)
covid_data.dtypes
covid_data.describe()
covid_data.shape
data_mean=np.mean(covid_data['new_cases'])
data_median=np.median(covid_data['new_cases'])
data_mode=stats.mode(covid_data['new_cases'])
data_variance=np.var(covid_data['new_cases'])
data_sd=np.std(covid_data['new_cases'])
data_max=np.max(covid_data['new_cases'])
data_min=np.min(covid_data['new_cases'])
data_percentiles=np.percentile(covid_data['new_cases'],60)
data_quartiles=np.percentile(covid_data['new_cases'],0.75)
data_IQR=stats.iqr(covid_data['new_cases'])