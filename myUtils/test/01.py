import tempfile
import shutil

dirpath = tempfile.mkdtemp()
# ... do stuff with dirpath
shutil.rmtree(dirpath)
print(dirpath)