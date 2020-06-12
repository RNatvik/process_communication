from threading import Thread

import proccom


def break_cmd(server: proccom.Server):
    stop = False
    while not stop:
        a = input()
        if a == 'q':
            stop = True
    server.stop()


def main():
    server = proccom.Server('127.0.0.1', 5000)  # Create server object
    break_thread = Thread(target=break_cmd, daemon=False, args=[server])
    break_thread.start()
    server.start()  # Start server


if __name__ == '__main__':
    main()
