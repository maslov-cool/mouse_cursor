import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 500, 500
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Свой курсор мыши')

    running = True
    cursor_image = load_image("arrow.png")
    clock = pygame.time.Clock()
    while running:
        pygame.mouse.set_visible(False)
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # Заполнение экрана черным цветом
        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused():
            # Получаем позицию мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Отрисовка пользовательского курсора
            screen.blit(cursor_image, (mouse_x - 10, mouse_y - 10))  # Центрируем курсор
        # обновление экрана
        pygame.display.flip()
    # завершение работы:
    pygame.quit()
