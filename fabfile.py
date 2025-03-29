from fabric import Connection, task

HOST = "myvmlab.senecapolytechnic.ca"
PORT = 7359
USER = "student"
PASSWORD = "9Un~Lqi+u6"
NEW_USER = "pshrestha24"
FOLDERS = [f"lab{i}" for i in range(1, 9)]

@task
def deploy(c):
    conn = Connection(host=HOST, user=USER, port=PORT)

    conn.sudo("yum install -y httpd", password=PASSWORD)
    conn.sudo(f"hostnamectl set-hostname {NEW_USER}", password=PASSWORD)
    conn.sudo(f"useradd -m -G wheel {NEW_USER}", password=PASSWORD)
    conn.sudo(f"echo '{NEW_USER} ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/{NEW_USER}", password=PASSWORD)

    for name in FOLDERS:
        path = f"/home/{NEW_USER}/ops445/{name}"
        conn.sudo(f"mkdir -p {path}", password=PASSWORD)
        conn.sudo(f"chown -R {NEW_USER}:{NEW_USER} /home/{NEW_USER}/ops445", password=PASSWORD)
