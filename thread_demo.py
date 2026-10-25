from threading import Thread
from time import sleep, time
from multiprocessing import process

class Hello:

    def do(self):
        for i in range(5):
            print("Hello", i+1)


class Hi:

    def do(self):
        for i in range(5):
            print("Hi", i+1)


# hello = Hello()
# hi = Hi()

# t1 = Thread(target=hello.do)
# t2 = Thread(target=hi.do)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("Both threads completed!")


def download(filename):
    print("File downloading...", filename)
    sleep(0.5)
    print("Download completed")


files = ["movies.mp4", "CV.pdf", "Profile.png"]

if __name__ == "__main__":
    start = time()
    for i in files:
        download(i)

    end = time()
    print(f"{end-start:.2f}")




    start = time()
    threads = []
    for f in files:
        t = Thread(target=download, args=(f,))
        t.start()
        threads.append(t)


    for t in threads:
        t.join()

    end = time()
    print(f"{end-start:.2f}")