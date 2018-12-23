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

    var = {index_of_pa[0]:{1:1}}
    var = {index_of_pa[0]:{k:v for k,v in tmp_dict.items() if index_of_pa[0] in k}}
    print(var)


    with open(path_of_csv, 'r', encoding='utf-8_sig') as f:
        for d1 in csv.DictReader(f):
            num += 1
            for i2 in range(len(index_of_val)):
                tmp_dict[index_of_val[i2] + '__' + str(num)] = {d1[index_of_conf]: d1[index_of_val[i2]]}


exec('d1[index_of_val[i2]] = {d1[index_of_conf]: d1[index_of_val[i2]]}')

for i in range(len(index_of_val)):
    list_of_v = []

    for k, v in tmp_dict.items():
        if index_of_val[i] in k:
            list_of_v.append(v)

    print(list_of_v)
    dev_dict[index_of_val[i]] = list_of_v
    print(dev_dict)
    print(dev_dict[index_of_val[i]])

    print(tmp_list2[0][3])
    dev_dict['aaa'] = dict((tmp_list2[0][3], tmp_list2[0][4]))
    print(dev_dict)

