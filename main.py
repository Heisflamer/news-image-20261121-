import shutil, os
src = os.path.join(os.path.dirname(__file__), "entry.png")
dst_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(dst_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(dst_dir, "entry.png"))
print("done")
