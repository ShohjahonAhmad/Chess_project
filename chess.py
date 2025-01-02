import pygame

class Piece:
    def __init__(self,color):
        self.color = color
        self.image = None
        self.name = None
    def get_valid_moves(self, position, board):
        raise NotImplementedError("This shouldn't called in this class")
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)  # Call the base class constructor
        if color == 'white':
            self.image = pygame.image.load('images/wp.png')
        else:
            self.image = pygame.image.load('images/bp.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.name = 'pawn'
    def get_valid_moves(self, position, board):
        moves = []
        x, y = position
        
        if self.color == 'black':
            
                if (x, y + 1) not in board.blocations and (x, y + 1) not in board.wlocations and y < 7:
                    moves.append((x, y + 1))
                    if (x, y + 2) not in board.blocations and (x, y + 2) not in board.wlocations and y == 1:
                        moves.append((x, y + 2))
                if (x + 1, y + 1) in board.wlocations:
                    moves.append((x + 1, y + 1))
                if (x - 1, y + 1) in board.wlocations:
                    moves.append((x - 1, y + 1))
        elif self.color == 'white':
                if (x, y - 1) not in board.wlocations and (x, y - 1) not in board.blocations and y > 0:
                    moves.append((x, y - 1))
                    if (x, y - 2) not in board.wlocations and (x, y + 2) not in board.blocations and y == 6:
                        moves.append((x, y - 2))
                if (x + 1, y - 1) in board.blocations:
                    moves.append((x + 1, y - 1))
                if (x - 1, y - 1) in board.blocations:
                    moves.append((x - 1, y - 1))

        return moves
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color) # Call the base class constructor
        if color == 'white':
            self.image = pygame.image.load('images/wr.png')
        else:
            self.image = pygame.image.load('images/br.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.name = 'rook'
    def get_valid_moves(self, position, board):
        moves = []
        x, y = position
        
        if self.color == 'white':
            enemies = board.blocations
            friends = board.wlocations
        else:
            enemies = board.wlocations
            friends = board.blocations
        for i in range(4):
            path = True
            chain = 1
            if i == 0:
                dx = 0
                dy = 1
            elif i == 1:
                dx = 0
                dy = -1
            elif i == 2:
                dx = 1
                dy = 0
            else:
                dx = -1
                dy = 0
            while path:
                if (x + chain * dx, y + chain * dy) not in friends and 0 <= x + chain * dx <= 7 and \
                0 <= y + chain * dy <= 7:
                    moves.append((x + chain * dx, y + chain * dy))
                    if (x + chain * dx, y + chain * dy) in enemies:
                        path = False
                    chain += 1
                else:
                    path = False
                    
            
        
        return moves
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color) # Call the base class constructor
        if color == 'white':
            self.image = pygame.image.load('images/wn.png')
        else:
            self.image = pygame.image.load('images/bn.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.name = 'knight'
    def get_valid_moves(self, position, board):
        moves = []
        x, y = position
        if self.color == 'white':
            friends = board.wlocations
        else:
            friends = board.blocations
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for i in range(8):
            move = (x + knight_moves[i][0], y + knight_moves[i][1])
            if move not in friends and 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                moves.append(move)
        return moves
    
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color) # Call the base class constructor
        if color == 'white':
            self.image = pygame.image.load('images/wb.png')
        else:
            self.image = pygame.image.load('images/bb.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.name = 'bishop'
    def get_valid_moves(self, position, board):
        moves = []
        x, y = position
        if self.color == 'white':
            enemies = board.blocations
            friends = board.wlocations
        else:
            enemies = board.wlocations
            friends = board.blocations
        for i in range(4):
            path = True
            chain = 1
            if i == 0:
                dx = 1
                dy = -1
            elif i == 1:
                dx = -1
                dy = -1
            elif i == 2:
                dx = 1
                dy = 1
            else:
                dx = -1
                dy = 1
            while path:
                 if (x + chain * dx, y + chain * dy) not in friends and 0 <= x + chain * dx <= 7 and \
                 0 <= y + chain * dy <= 7:
                     moves.append((x + chain * dx, y + chain * dy))
                     if (x + chain * dx, y + chain * dy) in enemies:
                         path = False
                     chain += 1
                 else:
                     path = False
             
        return moves

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color) # Call the base class constructor
        if color == 'white':
            self.image = pygame.image.load('images/wq.png')
        else:
            self.image = pygame.image.load('images/bq.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.name = 'queen'
    def get_valid_moves(self, position, board):
        moves = []
        x, y = position
        
        rook = Rook(self.color)
        bishop = Bishop(self.color)
        
        # Combine rook and bishop moves
        
        moves.extend(rook.get_valid_moves(position, board))
        moves.extend(bishop.get_valid_moves(position, board))
        
        return moves

class King(Piece):
    def __init__(self, color):
        super().__init__(color) # Call the base class constructor
        if color == 'white':
            self.image = pygame.image.load('images/wk.png')
        else:
            self.image = pygame.image.load('images/bk.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.name = 'king'
    def get_valid_moves(self, position, board):
        moves = []
        x, y = position
        if self.color == 'white':
            friends = board.wlocations
        else:
            friends = board.blocations
        king_moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
        for i in range(8):
            move = (x + king_moves[i][0], y + king_moves[i][1])
            if move not in friends and 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                moves.append(move)
        
        return moves            
class Board:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.blocations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                           (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
        self.wlocations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                           (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
        
        self.white_pieces = [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'),
                             Knight('white'), Rook('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')]
        self.black_pieces = [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), 
                             Knight('black'), Rook('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')]
        self.wimages = [Pawn('white').image, Queen('white').image, King('white').image, Knight('white').image, 
                        Rook('white').image, Bishop('white').image]
        self.bimages = [Pawn('black').image, Queen('black').image, King('black').image, Knight('black').image, 
                        Rook('black').image, Bishop('black').image]
        self.wppieces = [Rook('white'), Knight('white'), Bishop('white'), Queen('white')]
        self.bppieces = [Rook('black'), Knight('black'), Bishop('black'), Queen('black')]
        # self.piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop'] might be useless
        self.wking = self.white_pieces[4]
        self.bking = self.black_pieces[4]
        self.setup_board()
    def setup_board(self):
        self.board[0] = [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')]
        self.board[1] = [Pawn('black')] * 8
        self.board[6] = [Pawn('white')] * 8
        self.board[7] = [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
    def is_empty(self, position):
        x, y = position
        return self.board[x][y] is None
    def get_piece(self, position):
        x, y = position
        return self.board[x][y] 
    def is_valid_position(self, position):
        x, y = position
        return 0 <= x <= 7 and 0 <= y <= 7
    def move_piece(self, start, end):
        piece = self.get_piece(start)
        if piece and end in piece.get_valid_moves(start, self):
            self.board[end[1]][end[0]] = piece
            self.board[start[1]][start[0]] = None
            return True
        return False
    # def white_pieces(self):
    #     return self.white_pieces
    # def black_pieces(self):
    #     return self.black_pieces
    # def print_board(self):
    #     for row in self.board:
    #         print(" | ".join([type(piece).__name__[0] if piece else '.' for piece in row]))
    #         print("-" * 17)
    
pygame.init()
board = Board()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Chess")
font = pygame.font.Font('bahnschrift.ttf', 20)
medium_font = pygame.font.Font('bahnschrift.ttf', 45)
medium_font1 = pygame.font.Font('bahnschrift.ttf', 35)
big_font = pygame.font.Font('bahnschrift.ttf', 50)
timer = pygame.time.Clock()
fps = 60
turn_step = 0
selection = 100
captured_white = []
captured_black = []
counter = 0
winner = ''
game_over = False
button = 'RESIGN'
close = False
white_promotion = False
black_promotion = False
promote_index = 100
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(
                screen, "burlywood2", [700 - (column * 200), row * 100, 100, 100]
            )
        else:
            pygame.draw.rect(
                screen, "burlywood2", [600 - (column * 200), row * 100, 100, 100]
            )
        pygame.draw.rect(screen, "burlywood2", [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, "darkgoldenrod4", [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, "darkgoldenrod4", [800, 0, 200, HEIGHT], 5)
        status_text = [
            "White: Select a Piece to Move!",
            "White: Select a Destination!",
            "Black: Select a Piece to Move!",
            "Black: Select a Destination!",
        ]
        screen.blit(big_font.render(status_text[turn_step], True, "white"), (50, 825))
        if button == 'RESIGN':
            screen.blit(medium_font.render(button, True, 'white'), (822, 818))
        else:
            screen.blit(medium_font.render(button, True, 'white'), (805, 818))
            
        if white_promotion or black_promotion:
            pygame.draw.rect(screen, "burlywood2", [0, 800, WIDTH - 200, 100])
            pygame.draw.rect(screen, "darkgoldenrod4", [0, 800, WIDTH - 200, 100], 5)
            screen.blit(big_font.render("Select a Piece to Promote Pawn", True, "white"), (50, 825))
def draw_pieces():
    for i in range(len(board.white_pieces)):
       piece = board.white_pieces[i]
       location = board.wlocations[i]
       screen.blit(piece.image, (location[0] * 100 + 5, location[1] * 100 + 5))
       if turn_step < 2:
           if selection == i:
               pygame.draw.rect(screen, 'aqua', [location[0] * 100 + 1, location[1] * 100 + 1, 100, 100], 2)

    for i in range(len(board.black_pieces)):
       piece = board.black_pieces[i]
       location = board.blocations[i]
       screen.blit(piece.image, (location[0] * 100 + 5, location[1] * 100 + 5))
       if turn_step >= 2:
           if selection == i:
               pygame.draw.rect(screen, 'firebrick1', [location[0] * 100 + 1, location[1] * 100 + 1, 100, 100], 2)
def draw_options(moves):
    if turn_step < 2:
        color = 'aqua'
    else:
        color = 'firebrick1'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0]* 100 + 50, moves[i][1] * 100 + 50), 5)
def draw_captured():
    for i in range(len(captured_white)):
        current = captured_white[i].image
        current = pygame.transform.scale(current, (45, 45))
        screen.blit(current, (825, 750 - 50 * i))
    for i in range(len(captured_black)):
        current = captured_black[i].image
        current = pygame.transform.scale(current, (45, 45))
        screen.blit(current, (825, 5 + 50 * i))
def get_king_position(color):
    """Helper function to get the king's position based on color."""
    if color == 'white':
        for i, piece in enumerate(board.white_pieces):
            if piece.name == 'king':
                return board.wlocations[i]
    else:
        for i, piece in enumerate(board.black_pieces):
            if piece.name == 'king':
                return board.blocations[i]
    return None
def draw_check():
    if turn_step < 2:
        
        king_position = get_king_position('white')
        for i in range(len(black_options)):
            if king_position in black_options[i]:
                if counter < 15:
                    pygame.draw.rect(screen, 'firebrick1', [king_position[0] * 100 + 1, king_position[1] * 100 + 1, 100, 100], 5)
    else:
        
        king_position = get_king_position('black')
        for i in range(len(white_options)):
            if king_position in white_options[i]:
                if counter < 15:
                    pygame.draw.rect(screen, 'aqua', [king_position[0] * 100 + 1, king_position[1] * 100 + 1, 100, 100], 5)
        
def draw_game_over():
    box_width, box_height = 500, 300
    box_x, box_y = 150, 250
    pygame.draw.rect(screen, 'cornsilk3', [box_x, box_y, box_width, box_height])  
    pygame.draw.rect(screen, 'cornsilk4', [box_x, box_y, box_width, box_height], 5)
    close_button = pygame.Rect(box_x + box_width - 30, box_y + 10, 20, 20)
    close_text = font.render('X', True, 'cornsilk4')
    pygame.draw.rect(screen, 'gray', close_button)
    screen.blit(close_text, (close_button.x + 4, close_button.y))
    screen.blit(medium_font.render(f'{winner.capitalize()} won the game!', True, 'white'), (190, 350))  
    screen.blit(medium_font1.render('Press RESTART to rematch', True, 'white'), (190, 400))  
    return close_button
close_button = draw_game_over()
# funtion to check all valid moves of all pieces
def check_options(pieces, locations, turn):
    all_moves = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        all_moves.append(piece.get_valid_moves(location, board))
    return all_moves
valid_moves = []

def check_promotion():
    pawn_indexes = []
    white_promotion = False
    black_promotion = False
    promote_index = 100
    for i in range(len(board.white_pieces)):
        if board.white_pieces[i].name == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if board.wlocations[pawn_indexes[i]][1] == 0:
            white_promotion = True
            promote_index = pawn_indexes[i]
    pawn_indexes = []
    for i in range(len(board.black_pieces)):
        if board.black_pieces[i].name == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if board.blocations[pawn_indexes[i]][1] == 7:
            black_promotion = True
            promote_index = pawn_indexes[i]
    return white_promotion, black_promotion, promote_index

def draw_promotion():
    pygame.draw.rect(screen, 'cornsilk4', [800, 0, 200, 420])
    if white_promotion:
        for i in range(len(board.wppieces)):
            piece = board.wppieces[i]
            screen.blit(piece.image, (860, 5 + 100 * i))
    elif black_promotion:
        for i in range(len(board.bppieces)):
            piece = board.bppieces[i]
            screen.blit(piece.image, (860, 5 + 100 * i))
    pygame.draw.rect(screen, 'cornsilk3', [800, 0, 200, 420], 5)

def check_selection():
    mouse_position = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    x_pos = mouse_position[0] // 100
    y_pos = mouse_position[1] // 100
    if white_promotion and left_click and x_pos > 7 and y_pos < 4:
        board.white_pieces[promote_index] = board.wppieces[y_pos]
    elif black_promotion and left_click and x_pos > 7 and y_pos < 4:
        board.black_pieces[promote_index] = board.bppieces[y_pos]
    
    
valid_moves = []
black_options = check_options(board.black_pieces, board.blocations, 'black')
white_options = check_options(board.white_pieces, board.wlocations, 'white')
run = True
while run:
    pygame.time.Clock().tick(fps)
    if counter < 30:
        counter += 1
    else: 
        counter = 0
    screen.fill("white")
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if not game_over:
        white_promotion, black_promotion, promote_index = check_promotion()
        if white_promotion or black_promotion:
            draw_promotion()
            check_selection()
        
    if selection != 100:
        if turn_step < 2:
            valid_moves = board.white_pieces[selection].get_valid_moves(board.wlocations[selection], board)  
        else:
            valid_moves = board.black_pieces[selection].get_valid_moves(board.blocations[selection], board)
        draw_options(valid_moves)
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over: # checks left mouse click
            x_coord, y_coord = event.pos[0] // 100, event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step < 2:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                    button = 'RESTART'
                    close = True
                if click_coords in board.wlocations:
                    selection = board.wlocations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    board.wlocations[selection] = click_coords
                    board.move_piece(board.wlocations[selection], click_coords)
                    if click_coords in board.blocations:
                        black_piece = board.blocations.index(click_coords)
                        captured_white.append(board.black_pieces[black_piece])
                        if board.black_pieces[black_piece].name == 'king':
                            winner = 'white'
                            button = 'RESTART'
                            close = True
                        board.black_pieces.pop(black_piece)
                        board.blocations.pop(black_piece)
                        
                    black_options = check_options(board.black_pieces, board.blocations, 'black')
                    white_options = check_options(board.white_pieces, board.wlocations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step >= 2:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                    button = 'RESTART'
                    close = True
                if click_coords in board.blocations:
                    selection = board.blocations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    board.blocations[selection] = click_coords
                    board.move_piece(board.blocations[selection], click_coords)
                    if click_coords in board.wlocations:
                        white_piece = board.wlocations.index(click_coords)
                        captured_black.append(board.white_pieces[white_piece])
                        if board.white_pieces[white_piece].name == 'king':
                            winner = 'black'
                            button = 'RESTART'
                            close = True
                        board.white_pieces.pop(white_piece)
                        board.wlocations.pop(white_piece)
                    black_options = check_options(board.black_pieces, board.blocations, 'black')
                    white_options = check_options(board.white_pieces, board.wlocations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_over: # checks left mouse click
            x_coord, y_coord = event.pos[0] // 100, event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if click_coords == (8, 8) or click_coords == (9, 8) and game_over:  
                if button == 'RESTART':
                        game_over = False
                        close = False
                        winner = ''
                        board.blocations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                           (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                        board.wlocations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                           (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                        board.white_pieces = [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'),
                                             Knight('white'), Rook('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')]
                        board.black_pieces = [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), 
                                             Knight('black'), Rook('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')]
                        captured_white = []
                        captured_black = []
                        turn_step = 0
                        selection = 100
                        valid_moves = []
                        black_options = check_options(board.black_pieces, board.blocations, 'black')
                        white_options = check_options(board.white_pieces, board.wlocations, 'white')
                        button = 'RESIGN'
        if event.type == pygame.MOUSEBUTTONDOWN and close:
            mouse_pos = event.pos
            if close_button.collidepoint(mouse_pos):
                close = False
    if winner != '':
        game_over = True
        if close == True:
            draw_game_over()
            
    pygame.display.flip()
pygame.quit()
