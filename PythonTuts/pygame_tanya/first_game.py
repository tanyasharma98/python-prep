# import pygame
#
# x = pygame.init()
# # print(x)   Testing
#
# # Creating window
# gameWindow = pygame.display.set_mode((1200, 500))  # Setting display window width and height
# pygame.display.set_caption("MY_First_Game")
#
# # Setting variables
# exit_game = False  # True when exiting the game
# game_over = False  # True when game over
#
# # Creating a game loop
# while not exit_game:
#     for event in pygame.event.get():  # handling events with mouse or keyboard
#         # print(event)
#         if event.type == pygame.QUIT:
#             exit_game = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 print("You have pressed right key")
# pygame.quit()
# quit()
def demo (num1, num2):

    result = num1**num2
    def ml(numl, num2):
        return num1*num2
    check = ml(5, 10)
    return check+5

out = demo(10, 5)
print (out)