aviso_info = "Software"
aviso_erro = "ERROR"

# FUNÇÃO DE TRANSFORMAR LISTA EM STRING
def list_to_str(cid_list):
    cid_list = list(set(cid_list))  # cid_list is the list of ids from the csv file.
    the_cid_list = [int(value) for value in cid_list]
    cid_list_str = str(the_cid_list)[1:-1]  # This eliminates the [brackets around the list
    cid_list_str = cid_list_str.replace(', ', ',').replace(' ,', ',')
    # This eliminates the spaces before or after each comma.
    return cid_list_str

