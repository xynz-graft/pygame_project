import pygame
import random

WIDTH = 800

# Only road lanes.
# Removed 345 because that is your sidewalk / safe zone.
ROAD_LANES = [ 140, 200, 404, 500]


def load(path, size):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, size)
    return image


class Vehicle:
    def __init__(self, lane, x, level):
        self.vehicle_sets = [
            [
                load("transpo/car1.png", (90, 45)),
                load("transpo/car3.png", (90, 45))
            ],
            [
                load("transpo/jeepney1.png", (120, 55)),
                load("transpo/jeepney3.png", (120, 55))
            ],
            [
                load("transpo/van1.png", (110, 50)),
                load("transpo/van3.png", (110, 50))
            ]
        ]

        self.images = random.choice(self.vehicle_sets)
        self.frame = 0
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = lane

        self.speed = random.randint(3, 4) + level

    def update(self):
        # move right only
        self.rect.x += self.speed

        # animate image
        self.frame += 0.15
        if self.frame >= len(self.images):
            self.frame = 0

        self.image = self.images[int(self.frame)]

        # reset if it leaves screen
        if self.rect.left > WIDTH:
            self.reset_position()

    def reset_position(self):
        old_lane = self.rect.y

        self.images = random.choice(self.vehicle_sets)
        self.frame = 0
        self.image = self.images[0]

        self.rect = self.image.get_rect()

        # stay on road lane only
        self.rect.y = old_lane

        # respawn far left
        self.rect.x = random.randint(-1200, -400)

        self.speed = random.randint(3, 4)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #hitbox
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

def create_vehicles(level):
    vehicles = []

    for lane in ROAD_LANES:
        vehicles.append(Vehicle(lane, random.randint(-800, -400), level))
        vehicles.append(Vehicle(lane, random.randint(-1500, -900), level))

    return vehicles
