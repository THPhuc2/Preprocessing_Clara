# import os
# import glob
# import pydicom
# import numpy as np
# import cv2

# def dicom_to_png(dicom_path, output_png_path):
#     """Chuyển một file DICOM sang PNG."""
#     dicom_data = pydicom.dcmread(dicom_path)
#     img = dicom_data.pixel_array.astype(np.float32)
#     img = (img - img.min()) / (img.max() - img.min()) * 255.0
#     img_8bit = img.astype(np.uint8)
#     cv2.imwrite(output_png_path, img_8bit)

# def convert_folder(dicom_folder, output_folder):
#     """Chuyển tất cả file .dicom trong thư mục sang ảnh PNG."""
#     os.makedirs(output_folder, exist_ok=True)
#     dicom_files = glob.glob(os.path.join(dicom_folder, "*.dicom"))

#     print(f"Found {len(dicom_files)} DICOM files in {dicom_folder}")
#     for i, dicom_file in enumerate(dicom_files):
#         png_filename = os.path.basename(dicom_file).replace(".dicom", ".png")
#         output_path = os.path.join(output_folder, png_filename)
#         dicom_to_png(dicom_file, output_path)

#     print("All DICOM files have been converted to PNG.")

# if __name__ == "__main__":
#     input_dicom_folder = "/kaggle/input/vinbigdata-chest-xray-abnormalities-detection/train"
#     output_png_folder = "/kaggle/working/png_output"

#     convert_folder(input_dicom_folder, output_png_folder)
import os
import pydicom
import numpy as np
import cv2

def dicom_to_png(dicom_path, output_png_path):
    dicom_data = pydicom.dcmread(dicom_path)
    img = dicom_data.pixel_array.astype(np.float32)
    img = (img - img.min()) / (img.max() - img.min()) * 255.0
    img_8bit = img.astype(np.uint8)
    cv2.imwrite(output_png_path, img_8bit)

def convert_all_dicoms_in_thang1(input_root, output_root):
    os.makedirs(output_root, exist_ok=True)

    for root, _, files in os.walk(input_root):
        for file in files:
            if file.endswith(".dcm"):
                dicom_path = os.path.join(root, file)

                # Lấy tên folder cha cách file .dcm 3 cấp
                parts = os.path.normpath(dicom_path).split(os.sep)
                try:
                    # Lấy tên folder thứ -3 (vd: "123.757...")
                    folder_name = parts[-3]
                    output_path = os.path.join(output_root, f"{folder_name}.png")

                    dicom_to_png(dicom_path, output_path)
                    print(f"✅ Converted: {dicom_path} -> {output_path}")
                except Exception as e:
                    print(f"❌ Error with file {dicom_path}: {e}")

if __name__ == "__main__":
    input_root = "/home/tiennv/phucth/medical/data_all/data_path_2_med/data_vin/data_image/thang1"
    output_root = "/home/tiennv/phucth/medical/data_all/data_path_2_med/done_path_2"

    convert_all_dicoms_in_thang1(input_root, output_root)
# import os
# import pydicom
# import numpy as np
# import cv2
# from collections import defaultdict

# def dicom_to_png(dicom_path, output_png_path):
#     dicom_data = pydicom.dcmread(dicom_path)

#     if 'PixelData' not in dicom_data:
#         raise ValueError("File has no Pixel Data")

#     img = dicom_data.pixel_array.astype(np.float32)
#     img = (img - img.min()) / (img.max() - img.min()) * 255.0
#     img_8bit = img.astype(np.uint8)
#     cv2.imwrite(output_png_path, img_8bit)

# def convert_all_dicoms(input_root, output_root):
#     os.makedirs(output_root, exist_ok=True)
#     morefile_folder = os.path.join(output_root, "morefile")
#     os.makedirs(morefile_folder, exist_ok=True)

#     # Đếm số file .dcm trong từng folder chứa .dcm
#     folder_file_map = defaultdict(list)

#     for root, _, files in os.walk(input_root):
#         for file in files:
#             if file.endswith(".dcm"):
#                 folder_file_map[root].append(os.path.join(root, file))

#     # Log folder có nhiều file
#     morefile_log_path = os.path.join(output_root, "morefile_folders.txt")
#     with open(morefile_log_path, "w") as log_file:
#         for folder, dicom_files in folder_file_map.items():
#             if len(dicom_files) > 1:
#                 log_file.write(folder + "\n")

#             for dicom_path in dicom_files:
#                 try:
#                     # Tên ảnh là tên folder chứa trực tiếp file .dcm
#                     folder_name = os.path.basename(os.path.dirname(dicom_path))
#                     png_name = f"{folder_name}.png"

#                     if len(dicom_files) > 1:
#                         # Nằm trong folder morefile
#                         output_path = os.path.join(morefile_folder, png_name)
#                     else:
#                         output_path = os.path.join(output_root, png_name)

#                     dicom_to_png(dicom_path, output_path)
#                     print(f"✅ Converted: {dicom_path} -> {output_path}")

#                 except Exception as e:
#                     print(f"❌ Error with file {dicom_path}: {e}")

# if __name__ == "__main__":
#     input_root = "/home/tiennv/phucth/medical/data_all/data_path_2_med/data_vin/data_image/thang1"
#     output_root = "/home/tiennv/phucth/medical/data_all/data_path_2_med/done_path_2"

#     convert_all_dicoms(input_root, output_root)
