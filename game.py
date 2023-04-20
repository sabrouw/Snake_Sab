import random
import pygame


class Game():   
    def __init__(self):
        pygame.init()
        self.game_on = True
        # fenetre 
        self.screen = pygame.display.set_mode((800,600))
        # titre
        pygame.display.set_caption("Sab_Snake_")
        # position du snake
        self.snake_position_x = 300
        self.snake_position_y = 300 
        
        # deplacement du snake
        self.snake_direction_x = 0
        self.snake_direction_y = 0
        self.snake_body = 10 

       # position aléatoire de la apple
        self.apple_position_x = random.randrange(110, 690, 10)
        self.apple_position_y = random.randrange(110, 590, 10)
        self.apple = 10

       # fixer les fps
        self.clock = pygame.time.Clock()
    
       #tableau de position du serpent 
        self.snake_position = [] 

        self.size_serpent = 1
        self.start_screen = True

        self.image_snake = pygame.image.load("d45ed485-062c-4ab9-9e9e-96bb513647fd-2.png")
        self.image_title = pygame.transform.scale(self.image_snake,(200, 200))
        
    # boucle du jeu
    def while_loop(self):

        while self.start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.start_screen = False
                self.screen.fill((0,0,0))
                # self.start_message('grande', 'Snake_game',
                                #    (300,300, 100, 50),
                                #    (255,255,255))
                # self.start_message('moyenne', 'Presse une touche pour commencer!',
                                #    (200,400,300, 50),
                                #    (255,255,255))
                # self.screen.blit(self.image_title,(300,50,100,50) )
                pygame.display.flip()
        
        
        while self.game_on:
            # recupere tous les evenement de la souris dans la fenetre de jeu
            for event in pygame.event.get():           
                # pour quitter la fenetre
                if event.type == pygame.QUIT: 
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                # direction vers la droite
                    if event.key == pygame.K_RIGHT:
                        self.snake_direction_x = 10
                        self.snake_direction_y = 0
                        print("droite")
                    if event.key == pygame.K_LEFT:
                        self.snake_direction_x = -10
                        self.snake_direction_y = 0
                        print("gauche")
                    if event.key == pygame.K_DOWN:
                        self.snake_direction_y = 10
                        self.snake_direction_x = 0
                        print("en bas")
                    if event.key == pygame.K_UP:
                        self.snake_direction_y = -10
                        self.snake_direction_x = 0
                        print("en haut")
                
                if self.snake_position_x <= 10 or self.snake_position_x >= 780 or self.snake_position_y <= 10 or self.snake_position_y >= 580:
                    pygame.quit()
        # deplacement du snake
                self.snake_move()

        # deplacmeent de la pomme qi le snake la mange
                self.apple_move()
                # append les postion de la tete du serpent
                heads_snake = [] 
                heads_snake.append(self.snake_position_x)
                heads_snake.append(self.snake_position_y)

                # append les position du corps du     serpent
                self.snake_position.append(heads_snake)
                # gestion de la taille du serpent 
                self.size_snake()
                    
                # affichage du bg snake et apple
                self.display_elements()
                # si le serpent se mord la queue lejeu s'arrete
                for fragment_snake in self.snake_position[:-1]:
                    if heads_snake == fragment_snake:
                            pygame.quit()
                # limite de l'ecran enblanc
                self.limit_script()
                self.clock.tick(30)

            # maj de l'ecran or du for
            pygame.display.update()
            
    def limit_script(self):
        pygame.draw.rect(self.screen,(255,255,255),(0,0,800,600), 3)

    def snake_move(self):
        self.snake_position_x += self.snake_direction_x
        self.snake_position_y += self.snake_direction_y
        print(self.snake_position_x , self.snake_direction_y)

    def apple_move(self):
        if self.apple_position_y == self.snake_position_y and self.apple_position_x == self.snake_position_x:
            print('ok')
            self.apple_position_x = random.randrange(110, 690, 10)
            self.apple_position_y = random.randrange(110, 590, 10)
            self.size_serpent += 1

    def size_snake(self):
        if len(self.snake_position)> self.size_serpent:
            self.snake_position.pop(0)

    def display_elements(self):
        self.screen.fill((0,0,0))
                # affichage du snake
        pygame.draw.rect(self.screen,
                         (0, 255, 0), 
                         (self.snake_position_x, 
                          self.snake_position_y, 
                          self.snake_body, 
                          self.snake_body))
                # affichage de la pomme
        pygame.draw.rect(self.screen,
                         (255,0, 0), 
                         (self.apple_position_x, 
                          self.apple_position_y, 
                          self.apple, 
                          self.apple))
                # afficher le corps et la tete du  serpent apres manger la pomme
        for fragment_snake in self.snake_position:
            pygame.draw.rect(self.screen, 
                                     (0,255,0), 
                                     (fragment_snake[0], 
                                      fragment_snake[1],
                                      self.snake_body, 
                                      self.snake_body))
            
    def start_message(self, font,message, message_rect,  color):
        if font == 'petite':
            font = pygame.font.SysFont('Rubik Vinyl', 20, False)
        elif font == 'moyenne':
            font = pygame.font.SysFont('Rubik Vinyl', 30, False)
        elif font == 'grande':
            font = pygame.font.SysFont('Rubik Vinyl', 40, False)
        
        message = font.render(message, True, color)
        self.screen.blit(message, message_rect)
       
                    

    

        
            
        
            

    