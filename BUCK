load('//:buckaroo_macros.bzl','buckaroo_deps')

prebuilt_cxx_library(
  name = 'gstreamer',
  soname = 'libgstreamer.so',
  shared_lib = 'lib/libgstreamer-1.0.so',
  header_namespace = 'gst',
  exported_headers = subdir_glob([
    ('include/gstreamer-1.0/gst','**/*.h'),
  ]),
  exported_linker_flags = [
    '-lgobject-2.0'
  ],
  visibility = ['PUBLIC'],
  deps = buckaroo_deps()
)

