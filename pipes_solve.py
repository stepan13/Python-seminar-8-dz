# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной 
# данной работающей трубой (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн. 
# Сколько минут на это потребуется?
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
# Результат запишите в файл time.txt


def read_pipes():
    pipes = dict()
    
    with open("pipes.txt","r") as file:
        lines = file.read().splitlines()
        pipe_count = 0
        empty_line_count = 0
        for line in lines:
            if line == "":
                empty_line_count += 1
            else:
                if empty_line_count == 0:
                    pipe_count += 1
                    pipes[pipe_count] = int(line)
                elif empty_line_count == 1:
                    pipes_on = set(map(lambda x: int(x),line.split(" ")))
                    break
    return(pipes,pipes_on)

def calc_pipes(pipes,pipes_on):
    res = 0
    vel = 0
    for pipe_number in pipes_on:
        current_pipe = pipes[pipe_number]
        if current_pipe != 0:
            vel = vel + 1/current_pipe
    
    if vel != 0:
        res = 1 / vel
    
    return res



pipes,pipes_on = read_pipes()
res = calc_pipes(pipes,pipes_on)
with open("time.txt","w") as file:
    file.write(str(60*res))
