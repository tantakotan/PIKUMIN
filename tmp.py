def get_dictionary(path_of_csv, index_of_conf, index_of_pa):
    dev_dict = dict()
    with open(path_of_csv, 'r', encoding='utf-8_sig') as f:
        for i2 in csv.DictReader(f):
            print(i2)
            for i in range(len(index_of_pa)):
                tmp_dict = dict()
                tmp2_dict = dict()
                tmp_dict[i2[index_of_conf]] = i2[index_of_pa[i]]
                print(tmp_dict)
                tmp2_dict[index_of_pa[i]] = tmp_dict
                dev_dict.update(tmp2_dict)
                print(dev_dict)

