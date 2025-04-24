import os

def get_data_if_needed():
    # ✅ Local path to pre-downloaded PLATON data
    local_data_path = "/Users/Lenovo/projects/isro/data"

    if os.path.exists(local_data_path):
        print("✅ Using pre-downloaded PLATON data at:", local_data_path)
        os.environ["PLATON_DATA_PATH"] = local_data_path
        return
    else:
        raise RuntimeError(f"❌ Local PLATON data not found at {local_data_path}")

def get_data(target_dir):
    raise RuntimeError("🚫 Download blocked: using local PLATON data only.")
