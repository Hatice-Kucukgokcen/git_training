def text_feature_generator(data, text_column):
    #turn existing text column into string.
    #for dealing with non-str values in the text.
    #For example: If there is comment like only 3, we cannot use this comment in the any preprocessing of text. So we need to change type

    data[text_column]=data[text_column].astype(str)




