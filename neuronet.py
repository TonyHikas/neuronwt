import random
import math


def get_tast(num):
    tasks = [
        ([0.2, 0.8], 0.1),
        ([0.8, 0.8], 0.9),
        ([0.2, 0.2], 0.1),
        ([0.8, 0.2], 0.1),
    ]
    return tasks[random.randint(0, 3)]


def fix_out_error(idl, last_layer):
    last_layer[0][1] = idl - last_layer[0][0]


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


if __name__ == "__main__":
    layer1 = [
        [0, 0],
        [0, 0],
        [1, 0],
    ]
    # значение нейрона и ошибка
    layer2 = [
        [0, 0],
        [0, 0],
        [0, 0],
        [1, 0],
    ]
    layer3 = [
        [0, 0],
        [1, 0]
    ]
    links12 = [
        [random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random()],
        [random.random(), random.random(), random.random(), random.random()],
    ]
    links23 = [
        [random.random()],
        [random.random()],
        [random.random()],
        [random.random()],
    ]
    task = None
    is_ok = False
    counter = 0
    while(is_ok==False):
        for i in range(100):
            val_in, val_out = get_tast(i)

            layer1[0][0] = val_in[0]
            layer1[1][0] = val_in[1]

            forwards(layer1, links12, layer2)
            forwards(layer2, links23, layer3)

            fix_out_error(val_out, layer3)

            find_error(layer2, links23, layer3)
            find_error(layer1, links12, layer2)

            backwards(layer2, links23, layer3, 1)
            backwards(layer1, links12, layer2, 1)
            counter+=1
            #print(layer1)
            #print(layer2)
            print(str(layer3[0][0])+" "+str(layer3[0][1]))
        print("--------------------------------------------------------------")

        layer1[0][0] = 0.2
        layer1[1][0] = 0.2
        forwards(layer1, links12, layer2)
        forwards(layer2, links23, layer3)
        if layer3[0][0] <= 0.2:
            is_ok = True
        else:
            is_ok = False
        print(layer3)
        layer1[0][0] = 0.2
        layer1[1][0] = 0.8
        forwards(layer1, links12, layer2)
        forwards(layer2, links23, layer3)
        if layer3[0][0] <= 0.2 and is_ok == True:
            is_ok = True
        else:
            is_ok = False
        print(layer3)
        layer1[0][0] = 0.8
        layer1[1][0] = 0.2
        forwards(layer1, links12, layer2)
        forwards(layer2, links23, layer3)
        if layer3[0][0] <= 0.2 and is_ok == True:
            is_ok = True
        else:
            is_ok = False
        print(layer3)
        layer1[0][0] = 0.8
        layer1[1][0] = 0.8
        forwards(layer1, links12, layer2)
        forwards(layer2, links23, layer3)
        if layer3[0][0] >= 0.8 and is_ok == True:
            is_ok = True
        else:
            is_ok = False
        print(layer3)
    print(counter)







