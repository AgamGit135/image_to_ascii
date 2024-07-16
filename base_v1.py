import pygame
import sys
import tkinter as tk
from tkinter import filedialog

pygame.font.init()
my_font = pygame.font.SysFont('Arial', 60)

# Set up the window
screen = pygame.display.set_mode((800, 600))
screen.fill(pygame.Color("black"))
pygame.display.set_caption("Image Input Example")
text_surface = my_font.render('press space to upload photos', False, pygame.Color("white"))
screen.blit(text_surface, (75, 55))


def get_image_path():
    # Create a Tkinter root window (it will not be shown)
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog to choose an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

    return file_path


group_size = int(input("res (lower number, higher res):"))


def save_image(image):
    # Open a file dialog to select the save location
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG Image", "*.jpg"), ("All Files", "*.*")])
    if file_path:
        pygame.image.save(image, file_path)
        print("Image saved to:", file_path)


def process_image(image, group_width, group_height):
    image_width = image.get_width()
    image_height = image.get_height()
    # Define the size of each group of pixels

    # Divide the image into groups of pixels
    all_pixel_groups = []
    for y in range(0, image_height - group_height, group_height):
        for x in range(0, image_width - group_width, group_width):
            # Extract the pixels for the current group
            group_pixels = []
            for dy in range(group_height):
                for dx in range(group_width):
                    # Get the pixel color at position (x+dx, y+dy)
                    pixel_color = image.get_at((x + dx, y + dy))
                    luminance = int(0.3 * pixel_color.r + 0.59 * pixel_color.g + 0.11 * pixel_color.b)
                    group_pixels.append(luminance)
            all_pixel_groups.append(group_pixels)

    # Now pixel_groups contains the list of groups of pixels
    # Each group is represented as a list of pixel colors

    # Example: Print the first group of pixels
    average_luminance_list = []
    # for luminance in all_pixel_groups:
    for i in range(0, len(all_pixel_groups) * group_width * group_height // len(group_pixels)):
        # print(luminance)
        average_luminance = sum(all_pixel_groups[i]) / len(all_pixel_groups[i])
        average_luminance_list.append(average_luminance)
    print(image_height, image_width)
    print(group_pixels)
    print(len(all_pixel_groups))
    print(len(all_pixel_groups) * group_width * group_height)
    print(len(average_luminance_list))
    numbers_luminance = (222, 231, 159, 175, 200, 187, 242, 213, 213, 211, 210, 241, 237, 247, 213, 184,
                         201, 184, 188, 183, 183, 179, 205, 172, 178, 240, 237, 205, 203, 205, 209, 184,
                         168, 159, 188, 175, 161, 175, 173, 164, 196, 192, 164, 188, 147, 158, 180, 177,
                         157, 166, 176, 180, 178, 185, 153, 170, 187, 177, 206, 213, 206, 226, 226, 248,
                         184, 172, 197, 172, 180, 184, 166, 178, 204, 195, 179, 201, 171, 190, 195, 167,
                         167, 199, 190, 197, 192, 198, 181, 183, 180, 192, 210, 218, 210, 229, 223, 195,
                         185, 191, 179, 224, 178, 246, 186, 227, 216, 217, 237, 180, 226, 227, 186, 230,
                         231, 248, 181, 171, 249, 244, 236, 232, 216, 192, 203, 187, 209, 162, 162, 157,
                         157, 160, 159, 145, 178, 154, 154, 150, 152, 190, 190, 185, 188, 165, 146, 174,
                         174, 169, 169, 172, 212, 149, 171, 171, 166, 169, 180, 174, 170, 177, 177, 173,
                         173, 176, 174, 160, 187, 173, 173, 169, 172, 204, 204, 199, 202, 173, 179, 188,
                         188, 184, 184, 187, 223, 169, 186, 186, 181, 184, 173, 158, 171)
    # end list of numbers. appends in the end of for x in average_luminance_list block
    approximations = []
    # list of all the approximations
    new_index = []
    counter = 0
    lists = []
    for target_value in average_luminance_list:
        closest_number = min(numbers_luminance, key=lambda z: abs(z - target_value))
        # print("The closest number to", target_value, "is:", closest_number)
        approximations.append(closest_number)
        new_index.append(closest_number)
        counter += 1
        if counter == round(image_width // group_width):
            # If the condition is not satisfied, check if the current list is not empty
            lists.append(new_index)
            new_index = []
            counter = 0

    mapping = {
        222: '!',
        200: '%',
        242: "'",
        211: '*',
        241: ',',
        247: '.',
        205: '7',
        172: '8',
        178: '9',
        240: ':',
        237: ';',
        203: '=',
        209: '?',
        184: '@',
        168: 'A',
        159: 'B',
        188: 'C',
        175: 'D',
        161: 'E',
        164: 'H',
        196: 'I',
        192: 'J',
        147: 'M',
        158: 'N',
        177: 'P',
        157: 'Q',
        166: 'R',
        176: 'S',
        180: 'T',
        185: 'V',
        153: 'W',
        170: 'X',
        187: 'Y',
        213: '"',
        206: ']',
        248: '`',
        197: 'c',
        204: 'i',
        195: 'j',
        179: 'k',
        201: 'l',
        171: 'm',
        190: 'n',
        167: 'p',
        199: 'r',
        198: 'v',
        181: 'w',
        183: 'x',
        210: '{',
        218: '|',
        229: '~',
        223: '¡',
        191: '¤',
        224: '¦',
        246: '¨',
        186: '©',
        227: 'ª',
        216: '«',
        217: '¬',
        226: '¯',
        230: '²',
        231: '³',
        249: '·',
        244: '¸',
        236: '¹',
        232: 'º',
        162: 'Á',
        145: 'Æ',
        154: 'É',
        150: 'Ê',
        152: 'Ë',
        165: 'Ð',
        146: 'Ñ',
        169: 'Õ',
        212: '×',
        149: 'Ø',
        174: 'å',
        160: 'æ',
        173: 'é',
        202: 'ï',

    }
    for new_index in lists:
        actual_array = [mapping[closest_number] for closest_number in new_index]
        lol_string = ' '.join(map(str, actual_array))
        print(lol_string)


def upload():
    times_pressed = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for a key press to open the file dialog
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    image_path = get_image_path()
                    if image_path:
                        # Load and display the selected image
                        image = pygame.image.load(image_path)
                        height = image.get_height()
                        width = image.get_width()
                        if height <= 2400 or width <= 2500:
                            if not times_pressed:
                                bw_image = image.convert_alpha()  # Create a copy of the original image
                                bw_image = bw_image.convert()  # Convert the copy to a format suitable for pixel manipulation
                                bw_image = bw_image.convert_alpha()
                                for x in range(bw_image.get_width()):
                                    for y in range(bw_image.get_height()):
                                        r, g, b, a = bw_image.get_at(
                                            (x, y))  # Get the color channels (RGBA) of the pixel
                                        # Calculate the luminance (grayscale) value using the formula: L = 0.3R + 0.59G + 0.11B
                                        luminance = int(0.3 * r + 0.59 * g + 0.11 * b)
                                        # Set the pixel to the grayscale value
                                        bw_image.set_at((x, y), (luminance, luminance, luminance, a))

                                pygame.display.set_mode((width, height + 100))
                                screen.blit(bw_image, (0, 0))
                                text_surface3 = my_font.render('press letter s for saving photo', False,
                                                               pygame.Color("white"))
                                screen.blit(text_surface3, (20, height + 10))
                                times_pressed = True
                            else:
                                print("please do not try to upload/display more than 1 photo at a time")
                        elif height > 2400 or width > 2500:
                            text_surface2 = my_font.render('your photo is too big', False, pygame.Color("white"))
                            screen.blit(text_surface2, (175, 155))
                elif event.key == pygame.K_s:
                    save_image(bw_image)
                pygame.display.flip()
                process_image(bw_image, group_size, group_size)
        pygame.display.update()

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    upload()
