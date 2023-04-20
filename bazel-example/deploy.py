from subprocess import run, check_output
from pathlib import Path
from shutil import copy

build_cmd = {"bazel-6.1.1-windows-x86_64.exe", "build","mytool"}
query_cmd = {"bazel-6.1.1-windows-x86_64.exe","cquery", "PackageMyTool","--output", "files"}

run(build_cmd)
res = check_output(query_cmd).decode('utf-8').strip()
artifact_path = Path(res).absolute()
target_path = Path(".").joinpath(artifact_path)

copy(str(artifact_path),str(target_path))