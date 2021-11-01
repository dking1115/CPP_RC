import logging

import threading

import time

t=0
q=10
def thread_function(name):
        logging.info("Thread %s: starting", name)

        time.sleep(2)
        t+=1

        logging.info("Thread %s: finishing", name)


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")


    logging.info("Main    : before creating thread")

    x = threading.Thread(target=thread_function, args=(1,))
    y = threading.Thread(target=thread_function, args=(2,))
    logging.info("Main    : before running thread")
    for i in range(10):

        x.start()
        time.sleep(1)
        y.start()
        x.join()
        y.join()
    logging.info("Main    : wait for the thread to finish")


logging.info("Main    : all done")
    
