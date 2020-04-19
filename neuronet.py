import random
import math


def get_tast(num):
    # tasks = [
    #     ([0.2, 0.8], [1]),
    #     ([0.8, 0.8], [1]),
    #     ([0.2, 0.2], [0]),
    #     ([0.8, 0.2], [1]),
    # ]
    # return tasks[random.randint(0, 3)]
    if random.random() < 0.25:
        return ([
                ((random.random()-0.000001)/2),
                ((random.random()-0.000001)/2)
                 ], [0])
    if random.random() < 0.50:
        return ([
                ((random.random()+1)/2),
                ((random.random()-0.000001)/2)
                 ], [1])
    if random.random() < 0.75:
        return ([
                ((random.random()-0.000001)/2),
                ((random.random()+1)/2)
                 ], [1])
    if random.random() <= 1:
        return ([
                ((random.random()+1)/2),
                ((random.random()+1)/2)
                 ], [1])


def fix_out_error(idl, last_layer):
    for i in range(len(last_layer)-1):
        last_layer[i][1] = idl[i] - last_layer[i][0]


def forwards(lay1, links ,lay2):
    for i in range(len(lay2)-1):
        lay2[i][0] = 0
        for j in range(len(lay1)):
            lay2[i][0] = lay2[i][0] + lay1[j][0] * links[j][i]
        lay2[i][0] = 1 / (1 + math.exp(-1 * lay2[i][0]))  # логистическкая функция


def find_error(lay1, links, lay2):
    for i in range(len(lay1)):
        for j in range(len(lay2)-1):
            lay1[i][1] = lay2[j][1] * links[i][j]


def backwards(lay1, links, lay2, k):
    for i in range(len(lay1)):
        for j in range(len(lay2)-1):
            links[i][j] = links[i][j] + k*lay2[j][1]*lay2[j][0]*(1-lay2[j][0])*lay1[i][0]


def run_neuronet(lay_map, k, times):
    layers = []
    links = []
    layers.append([[0, 0] for j in range(lay_map[0])]+[[1, 0]])
    for i in range(len(lay_map)-1):
        layers.append([[0, 0] for j in range(lay_map[i+1])]+[[1, 0]])
        links.append([[random.random() for b in range(lay_map[i+1]+1)] for a in range(lay_map[i]+1)])
    print(layers)
    print(links)
    counter = 0
    for i in range(times):
        val_in, val_out = get_tast(i)

        # заполнение первого слоя входными данными
        for num, val in enumerate(val_in):
            layers[0][num][0] = val

        for num in range(len(layers)-1):
            forwards(layers[num], links[num], layers[num+1])

        fix_out_error(val_out, layers[-1])

        for num in reversed(range(len(layers)-1)):
            find_error(layers[num], links[num], layers[num+1])

        for num in reversed(range(len(layers)-1)):
            backwards(layers[num], links[num], layers[num+1], k)

        counter+=1
        print(str(layers[-1][0][0])+" "+str(layers[-1][0][1]))
    for layer in layers:
        print(layer)
    print("Layers cofig")
    print(lay_map)
    print("Links config")
    for link in links:
        print(link)
    while(True):
        a1 = input("Число 1: ")
        a2 = input("Число 2: ")
        layers[0][0][0] = float(a1)
        layers[0][1][0] = float(a2)
        for num in range(len(layers) - 1):
            forwards(layers[num], links[num], layers[num + 1])
        print(str(layers[-1][0][0])+" "+str(layers[-1][0][1]))


if __name__ == "__main__":
    run_neuronet(lay_map=[2, 3, 1], k=0.2, times=100)






