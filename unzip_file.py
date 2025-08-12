# import os
# import zipfile
# import re
# import sys

# def unzip_files(input_folder, output_folder):
#     os.makedirs(output_folder, exist_ok=True)

#     for file_name in os.listdir(input_folder):
#         file_path = os.path.join(input_folder, file_name)

#         if file_name.endswith(".zip") and os.path.isfile(file_path):
    
#             match = re.match(r"^(mask_)?(\d+)\.zip$", file_name)
#             if match:
#                 folder_name = match.group(0).replace(".zip", "")  # Tạo tên thư mục giống tên file
#                 dest_folder = os.path.join(output_folder, folder_name)
#                 os.makedirs(dest_folder, exist_ok=True)

#                 try:
#                     with zipfile.ZipFile(file_path, 'r') as zip_ref:
#                         zip_ref.extractall(dest_folder)
#                         print(f"Đã giải nén: {file_name} → {dest_folder}")
#                 except zipfile.BadZipFile:
#                     print(f"Lỗi: {file_name}")

#     print("done")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Sai cú pháp! Cách dùng:")
#         print("python unzip_all.py <input_folder> <output_folder>")
#         sys.exit(1)

#     input_dir = sys.argv[1]
#     output_dir = sys.argv[2]

#     unzip_files(input_dir, output_dir)

# import os
# import zipfile
# import sys

# def unzip_all_files(input_folder, output_folder):
#     """ Giải nén tất cả file ZIP trong thư mục đầu vào vào thư mục đầu ra """
#     if not os.path.isdir(input_folder):
#         print(f"❌ Lỗi: {input_folder} không phải là thư mục hợp lệ!")
#         return

#     os.makedirs(output_folder, exist_ok=True)

#     # Duyệt qua tất cả các file trong thư mục đầu vào
#     for file_name in os.listdir(input_folder):
#         file_path = os.path.join(input_folder, file_name)

#         if file_name.endswith(".zip") and os.path.isfile(file_path):
#             dest_folder = os.path.join(output_folder, file_name.replace(".zip", ""))
#             os.makedirs(dest_folder, exist_ok=True)

#             try:
#                 with zipfile.ZipFile(file_path, 'r') as zip_ref:
#                     zip_ref.extractall(dest_folder)
#                     print(f"✅ Đã giải nén: {file_name} → {dest_folder}")
#             except zipfile.BadZipFile:
#                 print(f"❌ Lỗi: {file_name} không phải file ZIP hợp lệ!")

#     print("🎉 Hoàn thành giải nén tất cả file ZIP!")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("❌ Sai cú pháp! Cách dùng:")
#         print("👉 python unzip_all.py <input_folder> <output_folder>")
#         sys.exit(1)

#     input_dir = sys.argv[1]
#     output_dir = sys.argv[2]

#     unzip_all_files(input_dir, output_dir)

import os
import zipfile
import sys

def unzip_all_files_recursive(input_folder, output_folder):
    """ Giải nén tất cả file ZIP trong mọi thư mục con của input_folder vào output_folder """
    if not os.path.isdir(input_folder):
        print(f"❌ Lỗi: {input_folder} không phải là thư mục hợp lệ!")
        return

    os.makedirs(output_folder, exist_ok=True)

    for root, _, files in os.walk(input_folder):
        for file_name in files:
            if file_name.endswith(".zip"):
                zip_path = os.path.join(root, file_name)

                # Tạo đường dẫn đích (giữ cấu trúc folder gốc tương đối từ input_folder)
                rel_path = os.path.relpath(root, input_folder)
                dest_folder = os.path.join(output_folder, rel_path, file_name.replace(".zip", ""))
                os.makedirs(dest_folder, exist_ok=True)

                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(dest_folder)
                        print(f"✅ Đã giải nén: {zip_path} → {dest_folder}")
                except zipfile.BadZipFile:
                    print(f"❌ Lỗi: {zip_path} không phải file ZIP hợp lệ!")

    print("🎉 Hoàn thành giải nén tất cả file ZIP!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Sai cú pháp! Cách dùng:")
        print("👉 python unzip_all.py <input_folder> <output_folder>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    unzip_all_files_recursive(input_dir, output_dir)



# import os
# import shutil
# import sys

# def merge_images(source_dir, target_dir):
#     os.makedirs(target_dir, exist_ok=True)

#     count = 0
#     for root, dirs, files in os.walk(source_dir):
#         for file in files:
#             if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
#                 src_path = os.path.join(root, file)
#                 dst_path = os.path.join(target_dir, file)

#                 # Đổi tên nếu trùng
#                 if os.path.exists(dst_path):
#                     base, ext = os.path.splitext(file)
#                     dst_path = os.path.join(target_dir, f"{base}_{count}{ext}")

#                 shutil.copy2(src_path, dst_path)
#                 count += 1

#     print(f"✅ Đã gộp {count} ảnh vào {target_dir}")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Cách dùng: python merge_images.py <thư_mục_nguồn> <thư_mục_đích>")
#     else:
#         source_dir = sys.argv[1]
#         target_dir = sys.argv[2]
#         merge_images(source_dir, target_dir)


# import os
# import sys
# import pandas as pd

# def merge_csv_files(source_dir, output_file):
#     all_dfs = []
#     csv_files = [f for f in os.listdir(source_dir) if f.endswith(".csv")]

#     if not csv_files:
#         print("⚠️ Không tìm thấy file CSV nào trong thư mục.")
#         return

#     for csv_file in sorted(csv_files):
#         csv_path = os.path.join(source_dir, csv_file)
#         print(f"🔄 Đang xử lý: {csv_file}")
#         try:
#             df = pd.read_csv(csv_path)
#             all_dfs.append(df)
#         except Exception as e:
#             print(f"❌ Lỗi khi đọc {csv_file}: {e}")

#     if all_dfs:
#         merged_df = pd.concat(all_dfs, ignore_index=True)
#         merged_df.to_csv(output_file, index=False)
#         print(f"✅ Đã gộp xong {len(csv_files)} file → {output_file}")
#     else:
#         print("❌ Không có dữ liệu để gộp.")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Cách dùng: python merge_csv.py <thư_mục_chứa_csv> <file_csv_đầu_ra>")
#     else:
#         source_dir = sys.argv[1]
#         output_file = sys.argv[2]
#         merge_csv_files(source_dir, output_file)
