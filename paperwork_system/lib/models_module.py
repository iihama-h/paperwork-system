def make_composite_key(main_table_key, sub_model):
    sub_model_query_set = sub_model.objects.all().filter(
        pk__startswith=str(main_table_key) + '_')

    if sub_model_query_set:
        key = []
        for recode in sub_model_query_set:
            value = recode.pk.split('_')
            key.append(value[-1])
        return str(main_table_key) + '_' + (str(int(max(key)) + 1))
    else:
        return str(main_table_key) + '_0'