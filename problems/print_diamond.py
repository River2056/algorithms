def print_diamond(width, min_width=1, spaces=0, container=[]):
    if width % 2 == 0 and min_width == 1:
        min_width = 2
    if width <= 0:
        return container
    if min_width < width:
        stars = ['*' for i in range(min_width)]
        space = (width - min_width) // 2
        for i in range(space):
            stars.insert(0, ' ')
            stars.append(' ')
        container.append(stars)
        return print_diamond(width, min_width+2, spaces, container)

    if spaces != 0:
        stars = ['*' for i in range(width)]
        insert_append_spaces = spaces // 2
        for i in range(insert_append_spaces):
            stars.insert(0, ' ')
            stars.append(' ')
        container.append(stars)
    else:
        container.append(['*' for i in range(width)])
    return print_diamond(width-2, min_width, spaces+2, container)

def main():
    height = int(input('Enter diamond height: '))
    arr = print_diamond(height + (height-1))
    for row in arr:
        for elem in row:
            print(elem, end='')
        print()

if __name__ == '__main__':
    main()
