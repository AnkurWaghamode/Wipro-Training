import subprocess

result = subprocess.run(
    "echo hello world",
    shell=True,
    capture_output=True,
    text=True
)
print (result.stdout)

subprocess.run("python","TC_Multiple Abstract.py")
