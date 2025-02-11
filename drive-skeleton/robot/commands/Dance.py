from subsystems.driveSubsystem import DriveSubsystems
import commands2
import time

DANCE_SPEED = 0.7
DANCE_WAIT_TIME = 60/122

class Dance(commands2.command.Command):
    def __init__(self, drive: DriveSubsystems):
        self.drive = drive
        self.addRequirements(self.drive)

    def initialize(self):
        self.startTime = time.time()

    def end(self, interrupted: bool):
        pass
    
    def execute(self) -> None:
        if time.time() - self.startTime >= DANCE_WAIT_TIME*2:
            self.startTime = time.time()
            
        elif time.time() - self.startTime >= DANCE_WAIT_TIME*1:
            self.drive.arcadeDrive(-DANCE_SPEED, 0)
        else:
            self.drive.arcadeDrive(DANCE_SPEED, 0)


# HOW TO INSTALL THIS COMMAND:
# Place this file into the "commands" folder
# Allow it to be managed in RobotContainer.py:
#   - add "from commands.Dance import Dance" to the top of the file
#   - In the init function, add "commands2.button.JoystickButton(self.driverController, 5).whileTrue(Dance(self.drive))"
# This will cause the robot to run the Dance command when the LB button is pressed