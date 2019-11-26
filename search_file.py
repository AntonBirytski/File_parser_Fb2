import glob, os

def search_move_files(input_path, output_path):
    file_name = ''
    os.chdir(input_path)
    file_name = []
    for file in glob.glob('*.*'):
        os.chdir(input_path)
        if file.endswith('.fb2'):
            file_name.append(os.path.abspath(file))
        else:
            oldPath = os.path.abspath(file)
            os.chdir(output_path)
            newPath = os.path.abspath(file)
            os.replace(oldPath,newPath)

    return  file_name
