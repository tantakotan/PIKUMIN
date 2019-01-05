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

try:
    path_of_csv = os.path.join(self.dict_of_ppini[S_GOD][I_GOD_FOLDER], self.dict_of_ppini[S_GOD][I_GOD_FILE])
    path_of_modulefile = os.path.join(self.dict_of_ppini[S_TPL][I_TPL_FOLDER], self.dict_of_ppini[S_TPL][I_TPL_FILE])
    index_of_module = self.dict_of_ppini[S_TPL][I_TPL_INDEX]

    index_of_nw = self.dict_of_ppini[S_NW][I_NW_INDEX]
    index_of_conf = self.dict_of_ppini[S_NW][I_NW_CONFIGINDEX]
    flag_of_nw = strtobool(self.dict_of_ppini[S_NW][I_NW_INDEX_ALL])

    path_of_ps = os.path.join(self.dict_of_ppini[S_PS][I_PS_FOLDER], self.dict_of_ppini[S_PS][I_PS_FILE])
    index_of_ps = self.dict_of_ppini[S_PS][I_PS_INDEX]
    index_of_sh = self.dict_of_ppini[S_PS][I_PS_SUBINDEX]
    flag_of_ps = strtobool(self.dict_of_ppini[S_PS][I_PS_INDEX_ALL])
except KeyError as er:
    print('KeyNotFound: ', er)
    pass
except ValueError as er:
    print('ValueError: ', 'check your .ini parameter: ', '"*_index_all" can be used "True,yes,y,1 or None,no,n,0"')
    exit()

if flag_of_nw:
    try:
        pppcsv = PppCsv()
        index_of_nw = pppcsv.get_index(path_of_csv)
    except FileNotFoundError as er:
        print('FileNotFoundError: ', er)
        exit()

    try:
        index_of_nw.remove(index_of_conf)
    except ValueError as er:
        print('ValueError: ', 'check your ini parameter: "config_index"=', index_of_conf)
        exit()

return
