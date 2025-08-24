from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pygame"],
    "include_files": [("asset", "asset")],  # garante que a pasta vá junto
    "include_msvcr": True
}

setup(
    name="Dash Submarine",
    version="1.0",
    description="Um exemplo de executável com cx_Freeze",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)
