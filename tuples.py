def get_rectangle(length, width):
    """
    Calculate the area and perimeter of Rect

    Args: length: length of rectangle
            width: width of rectangle

            Returns:
                A tuple containing (are, perimeter).
    """


    area = (length * width)
    perimeter = (2*(length + width))

    return area, perimeter

Area, Perimeter = get_rectangle(20, 5)

print(f"Area = {Area}")
print(f"Perimeter = {Perimeter}")