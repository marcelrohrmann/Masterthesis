expression = {}

with open("C:/Users/spacefactory/Desktop/Marcel/expressions.txt", encoding='utf-8-sig') as f:
    for line in f:
        name, value = line.split("=")
        expression[name] = float(value)

circle_color_number = expression["circle_color_number"]
cubesat_color_number = expression["cubesat_color_number"]
cubesat_length = expression["cubesat_length"]
diameter = expression["diameter"]
rectangle_color_number = expression["rectangle_color_number"]
rectangle_length = expression["rectangle_length"]
grab_pos_x = expression["grab_pos_x"]
grab_pos_y = expression["grab_pos_y"]

# rot = 188
# schwarz = 173
# grün = 29
