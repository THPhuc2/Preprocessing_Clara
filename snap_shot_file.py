from huggingface_hub import snapshot_download

folders = ["thang2"]   # Thay đổi tên folder theo nhu cầu của bạn

for folder in folders:
    print(f"Đang tải {folder}...")
    snapshot_download(
        repo_id="hieupth/vixr140k",
        repo_type="dataset",
        local_dir=f"/home/tiennv/phucth/medical/data_all/data_path_2_med/data_vin/{folder}",
        allow_patterns=f"{folder}/**"
    )
    print(f"Tải xong {folder}!\n")
