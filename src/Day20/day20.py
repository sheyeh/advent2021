image = []
num_steps = 50
with open('day20.txt', 'r') as f:
    image_key = f.readline().rstrip()
    f.readline()
    for line in f:
        # Add a frame of dots around the lines to the left and right
        image.append(list("." * (num_steps + 2) + line.rstrip() + "." * (num_steps + 2)))

image_width = len(image[0])
frame_horizontal = [list("." * image_width)]
# Also add top and bottom frame of dots
image = frame_horizontal * (num_steps + 2) + image + frame_horizontal * (num_steps + 2)


def pixel(x, y):
    square = image[x-1][y-1:y+2] + image[x][y-1:y+2] + image[x+1][y-1:y+2]
    pos = 0
    for s in square:
        pos = pos * 2 + (1 if s == "#" else 0)
    return image_key[pos]


for step in range(num_steps):
    processed_image = [list(line) for line in image]
    for i in range(1, image_width - 1):
        for j in range(1, image_width - 1):
            processed_image[i][j] = pixel(i, j)
    image = [list(line) for line in processed_image]
    # Since the first character in the mapping (first input line) is #, it means that
    # in the infinite image, the frame becomes # on odd rounds and since the last character
    # is . it becomes . on even rounds.
    fill = "." if step % 2 else "#"
    image[0] = [fill] * image_width
    image[image_width-1] = [fill] * image_width
    for i in range(image_width):
        image[i][0] = fill
        image[i][image_width-1] = fill
    if step == 1 or step == 49:
        count = len("".join(["".join(line) for line in image]).replace(".", ""))
        print(count)
