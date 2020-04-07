def describe_dataframe(data, color='Greens', bound=0.99):

    description = pd.DataFrame()
    description['column_name'] = data.columns
    description['column_dtype'] = data.dtypes.values
    description['count'] = len(data)
    description['null_count'] = data.isnull().sum().values
    description['null_ratio'] = description['null_count'] / description['count']
    description['not_null_count'] = data.notnull().sum().values
    description['unique_value_count'] = data.nunique().values
    description['quick_notes'] = np.where(description['count'] == description['unique_value_count'],
                                          'Can be taken as primary key',
                                          np.where(description['unique_value_count'] == 1,
                                                   'Same for all data set, can be dropped',
                                                   np.where(description['null_ratio'] >= bound,
                                                            'The null ratio is greater than ' + str(bound) + ', drop',
                                                            '')))

    description = description.style.background_gradient(cmap=color)

    return description

