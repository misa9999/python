import subprocess

# windows - ping 127.0.0.1
# linux - ping 127.0.0.1 -c 4


process = subprocess.run(
    ["ping", "127.0.0.1", "-c", "4"], capture_output=True, text=True
)

# print(process.stderr)
print(process.stdout)
# print(process.returncode)
# print(process.args)
