"Create a list of colors from comma-separated color names entered by user. Display \
 first and last colors. "

color_name=input("enter colors")
color_lst=color_name.split(',')
print("color list is",color_lst)
print("First color in the list",color_lst[0])
print("Last color  in the list",color_lst[-1])