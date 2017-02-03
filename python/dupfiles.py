#!/usr/local/bin/python3.4

""

import os , sys

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_dict = {}

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for dir in directories:
            dir_path = os.path.join(root,dir)
            #file_dict[os.path.join(root,dir)] = os.stat(os.path.join(root,dir)).st_size
        for filename in files:
            # Join the two strings in order to form the full filepath.
            #print(os.path.join(root,filename))
            #file_dict[os.path.join(root,filename)] = os.stat(os.path.join(root,filename)).st_size
            #print('filename is ' + filename)
            if filename in file_dict:
              #print('exists')
              inner_dict = file_dict[filename]
              inner_dict[root] =  os.stat(os.path.join(root,filename)).st_size
              file_dict[filename] = inner_dict
            else:
              #print('not exists')
              inner_dict = {}
              inner_dict[root] =  os.stat(os.path.join(root,filename)).st_size
              file_dict[filename] = inner_dict

    return file_dict  # Self-explanatory.

def print_dictofdict(dictt):
    """
    This function will print dict of dict
    """

    for key in dictt:
       for eachkey in dictt[key]:
          print(key , ':' , eachkey , '-->', dictt[key][eachkey])
       print('------------------------------------------------------')
    return   


if __name__ == '__main__':
    full_file_paths = get_filepaths(sys.argv[1])
    mismatch_dict = {}
    match_dict = {}
    nested_dict = {}

    for key in full_file_paths:
       if len(full_file_paths[key]) > 1:
         prev_size = -1
         mismatch_flag = 0
         for eachkey in full_file_paths[key]:
            if prev_size < 1:
               prev_size = full_file_paths[key][eachkey]
            if full_file_paths[key][eachkey] != prev_size:
               prev_size = full_file_paths[key][eachkey]
               mismatch_flag = 1
            else:
               prev_size = full_file_paths[key][eachkey]
            nested_dict = full_file_paths[key]
         if mismatch_flag == 0:
            match_dict[key] = nested_dict
         else:
            mismatch_dict[key] = nested_dict



    print('Matching files')
    print_dictofdict(match_dict)
    print('\n\n\n\n\n')
    print('File Size different')
    print_dictofdict(mismatch_dict)
