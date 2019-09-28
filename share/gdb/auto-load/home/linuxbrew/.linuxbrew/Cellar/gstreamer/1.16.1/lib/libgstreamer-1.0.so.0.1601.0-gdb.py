import sys
import gdb

# Update module path.
dir_ = '/home/linuxbrew/.linuxbrew/Cellar/gstreamer/1.16.1/share/gstreamer-1.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from gst_gdb import register
register (gdb.current_objfile ())
