def text_feature_generator(data, text_column):

    #turn existing text column into string.
    #for dealing with non-str values in the text.
    #For example: If there is comment like only 3, we cannot use this comment in the any preprocessing of text. So we need to change type
    data[text_column]=data[text_column].astype(str)

    #calculate raw length of the text column
    data[text_column+'_raw_length']=data[text_column].apply(len)

    #calculate number of punctuations before dropping punctuations
    import string
    import collections as ct
    punctuation_signs = string.punctuation
    print("Punctuation signs are ", punctuation_signs)
    r = []
    for i in range(len(df)):
        t = sum(v for c, v in ct.Counter(df['verbatim'][i]).items() if c in punctuation_signs)
        r.append(t)

    data[text_column+'_punctuation_count']=r
    df[text_column+'_punct_to_all_length_ratio'] = np.round(data[text_column+'_punctuation_count'] / data[text_column+'_raw_length'], decimals=3)

    #number of words in raw text data set
    data[text_column+'_raw_word_count']=data[text_column].apply(lambda x: len(str(x).split()))






