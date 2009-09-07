# A very simple setup script to create an executable for the Scrubba'
#
# If everything works well, you should find a subdirectory named 'dist'
# containing some files, among them scrubba.exe


from distutils.core import setup
import py2exe

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.1.0",
    description = "scrubba, the Microsoft publisher HTML scrubber",
    name = "scrubba",

    # targets to build
    console = [{
        "script": "scrubba.py",
        "icon_resources": [(1, "icons/Towel.ico")]
        }],

    options = { "py2exe": {
	"compressed": 1,
	"optimize": 2,
	"bundle_files": 2,
	"dll_excludes": [ "MSVCP90.dll" ]}
	}
)
