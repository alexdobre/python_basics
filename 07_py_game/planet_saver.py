import math
import pygame
from time import sleep
from random import randint


class PlanetSaver:
    GAME_TITLE = 'Planet Saver'
    BACKGROUND_COLOR = (40, 24, 20)
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 800
    CANVAS_CENTER = (400, 400)
    PLANET_RADIUS = 200
    ORBIT_RADIUS = 350
    LASER_BEAM_ACTIVATION_CYCLE = 40
    LASER_BEAM_RESET_CYCLE = 50
    ORBITAL_SIZE = 30
    CYCLE_PAUSE = 0.02
    WINNING_SCORE = 5
    NR_OF_BLISTERS = 3

    running = False
    paused = False
    going_left = False
    going_right = False
    orbital_angle = 0
    orbital_position = (0, 0)
    score = 0
    blister_positions = []
    laser_beam = [(0, 0), (0, 0)]
    laser_beam_active = False
    clock_cycles = 0

    def __init__(self):
        pygame.init()
        self.score_font = pygame.font.Font('freesansbold.ttf', 200)
        self.screen = pygame.display.set_mode((self.CANVAS_WIDTH, self.CANVAS_HEIGHT))
        pygame.display.set_caption(self.GAME_TITLE)
        pygame.display.flip()

    def play_game(self):
        self.__calculate_new_random_blister_positions()

        self.running = True
        while self.running:
            self.__handle_keyboard_inputs()
            if self.paused:
                continue
            self.__update_orbital_position()
            self.__update_laser_beam()
            for i, pos in enumerate(self.blister_positions):
                if self.__laser_beam_hits_blister(pos):
                    random_angle = randint(1, 360)
                    self.blister_positions[i] = self.calculate_position_on_circle(random_angle, self.PLANET_RADIUS + 1,
                                                                                   self.CANVAS_CENTER)
                    self.score = self.score + 1
            self.__draw()
            self.clock_cycles += 1
            sleep(self.CYCLE_PAUSE)
            if self.score == self.WINNING_SCORE:
                self.paused = True
                you_win_image = pygame.image.load('you_win.jpg').convert()
                self.screen.blit(you_win_image, (40, 220))
                pygame.display.flip()

    def __handle_keyboard_inputs(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.__quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # space pauses the game
                    self.paused = not self.paused
                if event.key == pygame.K_ESCAPE:  # escape quits the game
                    self.__quit_game()
                if event.key == pygame.K_LEFT:  # left arrow moves the orbital
                    self.going_left = True
                if event.key == pygame.K_RIGHT:  # right arrow moves the orbital 
                    self.going_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.going_left = False
                if event.key == pygame.K_RIGHT:
                    self.going_right = False

    def __update_orbital_position(self):
        if self.going_left:
            self.orbital_angle = self.orbital_angle - 2
        if self.going_right:
            self.orbital_angle = self.orbital_angle + 2
        self.orbital_position = self.calculate_position_on_circle(self.orbital_angle, self.ORBIT_RADIUS,
                                                                  self.CANVAS_CENTER)

    def __calculate_new_random_blister_positions(self):
        new_blister_positions = []
        for i in range(self.NR_OF_BLISTERS):
            random_angle = randint(1, 360)
            new_blister_positions.append(self.calculate_position_on_circle(random_angle, self.PLANET_RADIUS + 1,
                                                                       self.CANVAS_CENTER))
        self.blister_positions = new_blister_positions

    def __update_laser_beam(self):
        if self.clock_cycles > self.LASER_BEAM_ACTIVATION_CYCLE:
            self.laser_beam_active = True
            planet_impact_position = self.calculate_position_on_circle(self.orbital_angle, self.PLANET_RADIUS,
                                                                       self.CANVAS_CENTER)
            self.laser_beam[0] = planet_impact_position
            orbital_center = (self.orbital_position[0] + self.ORBITAL_SIZE / 2,
                              self.orbital_position[1] + self.ORBITAL_SIZE / 2)
            self.laser_beam[1] = orbital_center
        if self.clock_cycles == self.LASER_BEAM_RESET_CYCLE:
            self.laser_beam_active = False
            self.clock_cycles = 0

    def __laser_beam_hits_blister(self, pos):
        laser_beam_planet_impact = self.laser_beam[0]
        return ((pos[0] >= laser_beam_planet_impact[0] - 20) and
                (pos[0] <= laser_beam_planet_impact[0] + 20) and
                (pos[1] >= laser_beam_planet_impact[1] - 20) and
                (pos[1] <= laser_beam_planet_impact[1] + 20))

    def __draw(self):
        self.screen.fill(self.BACKGROUND_COLOR)
        score_text = self.score_font.render(str(self.score), True, (200, 200, 200))
        text_rectangle = score_text.get_rect()
        text_rectangle.center = (self.CANVAS_WIDTH / 2, 100)
        self.screen.blit(score_text, text_rectangle)
        for pos in self.blister_positions:
            pygame.draw.circle(self.screen, (0, 0, 255), pos, 10)
        if self.laser_beam_active:
            pygame.draw.line(self.screen, (0, 255, 0), self.laser_beam[0], self.laser_beam[1])
        pygame.draw.circle(self.screen, (255, 0, 0), self.CANVAS_CENTER, self.PLANET_RADIUS)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(*self.orbital_position, 30, 30))
        pygame.display.flip()

    def __quit_game(self):
        pygame.quit()
        self.paused = True
        self.running = False

    @staticmethod
    def calculate_position_on_circle(angle, radius, center_point):
        theta = math.radians(angle)
        return center_point[0] + radius * math.cos(theta), center_point[1] + radius * math.sin(theta)


if __name__ == '__main__':
    PlanetSaver().play_game()
