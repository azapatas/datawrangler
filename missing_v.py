import pandas

def missing_v(dataset, variable, factor):

    '''Esta función elimina los casos outliers de la variable del dataset, definidos como aquellos que están
    + - factor veces la desviaciones estándar respecto a la media'''
    
    cases = dataset.shape[0]
    if is_numeric_dtype(dataset[variable]) and factor.isnumeric():

        lower_lim_desv = dataset[variable].mean() - dataset[variable].std() * factor
        upper_lim_desv = dataset[variable].mean() + dataset[variable].std() * factor
        print(f'Lower Limit: {lower_lim_desv}\nUpper Limit: {upper_lim_desv}')
        dataset_desv = dataset.loc[(dataset[variable] <= upper_lim_desv) & (dataset[variable] >= lower_lim_desv)]
        print(cases - dataset_desv.shape[0], "casos eliminados.")
        return(dataset_desv)

    print(f"La variable", variable, "debe ser numérica")

