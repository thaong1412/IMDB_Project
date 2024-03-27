def col_info(data, col_ids=None):
    """
    The function takes a dataset and a list of columns supplied by the user. If only a dataset is passed,
    the function will default to providing info on all the columns. The columns are specified as either all "labels"
    or all indices and can be in any desired order. Column indices can be passed using either a range function (for a
    contiguous list of columns) or a simple list (for non-contiguous columns). If "labels" are specified,
    these are converted into indices by the function before use. \n\nEXAMPLES: Suppose the dataset has 10 columns
    labeled "A" to "J". \n\nSo for all columns use: col_info(range(0, df.shape[1]))\n\nFor the first 6 columns use:
    col_info(range(0, 5))\n\nFor columns 1, 3, 7, and 8 use: col_info([1, 3, 7, 8])\n\nFor columns "A", "D" and "F"
    use: col_info(["A", "D", "F"])
    """

    if col_ids is None:
        col_ids = range(0, data.shape[1])

    # if the list contains column names (strings) instead of indices:
    # check the 1st element only as all elements have the same type
    if type(col_ids[0]) == str:
        col_indices = []  # col_indices is the new list
        for col in col_ids:  # for each column in the passed list
            index = data.columns.get_loc(col)  # get column index
            col_indices.append(index)  # append column index to list
    else:  # if the list contains column indices
        col_indices = col_ids

    print("The full dataset contains:", data.shape[0], "rows and", data.shape[1],
          "columns. Details for the requested column(s)", "are as follows:\n")

    col_indices_to_use = col_indices  # col_indices_to_use will use all indices

    for col in col_indices_to_use:  # for each index in the col_indices_to_use list
        uniques_arr = data.iloc[:, col].unique()
        nb_uniques = len(data.iloc[:, col].unique())

        if nb_uniques < 2:
            print("\033[1m", data.columns[col], "\033[0m:", data.iloc[:, col].dtype, ":", nb_uniques, "level")
        else:
            print("\033[1m", data.columns[col], "\033[0m:", data.iloc[:, col].dtype, ":", nb_uniques, "levels")

        values_list = []
        total_length = len(str(uniques_arr[0]))
        total_values = 0

        for value in range(0, nb_uniques):
            if (total_length < 50) & (total_values < 12):
                values_list.append(uniques_arr[value])
                total_length += len(str(uniques_arr[value]))
                total_values += 1
            else:
                print(values_list, "...\n")
                break

        if (total_length < 50) & (total_values < 12):
            print(values_list, "\n")
