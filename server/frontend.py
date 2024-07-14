from ret import *
import sys
import json

def frontendfunction(description, color):
    data=[]
    data,label_to_folder =collect_all_data()
    arr_descs=[]
    arr_descs.append(description)
    folders=classify(data,arr_descs,label_to_folder)
    top_folder = top(folders,description)
    trans(top_folder)
    extracted_details = extract_details_advanced(description)
    user_feedback = None  # Placeholder for actual feedback mechanism
    updated_details = collect_feedback(description, extracted_details, user_feedback)
    html_file_path=paths("D:\GP\Website\Graduation_project\9")
    readandwrite(html_file_path,updated_details)
    css_files = get_linked_css_files(html_file_path)
    modifyallcss("D:\GP\Website\Graduation_project\9",css_files,color)

    source_dir = 'D:\GP\Website\Graduation_project\9'
    templates_dir = 'D:/GP/Website/Graduation_project/myproject/myapp/templates'
    static_dir = 'D:/GP/Website/Graduation_project/myproject/myapp/static'


    file_ext = '.html'  # Change this to '.css' or any other file extension as needed
    if os.path.exists(templates_dir):
            shutil.rmtree(templates_dir)
            print(f"Deleted the existing templates directory: {templates_dir}")
        
    if os.path.exists(static_dir):
        shutil.rmtree(static_dir)
        print(f"Deleted the existing static directory: {static_dir}")
    move_files_and_folders(source_dir, templates_dir, static_dir, file_ext)
    file_ext = '.css'  # Change this to '.css' or any other file extension as needed
    source_dir = 'D:\\GP\\Website\\Graduation_project\\admin'
    templates_dir = 'D:/GP/Website/Graduation_project/myproject/myapp/templates'
    static_dir = 'D:/GP/Website/Graduation_project/myproject/myapp/static'

    move_files_and_folders(source_dir, static_dir, templates_dir, file_ext)

    old_file = 'D:\\GP\\Website\\Graduation_project\\myproject\\myproject\\urls.py'
    new_file = 'D:\\GP\\Website\\Graduation_project\\urls.py'
    replace_file(old_file, new_file)
    views_file = 'D:\\GP\\Website\\Graduation_project\\myproject\\myapp\\views.py'
    

    add_home_view(views_file)


if __name__ == "__main__":
    input_data = json.loads(sys.argv[1])
    description = input_data.get("description")
    color = input_data.get("color")
    print(description)
    print(color)

    frontendfunction(description, color)

    print("template saved successfully.")
    