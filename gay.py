import numpy as np
import pandas as pd
from scipy import stats
covid_data = pd.read_csv('covid_data.csv')
covid_data=covid_data[['Entity','Code','Day','Central estimate']]
covid_data.head(5)
covid_data.dtypes
covid_data.shape
data_mean=np.mean(covid_data['Central estimate'])
data_median=np.median(covid_data['Central estimate'])
data_mode=stats.mode(covid_data['Central estimate'])
data_variance=np.var(covid_data['Central estimate'])
data_sd=np.std(covid_data['Central estimate'])
data_max=np.max(covid_data['Central estimate'])
data_min=np.min(covid_data['Central estimate'])
data_percentiles=np.percentile(covid_data['Central estimate'],60)
data_quartiles=np.percentile(covid_data['Central estimate'],0.75)
data_IQR=stats.iqr(covid_data['Central estimate'])