import pygame
import math
import Curve


def main():
    curve_color = (0, 	238,	0)
    circle_color = (255, 255, 255)
    dot_color = (255, 255, 255)
    line_color = (255, 255, 255)
    width, height = 1030, 1030
    name_of_window = "Lissajous Curve Simulation"
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name_of_window)
    clock = pygame.time.Clock()
    angle = 1
    circle_diameter = int(width / 10)
    columns = int(width / circle_diameter) - 1
    rows = int(height / circle_diameter) - 1
    circle_diameter_draw = circle_diameter - 10
    r = circle_diameter_draw / 2
    position = set()

    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        window.fill((0, 0, 0))
        lx_ = []
        for column in range(columns):
            # the circle x location
            cx = circle_diameter + column * circle_diameter + int(circle_diameter_draw / 2)
            # the circle y location
            cy = circle_diameter_draw / 2 + circle_diameter_draw / 10
            # the dot x location
            x = r * math.cos(angle * (column + 1))
            # the dot y location
            y = r * math.sin(angle * (column + 1))
            # draws circle
            pygame.draw.circle(window, circle_color, [cx, int(cy)], int(r), 1)
            # draws dot
            pygame.draw.circle(window, dot_color, [int(x + cx), int(y + cy)], 5)
            # draws line from dot pos
            pygame.draw.line(window, line_color, (cx + x, cy + y), (cx + x, height), 1)
            angle += 0.001
            # adds the x

            lx_.append((int(round(cx + x))))

        ly_ = []
        for row in range(rows):
            # the circle y location
            cy = circle_diameter + row * circle_diameter + int(circle_diameter_draw / 2)
            # the circle x location
            cx = circle_diameter_draw / 2 + circle_diameter_draw / 10
            # the dot x location
            x = r * math.cos(angle * (row + 1))
            # the dot y location
            y = r * math.sin(angle * (row + 1))
            # draws circle
            pygame.draw.circle(window, circle_color, [int(cx), int(cy)], int(r), 1)
            # draws dot
            pygame.draw.circle(window, dot_color, [int(x + cx), int(y + cy)], 5)
            # draws line from dot pos
            pygame.draw.line(window, line_color, (cx + x, cy + y), (width, cy + y), 1)
            angle += 0.0001

            ly_.append((int(round(cy + y))))

        # adds the values to the
        position.update([(x_, y_) for x_ in lx_ for y_ in ly_])

        for i in position:
            pygame.draw.circle(window, curve_color, i, 1)


        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    # call the main function
    main()
