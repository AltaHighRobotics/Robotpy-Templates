from subsystems.driveSubsystem import DriveSubsystems
import commands2
import time

SLITHER_SPEED = 0.7
ROTATION_AMOUNT = 45 #Degrees

class Slither(commands2.command.Command):
    def __init__(self, drive: DriveSubsystems):
        self.drive = drive
        self.addRequirements(self.drive)

    def initialize(self):
        self.startTime = time.time()
    
    def execute(self) -> None:
        if time.time() - self.startTime >= 1:
            self.startTime = time.time()
        elif time.time() - self.startTime >= 0.5:
            self.drive.arcadeDrive(SLITHER_SPEED, ROTATION_AMOUNT)
        else:
            self.drive.arcadeDrive(SLITHER_SPEED, -ROTATION_AMOUNT)


# HOW TO INSTALL THIS COMMAND:
# Place this file into the "commands" folder
# Allow it to be managed in RobotContainer.py:
#   - add "from commands.Sneke import Slither" to the top of the file
#   - In the init function, add "commands2.button.JoystickButton(self.driverController, 6).whileTrue(Slither(self.drive))"
# This will cause the robot to run the Dance command when the RB button is pressed