def describe_dataframe(data):

    a=pd.DataFrame()
    a['column_name']=data.columns
    a['column_dtype']=data.dtypes.values
    a['null_count']=data.isnull().sum().values
    a['unique_value_count']=data.nunique().values
    a.style.background_gradient(cmap='Reds')