

"""
Implementation of the Facade Pattern

In this example:

    We define subsystems (DVDPlayer, Projector, SoundSystem, Lights) with their own methods.
    We create a HomeTheaterFacade class that provides a simplified interface to control all these subsystems together.
"""

# Step 1: Define Subsystems (DVD Player, Projector, Sound System, Lights)

class DVDPlayer:
    def on(self):
        print("DVD Player is on.")

    def play(self, movie: str):
        print(f"Playing movie '{movie}'.")

    def off(self):
        print("DVD Player is off.")

class Projector:
    def on(self):
        print("Projector is on.")

    def set_input(self, input_source: str):
        print(f"Projector input set to '{input_source}'.")

    def off(self):
        print("Projector is off.")

class SoundSystem:
    def on(self):
        print("Sound System is on.")

    def set_volume(self, level: int):
        print(f"Sound System volume set to {level}.")

    def off(self):
        print("Sound System is off.")

class Lights:
    def dim(self, level: int):
        print(f"Lights dimmed to {level}%.")
        
    def on(self):
        print("Lights are on.")


"""
Step 2: Create the Facade (HomeTheaterFacade)

This facade will simplify the interface, providing methods like watch_movie and end_movie to interact with all subsystems at once.
"""

class HomeTheaterFacade:
    def __init__(self, dvd_player: DVDPlayer, projector: Projector, sound_system: SoundSystem, lights: Lights):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system
        self.lights = lights

    def watch_movie(self, movie: str):
        print("\nSetting up the home theater to watch a movie...")
        self.lights.dim(20)
        self.projector.on()
        self.projector.set_input("DVD")
        self.sound_system.on()
        self.sound_system.set_volume(7)
        self.dvd_player.on()
        self.dvd_player.play(movie)
        print("Movie is starting. Enjoy!\n")

    def end_movie(self):
        print("\nShutting down the home theater...")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()
        self.lights.on()
        print("Home theater shut down.\n")

# Usage

# Create instances of each subsystem component
dvd_player = DVDPlayer()
projector = Projector()
sound_system = SoundSystem()
lights = Lights()

# Create the facade
home_theater = HomeTheaterFacade(dvd_player, projector, sound_system, lights)

# Use the facade to start and end the movie experience
home_theater.watch_movie("Inception")
home_theater.end_movie()
