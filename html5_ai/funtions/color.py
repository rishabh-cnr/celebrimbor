required_rgb_dict = {
    'red':[255,0,0],
    'green':[0,128,0],
    'blue':[0,0,255],
    'yellow':[255,255,0],
    'magenta':[255,0,255],
    'cyan':[0,255,255],
    'grey':[128,128,128],
    'white':[255,255,255],
    'black':[0,2,0]
}

def get_color_name(rgb):

    dict_of_distance = {}

    manhattan_distance = lambda a, b: sum(abs(v1-v2) for v1, v2 in zip(a,b))

    for keys,values in  required_rgb_dict.items():
        distance = manhattan_distance(rgb,values)
        dict_of_distance.update({keys:distance})

    color = min(dict_of_distance , key=dict_of_distance.get)

    return color