from PIL import ImageColor
import os
import yaml

def hex_to_rgb(hex):
    return list(ImageColor.getcolor(hex, 'RGB'))

def extract_color_codes(s):
    color_list = s.split(',')
    return list(filter(lambda hex: len(hex) == 7, color_list))

def create_dataset():
    color_sets = os.listdir(RESOURCES_PATH)
    outputs = []

    for cs in color_sets:
        color_set_path = RESOURCES_PATH + '/' + cs
        with open(color_set_path, 'r') as c:
            color_set = c.read()
        
        
        color_set = extract_color_codes(color_set)
        color_set_data = []
        for hex in color_set:
            rgb = hex_to_rgb(hex)
            color_set_data.append({ 'hex': hex.replace('#', ''), 'rgb': rgb })
        
        outputs.append({ 'color_set': cs.replace('.txt', ''),
                     'data': color_set_data })
    
    return { 'outputs': outputs }

if __name__ == '__main__':
    WORKING_PATH = os.path.dirname(os.path.abspath(__file__))
    RESOURCES_PATH = os.path.join(WORKING_PATH, 'resources')
    OUTPUT_FILE = os.path.join(WORKING_PATH, 'output.yml')

    dataset = create_dataset()
    with open(OUTPUT_FILE, 'w') as output_file:
        yaml.dump(dataset, output_file, default_flow_style=False)
