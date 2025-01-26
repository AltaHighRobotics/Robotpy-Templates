import commands2
import wpilib
import wpilib.drive
import phoenix5 as ctre
import constants

class DriveSubsystems(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        
        #Connects the TalonFX motors to variables depending on their MotorID
        LEFT_MOTOR_1 = ctre.WPI_TalonFX(constants.kLeftMotor1ID)
        LEFT_MOTOR_2 = ctre.WPI_TalonFX(constants.kLeftMotor2ID)
        RIGHT_MOTOR_1 = ctre.WPI_TalonFX(constants.kRightMotor1ID)
        RIGHT_MOTOR_2 = ctre.WPI_TalonFX(constants.kRightMotor2ID)

        #Will cause the motors to stop moving when there is no input/vector controlling the motors
        self.left1 = LEFT_MOTOR_1.setNeutralMode(ctre.NeutralMode.Brake)
        self.left2 = LEFT_MOTOR_2.setNeutralMode(ctre.NeutralMode.Brake)
        self.right1 = RIGHT_MOTOR_1.setNeutralMode(ctre.NeutralMode.Brake)
        self.right2 = RIGHT_MOTOR_2.setNeutralMode(ctre.NeutralMode.Brake)

        #Groups the 2 left and 2 right motors for turning
        self.left = LEFT_SIDE = wpilib.MotorControllerGroup(LEFT_MOTOR_1, LEFT_MOTOR_2)
        self.right = RIGHT_SIDE = wpilib.MotorControllerGroup(RIGHT_MOTOR_1, RIGHT_MOTOR_2)
        
        self.right.setInverted(True)

        self.drive = wpilib.drive.DifferentialDrive(
            self.left,
            self.right,
        )

        self.maxOut = 0.5
        self.setMaxOutput(constants.MAX_SPEED)

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        self.drive.arcadeDrive(fwd, -rot)

    def setMaxOutput(self, maxOutput: float):
        self.maxOut = maxOutput
        self.drive.setMaxOutput(maxOutput)
