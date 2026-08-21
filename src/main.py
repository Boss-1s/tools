"""
Pythagorean Theorem (and other formulas)

Kind-of simple math programs written in python to speedrun
homework.
The following can currently be used:
Pythagorean Theorem a^2+b^2=c^2
Pythagorean Theorem Right Triangle Validation
Distance Formula (2D & 3D)
Area and circumfrence of a circle
volume of certain obejcts
Rotation Formula (2D)
Quadratic Forumula (Equation, Discriminant, Solutions, and Roots)

(c) 2025-2026 Boss_1s.
This work is licensced under the CC BY-NC-SA 3.0 Int'l Licensce.
To view a copy of the licence, visit creativecommons.org.

v26.8.1
(8/18/2026)  
"""


import warnings, sys, os
try:
  from key_multivalue_storage import Storage
except ImportError:
  Storage = None
try:
  from rich.console import Console
except ImportError:
  Console = None

print(os.name)
print(sys.platform)

if sys.platform == "emscripten":
  print("WARNING: external libraries are not avaliable in sandboxed environments.")


a = ["abc", "cab", "dist", "circle", "volume", "rotate", "quadratic", "mid"]

ans = input("abc, cab, dist, circle, volume, rotate, quadratic, mid: ")

if ans in a:
  with open(ans + ".py", "r") as file:
    code = file.read()
    exec(code)
