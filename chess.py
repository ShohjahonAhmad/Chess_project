import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chessify")  # naming the pygame window
font = pygame.font.Font("freesansbold.ttf", 20)
big_font = pygame.font.Font("freesansbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60
# game variables and images
white_pieces = [
    "rook",
    "knight",
    "bishop",
    "king",
    "queen",
    "bishop",
    "knight",
    "rook",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
]
white_locations = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 0),
    (6, 0),
    (7, 0),
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
]
black_pieces = [
    "rook",
    "knight",
    "bishop",
    "king",
    "queen",
    "bishop",
    "knight",
    "rook",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
    "pawn",
]
black_locations = [
    (0, 7),
    (1, 7),
    (2, 7),
    (3, 7),
    (4, 7),
    (5, 7),
    (6, 7),
    (7, 7),
    (0, 6),
    (1, 6),
    (2, 6),
    (3, 6),
    (4, 6),
    (5, 6),
    (6, 6),
    (7, 6),
]
captured_pieces_white = []
captured_pieces_black = []
# 0-white's turn no selection: 1-white's turn piece selected: 2-black's turn no selection: 3-black's turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# load in game piece images(queen, king, bishop, knight, rook, pawn) for black and white
black_queen = pygame.image.load("images/bq.png")
black_queen = pygame.transform.scale(black_queen, (90, 90))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load("images/bk.png")
black_king = pygame.transform.scale(black_king, (90, 90))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load("images/br.png")
black_rook = pygame.transform.scale(black_rook, (90, 90))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load("images/bb.png")
black_bishop = pygame.transform.scale(black_bishop, (90, 90))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load("images/bn.png")
black_knight = pygame.transform.scale(black_knight, (90, 90))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load("images/bp.png")
black_pawn = pygame.transform.scale(black_pawn, (90, 90))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load("images/wq.png")
white_queen = pygame.transform.scale(white_queen, (90, 90))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load("images/wk.png")
white_king = pygame.transform.scale(white_king, (90, 90))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load("images/wr.png")
white_rook = pygame.transform.scale(white_rook, (90, 90))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load("images/wb.png")
white_bishop = pygame.transform.scale(white_bishop, (90, 90))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load("images/wn.png")
white_knight = pygame.transform.scale(white_knight, (90, 90))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load("images/wp.png")
white_pawn = pygame.transform.scale(white_pawn, (90, 90))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_images = [
    white_pawn,
    white_queen,
    white_king,
    white_knight,
    white_rook,
    white_bishop,
]
small_white_images = [
    white_pawn_small,
    white_queen_small,
    white_king_small,
    white_knight_small,
    white_rook_small,
    white_bishop_small,
]
black_images = [
    black_pawn,
    black_queen,
    black_king,
    black_knight,
    black_rook,
    black_bishop,
 ]
small_black_images = [
    black_pawn_small,
    black_queen_small,
    black_king_small,
    black_knight_small,
    black_rook_small,
    black_bishop_small,
]
piece_list = ["pawn", "queen", "king", "knight", "rook", "bishop"]
# check_variables/ flashing counter


# draw main game board
def draw_board():
    
    
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(
                screen, "white", [600 - (column * 200), row * 100, 100, 100]
            )
        else:
            pygame.draw.rect(
                screen, "white", [700 - (column * 200), row * 100, 100, 100]
            )
        pygame.draw.rect(screen, "burlywood4", [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, "darkgoldenrod4", [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, "darkgoldenrod4", [800, 0, 200, HEIGHT], 5)
        status_text = [
            "White: Select a Piece to Move!",
            "White: Select a Destination!",
            "Black: Select a Piece to Move!",
            "Black: Select a Destination!",
        ]
        screen.blit(big_font.render(status_text[turn_step], True, "white"), (20, 825))
#draw pieces onto board        
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index((white_pieces[i]))
        screen.blit(white_images[index], (white_locations[i][0] * 100 + 5, white_locations[i][1] * 100 + 5))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'deepskyblue', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100, 100], 4)
    for i in range(len(black_pieces)):
        index = piece_list.index((black_pieces[i]))
        screen.blit(black_images[index], (black_locations[i][0] * 100 + 5, black_locations[i][1] * 100 + 5))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'orangered', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 4)

# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        if piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list
# check valid king moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    # 8 squares to check for king, they can go 1 square in any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

#check valid queen moves
def check_queen(position, color):
    return check_bishop(position, color) + check_rook(position, color)

#check valid rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4): # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
        
    
    return moves_list

# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and (position[0], position[1] + 1) not in black_locations and \
        position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if(position[0], position[1] + 2) not in white_locations and (position[0], position[1] + 2) not in black_locations and \
        position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    elif color == 'black':
        if (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations and \
        position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if(position[0], position[1] - 2) not in white_locations and (position[0], position[1] - 2) not in black_locations and \
        position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
            
    return moves_list

# check valid bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        enemies_list = white_locations
        friends_list = black_locations
    for i in range(4): # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
                
    return moves_list

# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

# draw valid moves on screen
def draw_valid(moves):
    color = 'orangered'
    if turn_step < 2:
        color = 'deepskyblue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)
    
# main game loop
black_options = check_options(black_pieces, black_locations, "black")
white_options = check_options(white_pieces, white_locations, "white")
run = True
while run:
    timer.tick(fps)  # it calculate the number of milliseconds since the previous call
    screen.fill("burlywood3")
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step < 2:
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, "black")
                    white_options = check_options(white_pieces, white_locations, "white")
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            elif turn_step >= 2:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, "black")
                    white_options = check_options(white_pieces, white_locations, "white")
                    turn_step = 0
                    selection = 100
                    valid_moves = []
    pygame.display.flip()  # update the screen
pygame.quit()
