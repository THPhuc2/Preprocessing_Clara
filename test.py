# import os
# import shutil
# import pydicom
# import numpy as np
# import cv2

# def dicom_to_png(dicom_path, output_png_path):
#     dicom_data = pydicom.dcmread(dicom_path)
#     if 'PixelData' not in dicom_data:
#         raise ValueError("No Pixel Data")
#     img = dicom_data.pixel_array.astype(np.float32)
#     img = (img - img.min()) / (img.max() - img.min()) * 255.0
#     img_8bit = img.astype(np.uint8)
#     cv2.imwrite(output_png_path, img_8bit)

# # def process_dicom_folders(thang1_root, done_folder, morefile_folder):
# #     os.makedirs(done_folder, exist_ok=True)
# #     os.makedirs(morefile_folder, exist_ok=True)

# #     # Duyệt qua từng ngày
# #     for date_folder in os.listdir(thang1_root):
# #         date_path = os.path.join(thang1_root, date_folder)
# #         if not os.path.isdir(date_path):
# #             continue

# #         # Duyệt qua từng folder bệnh nhân
# #         for patient_folder in os.listdir(date_path):
# #             patient_path = os.path.join(date_path, patient_folder)
# #             if not os.path.isdir(patient_path):
# #                 continue

# #             subfolders = [
# #                 f for f in os.listdir(patient_path)
# #                 if os.path.isdir(os.path.join(patient_path, f))
# #             ]

# #             if len(subfolders) >= 2:
# #                 # ➕ Có nhiều hơn 1 folder con
# #                 dst = os.path.join(morefile_folder, patient_folder)
# #                 print(f"📁 Copying to morefile/: {patient_path} → {dst}")
# #                 shutil.copytree(patient_path, dst, dirs_exist_ok=True)

# #             elif len(subfolders) == 1:
# #                 # ✅ Chỉ có 1 folder con
# #                 subfolder_path = os.path.join(patient_path, subfolders[0])
# #                 for root, _, files in os.walk(subfolder_path):
# #                     for file in files:
# #                         if file.endswith(".dcm"):
# #                             dcm_path = os.path.join(root, file)
# #                             try:
# #                                 # Tên file = tên folder con duy nhất
# #                                 name = subfolders[0]
# #                                 output_png = os.path.join(done_folder, f"{name}.png")
# #                                 dicom_to_png(dcm_path, output_png)
# #                                 print(f"✅ Converted: {dcm_path} → {output_png}")
# #                             except Exception as e:
# #                                 print(f"❌ Error with {dcm_path}: {e}")
# #             else:
# #                 print(f"⚠️ Không có folder con trong: {patient_path}")
# def process_dicom_folders(thang1_root, done_folder, morefile_folder, error_folder):
#     os.makedirs(done_folder, exist_ok=True)
#     os.makedirs(morefile_folder, exist_ok=True)
#     os.makedirs(error_folder, exist_ok=True)

#     for date_folder in os.listdir(thang1_root):
#         date_path = os.path.join(thang1_root, date_folder)
#         if not os.path.isdir(date_path):
#             continue

#         for patient_folder in os.listdir(date_path):
#             patient_path = os.path.join(date_path, patient_folder)
#             if not os.path.isdir(patient_path):
#                 continue

#             subfolders = [
#                 f for f in os.listdir(patient_path)
#                 if os.path.isdir(os.path.join(patient_path, f))
#             ]

#             if len(subfolders) >= 2:
#                 dst = os.path.join(morefile_folder, patient_folder)
#                 print(f"📁 Copying to morefile/: {patient_path} → {dst}")
#                 shutil.copytree(patient_path, dst, dirs_exist_ok=True)

#             elif len(subfolders) == 1:
#                 subfolder_path = os.path.join(patient_path, subfolders[0])
#                 error_occurred = False

#                 for root, _, files in os.walk(subfolder_path):
#                     for file in files:
#                         if file.endswith(".dcm"):
#                             dcm_path = os.path.join(root, file)
#                             try:
#                                 name = os.path.basename(os.path.dirname(patient_path))
#                                 output_png = os.path.join(done_folder, f"{name}.png")
#                                 dicom_to_png(dcm_path, output_png)
#                                 print(f"✅ Converted: {dcm_path} → {output_png}")
#                             except Exception as e:
#                                 print(f"❌ Error with {dcm_path}: {e}")
#                                 error_occurred = True
#                                 break  # Dừng xử lý file khác trong folder này
#                     if error_occurred:
#                         break

#                 if error_occurred:
#                     dst_error = os.path.join(error_folder, patient_folder)
#                     print(f"➡️ Moving entire folder to error/: {patient_path} → {dst_error}")
#                     shutil.copytree(patient_path, dst_error, dirs_exist_ok=True)

#             else:
#                 print(f"⚠️ Không có folder con trong: {patient_path}")

# if __name__ == "__main__":
#     input_root = "/home/tiennv/phucth/medical/data_all/data_path_2_med/data_vin/data_image/thang1"
#     output_png_folder = "/home/tiennv/phucth/medical/data_all/data_path_2_med/done_path_2_1"
#     output_morefile_folder = "/home/tiennv/phucth/medical/data_all/data_path_2_med/morefile"
#     output_error_folder = "/home/tiennv/phucth/medical/data_all/data_path_2_med/error"

#     process_dicom_folders(input_root, output_png_folder, output_morefile_folder, output_error_folder)



# import os
# import pydicom
# import numpy as np
# import cv2
# from pydicom.pixel_data_handlers.util import apply_voi_lut

# # --- cấu hình ---
# ROOT_DIR = "/home/tiennv/phucth/medical/data_all/data_path_2_med/error"
# OUTPUT_DIR = "/home/tiennv/phucth/medical/data_all/data_path_2_med/converted_2"
# os.makedirs(OUTPUT_DIR, exist_ok=True)
# # -----------------

# counters = {}  # dict: group_name -> next index

# def dicom_to_uint8(ds):
#     """Chuyển pydicom Dataset thành ảnh uint8 2D (áp dụng VOI LUT, rescale, normalize)."""
#     # đọc pixel array
#     arr = ds.pixel_array  # có thể ném exception nếu không có PixelData

#     # windowing (VOI LUT) nếu có
#     try:
#         arr = apply_voi_lut(arr, ds)
#     except Exception:
#         pass

#     # xử lý MONOCHROME1 (đảo màu)
#     photometric = getattr(ds, "PhotometricInterpretation", "").upper()
#     if photometric == "MONOCHROME1":
#         arr = np.max(arr) - arr

#     # áp scale intercept/slope nếu có
#     intercept = float(getattr(ds, "RescaleIntercept", 0.0))
#     slope = float(getattr(ds, "RescaleSlope", 1.0))
#     arr = arr.astype(float) * slope + intercept

#     # nếu multi-frame lấy frame đầu (nếu cần bạn báo mình thay đổi)
#     if arr.ndim == 3:
#         # nếu shape = (frames, h, w) hoặc (h, w, channels)
#         if arr.shape[0] > 1 and (arr.shape[1] == arr.shape[1] or arr.shape[2] == arr.shape[2]):
#             arr = arr[0]
#         else:
#             arr = np.squeeze(arr)

#     # chuẩn hóa về 0-255
#     amin, amax = float(arr.min()), float(arr.max())
#     if amax - amin > 0:
#         arr = (arr - amin) / (amax - amin) * 255.0
#     else:
#         arr = np.zeros_like(arr)

#     return np.uint8(arr)

# def process_all(root_dir, output_dir):
#     for dirpath, dirnames, filenames in os.walk(root_dir):
#         for fname in filenames:
#             if not fname.lower().endswith((".dcm", ".dicom")):
#                 continue

#             dcm_path = os.path.join(dirpath, fname)

#             # group_name là **tên folder cha của folder chứa file .dcm**
#             # ví dụ: .../<group>/<deep_folder>/file.dcm  => group = <group>
#             parent_of_dir = os.path.dirname(dirpath)
#             group_name = os.path.basename(parent_of_dir) or os.path.basename(dirpath)

#             # lấy index tiếp theo cho group này
#             idx = counters.get(group_name, 0) + 1
#             counters[group_name] = idx

#             # tạo output/<group_name>/<idx>/
#             out_parent = os.path.join(output_dir, group_name)
#             out_sub = os.path.join(out_parent, str(idx))
#             os.makedirs(out_sub, exist_ok=True)

#             out_fname = f"{group_name}.png"   # **tên file = tên folder cha**
#             out_path = os.path.join(out_sub, out_fname)

#             try:
#                 ds = pydicom.dcmread(dcm_path, force=True)
#                 if not hasattr(ds, "pixel_array"):
#                     print(f"[SKIP] No pixel data: {dcm_path}")
#                     continue

#                 img = dicom_to_uint8(ds)
#                 # lưu (OpenCV expects HxW or HxWxC uint8)
#                 cv2.imwrite(out_path, img)
#                 print(f"[OK] {dcm_path} -> {out_path}")
#             except Exception as e:
#                 print(f"[ERR] Failed to convert {dcm_path}: {e}")

# if __name__ == "__main__":
#     process_all(ROOT_DIR, OUTPUT_DIR)
#     print("Done.")


import os
import pydicom
import numpy as np
import cv2
from pydicom.pixel_data_handlers.util import apply_voi_lut

# --- Cấu hình ---
ROOT_DIR = "/home/tiennv/phucth/medical/data_all/data_path_2_med/error"
OUTPUT_DIR = "/home/tiennv/phucth/medical/data_all/converted_png"
DONE_DIR = "/home/tiennv/phucth/medical/data_all/data_path_2_med/done_thang_1"  # thư mục check
os.makedirs(OUTPUT_DIR, exist_ok=True)
# -----------------

counters = {}  # dict: group_name -> next index

def dicom_to_uint8(ds):
    """Chuyển pydicom Dataset thành ảnh uint8 2D (áp dụng VOI LUT, rescale, normalize)."""
    arr = ds.pixel_array

    try:
        arr = apply_voi_lut(arr, ds)
    except Exception:
        pass

    photometric = getattr(ds, "PhotometricInterpretation", "").upper()
    if photometric == "MONOCHROME1":
        arr = np.max(arr) - arr

    intercept = float(getattr(ds, "RescaleIntercept", 0.0))
    slope = float(getattr(ds, "RescaleSlope", 1.0))
    arr = arr.astype(float) * slope + intercept

    if arr.ndim == 3:
        arr = np.squeeze(arr)

    amin, amax = float(arr.min()), float(arr.max())
    if amax - amin > 0:
        arr = (arr - amin) / (amax - amin) * 255.0
    else:
        arr = np.zeros_like(arr)

    return np.uint8(arr)

def process_all(root_dir, output_dir, done_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for fname in filenames:
            if not fname.lower().endswith((".dcm", ".dicom")):
                continue

            dcm_path = os.path.join(dirpath, fname)

            # Lấy tên folder cha
            parent_of_dir = os.path.dirname(dirpath)
            group_name = os.path.basename(parent_of_dir) or os.path.basename(dirpath)

            # Check nếu ảnh đã tồn tại trong DONE_DIR thì bỏ qua
            done_path = os.path.join(done_dir, f"{group_name}.png")
            if os.path.exists(done_path):
                print(f"[SKIP] Đã có trong done_thang_1: {group_name}.png")
                continue

            # Lấy index cho group này
            idx = counters.get(group_name, 0) + 1
            counters[group_name] = idx

            out_parent = os.path.join(output_dir, group_name)
            out_sub = os.path.join(out_parent, str(idx))
            os.makedirs(out_sub, exist_ok=True)

            out_fname = f"{group_name}.png"
            out_path = os.path.join(out_sub, out_fname)

            try:
                ds = pydicom.dcmread(dcm_path, force=True)
                if not hasattr(ds, "pixel_array"):
                    print(f"[SKIP] No pixel data: {dcm_path}")
                    continue

                img = dicom_to_uint8(ds)
                cv2.imwrite(out_path, img)
                print(f"[OK] {dcm_path} -> {out_path}")
            except Exception as e:
                print(f"[ERR] Failed to convert {dcm_path}: {e}")

if __name__ == "__main__":
    process_all(ROOT_DIR, OUTPUT_DIR, DONE_DIR)
    print("Done.")
