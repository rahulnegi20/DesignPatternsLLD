
# Step 1: Define the Command Interface

"""
it separates the object that invokes an operation from the object that knows how to execute it.
"""

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# Step 2: Create Receiver Classe


class Light:
    def turn_on(self) -> None:
        print("Light is turned ON")

    def turn_off(self) -> None:
        print("Light is turned OFF")

class Fan:
    def start(self) -> None:
        print("Fan is started")

    def stop(self) -> None:
        print("Fan is stopped")



# Step 3: Create Concrete Command Classes

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()

class FanOnCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self) -> None:
        self.fan.start()

class FanOffCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self) -> None:
        self.fan.stop()


# Step 4: Create the Invoker (RemoteControl)

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command) -> None:
        self.command = command

    def press_button(self) -> None:
        if self.command:
            self.command.execute()


# USAGE 


# Create receivers
light = Light()
fan = Fan()

# Create command objects
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)
fan_on_command = FanOnCommand(fan)
fan_off_command = FanOffCommand(fan)

# Create remote control and set commands
remote = RemoteControl()

# Turn on the light
remote.set_command(light_on_command)
remote.press_button()

# Turn off the light
remote.set_command(light_off_command)
remote.press_button()

# Start the fan
remote.set_command(fan_on_command)
remote.press_button()

# Stop the fan
remote.set_command(fan_off_command)
remote.press_button()
