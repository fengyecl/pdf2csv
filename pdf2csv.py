import os
import sys
import tabula

def get_file(root_path,all_files=[]):
    files = os.listdir(root_path)
    for file in files:
        if not os.path.isdir(root_path + '/' + file):   # not a dir
            all_files.append(root_path + '/' + file)
        else:  # is a dir
            get_file((root_path+'/'+file),all_files)
    return all_files


if __name__ == '__main__':

    path = sys.path[0]
    print('current path:', path)

    for src_file in get_file(path):
        if src_file.find('.pdf') != -1:
            index = src_file.rfind('.pdf')
            dst_file = src_file[0 : index] + '.csv'
            if os.path.isfile(dst_file):
                print(dst_file, 'is alreay exist, skip it!')
            else:
                # dfs = tabula.read_pdf(src_file, stream=True, pages='all')
                # print(len(dfs))
                # print(dfs[1])
                tabula.convert_into(src_file, dst_file, stream=True, output_format="csv", pages='all')
                print(dst_file, 'is converted!')