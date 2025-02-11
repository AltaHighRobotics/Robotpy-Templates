import math

# Input
kDriverControllerPort = 0
kDeadband = .2
kTurnDeadband = .5

# States
kDefaultObjective = "I"
kDefaultBucket = 0
kDefaultIntake = 0
kDefaultEndStop = -1
kDefaultEndStopOverride = 0

# Swerve
kModuleMaxAngularVelocity = math.tau
kModuleMaxAngularAcceleration = 2*math.tau
kSwerveTurnGearRatio = 2.099982500145832 / 42

# Dimensions
kSwerveModCtrToCtr = .635
kWheelRadius = 0.0508


# Enstops
kOutEndstopPort = 3
kInEndstopPort = 2
kEndstopInversion = True

# Speeds
kBucketSpeed = .9
kIntakeSpeed = .8
kOuttakeSpeed = .4
kSwerveMinSpeed = .3
kSwerveMaxSpeed = 1
kSwerveMaxOutput = .8
# MotorIDs
# Bucket
kBucketID = 9

#Intake
kIntakeLID = 10
kIntakeRID = 11

# Front Left
kFLDriveID = 3
kFLTurnID = 33

# Front Right
kFRDriveID = 4
kFRTurnID = 44

# Back Left
kBLDriveID = 2
kBLTurnID = 22

# Back Right
kBRDriveID = 5
kBRTurnID = 55

# Turn PID
# Front Left
kTurnFLP = 13
kTurnFLI = 0
kTurnFLD = .3

# Front Right
kTurnFRP = kTurnFLP + 0
kTurnFRI = kTurnFLI + 0
kTurnFRD = kTurnFLD + 0

# Back Left
kTurnBLP = kTurnFLP + 0
kTurnBLI = kTurnFLI + 0
kTurnBLD = kTurnFLD + 0

# Back Right
kTurnBRP = kTurnFLP + 0
kTurnBRI = kTurnFLI + 0
kTurnBRD = kTurnFLD + 0

