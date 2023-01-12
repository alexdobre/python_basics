import pygame

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (600, 600)
window_title = "Connect 4"

# Create the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Set the colors
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

# Set the board size and starting player
board_size = (7, 6)
current_player = "red"

# Create a 2D array to represent the board
board = [[None] * board_size[1] for _ in range(board_size[0])]

# Create a font for the message text
font = pygame.font.Font(None, 36)

# Create a rectangle for each column in the board
columns = []
for x in range(board_size[0]):
    column = pygame.Rect(x * (window_size[0] // board_size[0]), 0, window_size[0] // board_size[0], window_size[1])
    columns.append(column)

# Create a function to draw the board
def draw_board():
    # Draw a black background
    screen.fill(black)

    # Draw the columns
    for column in columns:
        pygame.draw.rect(screen, black, column)

    # Draw the circles on the board
    for x in range(board_size[0]):
        for y in range(board_size[1]):
            if board[x][y] is not None:
                color = red if board[x][y] == "red" else yellow
                center_x = (x * (window_size[0] // board_size[0])) + (window_size[0] // board_size[0]) // 2
                center_y = (y * (window_size[1] // board_size[1])) + (window_size[1] // board_size[1]) // 2
                pygame.draw.circle(screen, color, (center_x, center_y), (window_size[0] // board_size[0]) // 2)
    pygame.display.update()


# Create a function to check for a win
def check_win(player):
    # Check for horizontal wins
    for y in range(board_size[1]):
        for x in range(board_size[0] - 3):
            if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                return True

    # Check for vertical wins
    for x in range(board_size[0]):
        for y in range(board_size[1] - 3):
            if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
                return True

    # Check for diagonal wins
    for x in range(board_size[0] - 3):
        for y in range(board_size[1] - 3):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                return True
            if board[x][y+3] == player and board[x+1][y+2] == player and board[x+2][y+1] == player and board[x+3][y] == player:
                return True

    return False

# Run the game loop
while True:
    # Check for a win
    if check_win(current_player):
        message = f"{current_player} wins!"
        text = font.render(message, True, yellow)
        screen.blit(text, (window_size[0] // 2 - text.get_width() // 2, window_size[1] // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(6000)
        break

    # Draw the board
    draw_board()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position and column clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            column_clicked = mouse_x // (window_size[0] // board_size[0])

            # Find the first empty spot in the column and add a piece
            for y in range(board_size[1] - 1, -1, -1):
                if board[column_clicked][y] is None:
                    board[column_clicked][y] = current_player
                    break

            # Switch to the other player
            current_player = "yellow" if current_player == "red" else "red"

# Quit Pygame
pygame.quit()

