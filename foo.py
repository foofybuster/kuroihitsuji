import multiprocessing
global result
result = [None] * 10

def func(numb: int, index: int, return_dict: dict):
    def fib(numb: int):
        if numb <= 1:
            return numb
        return fib(numb - 1) + fib(numb - 2) 
    return_dict[index] = fib(numb), index 

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    processes = []

    for i in range(0, 4):
        p = multiprocessing.Process(target=func, args=(1, i, return_dict))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(return_dict)
