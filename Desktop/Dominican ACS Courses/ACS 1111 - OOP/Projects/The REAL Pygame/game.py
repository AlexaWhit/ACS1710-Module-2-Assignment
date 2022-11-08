# Import and initialize pygame
import pygame   
pygame.init()

# Import random
import random
from random import randint

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Configure the screen of the surface
screen = pygame.display.set_mode([500, 500])

game_lanes = [93, 218, 343]


# Create a game object class that draws a rectangle
class GameObject(pygame.sprite.Sprite):
	def __init__(self, x, y, apple):
		super(GameObject, self).__init__()
		# self.surf = pygame.Surface((width, height))
		# self.surf.fill((255, 0, 255))
		self.surf = pygame.image.load(apple)
		self.x = x
		self.y = y

	def render(self, screen):
		screen.blit(self.surf, (self.x, self.y))

# Create a new Apple class
# This object will always start at a random x and y of 0. 
# It will always display the apple.
class Apple(GameObject):
	def __init__(self):
		# generates a random number for the x position
		# x = randint(50, 400)
		# initializes its superclass
		# initialize our superclass with an x and y of 0
		super(Apple, self).__init__(0, 0, 'apple.png')
		self.dx = 0
		# This attributes sets the speed at which apples will fall down the screen. 
		self.dy = (randint(0, 200) / 100) + 1
		self.reset()
	# adds the dx to the x each frame which should move an Apple down the screen.
	def move(self):
		self.x += self.dx
		self.y += self.dy
		# Check the y position of the apple, if greater than 500 we reset
		if self.y > 500:
			self.reset()

	# The new reset method sets the starting parameters
	def reset(self):
		self.x = random.choice(game_lanes)
		self.y = -64

class Strawberry(GameObject):
	def __init__(self):
		super(Strawberry, self).__init__(0, 0, 'strawberry.png')
		self.dx = (randint(0, 200) / 100) + 1
		self.dy =  0
		self.reset()
	
	def move(self):
		self.x += self.dx
		self.y += self.dy
		if self.x > 500:
			self.reset()

	def reset(self):
		self.x = -64
		self.y = random.choice(game_lanes)

# Create a new Player class
class Player(GameObject):
	def __init__(self):
		super(Player, self).__init__(0, 0, 'player.png')
		self.dx = 0
		self.dy = 0
		self.reset()
	
	def left(self):
		self.dx -= 100

	def right(self):
		self.dx += 100

	def up(self):
		self.dy -= 100

	def down(self):
		self.dy += 100

	def move(self):
		# Remember dx is where we want to go and x is our current position
		# (self.x - self.dx) = distanceToMove
		self.x -= (self.x - self.dx) * 0.25
		self.y -= (self.y - self.dy) * 0.25

	# Player implements the reset() method which will move it 
	# to the center of the screen. This is the player's starting 
	# position.
	def reset(self):
		self.x = 250 - 32
		self.y = 250 - 32

# Make an instance of GameObject

apple = Apple()
strawberry = Strawberry()
apple2 = Apple()
strawberry2 = Strawberry()
apple3 = Apple()
strawberry3 = Strawberry()
player = Player()

# strawberry = GameObject(200, 150, 'strawberry.png')
# Create the Game Loop
running = True 
while running: 
	# loop over each event in pygame.event.get()
	for event in pygame.event.get():
		# check if the event.type is equal to pygame.QUIT 
		if event.type == pygame.QUIT:
			# if so we stop the game loop
			running = False
		# Check for even type KEYBOARD
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running == False
			elif event.key == pygame.K_LEFT:
				player.left()
			elif event.key == pygame.K_RIGHT:
				player.right()
			elif event.key == pygame.K_UP:
				player.up()
			elif event.key == pygame.K_DOWN:
				player.down()
	
	# Clear the screen
	screen.fill((255, 255, 255))

	#Draw Apple
	apple.move()
	apple.render(screen)
	# apple2.move()
	# apple2.render(screen)
	# apple3.move()
	# apple3.render(screen)

	# Draw Strawberry
	strawberry.move()
	strawberry.render(screen)
	# strawberry2.move()
	# strawberry2.render(screen)
	# strawberry3.move()
	# strawberry3.render(screen)

	# Draw Player
	player.move()
	player.render(screen)

	# Update the display - tells pygame to update the screen
	pygame.display.flip()
	# tick the clock!
	clock.tick(60)

