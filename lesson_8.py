import time
import tracemalloc

def timing(f):
    def wapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        finish_time = time.time()
        print(f'Время выполнения функции {f.__name__}: {finish_time-start_time} секунд')
        return result
    return wapper

def RAM_memory(f):
    def wapper(*args, **kwargs):
        tracemalloc.start()
        result = f(*args, **kwargs)
        memory_size = tracemalloc.get_traced_memory()
        print(f'Объем оперативной памяти, потребляемый функцией: {memory_size[0]} байт; max: {memory_size[1]} байт')
        tracemalloc.stop()
        return result
    return wapper

print('---Для функции создания генератора---')
@RAM_memory
@timing
def gen_list_el(num):
    for i in range(num):
        yield i

@RAM_memory
@timing
def list_el(num):
    print('---Для функции создания списка с элементами---')
    result = []
    for i in range(num):
        result.append(i)
    return result

gen_list_el(1000000)
list_el(1000000)