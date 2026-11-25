import os

print(f"Parent process: PID = {os.getpid()}", flush=True)
pid = os.fork()

if pid == 0:
    print(f"Child process: PID = {os.getpid()}, "
          f"Parent PID = {os.getppid()}", flush=True)
    print("Child is about to exec 'ls -l'", flush=True)
    try:
        os.execlp("ls", "ls", "-l")
    except OSError:
        os._exit(1)
else:
    print(f"Parent waiting for child (PID = {pid})", flush=True)
    _, status = os.waitpid(pid, 0)
    if os.WIFEXITED(status):
        print("Child exited with status", os.WEXITSTATUS(status))
    print("Parent process resumes and exits.")