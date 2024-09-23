import os
import shutil
import glob

def pascal_xml_setup_directory_structure(project_path, source_filename):
    target_delete_folder_1 = 'Annotations'
    target_delete_folder_2 = 'ImageSets'

    # Membuat folder 'train' di dalam folder baru 'traffic-pascalVOC'
    train_dir = os.path.join(project_path, 'train')
    
    if os.path.exists(train_dir):
        print(f"Folder {train_dir} sudah dibuat.")
        return
    
    os.makedirs(train_dir, exist_ok=True)

    # Pindahkan file .xml dari 'annotations/' ke 'train/'
    xml_files = glob.glob(os.path.join(project_path, "**", '*.xml'), recursive=True)
    for xml_file in xml_files:
        shutil.move(xml_file, train_dir)

    # Pindahkan 'default.txt' dari 'ImageSets/Main/' ke direktori utama 'traffic-pascalVOC'
    file_names_path = glob.glob(os.path.join(project_path, "**", source_filename), recursive=True)[0]
    if os.path.exists(file_names_path):
        shutil.move(file_names_path, project_path)

    # Hapus folder lama jika sudah tidak diperlukan
    shutil.rmtree(os.path.join(project_path, target_delete_folder_1))
    shutil.rmtree(os.path.join(project_path, target_delete_folder_2))

    print("Folder berhasil diubah.")