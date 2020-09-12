# Important: This file is now exec() in the global scope
# Notes:
# - Enabling netplay in an emulator increases its size by ~350KB
# - Enabling profiling in an emulator increases its size by ~75KB
# - Keep at least 32KB free in a partition for future updates
# - Partitions must be 64K aligned

PROJECT_NAME = "Retro-Go"
PROJECT_VER  = shell_exec("git describe --tags --abbrev=5 --dirty")
PROJECT_TILE = "fw-icon.raw"
PROJECT_APPS = {
  # Note: Size will be adjusted if needed but flashmon needs accurate values to work correctly
  # Project name   Sub, Size
  'retro-go':     [16,  524288],
  'nofrendo-go':  [17,  524288],
  'gnuboy-go':    [18,  524288],
  'smsplusgx-go': [19,  589824],
  'huexpress-go': [20,  524288],
  'handy-go':     [21,  458752],
}