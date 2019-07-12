def check(height, width):
    if height <= 1:
        print "Height must be greater then one , your input :", height
        exit()

    elif (width % 2) != 0 or width <= 0:
        print "Width should be even  or positive number , your input :", width
        exit()

    else:
        return height, width



def trinagle(high,width):
    star = 1

    for i in range(0,high):
        space = (high-1)-i
        print (' ' * (space*width/2) + '*'*star)
        star = (width + star)


def main():
    # insert heigh  should be greater then 1 and width   even number or positive
    height=3 # input("Heigth :")
    width= 2   # input ("Width : ")

    check(height, width)
    trinagle(height, width)

main()

