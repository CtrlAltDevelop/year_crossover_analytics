import sys
from pathlib import Path
import PyInstaller.__main__

def build():
    # Define the project directory
    project_dir = Path.cwd()

    # Paths to necessary files and directories
    main_script = project_dir / 'run.py'
    version     = project_dir / 'VERSION'
    icon_path   = project_dir / 'icon.ico'
    venv_site   = project_dir / '.venv' / 'Lib' / 'site-packages'
    output_dir  = project_dir / '.dist'
    spec_dir    = project_dir / 'build'
    hooks_dir   = project_dir / '.hooks'

    # execute file name with the version
    exe_name = f"YearCrossoverAnalytics_v1.0.0"

    # Verify required files
    for path in (main_script, version, icon_path):
        if not path.exists():
            print(f"Missing: {path}")
            sys.exit(1)

    output_dir.mkdir(exist_ok=True)
    spec_dir.mkdir(exist_ok=True)

    opts = [
        str(main_script),
        '--onefile',
        '--noconsole',
        f'-n={exe_name}',
        f'-p={venv_site}',
        f'--distpath={output_dir}',
        f'--specpath={spec_dir}',
        f'--workpath={spec_dir}',
        f'--icon={icon_path}',
        f'--version-file={version}',
        f'--additional-hooks-dir={hooks_dir}',
        '--clean',
    ]

    # pyinstaller_options += [
    #     '--hidden-import=pandas',
    #     '--hidden-import=numpy'
    #     '--hidden-import=tkinter'
    # ]

    print("Running PyInstaller with options:")
    print(" ", " ".join(opts))
    try:
        PyInstaller.__main__.run(opts)
    except Exception as e:
        print("Build failed:", e)
        sys.exit(1)


if __name__ == '__main__':
    build()
