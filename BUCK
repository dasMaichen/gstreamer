load('//:buckaroo_macros.bzl','buckaroo_deps')

cxx_library(
  name = 'gstreamer',
  header_namespace = 'gst',
  exported_headers = subdir_glob([
    ('gst','**/*.h'),
  ]),
  visibility = ['PUBLIC'],
  deps = buckaroo_deps()
)

