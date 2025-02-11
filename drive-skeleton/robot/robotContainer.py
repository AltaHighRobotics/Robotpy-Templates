#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
from commands.forward import DefaultDrive
from subsystems.driveSubsystem import DriveSubsystems
# from subsystems.aprilTagSubsystem import AprilTagSubsystem
import constants
import wpilib
from commands.Dance import Dance
from commands.Sneke import Slither
import constants
import commands2

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        # The driver's controller
        self.driverController = wpilib.XboxController(constants.kDriverControllerPort)
        #self.driverController = wpilib.Joystick(constants.kDriverControllerPort)

        # The robot's subsystems
        self.drive = DriveSubsystems()

        # self.vision = AprilTagSubsystem()

        # set up default drive command
        self.drive.setDefaultCommand(
            DefaultDrive(
                self.drive,
                lambda: self.driverController.getRightTriggerAxis() - self.driverController.getLeftTriggerAxis(),
                lambda: min(1, max(-1, self.driverController.getLeftX() + self.driverController.getRightX())),
                lambda: 1
            )
        )
        
        ## JOYSTICK INPUT ##
        # commands2.button.JoystickButton(self.driverController, <<JOYSTICKBUTTON>>).whileTrue(<<COMMAND>>(self.drive))
        # Will activate the command as long as you are holding the button
        # e.g. -> commands2.button.JoystickButton(self.driverController, 5).whileTrue(Dance(self.drive)) will cause the robot to run the "Dance" command when you hold down RB
        
        # Button list
        commands2.button.JoystickButton(self.driverController, 5).whileTrue(Dance(self.drive))
        commands2.button.JoystickButton(self.driverController, 6).whileTrue(Slither(self.drive))

    def getAutonomousCommand(self) -> str:
        return None
