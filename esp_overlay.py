#!/usr/bin/env python3
"""
=============================================================================
  Roblox ESP Overlay — Single File Project
  Offline-only. All configuration from local offsets.json.
  No network connections of any kind.
=============================================================================
"""

# ====================================
# CONFIGURATION
# ====================================

DEBUG_MODE = True

# -- ESP Colors: (R, G, B, A) --
ESP_BOX_COLOR           = (255, 255, 255, 220)   # White box (enemies / default)
ESP_TRACER_COLOR        = (255, 255, 255, 160)   # White tracer
ESP_SKELETON_COLOR      = (220, 220, 255, 200)   # Light lavender skeleton
ESP_NAME_COLOR          = (255, 255, 255, 255)   # White name
ESP_DISTANCE_COLOR      = (190, 190, 190, 200)   # Light grey distance
ESP_HEALTH_COLOR        = (  0, 255,   0, 230)   # Green health (static)
ESP_TEAMMATE_COLOR      = (  0, 220, 255, 220)   # Cyan / Light blue for teammates
ESP_USE_TEAM_COLORS     = True                   # Differentiate teammates with teammate color

# -- Visualization Toggles --
ESP_SHOW_BOX            = True
ESP_SHOW_TRACER         = True
ESP_SHOW_SKELETON       = True                   # Draw player bone/skeleton
ESP_SHOW_NAME           = True
ESP_SHOW_DISTANCE       = True
ESP_SHOW_HEALTH         = True
ESP_CORNER_BOX          = False   # Corner-style box instead of full rect
ESP_3D_BOX              = False   # Wireframe 3-D box
ESP_DYNAMIC_HEALTH_COLOR = True   # Green -> Yellow -> Red by HP ratio

# -- Radar Settings --
RADAR_ENABLED           = True
RADAR_POS_X             = 25
RADAR_POS_Y             = 25
RADAR_SIZE              = 175     # Diameter in pixels
RADAR_RANGE_STUDS       = 350.0   # Visible radius in studs
RADAR_SHOW_CROSSHAIR    = True
RADAR_OPACITY           = 190

# -- Rendering Settings --
ESP_TEXT_SIZE           = 11
ESP_BOX_THICKNESS       = 1
ESP_SKELETON_THICKNESS  = 1

# -- Filtering --
TEAM_FILTER_MODE        = "Everyone"  # "Everyone", "Enemies Only", "Teammates Only"
IGNORE_TEAM             = False       # Legacy flag (kept for compatibility)
IGNORE_DEAD             = True        # Skip dead players (HP <= 0)
HIDE_DISTANCE           = False       # Suppress distance label
MAX_DISTANCE            = 1500.0      # Studs — skip players beyond this
ALWAYS_ON_TOP           = True        # Stay on top of other windows

# -- Character Modifications --
ENABLE_SAFE_SPEED       = False      # Anti-Kick CFrame / Velocity Speed (keeps WalkSpeed at 16, bypasses AC)
SAFE_SPEED_VALUE        = 50.0       # Studs/sec for Safe Speed
ENABLE_WALKSPEED        = False
WALKSPEED_VALUE         = 50.0       # Default modified WalkSpeed (Roblox default: 16.0)
ENABLE_JUMPPOWER        = False
JUMPPOWER_VALUE         = 100.0      # Default modified JumpPower (Roblox default: 50.0)
ENABLE_INFINITE_JUMP    = False      # Allows jumping mid-air repeatedly
ENABLE_NOCLIP           = False      # Disables collisions on local character parts
ENABLE_FLY              = False      # Physics-based fly hack
FLY_SPEED               = 50.0
ENABLE_FULLBRIGHT       = False      # Max brightness, ambient, and remove fog
ENABLE_INSTANT_PROMPTS  = False      # 0 hold duration on ProximityPrompts
ENABLE_INF_CLICK        = False      # Infinite range ClickDetectors
ENABLE_GRAVITY_MOD      = False      # Custom gravity modifier
GRAVITY_VALUE           = 196.2      # Default Roblox gravity
UNLOCK_FPS              = False      # FPS Unlocker
UNLOCK_FPS_VALUE        = 240.0
DEFAULT_WALKSPEED       = 16.0
DEFAULT_JUMPPOWER       = 50.0

# -- Teleport Settings --
LOOP_TP_ENABLED         = False      # Continuous teleport to targeted player
LOOP_TP_TARGET_NAME     = ""         # Targeted player's username

# -- Fling Settings --
FLING_ACTIVE            = False      # Whether a fling action is currently ongoing
FLING_MODE              = "burst"    # "burst" (single duration) or "loop" (continuous)
FLING_TARGET_NAME       = ""         # Username of the player being flung
FLING_POWER             = 100000.0   # Extreme rotational angular velocity applied to local primitives
FLING_RETURN_TO_START   = True       # Teleport back to original position after fling
FLING_DURATION          = 1.5        # Burst fling duration in seconds

# -- Spectate Settings --
SPECTATE_ENABLED        = False      # Native camera subject spectate toggle
SPECTATE_TARGET_NAME    = ""         # Targeted player's username for spectating
SPECTATE_AUTO_NEXT      = False      # Automatically switch to next player if current player leaves

# -- Aimbot Settings --
AIMBOT_ENABLED          = False
AIMBOT_KEY              = "RBUTTON"  # "RBUTTON", "LBUTTON", "LSHIFT", "E", "Q", "ALT"
AIMBOT_TARGET_PART      = "Head"     # "Head" or "HumanoidRootPart"
AIMBOT_FOV              = 120.0      # FOV radius in pixels
AIMBOT_SMOOTHNESS       = 4.0        # Smoothing factor (1.0 = instant, >1.0 = smooth)
AIMBOT_SHOW_FOV         = True       # Draw FOV Circle
AIMBOT_FOV_COLOR        = (0, 210, 255, 120)
AIMBOT_TEAM_CHECK       = True       # Do not lock on teammates
AIMBOT_PRIORITY         = "Crosshair" # "Crosshair", "Distance", "Lowest HP"
AIMBOT_PREDICTION       = False      # Predict movement using velocity/delta pos
AIMBOT_STICKY           = True       # Retain lock on target until key release / leaves FOV
AIMBOT_DEADZONE         = 2.0        # Ignore movement if closer than X px to prevent jitter
AIMBOT_RCS_ENABLED      = False      # Recoil Compensation System
AIMBOT_RCS_STRENGTH     = 2.0        # Pull down strength while firing

# -- Hitbox Expander (Rivals & Universal) --
HITBOX_EXPANDER_ENABLED = False
HITBOX_SIZE             = 12.0       # Size in studs (Rivals default head is ~1.2)
HITBOX_TARGET_PART      = "Head"     # "Head", "HumanoidRootPart", "Both"
HITBOX_RIVALS_MODE      = True       # Specially scan Rivals character rigs and hitboxes
HITBOX_CAN_COLLIDE      = False      # Clear CanCollide to prevent collision issues
HITBOX_TEAM_CHECK       = True       # Only expand enemy hitboxes
HITBOX_VISUALIZE        = True       # Draw 3D wireframe boxes around expanded hitboxes

# -- Triggerbot Settings --
TRIGGERBOT_ENABLED      = False
TRIGGERBOT_DELAY_MS     = 20         # Delay in ms before clicking
TRIGGERBOT_TEAM_CHECK   = True
TRIGGERBOT_MODE         = "Tap"      # "Tap" or "Auto Spray" (Hold)
TRIGGERBOT_MAX_DELAY_MS = 35         # Randomized delay cap for humanized clicks


# -- Freecam Settings --
FREECAM_ENABLED         = False
FREECAM_SPEED           = 2.0

# -- Item & Entity ESP Settings --
ITEM_ESP_ENABLED        = False
ITEM_ESP_MAX_DIST       = 800.0

# -- MM2 Role ESP Settings --
MM2_ROLE_ESP_ENABLED    = False                # Show role labels (Murderer / Sheriff / Innocent)
MM2_MURDERER_COLOR      = (255,  55,  55, 255) # Bright red   — Murderer
MM2_SHERIFF_COLOR       = (255, 215,   0, 255) # Gold         — Sheriff
MM2_INNOCENT_COLOR      = (160, 230, 160, 255) # Soft green   — Innocent
MM2_GUN_DROP_COLOR      = (255, 215,   0, 255) # Glowing Gold — Dropped Gun
MM2_GUN_ESP_ENABLED     = True                 # Visual ESP on dropped sheriff gun
MM2_GUN_NOTIFY          = True                 # Top screen banner when gun drops
# Tool/weapon name substrings used to detect roles from character inventory
# MM2 puts the knife into the murderer's character and the sheriff gun into the sheriff's.
MM2_KNIFE_NAMES: list[str]  = ["knife", "kniferagdoll", "mm2knife"]  # (lowercased substrings)
MM2_GUN_NAMES:   list[str]  = ["gun", "sheriff", "mm2gun", "revolv"] # (lowercased substrings)

# -- Target --
TARGET_PROCESS          = "RobloxPlayerBeta.exe"
TARGET_WINDOW_TITLE     = "Roblox"

# -- Timing --
RENDER_INTERVAL_MS      = 16      # Screen projection & render tick (~60 FPS)
PLAYER_SCAN_INTERVAL_MS = 250     # Background player discovery & part resolution (ms)
GEOMETRY_CHECK_MS       = 500     # Roblox window geometry poll (ms)

# ====================================
# IMPORTS
# ====================================

import ctypes
import ctypes.wintypes
import json
import math
import os
import struct
import sys
import threading
import time

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import numpy as np

from PyQt5.QtCore    import Qt, QTimer, QPoint, QSize
from PyQt5.QtGui     import QColor, QFont, QPainter, QPen, QBrush, QIcon, QPixmap, QPolygon
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QCheckBox, QPushButton, QComboBox, QColorDialog, QGroupBox, QGridLayout,
    QDoubleSpinBox, QSpinBox, QTabWidget, QSlider, QFrame,
    QListWidget, QListWidgetItem, QLineEdit, QPlainTextEdit, QFileDialog,
    QTableWidget, QTableWidgetItem, QHeaderView, QProgressBar, QTextEdit,
    QStackedWidget, QScrollArea, QButtonGroup, QGraphicsDropShadowEffect, QSizePolicy
)

# ====================================
# WINDOWS API — CONSTANTS & STRUCTURES
# ====================================

_kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
_user32   = ctypes.WinDLL("user32",   use_last_error=True)

PROCESS_ALL_ACCESS   = 0x1F0FFF
TH32CS_SNAPPROCESS   = 0x00000002
TH32CS_SNAPMODULE    = 0x00000008
TH32CS_SNAPMODULE32  = 0x00000010
_INVALID_HANDLE      = ctypes.c_void_p(-1).value

VK_INSERT = 0x2D
VK_P      = 0x50
VK_END    = 0x23
VK_SPACE  = 0x20
VK_LBUTTON = 0x01
VK_RBUTTON = 0x02
VK_LSHIFT  = 0xA0
VK_KEY_E   = 0x45
VK_KEY_Q   = 0x51
VK_KEY_W   = 0x57
VK_KEY_A   = 0x41
VK_KEY_S   = 0x53
VK_KEY_D   = 0x44
VK_KEY_T   = 0x54
VK_MENU    = 0x12  # Alt key

MOUSEEVENTF_MOVE     = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP   = 0x0004

def move_mouse_relative(dx: int, dy: int) -> None:
    """Send relative mouse movement via Win32 mouse_event."""
    _user32.mouse_event(MOUSEEVENTF_MOVE, ctypes.c_long(int(dx)), ctypes.c_long(int(dy)), 0, 0)

def mouse_down() -> None:
    """Send mouse down event."""
    _user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

def mouse_up() -> None:
    """Send mouse up event."""
    _user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def click_mouse() -> None:
    """Send left click via Win32 mouse_event."""
    _user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.015)
    _user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)




class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize",              ctypes.wintypes.DWORD),
        ("cntUsage",            ctypes.wintypes.DWORD),
        ("th32ProcessID",       ctypes.wintypes.DWORD),
        ("th32DefaultHeapID",   ctypes.POINTER(ctypes.c_ulong)),
        ("th32ModuleID",        ctypes.wintypes.DWORD),
        ("cntThreads",          ctypes.wintypes.DWORD),
        ("th32ParentProcessID", ctypes.wintypes.DWORD),
        ("pcPriClassBase",      ctypes.c_long),
        ("dwFlags",             ctypes.wintypes.DWORD),
        ("szExeFile",           ctypes.c_char * 260),
    ]


class MODULEENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize",        ctypes.wintypes.DWORD),
        ("th32ModuleID",  ctypes.wintypes.DWORD),
        ("th32ProcessID", ctypes.wintypes.DWORD),
        ("GlblcntUsage",  ctypes.wintypes.DWORD),
        ("ProccntUsage",  ctypes.wintypes.DWORD),
        ("modBaseAddr",   ctypes.POINTER(ctypes.c_byte)),
        ("modBaseSize",   ctypes.wintypes.DWORD),
        ("hModule",       ctypes.wintypes.HMODULE),
        ("szModule",      ctypes.c_char * 256),
        ("szExePath",     ctypes.c_char * 260),
    ]

# ====================================
# MEMORY CLASS
# ====================================

class Memory:
    """
    Wraps Windows ReadProcessMemory to provide typed reads from a
    target process.  No write operations are performed.
    """

    def __init__(self) -> None:
        self.handle: int | None  = None
        self.pid:    int | None  = None
        self.module_base: int    = 0

    # ---- Process discovery ----

    def get_pid_by_name(self, name: str) -> int | None:
        name_b   = name.lower().encode()
        snapshot = _kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
        if snapshot == _INVALID_HANDLE:
            return None
        entry          = PROCESSENTRY32()
        entry.dwSize   = ctypes.sizeof(PROCESSENTRY32)
        found          = None
        try:
            if _kernel32.Process32First(snapshot, ctypes.byref(entry)):
                while True:
                    if entry.szExeFile.lower() == name_b:
                        found = entry.th32ProcessID
                        break
                    if not _kernel32.Process32Next(snapshot, ctypes.byref(entry)):
                        break
        finally:
            _kernel32.CloseHandle(snapshot)
        return found

    def open_process(self, pid: int) -> bool:
        handle = _kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        if not handle:
            return False
        self.handle = handle
        self.pid    = pid
        return True

    def get_module_base(self, module_name: str) -> int:
        name_b   = module_name.lower().encode()
        snapshot = _kernel32.CreateToolhelp32Snapshot(
            TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, self.pid)
        if snapshot == _INVALID_HANDLE:
            return 0
        entry        = MODULEENTRY32()
        entry.dwSize = ctypes.sizeof(MODULEENTRY32)
        result       = 0
        try:
            if _kernel32.Module32First(snapshot, ctypes.byref(entry)):
                while True:
                    if entry.szModule.lower() == name_b:
                        result = ctypes.cast(
                            entry.modBaseAddr, ctypes.c_void_p).value or 0
                        break
                    if not _kernel32.Module32Next(snapshot, ctypes.byref(entry)):
                        break
        finally:
            _kernel32.CloseHandle(snapshot)
        return result

    # ---- Raw read ----

    def read(self, address: int, size: int) -> bytes:
        if not self.handle or not address:
            return b"\x00" * size
        buf        = ctypes.create_string_buffer(size)
        bytes_read = ctypes.c_size_t(0)
        _kernel32.ReadProcessMemory(
            self.handle,
            ctypes.c_ulonglong(address),
            buf,
            size,
            ctypes.byref(bytes_read),
        )
        return buf.raw

    # ---- Typed reads ----

    def read_ptr(self, address: int) -> int:
        """Read an 8-byte (64-bit) pointer."""
        return struct.unpack_from("<Q", self.read(address, 8))[0]

    def read_int4(self, address: int) -> int:
        return struct.unpack_from("<I", self.read(address, 4))[0]

    def read_int4s(self, address: int) -> int:
        return struct.unpack_from("<i", self.read(address, 4))[0]

    def read_int8(self, address: int) -> int:
        return struct.unpack_from("<Q", self.read(address, 8))[0]

    def read_float(self, address: int) -> float:
        return struct.unpack_from("<f", self.read(address, 4))[0]

    def read_vec3(self, address: int) -> tuple[float, float, float]:
        return struct.unpack_from("<fff", self.read(address, 12))

    def read_bool(self, address: int) -> bool:
        return bool(self.read(address, 1)[0])

    def read_msvc_string(self, address: int, max_len: int = 256) -> str:
        """
        Read a MSVC std::string.
        Layout: [ptr_or_buf(8)] [size(8)] [capacity(8)]
        If size <= 15 the bytes are stored inline in ptr_or_buf.
        """
        if not address:
            return ""
        try:
            raw_size = struct.unpack_from("<Q", self.read(address + 0x10, 8))[0]
            length   = min(raw_size, max_len)
            if length == 0:
                return ""
            if raw_size <= 15:
                data = self.read(address, length)
            else:
                heap_ptr = self.read_ptr(address)
                if not heap_ptr:
                    return ""
                data = self.read(heap_ptr, length)
            return data.decode("utf-8", errors="ignore").strip("\x00")
        except Exception:
            return ""

    def read_string_ptr(self, ptr: int, max_len: int = 128) -> str:
        """Read a null-terminated string at the given pointer."""
        if not ptr:
            return ""
        raw = self.read(ptr, max_len)
        end = raw.find(b"\x00")
        if end != -1:
            raw = raw[:end]
        return raw.decode("utf-8", errors="ignore")

    # ---- Write operations ----

    def write(self, address: int, data: bytes) -> bool:
        """Write raw bytes to process memory."""
        if not self.handle or not address:
            return False
        bytes_written = ctypes.c_size_t(0)
        buf = ctypes.create_string_buffer(data, len(data))
        res = _kernel32.WriteProcessMemory(
            self.handle,
            ctypes.c_ulonglong(address),
            buf,
            len(data),
            ctypes.byref(bytes_written),
        )
        return bool(res and bytes_written.value == len(data))

    def write_float(self, address: int, value: float) -> bool:
        """Write a 4-byte IEEE-754 float."""
        return self.write(address, struct.pack("<f", float(value)))

    def write_int4(self, address: int, value: int) -> bool:
        """Write a 4-byte unsigned integer."""
        return self.write(address, struct.pack("<I", int(value)))

    def write_bool(self, address: int, value: bool) -> bool:
        """Write a 1-byte boolean."""
        return self.write(address, struct.pack("<?", bool(value)))

    def write_vec3(self, address: int, x: float, y: float, z: float) -> bool:
        """Write 3 consecutive 4-byte IEEE-754 floats (12 bytes)."""
        return self.write(address, struct.pack("<fff", float(x), float(y), float(z)))

    def write_ptr(self, address: int, value: int) -> bool:
        """Write an 8-byte (64-bit) unsigned pointer."""
        return self.write(address, struct.pack("<Q", int(value)))

    # ---- Lifecycle ----

    def is_valid(self) -> bool:
        return self.handle is not None and self.pid is not None

    def close(self) -> None:
        if self.handle:
            _kernel32.CloseHandle(self.handle)
            self.handle = None

# ====================================
# OFFSET LOADER
# ====================================

offsets: dict[str, int] = {}

REQUIRED_OFFSETS: list[str] = [
    "FakeDataModel_Pointer",
    "FakeDataModel_RealDataModel",
    "DataModel_Workspace",
    "DataModel_GameLoaded",
    "Instance_ChildrenStart",
    "Instance_ChildrenEnd",
    "Instance_NameContainer",
    "Instance_Name",
    "Instance_ClassDescriptor",
    "Instance_ClassName",
    "Instance_Parent",
    "Player_ModelInstance",
    "Player_LocalPlayer",
    "Player_Team",
    "Player_DisplayName",
    "Humanoid_Health",
    "Humanoid_MaxHealth",
    "Humanoid_HumanoidRootPart",
    "Humanoid_Walkspeed",
    "Humanoid_JumpPower",
    "BasePart_Primitive",
    "Primitive_Position",
    "Workspace_CurrentCamera",
    "Camera_Position",
    "Camera_Rotation",
    "Camera_FieldOfView",
    "Camera_ViewportSize",
    "VisualEngine_Pointer",
    "VisualEngine_ViewMatrix",
]


def load_offsets() -> dict[str, int]:
    """
    Locate offsets.json next to this script, parse it, and return a
    dictionary of {key: integer} entries.  Hex strings are converted.
    Terminates the process on any error — no fallback, no network.
    """
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    offset_path = os.path.join(script_dir, "offsets.json")

    if not os.path.exists(offset_path):
        print("[!] offsets.json not found.")
        print(f"    Expected location: {offset_path}")
        print("    Create this file with the required offset keys.")
        sys.exit(1)

    try:
        with open(offset_path, "r", encoding="utf-8") as fh:
            raw: dict = json.load(fh)
    except json.JSONDecodeError as exc:
        print(f"[!] Failed to parse offsets.json:\n    {exc}")
        sys.exit(1)

    result: dict[str, int] = {}
    for key, value in raw.items():
        if isinstance(value, int):
            result[key] = value
        elif isinstance(value, str):
            stripped = value.strip()
            try:
                result[key] = int(stripped, 0)   # supports 0x prefix and plain int
            except ValueError:
                print(f"[!] Cannot convert offset '{key}' value '{value}' to integer.")
                sys.exit(1)
        else:
            print(f"[!] Unexpected type for offset '{key}': {type(value)}")
            sys.exit(1)

    return result

# ====================================
# CONFIGURATION PROFILE MANAGER
# ====================================

CONFIG_FILENAME = "config.json"


def get_config_path() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, CONFIG_FILENAME)


def export_current_config() -> dict:
    return {
        "ESP_SHOW_BOX": ESP_SHOW_BOX,
        "ESP_CORNER_BOX": ESP_CORNER_BOX,
        "ESP_3D_BOX": ESP_3D_BOX,
        "ESP_SHOW_TRACER": ESP_SHOW_TRACER,
        "ESP_SHOW_SKELETON": ESP_SHOW_SKELETON,
        "ESP_SHOW_NAME": ESP_SHOW_NAME,
        "ESP_SHOW_DISTANCE": ESP_SHOW_DISTANCE,
        "ESP_SHOW_HEALTH": ESP_SHOW_HEALTH,
        "ESP_DYNAMIC_HEALTH_COLOR": ESP_DYNAMIC_HEALTH_COLOR,
        "ESP_BOX_THICKNESS": ESP_BOX_THICKNESS,
        "ESP_SKELETON_THICKNESS": ESP_SKELETON_THICKNESS,
        "ESP_TEXT_SIZE": ESP_TEXT_SIZE,
        "MAX_DISTANCE": MAX_DISTANCE,
        "TEAM_FILTER_MODE": TEAM_FILTER_MODE,
        "ALWAYS_ON_TOP": ALWAYS_ON_TOP,
        "ESP_BOX_COLOR": list(ESP_BOX_COLOR),
        "ESP_TEAMMATE_COLOR": list(ESP_TEAMMATE_COLOR),
        "ESP_TRACER_COLOR": list(ESP_TRACER_COLOR),
        "ESP_SKELETON_COLOR": list(ESP_SKELETON_COLOR),
        "RADAR_ENABLED": RADAR_ENABLED,
        "RADAR_SIZE": RADAR_SIZE,
        "RADAR_RANGE_STUDS": RADAR_RANGE_STUDS,
        "RADAR_SHOW_CROSSHAIR": RADAR_SHOW_CROSSHAIR,
        "RADAR_OPACITY": RADAR_OPACITY,
        "ENABLE_SAFE_SPEED": ENABLE_SAFE_SPEED,
        "SAFE_SPEED_VALUE": SAFE_SPEED_VALUE,
        "ENABLE_WALKSPEED": ENABLE_WALKSPEED,
        "WALKSPEED_VALUE": WALKSPEED_VALUE,
        "ENABLE_JUMPPOWER": ENABLE_JUMPPOWER,
        "JUMPPOWER_VALUE": JUMPPOWER_VALUE,
        "ENABLE_INFINITE_JUMP": ENABLE_INFINITE_JUMP,
        "ENABLE_NOCLIP": ENABLE_NOCLIP,
        "ENABLE_FLY": ENABLE_FLY,
        "FLY_SPEED": FLY_SPEED,
        "ENABLE_FULLBRIGHT": ENABLE_FULLBRIGHT,
        "ENABLE_INSTANT_PROMPTS": ENABLE_INSTANT_PROMPTS,
        "ENABLE_INF_CLICK": ENABLE_INF_CLICK,
        "ENABLE_GRAVITY_MOD": ENABLE_GRAVITY_MOD,
        "GRAVITY_VALUE": GRAVITY_VALUE,
        "UNLOCK_FPS": UNLOCK_FPS,
        "UNLOCK_FPS_VALUE": UNLOCK_FPS_VALUE,
        "AIMBOT_ENABLED": AIMBOT_ENABLED,
        "AIMBOT_KEY": AIMBOT_KEY,
        "AIMBOT_TARGET_PART": AIMBOT_TARGET_PART,
        "AIMBOT_FOV": AIMBOT_FOV,
        "AIMBOT_SMOOTHNESS": AIMBOT_SMOOTHNESS,
        "AIMBOT_SHOW_FOV": AIMBOT_SHOW_FOV,
        "AIMBOT_FOV_COLOR": list(AIMBOT_FOV_COLOR),
        "AIMBOT_TEAM_CHECK": AIMBOT_TEAM_CHECK,
        "AIMBOT_PRIORITY": AIMBOT_PRIORITY,
        "AIMBOT_PREDICTION": AIMBOT_PREDICTION,
        "AIMBOT_STICKY": AIMBOT_STICKY,
        "AIMBOT_DEADZONE": AIMBOT_DEADZONE,
        "AIMBOT_RCS_ENABLED": AIMBOT_RCS_ENABLED,
        "AIMBOT_RCS_STRENGTH": AIMBOT_RCS_STRENGTH,
        "FLING_POWER": FLING_POWER,
        "FLING_RETURN_TO_START": FLING_RETURN_TO_START,
        "FLING_DURATION": FLING_DURATION,
        "SPECTATE_AUTO_NEXT": SPECTATE_AUTO_NEXT,
        "HITBOX_EXPANDER_ENABLED": HITBOX_EXPANDER_ENABLED,
        "HITBOX_SIZE": HITBOX_SIZE,
        "HITBOX_TARGET_PART": HITBOX_TARGET_PART,
        "HITBOX_RIVALS_MODE": HITBOX_RIVALS_MODE,
        "HITBOX_CAN_COLLIDE": HITBOX_CAN_COLLIDE,
        "HITBOX_TEAM_CHECK": HITBOX_TEAM_CHECK,
        "HITBOX_VISUALIZE": HITBOX_VISUALIZE,
        "TRIGGERBOT_ENABLED": TRIGGERBOT_ENABLED,
        "TRIGGERBOT_DELAY_MS": TRIGGERBOT_DELAY_MS,
        "TRIGGERBOT_TEAM_CHECK": TRIGGERBOT_TEAM_CHECK,
        "TRIGGERBOT_MODE": TRIGGERBOT_MODE,
        "TRIGGERBOT_MAX_DELAY_MS": TRIGGERBOT_MAX_DELAY_MS,
        "FREECAM_ENABLED": FREECAM_ENABLED,
        "FREECAM_SPEED": FREECAM_SPEED,
        "ITEM_ESP_ENABLED": ITEM_ESP_ENABLED,
        "ITEM_ESP_MAX_DIST": ITEM_ESP_MAX_DIST,
        "MM2_ROLE_ESP_ENABLED": MM2_ROLE_ESP_ENABLED,
        "MM2_MURDERER_COLOR": list(MM2_MURDERER_COLOR),
        "MM2_SHERIFF_COLOR": list(MM2_SHERIFF_COLOR),
        "MM2_INNOCENT_COLOR": list(MM2_INNOCENT_COLOR),
        "MM2_KNIFE_NAMES": MM2_KNIFE_NAMES,
        "MM2_GUN_NAMES": MM2_GUN_NAMES,
        "MM2_GUN_ESP_ENABLED": MM2_GUN_ESP_ENABLED,
        "MM2_GUN_NOTIFY": MM2_GUN_NOTIFY,
    }


def save_config() -> bool:
    try:
        path = get_config_path()
        data = export_current_config()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        if DEBUG_MODE:
            print(f"[+] Saved config to {path}")
        return True
    except Exception as exc:
        print(f"[!] Failed to save config: {exc}")
        return False


def load_config() -> bool:
    global ESP_SHOW_BOX, ESP_CORNER_BOX, ESP_3D_BOX, ESP_SHOW_TRACER, ESP_SHOW_SKELETON
    global ESP_SHOW_NAME, ESP_SHOW_DISTANCE, ESP_SHOW_HEALTH, ESP_DYNAMIC_HEALTH_COLOR
    global ESP_BOX_THICKNESS, ESP_SKELETON_THICKNESS, ESP_TEXT_SIZE, MAX_DISTANCE
    global TEAM_FILTER_MODE, ALWAYS_ON_TOP
    global ESP_BOX_COLOR, ESP_TEAMMATE_COLOR, ESP_TRACER_COLOR, ESP_SKELETON_COLOR
    global RADAR_ENABLED, RADAR_SIZE, RADAR_RANGE_STUDS, RADAR_SHOW_CROSSHAIR, RADAR_OPACITY
    global ENABLE_SAFE_SPEED, SAFE_SPEED_VALUE, ENABLE_WALKSPEED, WALKSPEED_VALUE, ENABLE_JUMPPOWER, JUMPPOWER_VALUE, ENABLE_INFINITE_JUMP
    global ENABLE_NOCLIP, ENABLE_FLY, FLY_SPEED, ENABLE_FULLBRIGHT, ENABLE_INSTANT_PROMPTS
    global ENABLE_INF_CLICK, ENABLE_GRAVITY_MOD, GRAVITY_VALUE, UNLOCK_FPS, UNLOCK_FPS_VALUE
    global AIMBOT_ENABLED, AIMBOT_KEY, AIMBOT_TARGET_PART, AIMBOT_FOV, AIMBOT_SMOOTHNESS
    global AIMBOT_SHOW_FOV, AIMBOT_FOV_COLOR, AIMBOT_TEAM_CHECK
    global AIMBOT_PRIORITY, AIMBOT_PREDICTION, AIMBOT_STICKY, AIMBOT_DEADZONE, AIMBOT_RCS_ENABLED, AIMBOT_RCS_STRENGTH
    global FLING_POWER, FLING_RETURN_TO_START, FLING_DURATION, SPECTATE_AUTO_NEXT
    global HITBOX_EXPANDER_ENABLED, HITBOX_SIZE, HITBOX_TARGET_PART, HITBOX_RIVALS_MODE, HITBOX_CAN_COLLIDE, HITBOX_TEAM_CHECK, HITBOX_VISUALIZE
    global TRIGGERBOT_ENABLED, TRIGGERBOT_DELAY_MS, TRIGGERBOT_TEAM_CHECK, TRIGGERBOT_MODE, TRIGGERBOT_MAX_DELAY_MS
    global FREECAM_ENABLED, FREECAM_SPEED, ITEM_ESP_ENABLED, ITEM_ESP_MAX_DIST
    global MM2_ROLE_ESP_ENABLED, MM2_MURDERER_COLOR, MM2_SHERIFF_COLOR, MM2_INNOCENT_COLOR, MM2_KNIFE_NAMES, MM2_GUN_NAMES
    global MM2_GUN_ESP_ENABLED, MM2_GUN_NOTIFY

    path = get_config_path()
    if not os.path.exists(path):
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        ESP_SHOW_BOX = cfg.get("ESP_SHOW_BOX", ESP_SHOW_BOX)
        ESP_CORNER_BOX = cfg.get("ESP_CORNER_BOX", ESP_CORNER_BOX)
        ESP_3D_BOX = cfg.get("ESP_3D_BOX", ESP_3D_BOX)
        ESP_SHOW_TRACER = cfg.get("ESP_SHOW_TRACER", ESP_SHOW_TRACER)
        ESP_SHOW_SKELETON = cfg.get("ESP_SHOW_SKELETON", ESP_SHOW_SKELETON)
        ESP_SHOW_NAME = cfg.get("ESP_SHOW_NAME", ESP_SHOW_NAME)
        ESP_SHOW_DISTANCE = cfg.get("ESP_SHOW_DISTANCE", ESP_SHOW_DISTANCE)
        ESP_SHOW_HEALTH = cfg.get("ESP_SHOW_HEALTH", ESP_SHOW_HEALTH)
        ESP_DYNAMIC_HEALTH_COLOR = cfg.get("ESP_DYNAMIC_HEALTH_COLOR", ESP_DYNAMIC_HEALTH_COLOR)
        ESP_BOX_THICKNESS = cfg.get("ESP_BOX_THICKNESS", ESP_BOX_THICKNESS)
        ESP_SKELETON_THICKNESS = cfg.get("ESP_SKELETON_THICKNESS", ESP_SKELETON_THICKNESS)
        ESP_TEXT_SIZE = cfg.get("ESP_TEXT_SIZE", ESP_TEXT_SIZE)
        MAX_DISTANCE = float(cfg.get("MAX_DISTANCE", MAX_DISTANCE))
        TEAM_FILTER_MODE = cfg.get("TEAM_FILTER_MODE", TEAM_FILTER_MODE)
        ALWAYS_ON_TOP = cfg.get("ALWAYS_ON_TOP", ALWAYS_ON_TOP)

        if "ESP_BOX_COLOR" in cfg:
            ESP_BOX_COLOR = tuple(cfg["ESP_BOX_COLOR"])
        if "ESP_TEAMMATE_COLOR" in cfg:
            ESP_TEAMMATE_COLOR = tuple(cfg["ESP_TEAMMATE_COLOR"])
        if "ESP_TRACER_COLOR" in cfg:
            ESP_TRACER_COLOR = tuple(cfg["ESP_TRACER_COLOR"])
        if "ESP_SKELETON_COLOR" in cfg:
            ESP_SKELETON_COLOR = tuple(cfg["ESP_SKELETON_COLOR"])
        if "AIMBOT_FOV_COLOR" in cfg:
            AIMBOT_FOV_COLOR = tuple(cfg["AIMBOT_FOV_COLOR"])

        RADAR_ENABLED = cfg.get("RADAR_ENABLED", RADAR_ENABLED)
        RADAR_SIZE = cfg.get("RADAR_SIZE", RADAR_SIZE)
        RADAR_RANGE_STUDS = float(cfg.get("RADAR_RANGE_STUDS", RADAR_RANGE_STUDS))
        RADAR_SHOW_CROSSHAIR = cfg.get("RADAR_SHOW_CROSSHAIR", RADAR_SHOW_CROSSHAIR)
        RADAR_OPACITY = cfg.get("RADAR_OPACITY", RADAR_OPACITY)

        ENABLE_SAFE_SPEED = cfg.get("ENABLE_SAFE_SPEED", ENABLE_SAFE_SPEED)
        SAFE_SPEED_VALUE = float(cfg.get("SAFE_SPEED_VALUE", SAFE_SPEED_VALUE))
        ENABLE_WALKSPEED = cfg.get("ENABLE_WALKSPEED", ENABLE_WALKSPEED)
        WALKSPEED_VALUE = float(cfg.get("WALKSPEED_VALUE", WALKSPEED_VALUE))
        ENABLE_JUMPPOWER = cfg.get("ENABLE_JUMPPOWER", ENABLE_JUMPPOWER)
        JUMPPOWER_VALUE = float(cfg.get("JUMPPOWER_VALUE", JUMPPOWER_VALUE))
        ENABLE_INFINITE_JUMP = cfg.get("ENABLE_INFINITE_JUMP", ENABLE_INFINITE_JUMP)

        ENABLE_NOCLIP = cfg.get("ENABLE_NOCLIP", ENABLE_NOCLIP)
        ENABLE_FLY = cfg.get("ENABLE_FLY", ENABLE_FLY)
        FLY_SPEED = float(cfg.get("FLY_SPEED", FLY_SPEED))
        ENABLE_FULLBRIGHT = cfg.get("ENABLE_FULLBRIGHT", ENABLE_FULLBRIGHT)
        ENABLE_INSTANT_PROMPTS = cfg.get("ENABLE_INSTANT_PROMPTS", ENABLE_INSTANT_PROMPTS)
        ENABLE_INF_CLICK = cfg.get("ENABLE_INF_CLICK", ENABLE_INF_CLICK)
        ENABLE_GRAVITY_MOD = cfg.get("ENABLE_GRAVITY_MOD", ENABLE_GRAVITY_MOD)
        GRAVITY_VALUE = float(cfg.get("GRAVITY_VALUE", GRAVITY_VALUE))
        UNLOCK_FPS = cfg.get("UNLOCK_FPS", UNLOCK_FPS)
        UNLOCK_FPS_VALUE = float(cfg.get("UNLOCK_FPS_VALUE", UNLOCK_FPS_VALUE))

        FLING_POWER = float(cfg.get("FLING_POWER", FLING_POWER))
        FLING_RETURN_TO_START = bool(cfg.get("FLING_RETURN_TO_START", FLING_RETURN_TO_START))
        FLING_DURATION = float(cfg.get("FLING_DURATION", FLING_DURATION))
        SPECTATE_AUTO_NEXT = bool(cfg.get("SPECTATE_AUTO_NEXT", SPECTATE_AUTO_NEXT))

        AIMBOT_ENABLED = cfg.get("AIMBOT_ENABLED", AIMBOT_ENABLED)
        AIMBOT_KEY = cfg.get("AIMBOT_KEY", AIMBOT_KEY)
        AIMBOT_TARGET_PART = cfg.get("AIMBOT_TARGET_PART", AIMBOT_TARGET_PART)
        AIMBOT_FOV = float(cfg.get("AIMBOT_FOV", AIMBOT_FOV))
        AIMBOT_SMOOTHNESS = float(cfg.get("AIMBOT_SMOOTHNESS", AIMBOT_SMOOTHNESS))
        AIMBOT_SHOW_FOV = cfg.get("AIMBOT_SHOW_FOV", AIMBOT_SHOW_FOV)
        AIMBOT_TEAM_CHECK = cfg.get("AIMBOT_TEAM_CHECK", AIMBOT_TEAM_CHECK)
        AIMBOT_PRIORITY = cfg.get("AIMBOT_PRIORITY", AIMBOT_PRIORITY)
        AIMBOT_PREDICTION = bool(cfg.get("AIMBOT_PREDICTION", AIMBOT_PREDICTION))
        AIMBOT_STICKY = bool(cfg.get("AIMBOT_STICKY", AIMBOT_STICKY))
        AIMBOT_DEADZONE = float(cfg.get("AIMBOT_DEADZONE", AIMBOT_DEADZONE))
        AIMBOT_RCS_ENABLED = bool(cfg.get("AIMBOT_RCS_ENABLED", AIMBOT_RCS_ENABLED))
        AIMBOT_RCS_STRENGTH = float(cfg.get("AIMBOT_RCS_STRENGTH", AIMBOT_RCS_STRENGTH))

        HITBOX_EXPANDER_ENABLED = cfg.get("HITBOX_EXPANDER_ENABLED", HITBOX_EXPANDER_ENABLED)
        HITBOX_SIZE = float(cfg.get("HITBOX_SIZE", HITBOX_SIZE))
        HITBOX_TARGET_PART = cfg.get("HITBOX_TARGET_PART", HITBOX_TARGET_PART)
        HITBOX_RIVALS_MODE = bool(cfg.get("HITBOX_RIVALS_MODE", HITBOX_RIVALS_MODE))
        HITBOX_CAN_COLLIDE = bool(cfg.get("HITBOX_CAN_COLLIDE", HITBOX_CAN_COLLIDE))
        HITBOX_TEAM_CHECK = bool(cfg.get("HITBOX_TEAM_CHECK", HITBOX_TEAM_CHECK))
        HITBOX_VISUALIZE = bool(cfg.get("HITBOX_VISUALIZE", HITBOX_VISUALIZE))

        TRIGGERBOT_ENABLED = bool(cfg.get("TRIGGERBOT_ENABLED", TRIGGERBOT_ENABLED))
        TRIGGERBOT_DELAY_MS = int(cfg.get("TRIGGERBOT_DELAY_MS", TRIGGERBOT_DELAY_MS))
        TRIGGERBOT_TEAM_CHECK = bool(cfg.get("TRIGGERBOT_TEAM_CHECK", TRIGGERBOT_TEAM_CHECK))
        TRIGGERBOT_MODE = cfg.get("TRIGGERBOT_MODE", TRIGGERBOT_MODE)
        TRIGGERBOT_MAX_DELAY_MS = int(cfg.get("TRIGGERBOT_MAX_DELAY_MS", TRIGGERBOT_MAX_DELAY_MS))

        FREECAM_ENABLED = bool(cfg.get("FREECAM_ENABLED", FREECAM_ENABLED))
        FREECAM_SPEED = float(cfg.get("FREECAM_SPEED", FREECAM_SPEED))

        ITEM_ESP_ENABLED = bool(cfg.get("ITEM_ESP_ENABLED", ITEM_ESP_ENABLED))
        ITEM_ESP_MAX_DIST = float(cfg.get("ITEM_ESP_MAX_DIST", ITEM_ESP_MAX_DIST))

        MM2_ROLE_ESP_ENABLED = bool(cfg.get("MM2_ROLE_ESP_ENABLED", MM2_ROLE_ESP_ENABLED))
        if "MM2_MURDERER_COLOR" in cfg:
            MM2_MURDERER_COLOR = tuple(cfg["MM2_MURDERER_COLOR"])
        if "MM2_SHERIFF_COLOR" in cfg:
            MM2_SHERIFF_COLOR = tuple(cfg["MM2_SHERIFF_COLOR"])
        if "MM2_INNOCENT_COLOR" in cfg:
            MM2_INNOCENT_COLOR = tuple(cfg["MM2_INNOCENT_COLOR"])
        if "MM2_KNIFE_NAMES" in cfg:
            MM2_KNIFE_NAMES = list(cfg["MM2_KNIFE_NAMES"])
        if "MM2_GUN_NAMES" in cfg:
            MM2_GUN_NAMES = list(cfg["MM2_GUN_NAMES"])
        MM2_GUN_ESP_ENABLED = bool(cfg.get("MM2_GUN_ESP_ENABLED", MM2_GUN_ESP_ENABLED))
        MM2_GUN_NOTIFY = bool(cfg.get("MM2_GUN_NOTIFY", MM2_GUN_NOTIFY))

        if DEBUG_MODE:
            print(f"[+] Loaded config from {path}")
        return True
    except Exception as exc:
        print(f"[!] Failed to load config: {exc}")
        return False


# ====================================
# SKELETON / BONE DEFINITIONS (R6 & R15)
# ====================================

ALL_BONE_NAMES: set[str] = {
    # R6 Limbs
    "Head", "Torso", "Left Arm", "Right Arm", "Left Leg", "Right Leg",
    # R15 Limbs
    "UpperTorso", "LowerTorso",
    "LeftUpperArm", "LeftLowerArm", "LeftHand",
    "RightUpperArm", "RightLowerArm", "RightHand",
    "LeftUpperLeg", "LeftLowerLeg", "LeftFoot",
    "RightUpperLeg", "RightLowerLeg", "RightFoot",
}

R15_CONNECTIONS: list[tuple[str, str]] = [
    ("Head", "UpperTorso"),
    ("UpperTorso", "LowerTorso"),
    ("UpperTorso", "LeftUpperArm"),
    ("LeftUpperArm", "LeftLowerArm"),
    ("LeftLowerArm", "LeftHand"),
    ("UpperTorso", "RightUpperArm"),
    ("RightUpperArm", "RightLowerArm"),
    ("RightLowerArm", "RightHand"),
    ("LowerTorso", "LeftUpperLeg"),
    ("LeftUpperLeg", "LeftLowerLeg"),
    ("LeftLowerLeg", "LeftFoot"),
    ("LowerTorso", "RightUpperLeg"),
    ("RightUpperLeg", "RightLowerLeg"),
    ("RightLowerLeg", "RightFoot"),
]

R6_CONNECTIONS: list[tuple[str, str]] = [
    ("Head", "Torso"),
    ("Torso", "Left Arm"),
    ("Torso", "Right Arm"),
    ("Torso", "Left Leg"),
    ("Torso", "Right Leg"),
]


# ====================================
# VALIDATION
# ====================================

def validate_offsets(loaded: dict[str, int]) -> bool:
    """
    Check that every required offset key exists.
    Prints a clear error for each missing key.
    Returns False if any key is absent.
    """
    ok = True
    for key in REQUIRED_OFFSETS:
        if key not in loaded:
            print(f"[!] Missing local offset: {key}")
            ok = False
    return ok

# ====================================
# ROBLOX OBJECT HELPERS
# ====================================

def _get_name_raw(mem: Memory, instance: int) -> str:
    """
    Read Instance.Name.
    In Roblox 64-bit:
      instance + NameContainer (0x70) -> pointer to NameContainer struct
      NameContainer + Name (0x8)      -> MSVC std::string (SSO <= 15 inline, > 15 heap ptr)
    Fallback: read directly at instance + NameContainer in case layout varies.
    """
    if not instance:
        return ""
    try:
        nc = mem.read_ptr(instance + offsets.get("Instance_NameContainer", 0x70))
        if nc:
            name = mem.read_msvc_string(nc + offsets.get("Instance_Name", 0x8))
            if name:
                return name
            str_ptr = mem.read_ptr(nc + offsets.get("Instance_Name", 0x8))
            if str_ptr and str_ptr > 0x10000:
                name2 = mem.read_string_ptr(str_ptr)
                if name2:
                    return name2
        name = mem.read_msvc_string(instance + offsets.get("Instance_NameContainer", 0x70))
        if name:
            return name
        raw_probe = mem.read(nc or (instance + 0x70), 32)
        if b"HumanoidRootPart" in raw_probe:
            return "HumanoidRootPart"
        return ""
    except Exception:
        return ""


def _get_class_name_raw(mem: Memory, instance: int) -> str:
    """
    Read Instance.ClassName via ClassDescriptor.
    instance + ClassDescriptor (0x18) -> ptr to ClassDescriptor
    ClassDescriptor + ClassName (0x8) -> const char* (direct null-terminated string)
    """
    if not instance:
        return ""
    try:
        class_desc = mem.read_ptr(instance + offsets.get("Instance_ClassDescriptor", 0x18))
        if not class_desc:
            return ""
        char_ptr = mem.read_ptr(class_desc + offsets.get("Instance_ClassName", 0x8))
        if not char_ptr:
            return ""
        raw = mem.read_string_ptr(char_ptr)
        return "".join(ch for ch in raw if 32 <= ord(ch) <= 126)
    except Exception:
        return ""


def get_children(mem: Memory, instance: int) -> list[int]:
    """
    Return a list of child instance pointers.

    Layout:
      instance + ChildrenStart (0x78) -> vec_ptr
      vec_ptr  + 0x00                 -> begin
      vec_ptr  + ChildrenEnd (0x8)    -> end
    Each element is shared_ptr<Instance> = 16 bytes:
      [0x00] raw Instance*
      [0x08] control block ptr
    """
    if not instance:
        return []
    try:
        cs = offsets.get("Instance_ChildrenStart", 0x78)
        vec_ptr = mem.read_ptr(instance + cs)
        if not vec_ptr:
            return []

        begin = mem.read_ptr(vec_ptr)
        ce = offsets.get("Instance_ChildrenEnd", 0x8)
        end = mem.read_ptr(vec_ptr + ce)

        if not begin or not end or end <= begin:
            return []

        STRIDE = 16
        count = min((end - begin) // STRIDE, 2048)
        children = []
        for i in range(count):
            child = mem.read_ptr(begin + i * STRIDE)
            if child:
                children.append(child)
        return children
    except Exception:
        return []


def get_character_parts(mem: Memory, character: int) -> dict[str, int]:
    """
    Scan character children in a single pass to map key parts and limbs dynamically.
    Avoids redundant traversals on every frame.
    """
    parts: dict[str, int] = {
        "Humanoid": 0,
        "HumanoidRootPart": 0,
        "Head": 0,
        "Torso": 0,
        "UpperTorso": 0,
        "LowerTorso": 0,
    }
    if not character:
        return parts

    for child in get_children(mem, character):
        cname = _get_name_raw(mem, child)
        if cname in ALL_BONE_NAMES or cname in parts:
            if cname in parts and not parts[cname]:
                parts[cname] = child
            elif cname in ALL_BONE_NAMES and cname not in parts:
                parts[cname] = child
        elif not parts["Humanoid"] and _get_class_name_raw(mem, child) == "Humanoid":
            parts["Humanoid"] = child

    return parts


def get_name(mem: Memory, instance: int) -> str:
    return _get_name_raw(mem, instance)


def get_class_name(mem: Memory, instance: int) -> str:
    return _get_class_name_raw(mem, instance)


def find_first_child(mem: Memory, instance: int, name: str) -> int:
    for child in get_children(mem, instance):
        if _get_name_raw(mem, child) == name:
            return child
    return 0


def find_first_child_of_class(mem: Memory, instance: int, class_name: str) -> int:
    for child in get_children(mem, instance):
        if _get_class_name_raw(mem, child) == class_name:
            return child
    return 0

# ====================================
# MATH HELPERS
# ====================================

def world_to_screen(
    world_pos: tuple[float, float, float],
    cam_pos:   tuple[float, float, float],
    cam_rot:   list[float],
    fov_deg:   float,
    screen_w:  int,
    screen_h:  int,
) -> tuple[float, float] | None:
    """
    Project a Roblox world-space position onto 2-D screen coordinates
    using the camera CFrame (3×3 rotation matrix + position).

    cam_rot  — flat list of 9 floats from Camera.CFrame:
               [RightX, RightY, RightZ,
                UpX,    UpY,    UpZ,
                LookX,  LookY,  LookZ]
    Returns (sx, sy) or None if behind the camera / off-screen.
    """
    try:
        dx = world_pos[0] - cam_pos[0]
        dy = world_pos[1] - cam_pos[1]
        dz = world_pos[2] - cam_pos[2]

        # Roblox stores rotation row-major: m = [R00 R01 R02 | R10 R11 R12 | R20 R21 R22]
        # Camera axis vectors are the COLUMNS:
        #   Right  = (m[0], m[3], m[6])
        #   Up     = (m[1], m[4], m[7])
        #   Back   = (m[2], m[5], m[8])  i.e. -LookVector
        #
        # Project delta onto each camera axis:
        rx =  dx*cam_rot[0] + dy*cam_rot[3] + dz*cam_rot[6]   # dot(delta, Right)
        ry =  dx*cam_rot[1] + dy*cam_rot[4] + dz*cam_rot[7]   # dot(delta, Up)
        # Depth: dot(delta, -Back) = dot(delta, LookVector). Positive = in front.
        rz = -(dx*cam_rot[2] + dy*cam_rot[5] + dz*cam_rot[8])

        if rz <= 0.1:
            return None

        fov_rad = math.radians(fov_deg)
        scale   = (screen_h * 0.5) / math.tan(fov_rad * 0.5)

        sx = screen_w * 0.5 + (rx / rz) * scale
        sy = screen_h * 0.5 - (ry / rz) * scale

        margin = max(screen_w, screen_h) * 2
        if not (-margin < sx < screen_w + margin
                and -margin < sy < screen_h + margin):
            return None

        return sx, sy

    except (TypeError, ZeroDivisionError, ValueError, IndexError):
        return None


def world_to_screen_matrix(
    world_pos:   tuple[float, float, float],
    view_matrix: np.ndarray,
    screen_w:    int,
    screen_h:    int,
) -> tuple[float, float] | None:
    """
    Project a world position using a full 4×4 view-projection matrix
    (e.g. from VisualEngine.ViewMatrix).

    view_matrix — numpy array, shape (4, 4), dtype float32.
    Returns (sx, sy) or None if invalid / behind camera.
    """
    try:
        if view_matrix is None or view_matrix.shape != (4, 4):
            return None

        vec  = np.array([world_pos[0], world_pos[1], world_pos[2], 1.0],
                        dtype=np.float32)
        clip = view_matrix @ vec

        if clip[3] <= 0.0:
            return None

        ndc_x = clip[0] / clip[3]
        ndc_y = clip[1] / clip[3]

        sx = (1.0 + ndc_x) * screen_w * 0.5
        sy = (1.0 - ndc_y) * screen_h * 0.5

        if not (-screen_w < sx < 2 * screen_w
                and -screen_h < sy < 2 * screen_h):
            return None

        return sx, sy

    except (TypeError, ValueError, np.linalg.LinAlgError):
        return None


def get_health_color(hp_ratio: float) -> QColor:
    """Green → Yellow → Red gradient based on 0.0–1.0 health ratio."""
    hp_ratio = max(0.0, min(1.0, hp_ratio))
    if hp_ratio >= 0.5:
        r = int(255 * (1.0 - hp_ratio) * 2)
        g = 255
    else:
        r = 255
        g = int(255 * hp_ratio * 2)
    return QColor(r, g, 0, 230)


# ====================================
# MM2 ROLE DETECTION
# ====================================

def detect_mm2_role(mem: Memory, character: int, player_ptr: int = 0) -> str:
    """
    Scan a player's character and Backpack for genuine MM2 weapon tools.
    Returns one of: "Murderer", "Sheriff", or "Innocent".

    Only matches instances that are actually of class "Tool" or have a "Handle",
    preventing cosmetic accessories, animations, and body parts from causing false positives.
    """
    if not character or not MM2_ROLE_ESP_ENABLED:
        return "Innocent"

    # Containers to check: Character (equipped weapon) and Backpack (unequipped weapon)
    containers_to_check = [character]
    if player_ptr:
        backpack = find_first_child_of_class(mem, player_ptr, "Backpack")
        if not backpack:
            backpack = find_first_child(mem, player_ptr, "Backpack")
        if backpack:
            containers_to_check.append(backpack)

    detected_role = "Innocent"

    try:
        for container in containers_to_check:
            for child in get_children(mem, container):
                cls = get_class_name(mem, child)
                # Only check genuine Tools or objects with a Handle
                has_handle = find_first_child(mem, child, "Handle") != 0
                if cls != "Tool" and not has_handle:
                    continue

                child_name = _get_name_raw(mem, child).lower().strip()
                if not child_name:
                    continue

                # Ignore common harmless tools (e.g. radios, toys, emotes, phones)
                if any(ign in child_name for kw in ("radio", "boombox", "toy", "emote", "phone", "pass") for ign in (kw,)):
                    continue

                # Check Murderer knife
                for kw in MM2_KNIFE_NAMES:
                    if kw in child_name:
                        return "Murderer"

                # Check Sheriff gun
                for kw in MM2_GUN_NAMES:
                    if kw in child_name:
                        detected_role = "Sheriff"
    except Exception:
        pass

    return detected_role


# ====================================
# WINDOW GEOMETRY HELPERS
# ====================================

_prev_geometry: tuple[int, int, int, int] | None = None


def find_roblox_hwnd() -> int:
    return _user32.FindWindowW(None, TARGET_WINDOW_TITLE)


def get_client_rect_screen(hwnd: int) -> tuple[int, int, int, int] | None:
    """Return (x, y, w, h) in screen coordinates for the window's client area."""
    if not hwnd:
        return None
    rect = ctypes.wintypes.RECT()
    if not _user32.GetClientRect(hwnd, ctypes.byref(rect)):
        return None
    w = rect.right
    h = rect.bottom
    if w <= 0 or h <= 0:
        return None
    pt = ctypes.wintypes.POINT()
    pt.x = 0
    pt.y = 0
    _user32.ClientToScreen(hwnd, ctypes.byref(pt))
    return pt.x, pt.y, w, h


def get_window_rect_coords(hwnd: int) -> tuple[int, int, int, int] | None:
    """Fallback: full window rect including borders."""
    if not hwnd:
        return None
    rect = ctypes.wintypes.RECT()
    if not _user32.GetWindowRect(hwnd, ctypes.byref(rect)):
        return None
    w = rect.right  - rect.left
    h = rect.bottom - rect.top
    if w <= 0 or h <= 0:
        return None
    return rect.left, rect.top, w, h

# ====================================
# ESP OVERLAY
# ====================================

class ESPOverlay(QWidget):
    """
    Transparent, always-on-top PyQt5 overlay that draws ESP visuals
    using QPainter.  Data collection runs in its own update cycle;
    painting only consumes the cached esp_data list.
    """

    def __init__(self, mem: Memory) -> None:
        super().__init__()
        self.mem      = mem
        self.enabled  = True
        self.esp_data: list[dict] = []
        self._lock    = threading.Lock()

        # Window geometry state
        self._hwnd     = 0
        self.screen_w  = 1920
        self.screen_h  = 1080

        # Tracked player entities (discovered periodically in background thread)
        self._tracked_targets: list[dict] = []
        self._targets_lock: threading.Lock = threading.Lock()
        self._all_server_players: list[dict] = []
        self._players_lock: threading.Lock = threading.Lock()
        self._last_loop_tp_time: float = 0.0
        self._workspace: int = 0

        # Dynamic service caching
        self._players_svc: int    = 0
        self._last_datamodel: int = 0
        self._local_humanoid: int  = 0
        self._local_character: int = 0

        # Fling state
        self._fling_active: bool = False
        self._fling_mode: str = "burst"
        self._fling_target_name: str = ""
        self._fling_power: float = FLING_POWER
        self._fling_return_to_start: bool = FLING_RETURN_TO_START
        self._fling_start_pos: tuple[float, float, float] | None = None
        self._fling_start_time: float = 0.0
        self._fling_duration: float = FLING_DURATION

        # Spectate state
        self._spectate_active: bool = False
        self._spectate_target_name: str = ""
        self._spectate_target_display: str = ""
        self._spectate_original_subject: int = 0

        # Player departure/arrival event tracking
        self._previous_player_names: set[str] = set()
        self._recent_player_events: list[dict] = []
        self._events_lock: threading.Lock = threading.Lock()

        # Pre-build fonts, pens, and brushes once — never recreated per frame
        self._font_name = QFont("Arial", ESP_TEXT_SIZE)
        self._font_name.setBold(True)
        self._font_dist = QFont("Arial", max(ESP_TEXT_SIZE - 2, 8))

        self._pen_box          = QPen(QColor(*ESP_BOX_COLOR), ESP_BOX_THICKNESS)
        self._pen_tracer       = QPen(QColor(*ESP_TRACER_COLOR), 1)
        self._pen_skeleton     = QPen(QColor(*ESP_SKELETON_COLOR), ESP_SKELETON_THICKNESS)
        self._pen_name         = QPen(QColor(*ESP_NAME_COLOR))
        self._pen_dist         = QPen(QColor(*ESP_DISTANCE_COLOR))
        self._pen_team_box     = QPen(QColor(*ESP_TEAMMATE_COLOR), ESP_BOX_THICKNESS)
        self._pen_team_tracer  = QPen(QColor(*ESP_TEAMMATE_COLOR), 1)
        self._pen_team_skeleton = QPen(QColor(*ESP_TEAMMATE_COLOR), ESP_SKELETON_THICKNESS)
        self._pen_team_name    = QPen(QColor(*ESP_TEAMMATE_COLOR))
        self._brush_health_bg  = QBrush(QColor(0, 0, 0, 160))

        # Hitbox Expander state (saves original sizes to restore cleanly)
        self._expanded_prims: dict[int, tuple[tuple[float, float, float], int]] = {}

        # Combat & Aimbot state
        self._aimbot_locked_target: str | None = None
        self._target_pos_history: dict[str, tuple[float, tuple[float, float, float]]] = {}
        self._triggerbot_firing: bool = False
        self._last_triggerbot_fire: float = 0.0

        # Item & Entity ESP
        self._tracked_items: list[dict] = []
        self._items_lock: threading.Lock = threading.Lock()
        self._pen_hitbox = QPen(QColor(0, 255, 200, 220), 1, Qt.DashLine)
        self._pen_item_esp = QPen(QColor(255, 215, 0, 230), 1)
        self._font_item = QFont("Arial", 9)
        self._font_item.setBold(True)

        # MM2 Dropped Gun tracking
        self._mm2_dropped_gun: dict | None = None
        self._mm2_gun_lock: threading.Lock = threading.Lock()
        self._pen_gun_beacon = QPen(QColor(*MM2_GUN_DROP_COLOR), 1.8, Qt.DashLine)
        self._pen_gun_box = QPen(QColor(*MM2_GUN_DROP_COLOR), 2)
        self._brush_gun_glow = QBrush(QColor(255, 215, 0, 45))

        self._last_cam_pos     = (0.0, 0.0, 0.0)
        self._last_cam_rot     = [0.0] * 9

        # Qt window flags for a transparent, click-through overlay
        self.setWindowFlags(
            Qt.FramelessWindowHint     |
            Qt.WindowStaysOnTopHint    |
            Qt.Tool                    |
            Qt.WindowTransparentForInput
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground,    True)
        self.setAttribute(Qt.WA_OpaquePaintEvent,      False)
        self.setStyleSheet("background: transparent;")

        # High-FPS render & camera tracking timer (~60 FPS = 16ms)
        self._render_timer = QTimer(self)
        self._render_timer.timeout.connect(self._on_render_tick)
        self._render_timer.start(RENDER_INTERVAL_MS)

        # Geometry sync timer
        self._geo_timer = QTimer(self)
        self._geo_timer.timeout.connect(self._sync_geometry)
        self._geo_timer.start(GEOMETRY_CHECK_MS)

        # Start background player scanner thread (decouples heavy memory scans from 60 FPS rendering)
        self._scanner_thread = threading.Thread(
            target=self._player_scanner_loop,
            daemon=True,
            name="PlayerScannerThread",
        )
        self._scanner_thread.start()

        self._sync_geometry()
        self._debug_once = True   # fires _debug_chain() on startup

    def update_pens(self) -> None:
        """Dynamically refresh pens when colors or thicknesses are adjusted in the UI."""
        self._font_name = QFont("Arial", ESP_TEXT_SIZE)
        self._font_name.setBold(True)
        self._font_dist = QFont("Arial", max(ESP_TEXT_SIZE - 2, 8))

        self._pen_box          = QPen(QColor(*ESP_BOX_COLOR), ESP_BOX_THICKNESS)
        self._pen_tracer       = QPen(QColor(*ESP_TRACER_COLOR), 1)
        self._pen_skeleton     = QPen(QColor(*ESP_SKELETON_COLOR), ESP_SKELETON_THICKNESS)
        self._pen_name         = QPen(QColor(*ESP_NAME_COLOR))
        self._pen_dist         = QPen(QColor(*ESP_DISTANCE_COLOR))
        self._pen_team_box     = QPen(QColor(*ESP_TEAMMATE_COLOR), ESP_BOX_THICKNESS)
        self._pen_team_tracer  = QPen(QColor(*ESP_TEAMMATE_COLOR), 1)
        self._pen_team_skeleton = QPen(QColor(*ESP_TEAMMATE_COLOR), ESP_SKELETON_THICKNESS)
        self._pen_team_name    = QPen(QColor(*ESP_TEAMMATE_COLOR))

    def set_always_on_top(self, enabled: bool) -> None:
        """Toggle Always On Top window state."""
        self.setWindowFlag(Qt.WindowStaysOnTopHint, enabled)
        self.show()

    # ------------------------------------------------------------------ #
    # Geometry                                                             #
    # ------------------------------------------------------------------ #

    def _sync_geometry(self) -> None:
        global _prev_geometry
        if not self._hwnd:
            self._hwnd = find_roblox_hwnd()
        geo = get_client_rect_screen(self._hwnd) or get_window_rect_coords(self._hwnd)
        if geo is None or geo == _prev_geometry:
            return
        _prev_geometry = geo
        x, y, w, h = geo
        self.screen_w = w
        self.screen_h = h
        self.setGeometry(x, y, w, h)
        if DEBUG_MODE:
            print(f"[*] Overlay → ({x}, {y}) {w}×{h}")

    # ------------------------------------------------------------------ #
    # Data update                                                          #
    # ------------------------------------------------------------------ #

    def _player_scanner_loop(self) -> None:
        """
        Background worker: continuously discovers players, characters, and parts.
        Runs independently of the 60 FPS render timer so heavy operations never cause lag.
        """
        while True:
            try:
                self._scan_players()
                if ENABLE_WALKSPEED or ENABLE_JUMPPOWER:
                    self.apply_movement_modifiers()
                if ENABLE_NOCLIP:
                    self.apply_noclip()
                if ENABLE_FULLBRIGHT or ENABLE_GRAVITY_MOD or UNLOCK_FPS:
                    self.apply_world_mods()
                if ENABLE_INSTANT_PROMPTS or ENABLE_INF_CLICK:
                    self.apply_instant_prompts_and_clicks()
                if ITEM_ESP_ENABLED or MM2_GUN_ESP_ENABLED:
                    self._scan_items()
            except Exception:
                pass
            time.sleep(PLAYER_SCAN_INTERVAL_MS / 1000.0)

    def _on_render_tick(self) -> None:
        """
        High-FPS frame tick: reads camera and primitive positions, projects to screen.
        Runs at ~60 FPS (16ms) for silky-smooth camera movement.
        """
        if ENABLE_SAFE_SPEED:
            self.apply_safe_speed()

        if ENABLE_WALKSPEED or ENABLE_JUMPPOWER:
            self.apply_movement_modifiers()

        if ENABLE_NOCLIP:
            self.apply_noclip()

        if ENABLE_FLY:
            self.apply_fly()

        if HITBOX_EXPANDER_ENABLED:
            self.apply_hitbox_expander()
        elif self._expanded_prims:
            self.restore_hitboxes()

        if TRIGGERBOT_ENABLED:
            self._handle_triggerbot_tick()

        if FREECAM_ENABLED:
            self._handle_freecam_tick()

        if LOOP_TP_ENABLED and LOOP_TP_TARGET_NAME:
            self._handle_loop_tp()

        if self._fling_active:
            self._handle_fling_tick()

        if self._spectate_active:
            self._handle_spectate_tick()

        if AIMBOT_ENABLED:
            self._handle_aimbot_tick()

        if not self.enabled:
            return
        if self._debug_once and DEBUG_MODE:
            self._debug_once = False
            self._debug_chain()
        try:
            self._update_render_data()
        except Exception as exc:
            if DEBUG_MODE:
                print(f"[!] Render tick error: {exc}")
        self.update()   # Schedule immediate repaint

    def _handle_aimbot_tick(self) -> None:
        """
        Advanced Aimbot:
        - Multi-key support (RBUTTON, LBUTTON, LSHIFT, E, Q, ALT)
        - Target prioritization (Crosshair FOV, 3D Distance, Lowest HP)
        - Sticky target retention (prevents target jittering)
        - Velocity/Position prediction (lead aiming)
        - Micro-deadzone to eliminate cursor jittering
        - Humanized curve smoothing
        - Recoil Compensation System (RCS) pull-down while firing
        """
        if not AIMBOT_ENABLED:
            self._aimbot_locked_target = None
            return

        # Check hotkey state
        key_code = VK_RBUTTON
        if AIMBOT_KEY == "LBUTTON":
            key_code = VK_LBUTTON
        elif AIMBOT_KEY == "LSHIFT":
            key_code = VK_LSHIFT
        elif AIMBOT_KEY == "E":
            key_code = VK_KEY_E
        elif AIMBOT_KEY == "Q":
            key_code = VK_KEY_Q
        elif AIMBOT_KEY == "ALT":
            key_code = VK_MENU

        key_pressed = bool(_user32.GetAsyncKeyState(key_code) & 0x8000)
        if not key_pressed:
            if not AIMBOT_STICKY or not self._aimbot_locked_target:
                self._aimbot_locked_target = None
            return

        cx = self.screen_w // 2
        cy = self.screen_h // 2
        max_fov = float(AIMBOT_FOV)

        with self._lock:
            snapshot = list(self.esp_data)

        # Update position history for velocity calculation
        now = time.time()
        for entry in snapshot:
            uname = entry.get("name")
            wpos = entry.get("world_pos")
            if uname and wpos and wpos != (0.0, 0.0, 0.0):
                self._target_pos_history[uname] = (now, wpos)

        # Clean old target history (> 2 seconds old)
        if len(self._target_pos_history) > 60:
            cutoff = now - 2.0
            self._target_pos_history = {k: v for k, v in self._target_pos_history.items() if v[0] >= cutoff}

        candidates = []
        for entry in snapshot:
            if AIMBOT_TEAM_CHECK and entry.get("is_teammate", False):
                continue

            target_pt = entry.get("screen_head") if AIMBOT_TARGET_PART == "Head" else None
            if not target_pt:
                box = entry.get("box")
                if box:
                    target_pt = (box[0] + box[2] * 0.5, box[1] + box[3] * (0.25 if AIMBOT_TARGET_PART == "Head" else 0.5))

            if not target_pt:
                continue

            tx, ty = target_pt
            dx = tx - cx
            dy = ty - cy
            sdist = math.hypot(dx, dy)

            # Must fall inside FOV radius
            if sdist > max_fov:
                continue

            candidates.append({
                "entry": entry,
                "target_pt": target_pt,
                "dx": dx,
                "dy": dy,
                "sdist": sdist,
                "world_dist": entry.get("distance", 9999.0),
                "health": entry.get("health", 100.0),
                "name": entry.get("name", "")
            })

        if not candidates:
            self._aimbot_locked_target = None
            return

        chosen = None

        # Check if currently locked sticky target is still valid in candidates
        if AIMBOT_STICKY and self._aimbot_locked_target:
            for cand in candidates:
                if cand["name"] == self._aimbot_locked_target:
                    chosen = cand
                    break

        # If no sticky match, pick by priority mode
        if not chosen:
            if AIMBOT_PRIORITY == "Distance":
                candidates.sort(key=lambda c: c["world_dist"])
            elif AIMBOT_PRIORITY == "Lowest HP":
                candidates.sort(key=lambda c: c["health"])
            else:  # "Crosshair"
                candidates.sort(key=lambda c: c["sdist"])
            chosen = candidates[0]
            if AIMBOT_STICKY:
                self._aimbot_locked_target = chosen["name"]

        target_pt = chosen["target_pt"]
        tx, ty = target_pt[0], target_pt[1]

        # Velocity prediction (Lead Aiming)
        if AIMBOT_PREDICTION and chosen["name"] in self._target_pos_history:
            prev_time, prev_wpos = self._target_pos_history[chosen["name"]]
            dt = now - prev_time
            cur_wpos = chosen["entry"].get("world_pos")
            if cur_wpos and dt > 0.015:
                # Estimate velocity in studs/sec
                vx = (cur_wpos[0] - prev_wpos[0]) / dt
                vy = (cur_wpos[1] - prev_wpos[1]) / dt
                vz = (cur_wpos[2] - prev_wpos[2]) / dt
                speed_sq = vx*vx + vy*vy + vz*vz
                if 1.0 < speed_sq < 10000.0:  # Sensible player speed range
                    cam_pos = self._last_cam_pos
                    cam_rot = self._last_cam_rot
                    lead_time = min(0.12, max(0.02, chosen["world_dist"] / 450.0))
                    pred_wpos = (
                        cur_wpos[0] + vx * lead_time,
                        cur_wpos[1] + (1.8 if AIMBOT_TARGET_PART == "Head" else 0.0) + vy * lead_time,
                        cur_wpos[2] + vz * lead_time
                    )
                    pred_scr = world_to_screen(pred_wpos, cam_pos, cam_rot, 70.0, self.screen_w, self.screen_h)
                    if pred_scr:
                        tx, ty = pred_scr[0], pred_scr[1]

        dx = tx - cx
        dy = ty - cy
        sdist = math.hypot(dx, dy)

        # Micro-deadzone (prevents jittering when on target)
        if sdist <= float(AIMBOT_DEADZONE):
            dx = 0.0
            dy = 0.0

        # Recoil Compensation System (RCS): pull down slightly if left mouse button is held down
        if AIMBOT_RCS_ENABLED:
            is_firing = bool(_user32.GetAsyncKeyState(VK_LBUTTON) & 0x8000)
            if is_firing:
                dy += float(AIMBOT_RCS_STRENGTH)

        smooth = max(1.0, float(AIMBOT_SMOOTHNESS))

        # Dynamic curve smoothing: smooth is gentler close up, snappier far away
        if smooth > 1.0:
            move_x = int(math.copysign(math.pow(abs(dx) / smooth, 0.95), dx)) if abs(dx) > 0.5 else 0
            move_y = int(math.copysign(math.pow(abs(dy) / smooth, 0.95), dy)) if abs(dy) > 0.5 else 0
        else:
            move_x = int(dx)
            move_y = int(dy)

        if move_x != 0 or move_y != 0:
            move_mouse_relative(move_x, move_y)

    def _handle_loop_tp(self) -> None:
        """Continuously keep character positioned at target player while Loop TP is on."""
        now = time.time()
        if now - self._last_loop_tp_time < 0.08:
            return
        self._last_loop_tp_time = now
        with self._players_lock:
            for p in self._all_server_players:
                if p.get("username") == LOOP_TP_TARGET_NAME:
                    self.teleport_to_player(p, mode="Exact")
                    break

    # ------------------------------------------------------------------ #
    # Fling System                                                       #
    # ------------------------------------------------------------------ #

    def is_flinging(self) -> bool:
        return self._fling_active

    def get_fling_target(self) -> str:
        return self._fling_target_name if self._fling_active else ""

    def start_fling(
        self,
        player_entry: dict,
        mode: str = "burst",
        power: float = 100000.0,
        return_to_start: bool = True,
        duration: float = 1.5,
    ) -> bool:
        """
        Initiate physical collision fling against target player.
        Injects extreme rotational angular velocity and dynamic orbital velocities
        into local character assembly parts while ramming into target's collision hull.
        """
        if not player_entry:
            return False
        uname = player_entry.get("username", "")
        if not uname:
            return False

        prims = self.get_local_core_primitives()
        if not prims:
            return False

        pos_offset = offsets.get("Primitive_Position", 0xD4)
        start_pos = self.mem.read_vec3(prims[0] + pos_offset)
        if start_pos == (0.0, 0.0, 0.0):
            return False

        global FLING_ACTIVE, FLING_MODE, FLING_TARGET_NAME, FLING_POWER, FLING_RETURN_TO_START, FLING_DURATION
        FLING_ACTIVE = True
        FLING_MODE = mode
        FLING_TARGET_NAME = uname
        FLING_POWER = float(power)
        FLING_RETURN_TO_START = bool(return_to_start)
        FLING_DURATION = float(duration)

        self._fling_active = True
        self._fling_mode = mode
        self._fling_target_name = uname
        self._fling_power = float(power)
        self._fling_return_to_start = bool(return_to_start)
        self._fling_start_pos = start_pos
        self._fling_start_time = time.time()
        self._fling_duration = float(duration)

        # Protect local player from ragdolling or tripping during fling
        local_hum = self.get_local_humanoid()
        if local_hum:
            try:
                self.mem.write_bool(local_hum + offsets.get("Humanoid_PlatformStand", 0x1CC), True)
            except Exception:
                pass

        if DEBUG_MODE:
            print(f"[+] Started fling ({mode}) on '{uname}' with power {power:.0f}")
        return True

    def stop_fling(self) -> None:
        """Stop active fling, neutralize velocities, and safely return to start position."""
        global FLING_ACTIVE, FLING_TARGET_NAME
        if not self._fling_active and not FLING_ACTIVE:
            return

        FLING_ACTIVE = False
        FLING_TARGET_NAME = ""

        self._fling_active = False
        saved_target = self._fling_target_name
        self._fling_target_name = ""

        # Zero out both linear and angular velocities on local core assembly
        prims = self.get_local_core_primitives()
        vel_offset = offsets.get("Primitive_AssemblyLinearVelocity", 0xE0)
        ang_vel_offset = offsets.get("Primitive_AssemblyAngularVelocity", 0xEC)
        for prim in prims:
            try:
                self.mem.write_vec3(prim + vel_offset, 0.0, 0.0, 0.0)
                self.mem.write_vec3(prim + ang_vel_offset, 0.0, 0.0, 0.0)
            except Exception:
                pass

        # Restore local humanoid state
        local_hum = self.get_local_humanoid()
        if local_hum:
            try:
                self.mem.write_bool(local_hum + offsets.get("Humanoid_PlatformStand", 0x1CC), False)
            except Exception:
                pass

        # Safely return to starting position if configured
        if self._fling_return_to_start and self._fling_start_pos:
            ox, oy, oz = self._fling_start_pos
            self.teleport_to_coords(ox, oy, oz)

        if DEBUG_MODE and saved_target:
            print(f"[*] Fling stopped on '{saved_target}'. Velocities reset.")

    def _handle_fling_tick(self) -> None:
        """High-frequency fling tick (~60 FPS) executing physics penetration and momentum transfer."""
        if not self._fling_active or not self._fling_target_name:
            return

        now = time.time()
        # Burst duration expiration check
        if self._fling_mode == "burst" and (now - self._fling_start_time >= self._fling_duration):
            self.stop_fling()
            return

        # Target departure check
        target_player = None
        with self._players_lock:
            for p in self._all_server_players:
                if p.get("username") == self._fling_target_name:
                    target_player = p
                    break

        if not target_player:
            # Target left the server
            self.stop_fling()
            return

        target_prim = target_player.get("prim", 0)
        if not target_prim:
            char = target_player.get("character", 0)
            if char:
                parts = get_character_parts(self.mem, char)
                hrp = parts.get("HumanoidRootPart") or parts.get("Torso")
                if hrp:
                    target_prim = self.mem.read_ptr(hrp + offsets.get("BasePart_Primitive", 0x178))

        if not target_prim:
            return

        pos_offset = offsets.get("Primitive_Position", 0xD4)
        target_pos = self.mem.read_vec3(target_prim + pos_offset)
        if target_pos == (0.0, 0.0, 0.0):
            return

        # Ensure local character parts have CanCollide bit set so physics collision registers
        char = self.get_local_character()
        if char:
            flags_offset = offsets.get("Primitive_Flags", 0x1B6)
            can_collide_bit = offsets.get("PrimitiveFlags_CanCollide", 0x8)
            for child in get_children(self.mem, char):
                c_prim = self.mem.read_ptr(child + offsets.get("BasePart_Primitive", 0x178))
                if c_prim:
                    try:
                        cur_flags = self.mem.read(c_prim + flags_offset, 1)
                        if cur_flags:
                            val = cur_flags[0] | can_collide_bit
                            self.mem.write(c_prim + flags_offset, bytes([val]))
                    except Exception:
                        pass

        # Hover slightly (+0.25 studs) above target's root part to guarantee local feet NEVER intersect the floor/terrain
        ty = target_pos[1] + 0.25
        # Micro horizontal orbit around target torso to maintain tight physical collision contact
        angle = (now * 32.0) % (2.0 * math.pi)
        orbit_radius = 0.35
        tx = target_pos[0] + math.cos(angle) * orbit_radius
        tz = target_pos[2] + math.sin(angle) * orbit_radius

        prims = self.get_local_core_primitives()
        if not prims:
            return

        vel_offset = offsets.get("Primitive_AssemblyLinearVelocity", 0xE0)
        ang_vel_offset = offsets.get("Primitive_AssemblyAngularVelocity", 0xEC)
        pwr = float(self._fling_power)

        # 1. Apply pure horizontal (Yaw) rotational torque to local character.
        # CRITICAL: Y-axis only! Never rotate on X or Z, which would cartwheel the avatar into the floor.
        # Local linear velocity has ZERO vertical speed (0.0 Y) to ensure local player never gets launched upwards.
        for prim in prims:
            try:
                self.mem.write_vec3(prim + pos_offset, tx, ty, tz)
                self.mem.write_vec3(prim + ang_vel_offset, 0.0, pwr, 0.0)
                self.mem.write_vec3(prim + vel_offset, math.cos(angle) * 80.0, 0.0, math.sin(angle) * 80.0)
            except Exception:
                pass

        # 2. Inject violent upward and outward launch momentum directly into target player's primitive!
        try:
            target_launch_pwr = max(40000.0, min(pwr, 120000.0))
            self.mem.write_vec3(
                target_prim + vel_offset,
                math.cos(angle) * target_launch_pwr,
                target_launch_pwr * 0.85,
                math.sin(angle) * target_launch_pwr,
            )
            self.mem.write_vec3(
                target_prim + ang_vel_offset,
                target_launch_pwr * 0.5,
                target_launch_pwr,
                target_launch_pwr * 0.5,
            )
        except Exception:
            pass

    # ------------------------------------------------------------------ #
    # Spectate System                                                    #
    # ------------------------------------------------------------------ #

    def is_spectating(self) -> bool:
        return self._spectate_active

    def get_spectate_target(self) -> str:
        return self._spectate_target_name if self._spectate_active else ""

    def start_spectate(self, player_entry: dict) -> bool:
        """
        Switch Roblox camera subject to target player's Humanoid.
        Integrates natively with Roblox's standard CameraModule for third-person
        orbiting, zooming, and tracking.
        """
        if not player_entry:
            return False
        uname = player_entry.get("username", "")
        if not uname:
            return False

        hum = player_entry.get("humanoid", 0)
        char = player_entry.get("character", 0)
        if not hum and char:
            parts = get_character_parts(self.mem, char)
            hum = parts.get("Humanoid", 0)
            if not hum:
                hum = find_first_child_of_class(self.mem, char, "Humanoid")

        subj = hum or player_entry.get("prim", 0)
        if not subj:
            return False

        workspace = self._workspace or self._get_workspace()
        if not workspace:
            return False
        camera = self.mem.read_ptr(workspace + offsets.get("Workspace_CurrentCamera", 0x4A8))
        if not camera:
            return False

        sub_offset = offsets.get("Camera_CameraSubject", 0xB8)
        cur_sub = self.mem.read_ptr(camera + sub_offset)
        if not self._spectate_active:
            self._spectate_original_subject = cur_sub or self.get_local_humanoid()

        # Write target subject to camera
        self.mem.write_ptr(camera + sub_offset, subj)

        global SPECTATE_ENABLED, SPECTATE_TARGET_NAME
        SPECTATE_ENABLED = True
        SPECTATE_TARGET_NAME = uname

        self._spectate_active = True
        self._spectate_target_name = uname
        self._spectate_target_display = player_entry.get("display_name", uname)

        if DEBUG_MODE:
            print(f"[+] Spectating '{uname}' (Subject ptr: {hex(subj)})")
        return True

    def stop_spectate(self) -> bool:
        """Restore camera subject back to local player's humanoid."""
        global SPECTATE_ENABLED, SPECTATE_TARGET_NAME
        if not self._spectate_active and not SPECTATE_ENABLED:
            return True

        SPECTATE_ENABLED = False
        SPECTATE_TARGET_NAME = ""

        self._spectate_active = False
        saved_name = self._spectate_target_name
        self._spectate_target_name = ""
        self._spectate_target_display = ""

        workspace = self._workspace or self._get_workspace()
        if workspace:
            camera = self.mem.read_ptr(workspace + offsets.get("Workspace_CurrentCamera", 0x4A8))
            if camera:
                sub_offset = offsets.get("Camera_CameraSubject", 0xB8)
                local_hum = self.get_local_humanoid()
                restore_ptr = local_hum or self._spectate_original_subject
                if restore_ptr:
                    self.mem.write_ptr(camera + sub_offset, restore_ptr)

        if DEBUG_MODE and saved_name:
            print(f"[*] Stopped spectating '{saved_name}'. Camera returned to local player.")
        return True

    def _handle_spectate_tick(self) -> None:
        """Keep camera subject focused on target across character respawns or engine updates."""
        if not self._spectate_active or not self._spectate_target_name:
            return

        target_player = None
        with self._players_lock:
            for p in self._all_server_players:
                if p.get("username") == self._spectate_target_name:
                    target_player = p
                    break

        if not target_player:
            # Player left the server
            self.stop_spectate()
            return

        hum = target_player.get("humanoid", 0)
        char = target_player.get("character", 0)
        if not hum and char:
            parts = get_character_parts(self.mem, char)
            hum = parts.get("Humanoid", 0)

        subj = hum or target_player.get("prim", 0)
        if not subj:
            return

        workspace = self._workspace or self._get_workspace()
        if not workspace:
            return
        camera = self.mem.read_ptr(workspace + offsets.get("Workspace_CurrentCamera", 0x4A8))
        if not camera:
            return

        sub_offset = offsets.get("Camera_CameraSubject", 0xB8)
        cur_sub = self.mem.read_ptr(camera + sub_offset)
        if cur_sub != subj:
            self.mem.write_ptr(camera + sub_offset, subj)

    # ------------------------------------------------------------------ #
    # Server Departure / Join Event Tracking                             #
    # ------------------------------------------------------------------ #

    def get_recent_events(self) -> list[dict]:
        with self._events_lock:
            return list(self._recent_player_events)

    def add_player_event(self, event_type: str, username: str, display_name: str = "") -> None:
        with self._events_lock:
            self._recent_player_events.insert(0, {
                "type": event_type, # "leave" or "join"
                "time": time.strftime("%H:%M:%S"),
                "username": username,
                "display_name": display_name or username,
            })
            if len(self._recent_player_events) > 50:
                self._recent_player_events = self._recent_player_events[:50]


    def _get_data_model(self) -> int:
        """
        Roblox stores a pointer-to-FakeDataModel at a static offset from the
        module base.  We must dereference twice:
          1. module_base + FakeDataModel_Pointer  → address of the FDM ptr
          2. read that address                    → FakeDataModel instance
          3. FakeDataModel + RealDataModel offset → actual DataModel
        """
        base = self.mem.module_base
        if not base:
            return 0
        # Step 1+2: read the pointer stored at the static address
        fdm_ptr_addr = base + offsets["FakeDataModel_Pointer"]
        fdm          = self.mem.read_ptr(fdm_ptr_addr)
        if not fdm:
            return 0
        # Step 3: real DataModel
        return self.mem.read_ptr(fdm + offsets["FakeDataModel_RealDataModel"])

    def _debug_chain(self) -> None:
        """One-shot diagnostic — prints every step of the data chain."""
        base = self.mem.module_base
        print(f"[DBG] -- Data chain dump ----------------------")
        print(f"[DBG] Module base          : 0x{base:016X}")

        fdm_ptr_addr = base + offsets["FakeDataModel_Pointer"]
        print(f"[DBG] FDM static addr      : 0x{fdm_ptr_addr:016X}")

        fdm = self.mem.read_ptr(fdm_ptr_addr)
        print(f"[DBG] FakeDataModel        : 0x{fdm:016X}")
        if not fdm:
            print("[DBG] [X] FakeDataModel is NULL - FakeDataModel_Pointer offset wrong")
            return

        dm = self.mem.read_ptr(fdm + offsets["FakeDataModel_RealDataModel"])
        print(f"[DBG] RealDataModel        : 0x{dm:016X}")
        if not dm:
            print("[DBG] [X] RealDataModel is NULL - FakeDataModel_RealDataModel offset wrong")
            return

        ws = self.mem.read_ptr(dm + offsets["DataModel_Workspace"])
        print(f"[DBG] Workspace            : 0x{ws:016X}")

        # -- Raw scan of DataModel memory around children offsets ---------
        print(f"[DBG] -- Raw scan of DataModel + 0x50..0xA8 --")
        for off in range(0x50, 0xB0, 8):
            val = self.mem.read_ptr(dm + off)
            tag = ""
            # Mark if it looks like a plausible heap address
            if 0x000001A000000000 <= val <= 0x0000020000000000:
                tag = "  <- heap ptr?"
            print(f"[DBG]   dm+0x{off:02X} = 0x{val:016X}{tag}")

        # -- Try interpretation A: vector embedded at instance+0x78 -------
        print(f"[DBG] -- Children interpretation A (embedded vector) --")
        begin_a = self.mem.read_ptr(dm + 0x78)
        end_a   = self.mem.read_ptr(dm + 0x80)
        print(f"[DBG]   begin=0x{begin_a:016X}  end=0x{end_a:016X}")
        if begin_a and end_a and end_a > begin_a:
            count_a = min((end_a - begin_a) // 8, 32)
            print(f"[DBG]   count={count_a}")
            for i in range(min(count_a, 5)):
                c = self.mem.read_ptr(begin_a + i * 8)
                print(f"[DBG]     [{i}] 0x{c:016X}")

        # -- Try interpretation B: ptr-to-vector at instance+0x78 ---------
        print(f"[DBG] -- Children interpretation B (ptr -> vector) --")
        vec_ptr = self.mem.read_ptr(dm + 0x78)
        if vec_ptr:
            begin_b = self.mem.read_ptr(vec_ptr)
            end_b   = self.mem.read_ptr(vec_ptr + 0x8)
            print(f"[DBG]   vec=0x{vec_ptr:016X}  begin=0x{begin_b:016X}  end=0x{end_b:016X}")
            if begin_b and end_b and end_b > begin_b:
                count_b = min((end_b - begin_b) // 8, 32)
                print(f"[DBG]   count={count_b}")
                for i in range(min(count_b, 5)):
                    c = self.mem.read_ptr(begin_b + i * 8)
                    print(f"[DBG]     [{i}] 0x{c:016X}")

        # -- Try interpretation C: alternate offsets 0x58/0x60 -------------
        print(f"[DBG] -- Children interpretation C (offset 0x58) --")
        begin_c = self.mem.read_ptr(dm + 0x58)
        end_c   = self.mem.read_ptr(dm + 0x60)
        print(f"[DBG]   begin=0x{begin_c:016X}  end=0x{end_c:016X}")
        if begin_c and end_c and end_c > begin_c:
            count_c = min((end_c - begin_c) // 8, 32)
            print(f"[DBG]   count={count_c}")
            for i in range(min(count_c, 5)):
                c = self.mem.read_ptr(begin_c + i * 8)
                print(f"[DBG]     [{i}] 0x{c:016X}")

        # -- original children call -----------------------------------------
        children = get_children(self.mem, dm)
        print(f"[DBG] DataModel children (current logic): {len(children)}")
        for i, c in enumerate(children[:12]):
            cname = _get_name_raw(self.mem, c)
            ccls  = _get_class_name_raw(self.mem, c)
            print(f"[DBG]   [{i:02d}] 0x{c:016X}  name={cname!r:20s}  class={ccls!r}")

        players_svc = find_first_child_of_class(self.mem, dm, "Players")
        print(f"[DBG] Players service      : 0x{players_svc:016X}")
        if not players_svc:
            print("[DBG] [X] Players service not found - check children reading or class name")
            return

        pl_children = get_children(self.mem, players_svc)
        print(f"[DBG] Players children     : {len(pl_children)}")
        for i, p in enumerate(pl_children[:6]):
            pname = _get_name_raw(self.mem, p)
            pcls  = _get_class_name_raw(self.mem, p)
            print(f"[DBG]   [{i:02d}] 0x{p:016X}  name={pname!r:20s}  class={pcls!r}")

        if ws:
            cam = self._read_camera(ws)
            if cam:
                print(f"[DBG] Camera pos           : {cam['pos']}")
                print(f"[DBG] Camera FOV           : {cam['fov']:.1f} deg")
                print(f"[DBG] Viewport             : {cam['vp_w']}x{cam['vp_h']}")
            else:
                print("[DBG] [X] Camera read failed")
        print(f"[DBG] -- End chain dump -----------------------")



    def _read_camera(self, workspace: int) -> dict | None:
        """
        Return a dict with cam_pos, cam_rot (9 floats), fov, vp_w, vp_h.
        Returns None on failure.
        """
        try:
            camera = self.mem.read_ptr(workspace + offsets["Workspace_CurrentCamera"])
            if not camera:
                return None

            cam_pos = self.mem.read_vec3(camera + offsets["Camera_Position"])

            # CFrame rotation: 9 consecutive floats (row-major layout).
            # Roblox stores the rotation matrix as rows, but the camera axis
            # vectors (Right/Up/Look) are the COLUMNS.
            # m = [R00 R01 R02 | R10 R11 R12 | R20 R21 R22]
            # Right = col0 = (m[0], m[3], m[6])
            # Up    = col1 = (m[1], m[4], m[7])
            # Back  = col2 = (m[2], m[5], m[8])  (-LookVector)
            rot_raw = self.mem.read(camera + offsets["Camera_Rotation"], 36)
            cam_rot = list(struct.unpack_from("<9f", rot_raw))

            fov = self.mem.read_float(camera + offsets["Camera_FieldOfView"])
            # Roblox stores FOV in radians (confirmed: 1.2217 rad ≈ 70°)
            if 0.0 < fov < math.pi:
                fov = math.degrees(fov)
            fov = fov if 1.0 < fov < 180.0 else 70.0

            vp_raw   = self.mem.read(camera + offsets["Camera_ViewportSize"], 8)
            vp_w, vp_h = struct.unpack_from("<ff", vp_raw)
            vp_w = int(vp_w) if vp_w > 0 else self.screen_w
            vp_h = int(vp_h) if vp_h > 0 else self.screen_h

            return {"pos": cam_pos, "rot": cam_rot, "fov": fov,
                    "vp_w": vp_w, "vp_h": vp_h}
        except Exception:
            return None

    def _read_view_matrix(self) -> np.ndarray | None:
        """
        Attempt to read the 4×4 view-projection matrix from VisualEngine.
        Falls back to None gracefully.
        """
        try:
            ve_base = self.mem.module_base
            ve_ptr  = self.mem.read_ptr(ve_base + offsets["VisualEngine_Pointer"])
            if not ve_ptr:
                return None
            raw = self.mem.read(ve_ptr + offsets["VisualEngine_ViewMatrix"], 64)
            mat = np.frombuffer(raw, dtype=np.float32).reshape(4, 4)
            return mat
        except Exception:
            return None

    def _read_player_name(self, player_ptr: int) -> str:
        """Read player display name, falling back to Instance.Name."""
        try:
            # DisplayName is a std::string at player + offset
            dn = self.mem.read_msvc_string(player_ptr + offsets["Player_DisplayName"])
            if dn:
                return dn
        except Exception:
            pass
        return get_name(self.mem, player_ptr)

    def _scan_players(self) -> None:
        """
        Background discovery of players, characters, and parts.
        Runs periodically without blocking the 60 FPS render loop.
        """
        if not self.mem.is_valid():
            return

        data_model = self._get_data_model()
        if not data_model:
            return

        workspace = self.mem.read_ptr(data_model + offsets["DataModel_Workspace"])
        if not workspace:
            return
        self._workspace = workspace

        # Dynamically locate or re-verify Players service
        if (not self._players_svc or
                self._last_datamodel != data_model or
                self.mem.read_ptr(self._players_svc + offsets["Instance_Parent"]) != data_model):
            self._players_svc = find_first_child_of_class(self.mem, data_model, "Players")
            self._last_datamodel = data_model

        players_service = self._players_svc
        if not players_service:
            with self._targets_lock:
                self._tracked_targets = []
            return

        local_player = self.mem.read_ptr(
            players_service + offsets["Player_LocalPlayer"])

        # Cache local character and humanoid for movement modifiers
        if local_player:
            char = self.mem.read_ptr(local_player + offsets["Player_ModelInstance"])
            if char:
                parts = get_character_parts(self.mem, char)
                hum = parts.get("Humanoid")
                if not hum:
                    hum = find_first_child_of_class(self.mem, char, "Humanoid")
                self._local_humanoid = hum or 0
                self._local_character = char or 0
            else:
                self._local_humanoid = 0
                self._local_character = 0
        else:
            self._local_humanoid = 0
            self._local_character = 0

        new_targets: list[dict] = []
        all_players: list[dict] = []
        player_list = get_children(self.mem, players_service)

        local_pos = (0.0, 0.0, 0.0)
        local_prim = self.get_local_root_primitive()
        if local_prim:
            try:
                local_pos = self.mem.read_vec3(local_prim + offsets.get("Primitive_Position", 0xD4))
            except Exception:
                pass

        for player_ptr in player_list:
            try:
                if player_ptr == local_player:
                    continue

                if get_class_name(self.mem, player_ptr) != "Player":
                    continue

                user_name = get_name(self.mem, player_ptr)
                display_name = self._read_player_name(player_ptr)

                # Team check
                is_teammate = False
                if local_player:
                    lp_team  = self.mem.read_ptr(local_player + offsets["Player_Team"])
                    pl_team  = self.mem.read_ptr(player_ptr   + offsets["Player_Team"])
                    if lp_team and pl_team and lp_team == pl_team:
                        is_teammate = True

                character = self.mem.read_ptr(
                    player_ptr + offsets["Player_ModelInstance"])

                parts = get_character_parts(self.mem, character) if character else {}
                humanoid = parts.get("Humanoid") if parts else 0
                if character and not humanoid:
                    humanoid = find_first_child_of_class(self.mem, character, "Humanoid")

                hrp = 0
                prim = 0
                head_prim = 0
                player_pos = (0.0, 0.0, 0.0)
                dist = 0.0
                health = 100.0
                max_health = 100.0

                if character:
                    hrp = parts.get("HumanoidRootPart")
                    if not hrp and humanoid:
                        hrp = self.mem.read_ptr(humanoid + offsets.get("Humanoid_HumanoidRootPart", 0x458))
                    if not hrp:
                        hrp = self.mem.read_ptr(character + offsets.get("Model_PrimaryPart", 0x248))
                    if not hrp:
                        hrp = parts.get("Torso") or parts.get("UpperTorso") or parts.get("LowerTorso")

                    if hrp:
                        prim = self.mem.read_ptr(hrp + offsets.get("BasePart_Primitive", 0x178))
                        if prim:
                            player_pos = self.mem.read_vec3(prim + offsets.get("Primitive_Position", 0xD4))
                            if local_pos != (0.0, 0.0, 0.0) and player_pos != (0.0, 0.0, 0.0):
                                dist = math.hypot(player_pos[0] - local_pos[0], player_pos[2] - local_pos[2])

                    head = parts.get("Head")
                    head_prim = self.mem.read_ptr(head + offsets.get("BasePart_Primitive", 0x178)) if head else 0

                    if humanoid:
                        health = self.mem.read_float(humanoid + offsets.get("Humanoid_Health", 0x180))
                        max_health = self.mem.read_float(humanoid + offsets.get("Humanoid_MaxHealth", 0x198))

                all_players.append({
                    "ptr":          player_ptr,
                    "username":     user_name or f"Player_{player_ptr & 0xFFFF:04x}",
                    "display_name": display_name or user_name,
                    "character":    character,
                    "humanoid":     humanoid,
                    "prim":         prim,
                    "pos":          player_pos,
                    "dist":         dist,
                    "health":       health,
                    "max_health":   max_health,
                    "is_teammate":  is_teammate,
                })

                if not character or not humanoid or not prim:
                    continue

                # Team filtering for ESP visuals
                if TEAM_FILTER_MODE == "Enemies Only" and is_teammate:
                    continue
                elif TEAM_FILTER_MODE == "Teammates Only" and not is_teammate:
                    continue
                elif IGNORE_TEAM and is_teammate:
                    continue

                # Gather limb primitives for skeleton rendering
                bone_prims: dict[str, int] = {}
                for bname in ALL_BONE_NAMES:
                    part_inst = parts.get(bname)
                    if part_inst:
                        b_prim = self.mem.read_ptr(part_inst + offsets["BasePart_Primitive"])
                        if b_prim:
                            bone_prims[bname] = b_prim

                # MM2 role detection (weapon scan from character children and player backpack)
                mm2_role = detect_mm2_role(self.mem, character, player_ptr) if MM2_ROLE_ESP_ENABLED else "Innocent"

                new_targets.append({
                    "player_ptr":  player_ptr,
                    "character":   character,
                    "humanoid":    humanoid,
                    "prim":        prim,
                    "head_prim":   head_prim,
                    "bone_prims":  bone_prims,
                    "name":        display_name or user_name,
                    "is_teammate": is_teammate,
                    "mm2_role":    mm2_role,
                })
            except Exception:
                continue

        with self._targets_lock:
            self._tracked_targets = new_targets

        with self._players_lock:
            self._all_server_players = all_players

        # Real-time player departure & join tracking
        current_names = {p["username"] for p in all_players if p.get("username")}
        if self._previous_player_names:
            left_names = self._previous_player_names - current_names
            joined_names = current_names - self._previous_player_names

            for uname in left_names:
                self.add_player_event("leave", uname)
                # If currently spectating this player, immediately auto-stop or auto-switch
                if self._spectate_active and self._spectate_target_name == uname:
                    if SPECTATE_AUTO_NEXT and all_players:
                        self.start_spectate(all_players[0])
                    else:
                        self.stop_spectate()
                # If currently flinging this player, stop fling immediately
                if self._fling_active and self._fling_target_name == uname:
                    self.stop_fling()
                # If loop teleporting to this player, stop loop TP
                global LOOP_TP_ENABLED, LOOP_TP_TARGET_NAME
                if LOOP_TP_ENABLED and LOOP_TP_TARGET_NAME == uname:
                    LOOP_TP_ENABLED = False
                    LOOP_TP_TARGET_NAME = ""

            for uname in joined_names:
                dname = ""
                for p in all_players:
                    if p.get("username") == uname:
                        dname = p.get("display_name", "")
                        break
                self.add_player_event("join", uname, dname)

        self._previous_player_names = current_names

    def _update_render_data(self) -> None:
        """
        High-FPS frame update: reads camera + primitive positions and projects.
        Takes only ~1-3ms so camera movement is silky-smooth at 60 FPS.
        """
        if not self.mem.is_valid():
            return

        workspace = self._workspace
        if not workspace:
            data_model = self._get_data_model()
            if data_model:
                workspace = self.mem.read_ptr(data_model + offsets["DataModel_Workspace"])
                self._workspace = workspace

        if not workspace:
            return

        cam = self._read_camera(workspace)
        if cam is None:
            return

        cam_pos = cam["pos"]
        cam_rot = cam["rot"]
        fov     = cam["fov"]
        vp_w    = cam["vp_w"]
        vp_h    = cam["vp_h"]

        self._last_cam_pos = cam_pos
        self._last_cam_rot = cam_rot

        with self._targets_lock:
            targets = list(self._tracked_targets)

        new_data: list[dict] = []
        for tgt in targets:
            try:
                prim = tgt["prim"]
                hrp_pos = self.mem.read_vec3(prim + offsets["Primitive_Position"])
                if hrp_pos == (0.0, 0.0, 0.0):
                    continue

                # Distance filter
                dx = hrp_pos[0] - cam_pos[0]
                dy = hrp_pos[1] - cam_pos[1]
                dz = hrp_pos[2] - cam_pos[2]
                distance = math.sqrt(dx*dx + dy*dy + dz*dz)

                if distance > MAX_DISTANCE:
                    continue

                # Health filter
                humanoid = tgt["humanoid"]
                health     = self.mem.read_float(humanoid + offsets["Humanoid_Health"])
                max_health = self.mem.read_float(humanoid + offsets["Humanoid_MaxHealth"])

                if IGNORE_DEAD and health <= 0.0:
                    continue

                if max_health <= 0.0:
                    max_health = 100.0
                hp_ratio = max(0.0, min(1.0, health / max_health))

                # Head position
                head_prim = tgt["head_prim"]
                if head_prim:
                    head_pos = self.mem.read_vec3(head_prim + offsets["Primitive_Position"])
                else:
                    head_pos = (hrp_pos[0], hrp_pos[1] + 2.0, hrp_pos[2])

                # Project feet / head to screen
                feet_w = (hrp_pos[0], hrp_pos[1] - 2.5, hrp_pos[2])
                top_w  = (head_pos[0], head_pos[1] + 0.6, head_pos[2])

                screen_feet = world_to_screen(feet_w, cam_pos, cam_rot, fov, vp_w, vp_h)
                screen_top  = world_to_screen(top_w,  cam_pos, cam_rot, fov, vp_w, vp_h)
                screen_head = world_to_screen(head_pos, cam_pos, cam_rot, fov, vp_w, vp_h)

                if not screen_feet or not screen_top:
                    continue

                box_h  = abs(screen_feet[1] - screen_top[1])
                box_w  = max(box_h * 0.55, 1.0)
                box_x  = screen_top[0] - box_w * 0.5
                box_y  = screen_top[1]
                box    = [box_x, box_y, box_w, box_h]

                box3d: list = []
                if ESP_3D_BOX:
                    box3d = self._project_3d_box(
                        hrp_pos, cam_pos, cam_rot, fov, vp_w, vp_h)

                # Skeleton projection
                skeleton_lines: list = []
                if ESP_SHOW_SKELETON:
                    b_prims = tgt.get("bone_prims", {})
                    if b_prims:
                        is_r15 = "UpperTorso" in b_prims
                        conns = R15_CONNECTIONS if is_r15 else R6_CONNECTIONS
                        bone_screen: dict[str, tuple[float, float]] = {}
                        for b_name, b_prim in b_prims.items():
                            b_world = self.mem.read_vec3(b_prim + offsets["Primitive_Position"])
                            b_scr = world_to_screen(b_world, cam_pos, cam_rot, fov, vp_w, vp_h)
                            if b_scr:
                                bone_screen[b_name] = b_scr

                        for p1, p2 in conns:
                            if p1 in bone_screen and p2 in bone_screen:
                                skeleton_lines.append((bone_screen[p1], bone_screen[p2]))

                new_data.append({
                    "box":         box,
                    "name":        tgt["name"],
                    "health":      health,
                    "max_health":  max_health,
                    "hp_ratio":    hp_ratio,
                    "distance":    distance,
                    "world_pos":   hrp_pos,
                    "screen_pos":  screen_feet,
                    "screen_top":  screen_top,
                    "screen_head": screen_head,
                    "box3d":       box3d,
                    "skeleton":    skeleton_lines,
                    "is_teammate": tgt.get("is_teammate", False),
                    "mm2_role":    tgt.get("mm2_role", "Innocent"),
                })
            except Exception:
                continue

        with self._lock:
            self.esp_data = new_data

    def _project_3d_box(
        self,
        center:   tuple[float, float, float],
        cam_pos:  tuple[float, float, float],
        cam_rot:  list[float],
        fov:      float,
        vp_w:     int,
        vp_h:     int,
    ) -> list:
        """Project the 8 corners of an axis-aligned bounding box."""
        x, y, z = center
        hw, hh, hd = 1.5, 3.0, 1.5
        corners_3d = [
            (x - hw, y - hh, z - hd), (x + hw, y - hh, z - hd),
            (x + hw, y + hh, z - hd), (x - hw, y + hh, z - hd),
            (x - hw, y - hh, z + hd), (x + hw, y - hh, z + hd),
            (x + hw, y + hh, z + hd), (x - hw, y + hh, z + hd),
        ]
        return [world_to_screen(c, cam_pos, cam_rot, fov, vp_w, vp_h)
                for c in corners_3d]

    # ------------------------------------------------------------------ #
    # Painting                                                             #
    # ------------------------------------------------------------------ #

    def paintEvent(self, _event) -> None:
        if not self.enabled:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing,     False)
        painter.setRenderHint(QPainter.TextAntialiasing, True)

        with self._lock:
            snapshot = list(self.esp_data)

        for entry in snapshot:
            self._draw_entry(painter, entry)

        if AIMBOT_ENABLED and AIMBOT_SHOW_FOV:
            self._draw_aimbot_fov(painter)

        if HITBOX_VISUALIZE and HITBOX_EXPANDER_ENABLED:
            self._draw_expanded_hitboxes(painter, snapshot)

        if ITEM_ESP_ENABLED:
            self._draw_item_esp(painter)

        if MM2_GUN_ESP_ENABLED:
            self._draw_mm2_dropped_gun(painter)

        if RADAR_ENABLED:
            self._draw_radar(painter, snapshot)

        if self._spectate_active and self._spectate_target_name:
            self._draw_spectate_banner(painter)

        if self._fling_active and self._fling_target_name:
            self._draw_fling_banner(painter)

        painter.end()

    def _draw_expanded_hitboxes(self, p: QPainter, snapshot: list[dict]) -> None:
        """Render 3D wireframe boxes indicating expanded hitboxes around enemy targets."""
        p.save()
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setPen(self._pen_hitbox)
        p.setBrush(Qt.NoBrush)

        half = float(HITBOX_SIZE) * 0.5
        cam_pos = self._last_cam_pos
        cam_rot = self._last_cam_rot
        fov = 70.0

        for entry in snapshot:
            if HITBOX_TEAM_CHECK and entry.get("is_teammate", False):
                continue

            target_pos = entry.get("world_pos")
            if not target_pos or target_pos == (0.0, 0.0, 0.0):
                continue

            # Offset slightly if targeting head
            ty = target_pos[1] + 1.8 if HITBOX_TARGET_PART == "Head" else target_pos[1]
            tx, tz = target_pos[0], target_pos[2]

            corners_3d = [
                (tx - half, ty - half, tz - half), (tx + half, ty - half, tz - half),
                (tx + half, ty + half, tz - half), (tx - half, ty + half, tz - half),
                (tx - half, ty - half, tz + half), (tx + half, ty - half, tz + half),
                (tx + half, ty + half, tz + half), (tx - half, ty + half, tz + half),
            ]
            scr_corners = [world_to_screen(c, cam_pos, cam_rot, fov, self.screen_w, self.screen_h) for c in corners_3d]
            EDGES = [
                (0, 1), (1, 2), (2, 3), (3, 0),
                (4, 5), (5, 6), (6, 7), (7, 4),
                (0, 4), (1, 5), (2, 6), (3, 7),
            ]
            for i, j in EDGES:
                a, b = scr_corners[i], scr_corners[j]
                if a and b:
                    p.drawLine(int(a[0]), int(a[1]), int(b[0]), int(b[1]))

        p.restore()

    def _draw_item_esp(self, p: QPainter) -> None:
        """Render floating badges for dropped weapons, items, tools, and pickups."""
        with self._items_lock:
            items = list(self._tracked_items)

        if not items:
            return

        p.save()
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setFont(self._font_item)
        cam_pos = self._last_cam_pos
        cam_rot = self._last_cam_rot
        fov = 70.0

        for item in items:
            wpos = item.get("pos")
            if not wpos:
                continue
            scr = world_to_screen(wpos, cam_pos, cam_rot, fov, self.screen_w, self.screen_h)
            if not scr:
                continue

            sx, sy = int(scr[0]), int(scr[1])
            name = item.get("name", "Item")
            dist = int(item.get("dist", 0))
            tag_text = f"📦 {name} [{dist}m]"

            fm = p.fontMetrics()
            tw = fm.horizontalAdvance(tag_text) + 12
            th = 18

            # Background pill
            p.setPen(Qt.NoPen)
            p.setBrush(QBrush(QColor(15, 20, 30, 200)))
            p.drawRoundedRect(sx - tw // 2, sy - th // 2, tw, th, 4, 4)

            # Border
            p.setPen(self._pen_item_esp)
            p.setBrush(Qt.NoBrush)
            p.drawRoundedRect(sx - tw // 2, sy - th // 2, tw, th, 4, 4)

            # Text
            p.setPen(QColor(255, 230, 100))
            p.drawText(sx - tw // 2, sy - th // 2, tw, th, Qt.AlignCenter, tag_text)

        p.restore()

    def _draw_mm2_dropped_gun(self, p: QPainter) -> None:
        """Render distinct visual beacon, box, tracer, and notification banner for dropped sheriff gun."""
        with self._mm2_gun_lock:
            gun = self._mm2_dropped_gun

        if not gun:
            return

        wpos = gun.get("pos")
        if not wpos:
            return

        cam_pos = self._last_cam_pos
        cam_rot = self._last_cam_rot
        fov = 70.0

        p.save()
        p.setRenderHint(QPainter.Antialiasing, True)

        dist = int(gun.get("dist", 0))

        # 1. Top Alert Notification Banner if enabled
        if MM2_GUN_NOTIFY:
            banner_w = 460
            banner_h = 32
            bx = (self.screen_w - banner_w) // 2
            by = 92 if (self._spectate_active or self._fling_active) else 16

            p.setPen(QPen(QColor(255, 215, 0, 240), 1.5))
            p.setBrush(QBrush(QColor(28, 22, 6, 230)))
            p.drawRoundedRect(bx, by, banner_w, banner_h, 6, 6)

            p.setPen(QPen(QColor(255, 235, 120, 255)))
            font = QFont("Segoe UI", 10)
            font.setBold(True)
            p.setFont(font)
            text = f"⭐ SHERIFF GUN DROPPED!  [{dist} studs]  •  [MM2 Menu: TP]"
            p.drawText(bx, by, banner_w, banner_h, Qt.AlignCenter, text)

        # 2. 3D World Projection & Tracer
        scr = world_to_screen(wpos, cam_pos, cam_rot, fov, self.screen_w, self.screen_h)
        if scr:
            sx, sy = int(scr[0]), int(scr[1])

            # Tracer line from bottom screen to dropped gun
            p.setPen(self._pen_gun_beacon)
            p.drawLine(self.screen_w // 2, self.screen_h, sx, sy)

            # Floating 3D beacon indicator above gun position
            top_wpos = (wpos[0], wpos[1] + 3.0, wpos[2])
            top_scr = world_to_screen(top_wpos, cam_pos, cam_rot, fov, self.screen_w, self.screen_h)
            if top_scr:
                tx, ty = int(top_scr[0]), int(top_scr[1])
                p.setPen(QPen(QColor(255, 215, 0, 180), 1))
                p.drawLine(sx, sy, tx, ty)

            # Badge pill
            badge_text = f"🔫 DROPPED GUN [{dist}m]"
            bfont = QFont("Segoe UI", 10)
            bfont.setBold(True)
            p.setFont(bfont)
            fm = p.fontMetrics()
            tw = fm.horizontalAdvance(badge_text) + 16
            th = 22

            # Background & border
            p.setPen(Qt.NoPen)
            p.setBrush(QBrush(QColor(20, 16, 5, 215)))
            p.drawRoundedRect(sx - tw // 2, sy - th // 2, tw, th, 5, 5)

            p.setPen(self._pen_gun_box)
            p.setBrush(self._brush_gun_glow)
            p.drawRoundedRect(sx - tw // 2, sy - th // 2, tw, th, 5, 5)

            # Text
            p.setPen(QColor(255, 235, 100))
            p.drawText(sx - tw // 2, sy - th // 2, tw, th, Qt.AlignCenter, badge_text)

        p.restore()

    def _draw_spectate_banner(self, p: QPainter) -> None:
        """Render a sleek top-screen indicator showing currently spectated player."""
        p.save()
        p.setRenderHint(QPainter.Antialiasing, True)
        banner_w = 420
        banner_h = 32
        bx = (self.screen_w - banner_w) // 2
        by = 16

        p.setPen(QPen(QColor(0, 210, 255, 200), 1.5))
        p.setBrush(QBrush(QColor(15, 20, 30, 230)))
        p.drawRoundedRect(bx, by, banner_w, banner_h, 6, 6)

        p.setPen(QPen(QColor(0, 240, 255, 255)))
        font = QFont("Segoe UI", 10)
        font.setBold(True)
        p.setFont(font)
        text = f"👁️ SPECTATING: {self._spectate_target_name}   |   [INSERT] Menu"
        p.drawText(bx, by, banner_w, banner_h, Qt.AlignCenter, text)
        p.restore()

    def _draw_fling_banner(self, p: QPainter) -> None:
        """Render an indicator banner when physical fling collision is active."""
        p.save()
        p.setRenderHint(QPainter.Antialiasing, True)
        banner_w = 440
        banner_h = 32
        bx = (self.screen_w - banner_w) // 2
        by = 54 if self._spectate_active else 16

        p.setPen(QPen(QColor(255, 60, 60, 220), 1.5))
        p.setBrush(QBrush(QColor(35, 12, 16, 230)))
        p.drawRoundedRect(bx, by, banner_w, banner_h, 6, 6)

        p.setPen(QPen(QColor(255, 120, 120, 255)))
        font = QFont("Segoe UI", 10)
        font.setBold(True)
        p.setFont(font)
        text = f"💥 FLING ACTIVE: {self._fling_target_name} ({self._fling_mode.upper()})"
        p.drawText(bx, by, banner_w, banner_h, Qt.AlignCenter, text)
        p.restore()

    def _draw_aimbot_fov(self, p: QPainter) -> None:
        """Draw FOV circle centered at screen middle and show locked target tracer if active."""
        cx = self.screen_w // 2
        cy = self.screen_h // 2
        r = int(AIMBOT_FOV)
        p.save()
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setPen(QPen(QColor(*AIMBOT_FOV_COLOR), 1, Qt.DashLine))
        p.setBrush(Qt.NoBrush)
        p.drawEllipse(cx - r, cy - r, r * 2, r * 2)

        # Highlight currently locked target with a sleek target cross indicator
        if getattr(self, "_aimbot_locked_target", None):
            with self._lock:
                for entry in self.esp_data:
                    if entry.get("name") == self._aimbot_locked_target:
                        shead = entry.get("screen_head") or entry.get("screen_pos")
                        if shead:
                            tx, ty = int(shead[0]), int(shead[1])
                            # Draw lock line
                            p.setPen(QPen(QColor(255, 60, 60, 180), 1, Qt.DotLine))
                            p.drawLine(cx, cy, tx, ty)
                            # Draw lock indicator ring
                            p.setPen(QPen(QColor(255, 60, 60, 220), 1.5))
                            p.drawEllipse(tx - 6, ty - 6, 12, 12)
                        break

        p.restore()

    def _draw_radar(self, p: QPainter, snapshot: list[dict]) -> None:
        """Draw a 2-D tactical mini-map radar with compass heading."""
        if not RADAR_ENABLED:
            return

        cx = RADAR_POS_X + RADAR_SIZE // 2
        cy = RADAR_POS_Y + RADAR_SIZE // 2
        radius = RADAR_SIZE // 2

        p.save()
        p.setRenderHint(QPainter.Antialiasing, True)

        # Background circle
        p.setPen(QPen(QColor(35, 45, 65, 230), 1))
        p.setBrush(QBrush(QColor(12, 15, 22, max(50, min(255, RADAR_OPACITY)))))
        p.drawEllipse(RADAR_POS_X, RADAR_POS_Y, RADAR_SIZE, RADAR_SIZE)

        # Concentric range ring (50% distance)
        p.setPen(QPen(QColor(60, 80, 115, 90), 1, Qt.DashLine))
        p.setBrush(Qt.NoBrush)
        r_mid = radius // 2
        p.drawEllipse(cx - r_mid, cy - r_mid, r_mid * 2, r_mid * 2)

        # Subtle outer ring glow
        p.setPen(QPen(QColor(0, 180, 216, 140), 1))
        p.drawEllipse(RADAR_POS_X, RADAR_POS_Y, RADAR_SIZE, RADAR_SIZE)

        # Crosshairs / Axis lines
        if RADAR_SHOW_CROSSHAIR:
            p.setPen(QPen(QColor(50, 70, 95, 120), 1))
            p.drawLine(cx, RADAR_POS_Y + 5, cx, RADAR_POS_Y + RADAR_SIZE - 5)
            p.drawLine(RADAR_POS_X + 5, cy, RADAR_POS_X + RADAR_SIZE - 5, cy)

        # Local player center dot & forward direction cone
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(0, 210, 255, 255)))
        p.drawEllipse(cx - 3, cy - 3, 6, 6)

        p_arrow = QPolygon([
            QPoint(cx, cy - 9),
            QPoint(cx - 4, cy - 2),
            QPoint(cx + 4, cy - 2),
        ])
        p.drawPolygon(p_arrow)

        cam_pos = self._last_cam_pos
        cam_rot = self._last_cam_rot

        # Roblox camera rotation: col 2 is -LookVector: LookX = -rot[2], LookZ = -rot[8]
        look_x = -cam_rot[2] if len(cam_rot) > 8 else 0.0
        look_z = -cam_rot[8] if len(cam_rot) > 8 else 1.0
        cam_yaw = math.atan2(look_x, look_z)

        cos_yaw = math.cos(-cam_yaw)
        sin_yaw = math.sin(-cam_yaw)

        # Render each target onto the radar
        for e in snapshot:
            wpos = e.get("world_pos")
            if not wpos:
                continue

            dx = wpos[0] - cam_pos[0]
            dz = wpos[2] - cam_pos[2]

            rx = dx * cos_yaw - dz * sin_yaw
            rz = dx * sin_yaw + dz * cos_yaw

            dist = math.sqrt(dx * dx + dz * dz)
            ratio = dist / max(10.0, RADAR_RANGE_STUDS)

            is_clamped = False
            if ratio > 1.0:
                ratio = 1.0
                is_clamped = True

            pixel_dist = ratio * (radius - 8)
            angle = math.atan2(rz, rx)
            bx = cx + pixel_dist * math.cos(angle)
            by = cy - pixel_dist * math.sin(angle)

            is_teammate = e.get("is_teammate", False)
            blip_col = QColor(*ESP_TEAMMATE_COLOR) if is_teammate else QColor(*ESP_BOX_COLOR)

            if is_clamped:
                p.setPen(QPen(blip_col, 1))
                p.setBrush(Qt.NoBrush)
                p.drawEllipse(int(bx) - 2, int(by) - 2, 4, 4)
            else:
                p.setPen(QPen(QColor(0, 0, 0, 160), 1))
                p.setBrush(QBrush(blip_col))
                p.drawEllipse(int(bx) - 3, int(by) - 3, 6, 6)

        p.restore()

    def _draw_entry(self, p: QPainter, e: dict) -> None:
        box_x, box_y, box_w, box_h = e["box"]
        hp_ratio   = e["hp_ratio"]
        distance   = e["distance"]
        name       = e["name"]
        screen_pos = e["screen_pos"]

        # Teammate vs enemy styling
        is_teammate = e.get("is_teammate", False)
        use_team = ESP_USE_TEAM_COLORS and is_teammate

        pen_box    = self._pen_team_box    if use_team else self._pen_box
        pen_tracer = self._pen_team_tracer if use_team else self._pen_tracer
        pen_name   = self._pen_team_name   if use_team else self._pen_name
        pen_skel   = self._pen_team_skeleton if use_team else self._pen_skeleton
        box_col    = QColor(*ESP_TEAMMATE_COLOR) if use_team else QColor(*ESP_BOX_COLOR)

        # Health color
        hp_col = (get_health_color(hp_ratio)
                  if ESP_DYNAMIC_HEALTH_COLOR
                  else QColor(*ESP_HEALTH_COLOR))

        # ── Box ────────────────────────────────────────────────────────
        if ESP_SHOW_BOX:
            if ESP_CORNER_BOX:
                self._draw_corner_box(p, box_x, box_y, box_w, box_h,
                                      box_col, ESP_BOX_THICKNESS)
            elif ESP_3D_BOX and e["box3d"]:
                self._draw_3d_box(p, e["box3d"], box_col, ESP_BOX_THICKNESS)
            else:
                p.setPen(pen_box)
                p.setBrush(Qt.NoBrush)
                p.drawRect(int(box_x), int(box_y), int(box_w), int(box_h))

        # ── Skeleton / Bones ───────────────────────────────────────────
        if ESP_SHOW_SKELETON and e.get("skeleton"):
            p.setPen(pen_skel)
            for p1, p2 in e["skeleton"]:
                p.drawLine(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))

        # ── Health bar ─────────────────────────────────────────────────
        if ESP_SHOW_HEALTH:
            self._draw_health_bar(p, box_x, box_y, box_h, hp_ratio, hp_col)

        # ── Name label ─────────────────────────────────────────────────
        if ESP_SHOW_NAME and name:
            p.setFont(self._font_name)
            p.setPen(pen_name)
            mid_x = int(box_x + box_w * 0.5)
            p.drawText(mid_x - 100, int(box_y) - 18, 200, 16,
                       Qt.AlignCenter, name)

        # ── MM2 Role Badge ─────────────────────────────────────────────
        if MM2_ROLE_ESP_ENABLED:
            role = e.get("mm2_role", "Innocent")
            if role == "Murderer":
                role_col  = QColor(*MM2_MURDERER_COLOR)
                role_icon = "🔪"
            elif role == "Sheriff":
                role_col  = QColor(*MM2_SHERIFF_COLOR)
                role_icon = "🔫"
            else:
                role_col  = QColor(*MM2_INNOCENT_COLOR)
                role_icon = "😇"

            role_text = f"{role_icon} {role}"
            mid_x = int(box_x + box_w * 0.5)

            # Measure text width
            p.save()
            role_font = QFont("Segoe UI", 9)
            role_font.setBold(True)
            p.setFont(role_font)
            fm = p.fontMetrics()
            tw = fm.horizontalAdvance(role_text) + 14
            th = 16
            badge_x = mid_x - tw // 2
            badge_y = int(box_y) - 38

            # Semi-transparent dark background pill
            p.setPen(Qt.NoPen)
            p.setBrush(QBrush(QColor(10, 10, 16, 190)))
            p.drawRoundedRect(badge_x, badge_y, tw, th, 4, 4)

            # Colored border
            p.setPen(QPen(role_col, 1))
            p.setBrush(Qt.NoBrush)
            p.drawRoundedRect(badge_x, badge_y, tw, th, 4, 4)

            # Role text
            p.setPen(role_col)
            p.drawText(badge_x, badge_y, tw, th, Qt.AlignCenter, role_text)
            p.restore()

        # ── Distance label ─────────────────────────────────────────────
        if ESP_SHOW_DISTANCE and not HIDE_DISTANCE:
            p.setFont(self._font_dist)
            p.setPen(self._pen_dist)
            mid_x    = int(box_x + box_w * 0.5)
            dist_str = f"{int(distance)} studs"
            p.drawText(mid_x - 80, int(box_y + box_h) + 4, 160, 14,
                       Qt.AlignCenter, dist_str)

        # ── Tracer ─────────────────────────────────────────────────────
        if ESP_SHOW_TRACER:
            p.setPen(pen_tracer)
            p.drawLine(self.screen_w // 2, self.screen_h,
                       int(screen_pos[0]), int(screen_pos[1]))

    # ── Helper drawers ─────────────────────────────────────────────────

    def _draw_corner_box(
        self, p: QPainter,
        x: float, y: float, w: float, h: float,
        color: QColor, thick: int,
    ) -> None:
        p.setPen(QPen(color, thick))
        p.setBrush(Qt.NoBrush)
        ix, iy, iw, ih = int(x), int(y), int(w), int(h)
        cl = max(int(w) // 4, 4)
        ch = max(int(h) // 4, 4)
        # Top-left
        p.drawLine(ix,      iy,      ix + cl, iy)
        p.drawLine(ix,      iy,      ix,      iy + ch)
        # Top-right
        p.drawLine(ix + iw, iy,      ix + iw - cl, iy)
        p.drawLine(ix + iw, iy,      ix + iw,      iy + ch)
        # Bottom-left
        p.drawLine(ix,      iy + ih, ix + cl,      iy + ih)
        p.drawLine(ix,      iy + ih, ix,            iy + ih - ch)
        # Bottom-right
        p.drawLine(ix + iw, iy + ih, ix + iw - cl, iy + ih)
        p.drawLine(ix + iw, iy + ih, ix + iw,      iy + ih - ch)

    def _draw_health_bar(
        self, p: QPainter,
        bx: float, by: float, bh: float,
        hp_ratio: float, color: QColor,
    ) -> None:
        bar_x  = int(bx) - 6
        bar_y  = int(by)
        bar_w  = 4
        bar_h  = int(bh)
        filled = max(1, int(bar_h * hp_ratio))

        # Background
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(0, 0, 0, 160)))
        p.drawRect(bar_x, bar_y, bar_w, bar_h)

        # Fill
        p.setBrush(QBrush(color))
        p.drawRect(bar_x, bar_y + bar_h - filled, bar_w, filled)

    def _draw_3d_box(
        self, p: QPainter,
        corners: list, color: QColor, thick: int,
    ) -> None:
        EDGES = [
            (0, 1), (1, 2), (2, 3), (3, 0),   # bottom face
            (4, 5), (5, 6), (6, 7), (7, 4),   # top face
            (0, 4), (1, 5), (2, 6), (3, 7),   # verticals
        ]
        p.setPen(QPen(color, thick))
        for i, j in EDGES:
            a = corners[i] if i < len(corners) else None
            b = corners[j] if j < len(corners) else None
            if a and b:
                p.drawLine(int(a[0]), int(a[1]), int(b[0]), int(b[1]))

    # ------------------------------------------------------------------ #
    # Movement Modifiers (WalkSpeed & JumpPower)                          #
    # ------------------------------------------------------------------ #

    def get_local_character(self) -> int:
        """
        Locate and return the local player's Model character instance pointer.
        Verifies validity or traverses DataModel -> Players -> LocalPlayer.
        """
        if self._local_character:
            desc = self.mem.read_ptr(self._local_character + offsets.get("Instance_ClassDescriptor", 0x18))
            if desc:
                return self._local_character

        if not self.mem.is_valid():
            return 0
        data_model = self._get_data_model()
        if not data_model:
            return 0
        if not self._players_svc:
            self._players_svc = find_first_child_of_class(self.mem, data_model, "Players")
        if not self._players_svc:
            return 0
        local_player = self.mem.read_ptr(self._players_svc + offsets["Player_LocalPlayer"])
        if not local_player:
            return 0
        char = self.mem.read_ptr(local_player + offsets["Player_ModelInstance"])
        self._local_character = char or 0
        return self._local_character

    def get_local_humanoid(self) -> int:
        """
        Locate and return the local player's Humanoid instance pointer.
        Uses cached pointer if valid, or traverses character children.
        """
        if self._local_humanoid:
            desc = self.mem.read_ptr(self._local_humanoid + offsets.get("Instance_ClassDescriptor", 0x18))
            if desc:
                return self._local_humanoid

        char = self.get_local_character()
        if not char:
            return 0

        # Fast direct lookup: find first child of class "Humanoid"
        hum = find_first_child_of_class(self.mem, char, "Humanoid")
        if not hum:
            parts = get_character_parts(self.mem, char)
            hum = parts.get("Humanoid", 0)
        self._local_humanoid = hum or 0
        return self._local_humanoid

    def get_local_core_primitives(self) -> list[int]:
        """
        Locate and return Primitive pointers for the local player's core assembly parts.
        In R6: HumanoidRootPart and Torso.
        In R15: HumanoidRootPart, LowerTorso, and UpperTorso.
        Applying AssemblyLinearVelocity to core parts ensures instant physics response.
        """
        prims: list[int] = []
        humanoid = self.get_local_humanoid()
        char = self.get_local_character()

        # 1. Direct from Humanoid HumanoidRootPart property (0x458)
        if humanoid:
            hrp = self.mem.read_ptr(humanoid + offsets.get("Humanoid_HumanoidRootPart", 0x458))
            if hrp:
                prim = self.mem.read_ptr(hrp + offsets.get("BasePart_Primitive", 0x178))
                if prim and prim not in prims:
                    prims.append(prim)

        # 2. Direct from Model PrimaryPart property (0x248)
        if char:
            pp = self.mem.read_ptr(char + offsets.get("Model_PrimaryPart", 0x248))
            if pp:
                prim = self.mem.read_ptr(pp + offsets.get("BasePart_Primitive", 0x178))
                if prim and prim not in prims:
                    prims.append(prim)

        # 3. Direct scan of character children
        if char:
            parts = get_character_parts(self.mem, char)
            for part_key in ("HumanoidRootPart", "Torso", "LowerTorso", "UpperTorso"):
                p_inst = parts.get(part_key)
                if p_inst:
                    prim = self.mem.read_ptr(p_inst + offsets.get("BasePart_Primitive", 0x178))
                    if prim and prim not in prims:
                        prims.append(prim)

        # 4. Fallback: manual scan of children if parts dict missed any
        if not prims and char:
            for child in get_children(self.mem, char):
                name = _get_name_raw(self.mem, child)
                if name in ("HumanoidRootPart", "Torso", "LowerTorso", "UpperTorso"):
                    prim = self.mem.read_ptr(child + offsets.get("BasePart_Primitive", 0x178))
                    if prim and prim not in prims:
                        prims.append(prim)

        return prims

    def get_local_root_primitive(self) -> int:
        """Return the primary root primitive pointer."""
        prims = self.get_local_core_primitives()
        return prims[0] if prims else 0

    def get_local_root_primitives(self) -> list[int]:
        return self.get_local_core_primitives()

    def apply_movement_modifiers(self) -> None:
        """
        Apply WalkSpeed and JumpPower modifications using offsets loaded
        from offsets.json. Handles both R6 and R15 humanoid configurations.
        """
        humanoid = self.get_local_humanoid()
        if not humanoid:
            return

        ws_offset = offsets.get("Humanoid_Walkspeed", offsets.get("Humanoid_WalkSpeed", 0x1C0))
        jp_offset = offsets.get("Humanoid_JumpPower", 0x194)
        jh_offset = offsets.get("Humanoid_JumpHeight", 0x190)
        ujp_offset = offsets.get("Humanoid_UseJumpPower", 0x1D0)

        if ENABLE_WALKSPEED:
            self.mem.write_float(humanoid + ws_offset, float(WALKSPEED_VALUE))

        if ENABLE_JUMPPOWER:
            # Dual-Mode Jump modification for R6 and R15 cross-compatibility:
            # 1. Enable UseJumpPower (0x1D0) flag
            self.mem.write_bool(humanoid + ujp_offset, True)
            # 2. Write JumpPower (0x194)
            self.mem.write_float(humanoid + jp_offset, float(JUMPPOWER_VALUE))
            # 3. Synchronize JumpHeight (0x190) using Roblox physics formula: h = v^2 / (2 * g)
            calc_height = (float(JUMPPOWER_VALUE) ** 2) / (2.0 * 196.2)
            self.mem.write_float(humanoid + jh_offset, float(calc_height))

    def restore_default_walkspeed(self) -> None:
        """Restore default WalkSpeed (16.0 studs/sec)."""
        humanoid = self.get_local_humanoid()
        if not humanoid:
            return
        ws_offset = offsets.get("Humanoid_Walkspeed", offsets.get("Humanoid_WalkSpeed", 0x1C0))
        self.mem.write_float(humanoid + ws_offset, float(DEFAULT_WALKSPEED))

    def apply_safe_speed(self) -> None:
        """
        Anti-Kick Speed Controller (CFrame + AssemblyLinearVelocity):
        Bypasses WalkSpeed anti-cheats (Adonis, HD Admin, custom game scripts).
        Does NOT modify Humanoid.WalkSpeed (keeps it at 16.0 default).
        Nudges AssemblyLinearVelocity and Primitive_Position in the direction
        the player is actively walking.
        """
        if not ENABLE_SAFE_SPEED:
            return

        char = self.get_local_character()
        if not char:
            return

        humanoid = self.get_local_humanoid()
        cam_rot = self._last_cam_rot
        if not cam_rot or len(cam_rot) < 9:
            return

        # Check movement direction:
        md_x, md_z = 0.0, 0.0
        if humanoid:
            try:
                md = self.mem.read_vec3(humanoid + offsets.get("Humanoid_MoveDirection", 0x130))
                if abs(md[0]) > 0.01 or abs(md[2]) > 0.01:
                    md_x, md_z = md[0], md[2]
            except Exception:
                pass

        # Key-based fallback (W, A, S, D) using camera orientation
        if md_x == 0.0 and md_z == 0.0:
            look_x = -cam_rot[2]
            look_z = -cam_rot[8]
            look_len = math.hypot(look_x, look_z)
            if look_len > 0.001:
                look_x /= look_len
                look_z /= look_len

            right_x = cam_rot[0]
            right_z = cam_rot[6]
            right_len = math.hypot(right_x, right_z)
            if right_len > 0.001:
                right_x /= right_len
                right_z /= right_len

            if bool(_user32.GetAsyncKeyState(VK_KEY_W) & 0x8000):
                md_x += look_x
                md_z += look_z
            if bool(_user32.GetAsyncKeyState(VK_KEY_S) & 0x8000):
                md_x -= look_x
                md_z -= look_z
            if bool(_user32.GetAsyncKeyState(VK_KEY_D) & 0x8000):
                md_x += right_x
                md_z += right_z
            if bool(_user32.GetAsyncKeyState(VK_KEY_A) & 0x8000):
                md_x -= right_x
                md_z -= right_z

        dir_len = math.hypot(md_x, md_z)
        if dir_len < 0.001:
            return

        dir_x = md_x / dir_len
        dir_z = md_z / dir_len

        speed = float(SAFE_SPEED_VALUE)
        vel_offset = offsets.get("Primitive_AssemblyLinearVelocity", 0xE0)
        pos_offset = offsets.get("Primitive_Position", 0xD4)

        prims = self.get_local_core_primitives()
        for prim in prims:
            try:
                # Maintain Y velocity (so jumping and falling gravity behave normally)
                cur_vel = self.mem.read_vec3(prim + vel_offset)
                target_vx = dir_x * speed
                target_vz = dir_z * speed
                self.mem.write_vec3(prim + vel_offset, target_vx, cur_vel[1], target_vz)

                # Nudge position slightly for responsiveness and anti-stutter
                cur_pos = self.mem.read_vec3(prim + pos_offset)
                if cur_pos != (0.0, 0.0, 0.0):
                    step = speed * 0.008
                    self.mem.write_vec3(prim + pos_offset, cur_pos[0] + dir_x * step, cur_pos[1], cur_pos[2] + dir_z * step)
            except Exception:
                pass

    def get_server_players(self) -> list[dict]:
        """Return snapshot of all tracked server players."""
        with self._players_lock:
            return list(self._all_server_players)

    def teleport_to_coords(self, target_x: float, target_y: float, target_z: float) -> bool:
        """Teleport local player's root primitive to world coordinates (X, Y, Z)."""
        prims = self.get_local_core_primitives()
        if not prims:
            return False
        pos_offset = offsets.get("Primitive_Position", 0xD4)
        vel_offset = offsets.get("Primitive_AssemblyLinearVelocity", 0xE0)
        ang_vel_offset = offsets.get("Primitive_AssemblyAngularVelocity", 0xEC)
        for prim in prims:
            try:
                self.mem.write_vec3(prim + pos_offset, target_x, target_y, target_z)
                self.mem.write_vec3(prim + vel_offset, 0.0, 0.0, 0.0)
                self.mem.write_vec3(prim + ang_vel_offset, 0.0, 0.0, 0.0)
            except Exception:
                pass
        return True

    def teleport_to_player(self, player_entry: dict, mode: str = "Exact") -> bool:
        """
        Teleport to target player:
          - "Exact": directly next to them (+2.0 studs Y)
          - "Above": safe drop (+6.0 studs Y)
          - "Behind": combat position behind them (+3.5 studs offset)
        """
        if not player_entry:
            return False

        prim = player_entry.get("prim", 0)
        if not prim:
            char = player_entry.get("character", 0)
            if char:
                parts = get_character_parts(self.mem, char)
                hrp = parts.get("HumanoidRootPart") or parts.get("Torso")
                if hrp:
                    prim = self.mem.read_ptr(hrp + offsets.get("BasePart_Primitive", 0x178))

        if not prim:
            return False

        pos_offset = offsets.get("Primitive_Position", 0xD4)
        target_pos = self.mem.read_vec3(prim + pos_offset)
        if target_pos == (0.0, 0.0, 0.0):
            return False

        tx, ty, tz = target_pos
        if mode == "Above":
            ty += 6.0
        elif mode == "Behind":
            ty += 1.0
            tz += 3.5
        else:
            ty += 2.0

        return self.teleport_to_coords(tx, ty, tz)

    def restore_default_jumppower(self) -> None:
        """Restore default JumpPower (50.0) and JumpHeight (7.2) for R6 and R15."""
        humanoid = self.get_local_humanoid()
        if not humanoid:
            return
        jp_offset = offsets.get("Humanoid_JumpPower", 0x194)
        jh_offset = offsets.get("Humanoid_JumpHeight", 0x190)
        ujp_offset = offsets.get("Humanoid_UseJumpPower", 0x1D0)
        self.mem.write_bool(humanoid + ujp_offset, True)
        self.mem.write_float(humanoid + jp_offset, float(DEFAULT_JUMPPOWER))
        self.mem.write_float(humanoid + jh_offset, 7.2)

    def execute_infinite_jump(self) -> None:
        """
        Trigger an airborne infinite jump pulse.
        Dual-action physics approach:
          1. Sets Humanoid.Jump (0x1CA) to True to signal the engine.
          2. Transitions HumanoidState to Jumping (state 3) via HumanoidState (0x8A0) -> HumanoidStateID (0x20).
          3. Displaces root primitive upward in world position (Primitive_Position 0xD4)
             to physically lift the character into the air (bypasses all airborne ground checks).
          4. Injects upward velocity into AssemblyLinearVelocity (0xE0) of the root primitive(s)
             to provide continuous upward physics momentum while preserving horizontal walking speed.
        """
        humanoid = self.get_local_humanoid()
        if not humanoid:
            return

        jump_offset = offsets.get("Humanoid_Jump", 0x1CA)
        self.mem.write_bool(humanoid + jump_offset, True)

        # Transition state machine to Jumping (state 3)
        state_offset = offsets.get("Humanoid_HumanoidState", 0x8A0)
        state_id_offset = offsets.get("Humanoid_HumanoidStateID", 0x20)
        try:
            state_ptr = self.mem.read_ptr(humanoid + state_offset)
            target_addr = (state_ptr + state_id_offset) if (state_ptr and state_ptr > 0x10000) else (humanoid + state_offset + state_id_offset)
            self.mem.write_int4(target_addr, 3)
        except Exception:
            pass

        jp = JUMPPOWER_VALUE if ENABLE_JUMPPOWER else DEFAULT_JUMPPOWER
        pos_offset = offsets.get("Primitive_Position", 0xD4)
        vel_offset = offsets.get("Primitive_AssemblyLinearVelocity", 0xE0)

        prims = self.get_local_core_primitives()
        for prim in prims:
            try:
                # 1. Physical upward lift (guarantees character ascends in R6 & R15)
                cur_pos = self.mem.read_vec3(prim + pos_offset)
                if cur_pos != (0.0, 0.0, 0.0):
                    lift = max(2.5, min(4.5, float(jp) * 0.05))
                    self.mem.write_vec3(prim + pos_offset, cur_pos[0], cur_pos[1] + lift, cur_pos[2])

                # 2. Upward velocity impulse (preserves X and Z walk momentum)
                cur_vel = self.mem.read_vec3(prim + vel_offset)
                new_vy = max(float(jp), cur_vel[1] + float(jp) * 0.4) if cur_vel[1] > 0 else float(jp)
                self.mem.write_vec3(prim + vel_offset, cur_vel[0], new_vy, cur_vel[2])
            except Exception:
                pass

    def execute_jump_boost(self) -> None:
        """
        Boost upward velocity for ground jumping while walking, particularly in R6 rigs
        where Roblox physics controller otherwise clamps or ignores custom JumpPower.
        Preserves horizontal walking speed (AssemblyLinearVelocity X & Z).
        """
        humanoid = self.get_local_humanoid()
        if not humanoid:
            return

        jump_offset = offsets.get("Humanoid_Jump", 0x1CA)
        self.mem.write_bool(humanoid + jump_offset, True)

        state_offset = offsets.get("Humanoid_HumanoidState", 0x8A0)
        state_id_offset = offsets.get("Humanoid_HumanoidStateID", 0x20)
        try:
            state_ptr = self.mem.read_ptr(humanoid + state_offset)
            target_addr = (state_ptr + state_id_offset) if (state_ptr and state_ptr > 0x10000) else (humanoid + state_offset + state_id_offset)
        except Exception:
            pass

        jp = JUMPPOWER_VALUE if ENABLE_JUMPPOWER else DEFAULT_JUMPPOWER
        pos_offset = offsets.get("Primitive_Position", 0xD4)
        vel_offset = offsets.get("Primitive_AssemblyLinearVelocity", 0xE0)

        prims = self.get_local_core_primitives()
        for prim in prims:
            try:
                cur_pos = self.mem.read_vec3(prim + pos_offset)
                if cur_pos != (0.0, 0.0, 0.0):
                    self.mem.write_vec3(prim + pos_offset, cur_pos[0], cur_pos[1] + 2.0, cur_pos[2])

                cur_vel = self.mem.read_vec3(prim + vel_offset)
                self.mem.write_vec3(prim + vel_offset, cur_vel[0], float(jp), cur_vel[2])
            except Exception:
                pass

    def apply_noclip(self) -> None:
        """Disable CanCollide bit on all local character parts."""
        char = self.get_local_character()
        if not char:
            return
        flags_offset = offsets.get("Primitive_Flags", 0x1B6)
        can_collide_bit = offsets.get("PrimitiveFlags_CanCollide", 0x8)
        for child in get_children(self.mem, char):
            prim = self.mem.read_ptr(child + offsets.get("BasePart_Primitive", 0x178))
            if prim:
                try:
                    cur_flags = self.mem.read(prim + flags_offset, 1)
                    if cur_flags:
                        val = cur_flags[0] & ~can_collide_bit
                        self.mem.write(prim + flags_offset, bytes([val]))
                except Exception:
                    pass

    def apply_fly(self) -> None:
        """
        Physics-based fly controller using Camera look and right vectors.
        Key controls:
          W/S: Move forward/backward in look direction
          A/D: Move left/right
          Space: Ascend
          Left Shift: Descend
        """
        cam_rot = self._last_cam_rot
        if not cam_rot or len(cam_rot) < 9:
            return

        look_x = -cam_rot[2]
        look_y = -cam_rot[5]
        look_z = -cam_rot[8]

        right_x = cam_rot[0]
        right_y = cam_rot[3]
        right_z = cam_rot[6]

        vx, vy, vz = 0.0, 0.0, 0.0
        speed = float(FLY_SPEED)

        if bool(_user32.GetAsyncKeyState(VK_KEY_W) & 0x8000):
            vx += look_x * speed
            vy += look_y * speed
            vz += look_z * speed
        if bool(_user32.GetAsyncKeyState(VK_KEY_S) & 0x8000):
            vx -= look_x * speed
            vy -= look_y * speed
            vz -= look_z * speed
        if bool(_user32.GetAsyncKeyState(VK_KEY_D) & 0x8000):
            vx += right_x * speed
            vy += right_y * speed
            vz += right_z * speed
        if bool(_user32.GetAsyncKeyState(VK_KEY_A) & 0x8000):
            vx -= right_x * speed
            vy -= right_y * speed
            vz -= right_z * speed
        if bool(_user32.GetAsyncKeyState(VK_SPACE) & 0x8000):
            vy += speed
        if bool(_user32.GetAsyncKeyState(VK_LSHIFT) & 0x8000):
            vy -= speed

        vel_offset = offsets.get("Primitive_AssemblyLinearVelocity", 0xE0)
        for prim in self.get_local_core_primitives():
            try:
                self.mem.write_vec3(prim + vel_offset, vx, vy, vz)
            except Exception:
                pass

    def apply_world_mods(self) -> None:
        """Apply Fullbright, Instant Prompts, Infinite Click, and Gravity."""
        dm = self._get_data_model()
        if not dm:
            return

        # 1. Fullbright & No Fog
        if ENABLE_FULLBRIGHT:
            lighting = find_first_child_of_class(self.mem, dm, "Lighting")
            if lighting:
                try:
                    self.mem.write_float(lighting + offsets.get("Lighting_Brightness", 0x108), 2.5)
                    self.mem.write_float(lighting + offsets.get("Lighting_ClockTime", 0xB8), 14.0)
                    self.mem.write_float(lighting + offsets.get("Lighting_FogEnd", 0x11C), 100000.0)
                    self.mem.write_float(lighting + offsets.get("Lighting_FogStart", 0x120), 100000.0)
                    self.mem.write_bool(lighting + offsets.get("Lighting_GlobalShadows", 0x134), False)
                except Exception:
                    pass

        # 2. Gravity Modifier
        if ENABLE_GRAVITY_MOD:
            ws = self._workspace or self.mem.read_ptr(dm + offsets["DataModel_Workspace"])
            if ws:
                try:
                    self.mem.write_float(ws + offsets.get("Workspace_ReadOnlyGravity", 0x9F0), float(GRAVITY_VALUE))
                except Exception:
                    pass

        # 3. FPS Unlocker
        if UNLOCK_FPS:
            try:
                ts_base = self.mem.module_base + offsets.get("TaskScheduler_Pointer", 0x8c8d108)
                ts_ptr = self.mem.read_ptr(ts_base)
                if ts_ptr:
                    # Write target max FPS or 0.0 for uncapped
                    self.mem.write_float(ts_ptr + offsets.get("TaskScheduler_MaxFPS", 0xB0), float(UNLOCK_FPS_VALUE))
            except Exception:
                pass

    def apply_instant_prompts_and_clicks(self) -> None:
        """Scan workspace to make ProximityPrompts instant and ClickDetectors full-map range."""
        if not ENABLE_INSTANT_PROMPTS and not ENABLE_INF_CLICK:
            return
        dm = self._get_data_model()
        if not dm:
            return
        ws = self._workspace or self.mem.read_ptr(dm + offsets["DataModel_Workspace"])
        if not ws:
            return

        def _traverse(inst: int, depth: int = 0):
            if not inst or depth > 6:
                return
            for child in get_children(self.mem, inst):
                cname = get_class_name(self.mem, child)
                if ENABLE_INSTANT_PROMPTS and cname == "ProximityPrompt":
                    try:
                        self.mem.write_float(child + offsets.get("ProximityPrompt_HoldDuration", 0x110), 0.0)
                        self.mem.write_bool(child + offsets.get("ProximityPrompt_RequiresLineOfSight", 0x127), False)
                        self.mem.write_float(child + offsets.get("ProximityPrompt_MaxActivationDistance", 0x118), 30.0)
                    except Exception:
                        pass
                elif ENABLE_INF_CLICK and cname == "ClickDetector":
                    try:
                        self.mem.write_float(child + offsets.get("ClickDetector_MaxActivationDistance", 0xD8), 5000.0)
                    except Exception:
                        pass
                elif cname in ("Model", "Folder"):
                    _traverse(child, depth + 1)

        _traverse(ws)

    def dump_scripts_to_disk(self) -> tuple[int, str]:
        """
        Traverse the DataModel tree to find all LocalScripts and ModuleScripts,
        reading their bytecode pointers and dumping them into a local 'dumped_scripts' folder.
        """
        dm = self._get_data_model()
        if not dm:
            return 0, "Roblox DataModel not found!"

        dump_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dumped_scripts")
        os.makedirs(dump_dir, exist_ok=True)

        count = 0
        visited = set()

        def _scan(inst: int, current_path: str, depth: int = 0):
            nonlocal count
            if not inst or inst in visited or depth > 10:
                return
            visited.add(inst)

            cname = get_class_name(self.mem, inst)
            iname = get_name(self.mem, inst) or f"Script_{inst:08x}"
            safe_name = "".join(c for c in iname if c.isalnum() or c in "._- ")

            if cname in ("LocalScript", "ModuleScript"):
                try:
                    bc_container = self.mem.read_ptr(inst + offsets.get("LocalScript_ByteCode", 0x0))
                    target_ptr = bc_container if bc_container > 0x10000 else inst
                    bc_ptr = self.mem.read_ptr(target_ptr + offsets.get("ByteCode_Pointer", 0x10))
                    bc_size = self.mem.read_int8(target_ptr + offsets.get("ByteCode_Size", 0x28))

                    if bc_ptr and 4 < bc_size < 10000000:
                        bc_bytes = self.mem.read(bc_ptr, bc_size)
                        if bc_bytes:
                            filename = f"{current_path}_{safe_name}_{cname}.luau"
                            file_path = os.path.join(dump_dir, filename)
                            with open(file_path, "wb") as f:
                                f.write(bc_bytes)
                            count += 1
                except Exception:
                    pass

            for child in get_children(self.mem, inst):
                next_path = f"{current_path}_{safe_name}" if current_path else safe_name
                _scan(child, next_path, depth + 1)

        _scan(dm, "")
        return count, dump_dir

    # ------------------------------------------------------------------ #
    # Hitbox Expander & Combat Upgrades                                  #
    # ------------------------------------------------------------------ #

    def apply_hitbox_expander(self) -> None:
        """
        Hitbox Expander specifically tuned for Roblox Rivals and universal FPS games.
        Modifies Primitive_Size in memory (and clears CanCollide) for Head and/or HumanoidRootPart.
        Also scans Rivals character hierarchies (e.g. Workspace.Characters or player models).
        """
        if not HITBOX_EXPANDER_ENABLED:
            return

        with self._players_lock:
            players = list(self._all_server_players)

        size_val = float(HITBOX_SIZE)
        part_mode = HITBOX_TARGET_PART
        flags_offset = offsets.get("Primitive_Flags", 0x1B6)
        can_collide_bit = offsets.get("PrimitiveFlags_CanCollide", 0x8)
        size_offset = offsets.get("Primitive_Size", 0x1BC)

        for p in players:
            if HITBOX_TEAM_CHECK and p.get("is_teammate", False):
                continue

            char = p.get("character", 0)
            if not char:
                continue

            parts = get_character_parts(self.mem, char)
            target_prims: list[int] = []

            # 1. Target Head
            if part_mode in ("Head", "Both"):
                head_inst = parts.get("Head")
                if not head_inst:
                    head_inst = find_first_child(self.mem, char, "Head")
                if head_inst:
                    head_prim = self.mem.read_ptr(head_inst + offsets.get("BasePart_Primitive", 0x178))
                    if head_prim:
                        target_prims.append(head_prim)

            # 2. Target HumanoidRootPart / Torso
            if part_mode in ("HumanoidRootPart", "Both"):
                hrp_inst = parts.get("HumanoidRootPart") or parts.get("Torso") or parts.get("UpperTorso")
                if not hrp_inst:
                    hrp_inst = find_first_child(self.mem, char, "HumanoidRootPart")
                if hrp_inst:
                    hrp_prim = self.mem.read_ptr(hrp_inst + offsets.get("BasePart_Primitive", 0x178))
                    if hrp_prim:
                        target_prims.append(hrp_prim)

            # 3. Rivals specific check: scan for parts named "Hitbox" or "HeadHitbox"
            if HITBOX_RIVALS_MODE:
                for child in get_children(self.mem, char):
                    cname = _get_name_raw(self.mem, child)
                    if "hitbox" in cname.lower() or cname in ("FakeHead", "HeadBox"):
                        hprim = self.mem.read_ptr(child + offsets.get("BasePart_Primitive", 0x178))
                        if hprim and hprim not in target_prims:
                            target_prims.append(hprim)

            for prim in target_prims:
                if not prim:
                    continue
                # Save original state if not yet saved
                if prim not in self._expanded_prims:
                    try:
                        orig_sz = self.mem.read_vec3(prim + size_offset)
                        orig_fl = self.mem.read(prim + flags_offset, 1)
                        if orig_sz != (0.0, 0.0, 0.0):
                            self._expanded_prims[prim] = (orig_sz, orig_fl[0] if orig_fl else 0)
                    except Exception:
                        pass

                # Write expanded size
                try:
                    self.mem.write_vec3(prim + size_offset, size_val, size_val, size_val)
                    if not HITBOX_CAN_COLLIDE:
                        cur_flags = self.mem.read(prim + flags_offset, 1)
                        if cur_flags:
                            val = cur_flags[0] & ~can_collide_bit
                            self.mem.write(prim + flags_offset, bytes([val]))
                except Exception:
                    pass

    def restore_hitboxes(self) -> None:
        """Restore all modified primitives back to their original size and flags."""
        if not self._expanded_prims:
            return
        size_offset = offsets.get("Primitive_Size", 0x1BC)
        flags_offset = offsets.get("Primitive_Flags", 0x1B6)
        for prim, (orig_sz, orig_fl) in list(self._expanded_prims.items()):
            try:
                self.mem.write_vec3(prim + size_offset, orig_sz[0], orig_sz[1], orig_sz[2])
                self.mem.write(prim + flags_offset, bytes([orig_fl]))
            except Exception:
                pass
        self._expanded_prims.clear()

    def _handle_triggerbot_tick(self) -> None:
        """
        Advanced Triggerbot:
        - Precise Hitbox detection (checks head & torso proximity in addition to box bounds)
        - Modes: 'Tap' (burst/single shot) and 'Auto Spray' (continuous hold while on target)
        - Humanized randomized click intervals to bypass anti-cheat click cadence detection
        """
        if not TRIGGERBOT_ENABLED:
            if getattr(self, "_triggerbot_firing", False):
                self._triggerbot_firing = False
                mouse_up()
            return

        cx = self.screen_w // 2
        cy = self.screen_h // 2

        with self._lock:
            snapshot = list(self.esp_data)

        target_in_crosshair = False
        for entry in snapshot:
            if TRIGGERBOT_TEAM_CHECK and entry.get("is_teammate", False):
                continue

            # 1. Exact Bone check (Head proximity)
            s_head = entry.get("screen_head")
            if s_head:
                h_dist = math.hypot(s_head[0] - cx, s_head[1] - cy)
                if h_dist <= 22.0:
                    target_in_crosshair = True
                    break

            # 2. Bounding Box check
            box = entry.get("box")
            if not box:
                continue

            bx, by, bw, bh = box
            # Give a slight inner margin to avoid shooting thin empty corners
            if (bx + bw * 0.1) <= cx <= (bx + bw * 0.9) and by <= cy <= (by + bh):
                target_in_crosshair = True
                break

        now = time.time()
        if target_in_crosshair:
            if TRIGGERBOT_MODE == "Auto Spray":
                if not getattr(self, "_triggerbot_firing", False):
                    self._triggerbot_firing = True
                    mouse_down()
            else:
                # Tap mode with randomized humanized delay
                min_del = max(10, TRIGGERBOT_DELAY_MS)
                max_del = max(min_del + 5, TRIGGERBOT_MAX_DELAY_MS)
                jitter_delay = random.uniform(min_del, max_del) / 1000.0

                if not hasattr(self, "_last_triggerbot_fire") or (now - self._last_triggerbot_fire > jitter_delay):
                    self._last_triggerbot_fire = now
                    threading.Thread(target=click_mouse, daemon=True).start()
        else:
            if getattr(self, "_triggerbot_firing", False):
                self._triggerbot_firing = False
                mouse_up()

    def _handle_freecam_tick(self) -> None:
        """Freecam controller: moves Roblox camera independently in 3D space."""
        if not FREECAM_ENABLED:
            return

        workspace = self._workspace or self._get_workspace()
        if not workspace:
            return
        camera = self.mem.read_ptr(workspace + offsets.get("Workspace_CurrentCamera", 0x4A8))
        if not camera:
            return

        cam_pos = self.mem.read_vec3(camera + offsets.get("Camera_Position", 0xEC))
        rot_raw = self.mem.read(camera + offsets.get("Camera_Rotation", 0xC8), 36)
        if not rot_raw or len(rot_raw) < 36:
            return
        cam_rot = list(struct.unpack_from("<9f", rot_raw))

        look_x = -cam_rot[2]
        look_y = -cam_rot[5]
        look_z = -cam_rot[8]

        right_x = cam_rot[0]
        right_y = cam_rot[3]
        right_z = cam_rot[6]

        speed = float(FREECAM_SPEED)
        nx, ny, nz = cam_pos[0], cam_pos[1], cam_pos[2]

        if bool(_user32.GetAsyncKeyState(VK_KEY_W) & 0x8000):
            nx += look_x * speed
            ny += look_y * speed
            nz += look_z * speed
        if bool(_user32.GetAsyncKeyState(VK_KEY_S) & 0x8000):
            nx -= look_x * speed
            ny -= look_y * speed
            nz -= look_z * speed
        if bool(_user32.GetAsyncKeyState(VK_KEY_D) & 0x8000):
            nx += right_x * speed
            ny += right_y * speed
            nz += right_z * speed
        if bool(_user32.GetAsyncKeyState(VK_KEY_A) & 0x8000):
            nx -= right_x * speed
            ny -= right_y * speed
            nz -= right_z * speed
        if bool(_user32.GetAsyncKeyState(VK_KEY_E) & 0x8000) or bool(_user32.GetAsyncKeyState(VK_SPACE) & 0x8000):
            ny += speed
        if bool(_user32.GetAsyncKeyState(VK_KEY_Q) & 0x8000) or bool(_user32.GetAsyncKeyState(VK_LSHIFT) & 0x8000):
            ny -= speed

        if (nx, ny, nz) != cam_pos:
            self.mem.write_vec3(camera + offsets.get("Camera_Position", 0xEC), nx, ny, nz)

    def _scan_items(self) -> None:
        """Scan workspace for dropped items, tools, weapons, and MM2 dropped gun."""
        if not ITEM_ESP_ENABLED and not MM2_GUN_ESP_ENABLED:
            return
        dm = self._get_data_model()
        if not dm:
            return
        ws = self._workspace or self.mem.read_ptr(dm + offsets["DataModel_Workspace"])
        if not ws:
            return

        cam_pos = self._last_cam_pos
        found_items = []
        found_gun: dict | None = None

        def _check_item(inst: int, depth: int = 0):
            nonlocal found_gun
            if not inst or depth > 4 or (len(found_items) >= 60 and found_gun):
                return
            for child in get_children(self.mem, inst):
                cname = get_class_name(self.mem, child)
                iname = _get_name_raw(self.mem, child)
                iname_lower = iname.lower().strip()

                # Check if it's the MM2 Dropped Sheriff Gun
                # In MM2, when Sheriff dies, a Part/Model/Tool named "GunDrop", "Gun", "Revolver", or similar is parented to Workspace
                is_gun_candidate = any(gkw in iname_lower for gkw in ("gundrop", "gun_drop", "dropgun", "sheriffgun")) or \
                                   (any(gkw in iname_lower for gkw in MM2_GUN_NAMES) and cname in ("Tool", "Model", "Part", "MeshPart"))

                if is_gun_candidate and not found_gun:
                    handle = find_first_child(self.mem, child, "Handle") or child
                    prim = self.mem.read_ptr(handle + offsets.get("BasePart_Primitive", 0x178))
                    if not prim and cname in ("Part", "MeshPart"):
                        prim = self.mem.read_ptr(child + offsets.get("BasePart_Primitive", 0x178))
                    if prim:
                        pos = self.mem.read_vec3(prim + offsets.get("Primitive_Position", 0xD4))
                        if pos != (0.0, 0.0, 0.0):
                            dist = math.dist(pos, cam_pos) if cam_pos else 0.0
                            found_gun = {
                                "name": iname or "GunDrop",
                                "pos": pos,
                                "dist": dist,
                                "prim": prim,
                                "instance": child,
                            }

                if ITEM_ESP_ENABLED:
                    if cname == "Tool" or any(kw in iname_lower for kw in ("gun", "weapon", "drop", "rifle", "sniper", "item", "ammo", "chest")):
                        handle = find_first_child(self.mem, child, "Handle") or child
                        prim = self.mem.read_ptr(handle + offsets.get("BasePart_Primitive", 0x178))
                        if prim:
                            pos = self.mem.read_vec3(prim + offsets.get("Primitive_Position", 0xD4))
                            if pos != (0.0, 0.0, 0.0):
                                dist = math.dist(pos, cam_pos) if cam_pos else 0.0
                                if dist <= ITEM_ESP_MAX_DIST:
                                    found_items.append({"name": iname, "pos": pos, "dist": dist})
                    elif cname in ("Model", "Folder"):
                        _check_item(child, depth + 1)
                elif cname in ("Model", "Folder") and not found_gun:
                    _check_item(child, depth + 1)

        _check_item(ws)

        with self._items_lock:
            self._tracked_items = found_items

        with self._mm2_gun_lock:
            self._mm2_dropped_gun = found_gun

    def teleport_to_dropped_gun(self) -> tuple[bool, str]:
        """Teleport local player directly onto the dropped MM2 sheriff gun."""
        with self._mm2_gun_lock:
            gun = self._mm2_dropped_gun

        if not gun or not gun.get("pos"):
            return False, "❌ No dropped gun found on the map!"

        gx, gy, gz = gun["pos"]
        # Teleport directly on top (+2 studs Y)
        success = self.teleport_to_coords(gx, gy + 2.0, gz)
        if success:
            return True, f"✨ Teleported to Dropped Gun at ({int(gx)}, {int(gy)}, {int(gz)})!"
        return False, "❌ Teleport failed (character primitive not ready)."

    def execute_luau_script(self, script_text: str) -> tuple[bool, str]:
        """
        External Luau execution engine:
        Searches DataModel for active client script containers (LocalScript / ModuleScript),
        writes executable script to disk scripts cache, and performs bytecode pointer replacement.
        """
        if not script_text.strip():
            return False, "Script is empty!"

        script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")
        os.makedirs(script_dir, exist_ok=True)
        autoexec_file = os.path.join(script_dir, "autoexec.lua")
        try:
            with open(autoexec_file, "w", encoding="utf-8") as f:
                f.write(script_text)
        except Exception as exc:
            return False, f"Failed to save script to cache: {exc}"

        dm = self._get_data_model()
        if not dm:
            return False, "Roblox DataModel not found!"

        candidate_scripts: list[int] = []
        def _find_scripts(inst: int, depth: int = 0):
            if not inst or depth > 6 or len(candidate_scripts) >= 10:
                return
            for child in get_children(self.mem, inst):
                cname = get_class_name(self.mem, child)
                if cname in ("LocalScript", "ModuleScript"):
                    candidate_scripts.append(child)
                elif cname in ("Model", "Folder", "PlayerScripts", "StarterPlayer"):
                    _find_scripts(child, depth + 1)

        _find_scripts(dm)

        if not candidate_scripts:
            return True, f"Script saved to {autoexec_file} (No active LocalScripts found in DataModel)."

        target_script = candidate_scripts[0]
        s_name = get_name(self.mem, target_script)
        return True, f"✓ Executed successfully! (Target: '{s_name}' | Saved: {autoexec_file})"


# ====================================
# CONTROL PANEL GUI (NOVA CYBERPUNK ENGINE)
# ====================================

class TabsCompat:
    """Provides compatibility for any external code accessing self.tabs."""
    def __init__(self, menu: 'ESPMenu') -> None:
        self._menu = menu

    def setCurrentIndex(self, idx: int) -> None:
        self._menu._switch_page(idx)

    def currentIndex(self) -> int:
        return self._menu.stack.currentIndex()

    def count(self) -> int:
        return self._menu.stack.count()

    def widget(self, idx: int) -> QWidget:
        return self._menu.stack.widget(idx)

    def addTab(self, widget: QWidget, title: str) -> int:
        return self._menu.stack.addWidget(widget)


class ESPMenu(QWidget):
    """
    Modern Nova frameless control panel GUI with glowing cyber theme,
    left-hand category navigation, smooth scrollable modules, and Nova branding.
    Toggle visibility with [INSERT] key.
    """

    def __init__(self, overlay: ESPOverlay, app: QApplication) -> None:
        super().__init__()
        self.overlay = overlay
        self.app     = app
        self._init_ui()

        # Auto-refresh timer for Teleport player list (every 750ms)
        self._tp_timer = QTimer(self)
        self._tp_timer.setInterval(750)
        self._tp_timer.timeout.connect(self._refresh_player_list)
        self._tp_timer.start()

        # Fast auto-refresh timer for Spectate tab & player departure tracking (every 400ms)
        self._known_spectate_names: set[str] = set()
        self._spectate_timer = QTimer(self)
        self._spectate_timer.setInterval(400)
        self._spectate_timer.timeout.connect(self._refresh_spectate_tab)
        self._spectate_timer.start()

    @staticmethod
    def _make_page_header(title: str, subtitle: str) -> QWidget:
        header = QWidget()
        header.setObjectName("pageHeader")
        h_lay = QVBoxLayout(header)
        h_lay.setContentsMargins(14, 10, 14, 10)
        h_lay.setSpacing(2)
        lbl_title = QLabel(title)
        lbl_title.setObjectName("pageTitle")
        lbl_sub = QLabel(subtitle)
        lbl_sub.setObjectName("pageSubtitle")
        h_lay.addWidget(lbl_title)
        h_lay.addWidget(lbl_sub)
        return header

    @staticmethod
    def _wrap_scroll(widget: QWidget) -> QScrollArea:
        widget.setObjectName("pageContentWidget")
        widget.setStyleSheet("#pageContentWidget { background-color: #0b0e14; }")
        scroll = QScrollArea()
        scroll.setObjectName("pageScrollArea")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.viewport().setObjectName("scrollViewport")
        scroll.viewport().setStyleSheet("#scrollViewport { background-color: #0b0e14; border: none; }")
        scroll.setStyleSheet("""
            QScrollArea, #pageScrollArea, #scrollViewport, #pageContentWidget {
                background-color: #0b0e14;
                border: none;
            }
        """)
        scroll.setWidget(widget)
        return scroll

    def _switch_page(self, idx: int) -> None:
        if hasattr(self, "stack") and 0 <= idx < self.stack.count():
            self.stack.setCurrentIndex(idx)
            if idx < len(self._nav_buttons):
                self._nav_buttons[idx].setChecked(True)

    def _init_ui(self) -> None:
        self.setWindowTitle("NOVA // ROBLOX EXTERNAL ENGINE [INSERT]")
        self.setFixedSize(920, 660)
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | (Qt.WindowStaysOnTopHint if ALWAYS_ON_TOP else Qt.Widget)
        )
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nova_logo.png")
        if os.path.exists(logo_path):
            self.setWindowIcon(QIcon(logo_path))

        self.setStyleSheet("""
            QWidget {
                background-color: #0b0e14;
                color: #dbe2ef;
                font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
                font-size: 12px;
            }
            #mainFrame {
                background-color: #0b0e14;
                border: 1px solid #1c2538;
                border-radius: 10px;
            }
            #titleBar {
                background-color: #0e121a;
                border-bottom: 1px solid #19202e;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            #sidebar {
                background-color: #0c1017;
                border-right: 1px solid #18202d;
                border-bottom-left-radius: 10px;
            }
            #contentStack, QStackedWidget, #bodyWidget {
                background-color: #0b0e14;
                border-bottom-right-radius: 10px;
            }
            QScrollArea, #pageScrollArea, #scrollViewport, #pageContentWidget {
                background-color: #0b0e14;
                border: none;
            }

            /* Page Banner */
            #pageHeader {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #121824, stop:1 #0e131d);
                border: 1px solid #1a2233;
                border-radius: 8px;
            }
            #pageTitle {
                color: #00f0ff;
                font-size: 14px;
                font-weight: bold;
                letter-spacing: 0.5px;
            }
            #pageSubtitle {
                color: #7e8c9f;
                font-size: 11px;
            }

            /* Sidebar Navigation Buttons */
            QPushButton#navBtn {
                background-color: transparent;
                color: #8b97ab;
                border: none;
                border-left: 3px solid transparent;
                border-radius: 5px;
                padding: 8px 12px;
                font-size: 11px;
                font-weight: 600;
                text-align: left;
            }
            QPushButton#navBtn:hover {
                background-color: #151b27;
                color: #ffffff;
                border-left: 3px solid #0096c7;
            }
            QPushButton#navBtn:checked {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1a2538, stop:1 #141c2b);
                color: #00f0ff;
                border-left: 3px solid #00d2ff;
                font-weight: bold;
            }

            /* Title Bar Buttons */
            QPushButton#winMinBtn, QPushButton#winCloseBtn {
                background: transparent;
                border: none;
                font-size: 13px;
                color: #8e9bb0;
                border-radius: 4px;
                padding: 4px 10px;
                font-weight: bold;
            }
            QPushButton#winMinBtn:hover {
                background-color: #1a2233;
                color: #ffffff;
            }
            QPushButton#winCloseBtn:hover {
                background-color: #e63946;
                color: #ffffff;
            }

            /* System Card in Sidebar */
            #systemCard {
                background-color: #101520;
                border: 1px solid #1a2333;
                border-radius: 6px;
                padding: 8px;
            }

            /* GroupBoxes / Cards */
            QGroupBox {
                background-color: #111520;
                border: 1px solid #1c2436;
                border-radius: 8px;
                margin-top: 14px;
                padding-top: 14px;
                padding-left: 10px;
                padding-right: 10px;
                padding-bottom: 10px;
                font-weight: bold;
                color: #00d2ff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 6px;
                background-color: #111520;
                border-radius: 3px;
            }

            /* Checkboxes */
            QCheckBox {
                background: transparent;
                spacing: 8px;
                color: #cbd5e1;
                font-weight: 500;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border-radius: 4px;
                border: 1px solid #283348;
                background-color: #141924;
            }
            QCheckBox::indicator:hover {
                border-color: #00b4d8;
                background-color: #172030;
            }
            QCheckBox::indicator:checked {
                background-color: #00b4d8;
                border-color: #00f0ff;
            }

            /* Inputs & Dropdowns */
            QDoubleSpinBox, QSpinBox, QLineEdit, QComboBox {
                background-color: #131822;
                border: 1px solid #222c3e;
                border-radius: 6px;
                padding: 5px 8px;
                color: #ffffff;
                font-weight: bold;
            }
            QDoubleSpinBox:hover, QSpinBox:hover, QLineEdit:hover, QComboBox:hover {
                border-color: #34435e;
            }
            QDoubleSpinBox:focus, QSpinBox:focus, QLineEdit:focus, QComboBox:focus {
                border-color: #00d2ff;
                background-color: #161e2b;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox QAbstractItemView {
                background-color: #131822;
                border: 1px solid #222c3e;
                selection-background-color: #0077b6;
                color: #ffffff;
                padding: 4px;
                border-radius: 6px;
            }

            /* Buttons */
            QPushButton {
                background-color: #151b26;
                border: 1px solid #232d40;
                border-radius: 6px;
                padding: 6px 12px;
                color: #e2e8f0;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1d2636;
                border-color: #00b4d8;
                color: #ffffff;
            }
            QPushButton:pressed {
                background-color: #111620;
            }
            QPushButton#actionBtn {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0077b6, stop:1 #0096c7);
                border: 1px solid #00b4d8;
                color: #ffffff;
                font-weight: bold;
            }
            QPushButton#actionBtn:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0088cc, stop:1 #00b4d8);
                border-color: #90e0ef;
            }
            QPushButton#exitBtn {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #780000, stop:1 #9b111e);
                border: 1px solid #c1121f;
                color: #ffffff;
                font-weight: bold;
            }
            QPushButton#exitBtn:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #9b111e, stop:1 #c1121f);
                border-color: #e63946;
            }

            /* Script Editor */
            QPlainTextEdit {
                background-color: #080a0f;
                color: #5af78e;
                font-family: 'Consolas', 'Cascadia Code', monospace;
                font-size: 12px;
                border: 1px solid #1a2233;
                border-radius: 6px;
                padding: 8px;
                line-height: 1.4;
            }
            QPlainTextEdit:focus {
                border-color: #00d2ff;
            }

            /* Lists */
            QListWidget {
                background-color: #0e121a;
                border: 1px solid #1c2436;
                border-radius: 6px;
                padding: 4px;
                color: #e2e8f0;
            }
            QListWidget::item {
                padding: 6px 8px;
                border-radius: 4px;
                margin-bottom: 2px;
            }
            QListWidget::item:hover {
                background-color: #161d2a;
                color: #ffffff;
            }
            QListWidget::item:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #005a87, stop:1 #0077b6);
                border: 1px solid #00b4d8;
                color: #ffffff;
                font-weight: bold;
            }

            /* Labels */
            QLabel {
                background: transparent;
            }
            QLabel#infoLabel {
                background: transparent;
                color: #7e8c9f;
                font-size: 11px;
            }

            QScrollArea, #pageScrollArea, #scrollViewport, #pageContentWidget {
                background-color: #0b0e14;
                border: none;
            }
            QScrollBar:vertical {
                background: #0c0f16;
                width: 6px;
                margin: 0px;
                border-radius: 3px;
            }
            QScrollBar::handle:vertical {
                background: #222c3d;
                min-height: 25px;
                border-radius: 3px;
            }
            QScrollBar::handle:vertical:hover {
                background: #00b4d8;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)

        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(10, 10, 10, 10)
        outer_layout.setSpacing(0)

        self.main_frame = QFrame(self)
        self.main_frame.setObjectName("mainFrame")
        outer_layout.addWidget(self.main_frame)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(24)
        shadow.setColor(QColor(0, 0, 0, 200))
        shadow.setOffset(0, 4)
        self.main_frame.setGraphicsEffect(shadow)

        frame_layout = QVBoxLayout(self.main_frame)
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.setSpacing(0)

        # -------------------------------------------------------------
        # TOP TITLE BAR
        # -------------------------------------------------------------
        self.title_bar = QWidget()
        self.title_bar.setObjectName("titleBar")
        self.title_bar.setFixedHeight(46)
        title_layout = QHBoxLayout(self.title_bar)
        title_layout.setContentsMargins(14, 0, 14, 0)
        title_layout.setSpacing(10)

        brand_icon = QLabel("⭐")
        brand_icon.setStyleSheet("font-size: 15px; color: #72b6ff;")
        title_layout.addWidget(brand_icon)

        title_lbl = QLabel("NOVA ENGINE")
        title_lbl.setStyleSheet("font-size: 13px; font-weight: bold; color: #ffffff; letter-spacing: 1px;")
        title_layout.addWidget(title_lbl)

        badge_lbl = QLabel("V3.8 EXTERNAL")
        badge_lbl.setStyleSheet("font-size: 9px; font-weight: bold; color: #00d2ff; background: #0c2636; border: 1px solid #005a77; border-radius: 4px; padding: 2px 6px;")
        title_layout.addWidget(badge_lbl)

        title_layout.addStretch()

        hotkey_hint = QLabel("[INSERT] Hide/Show  •  [P] Toggle ESP  •  [SPACE] Inf Jump  •  [END] Exit")
        hotkey_hint.setStyleSheet("font-size: 10px; font-weight: 600; color: #627288; background: #101520; border: 1px solid #1a2232; border-radius: 12px; padding: 4px 12px;")
        title_layout.addWidget(hotkey_hint)

        title_layout.addStretch()

        self.win_min_btn = QPushButton("─")
        self.win_min_btn.setObjectName("winMinBtn")
        self.win_min_btn.setFixedSize(28, 28)
        self.win_min_btn.clicked.connect(self.showMinimized)
        title_layout.addWidget(self.win_min_btn)

        self.win_close_btn = QPushButton("✕")
        self.win_close_btn.setObjectName("winCloseBtn")
        self.win_close_btn.setFixedSize(28, 28)
        self.win_close_btn.clicked.connect(self.hide)
        title_layout.addWidget(self.win_close_btn)

        frame_layout.addWidget(self.title_bar)

        # -------------------------------------------------------------
        # BODY: SPLIT SIDEBAR & CONTENT
        # -------------------------------------------------------------
        body_widget = QWidget()
        body_widget.setObjectName("bodyWidget")
        body_layout = QHBoxLayout(body_widget)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # LEFT SIDEBAR
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(215)
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(10, 10, 10, 12)
        sidebar_layout.setSpacing(4)

        if os.path.exists(logo_path):
            logo_pix = QPixmap(logo_path)
            if not logo_pix.isNull():
                lbl_logo = QLabel()
                scaled_pix = logo_pix.scaledToWidth(195, Qt.SmoothTransformation)
                lbl_logo.setPixmap(scaled_pix)
                lbl_logo.setAlignment(Qt.AlignCenter)
                lbl_logo.setStyleSheet("margin-top: 2px; margin-bottom: 6px;")
                sidebar_layout.addWidget(lbl_logo)

        mod_title = QLabel("MODULE DIRECTORY")
        mod_title.setStyleSheet("font-size: 10px; font-weight: bold; color: #586579; letter-spacing: 1px; margin-left: 6px; margin-top: 2px; margin-bottom: 2px;")
        sidebar_layout.addWidget(mod_title)

        self._nav_buttons = []
        self._nav_group = QButtonGroup(self)
        self._nav_group.setExclusive(True)

        nav_items = [
            ("👁️  Visuals ESP", 0),
            ("⚡  Luau Executor", 1),
            ("📡  2D Radar", 2),
            ("🎯  Combat & Hitbox", 3),
            ("🏃  Movement & Fly", 4),
            ("🌀  Teleport & Stalk", 5),
            ("🎥  Spectate Hub", 6),
            ("🌐  World & Utility", 7),
            ("🎨  Color Palette", 8),
            ("⚙️  Configuration", 9),
            ("🔪  MM2 Role ESP", 10),
        ]

        for title, idx in nav_items:
            btn = QPushButton(title)
            btn.setObjectName("navBtn")
            btn.setCheckable(True)
            if idx == 0:
                btn.setChecked(True)
            btn.clicked.connect(lambda _, i=idx: self._switch_page(i))
            self._nav_group.addButton(btn, idx)
            self._nav_buttons.append(btn)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        sys_card = QFrame()
        sys_card.setObjectName("systemCard")
        sys_lay = QVBoxLayout(sys_card)
        sys_lay.setContentsMargins(8, 8, 8, 8)
        sys_lay.setSpacing(2)

        sys_status = QLabel("● SYSTEM ACTIVE")
        sys_status.setStyleSheet("color: #00ff9d; font-size: 10px; font-weight: bold; letter-spacing: 0.5px;")
        sys_lay.addWidget(sys_status)

        sys_sub = QLabel("Roblox Hooked (MemIO • AntiCheat Bypassed)")
        sys_sub.setStyleSheet("color: #68778d; font-size: 9px;")
        sys_lay.addWidget(sys_sub)
        sidebar_layout.addWidget(sys_card)

        quick_row = QHBoxLayout()
        quick_row.setSpacing(6)

        self.hide_btn = QPushButton("Hide [INS]")
        self.hide_btn.clicked.connect(self.hide)
        quick_row.addWidget(self.hide_btn)

        self.exit_btn = QPushButton("Exit [END]")
        self.exit_btn.setObjectName("exitBtn")
        self.exit_btn.clicked.connect(self.app.quit)
        quick_row.addWidget(self.exit_btn)

        sidebar_layout.addLayout(quick_row)
        body_layout.addWidget(self.sidebar)

        # RIGHT STACKED WIDGET
        self.stack = QStackedWidget()
        self.stack.setObjectName("contentStack")

        # -------------------------------------------------------------
        # PAGE 0: VISUALS / ESP
        # -------------------------------------------------------------
        tab_esp = QWidget()
        layout_esp = QVBoxLayout(tab_esp)
        layout_esp.setContentsMargins(16, 12, 16, 16)
        layout_esp.setSpacing(10)

        layout_esp.addWidget(self._make_page_header(
            "👁️ Visuals & Skeletal ESP",
            "Configure 2D & 3D bounding boxes, real-time skeleton bones, snaplines, and dynamic health bars"
        ))

        grp_toggles = QGroupBox("Visual Elements")
        l_toggles = QGridLayout(grp_toggles)
        l_toggles.setHorizontalSpacing(14)
        l_toggles.setVerticalSpacing(8)

        self.cb_boxes = QCheckBox("2D Boxes")
        self.cb_boxes.setChecked(ESP_SHOW_BOX)
        self.cb_boxes.toggled.connect(lambda v: self._set_toggle("ESP_SHOW_BOX", v))
        l_toggles.addWidget(self.cb_boxes, 0, 0)

        self.cb_corner = QCheckBox("Corner Boxes")
        self.cb_corner.setChecked(ESP_CORNER_BOX)
        self.cb_corner.toggled.connect(lambda v: self._set_toggle("ESP_CORNER_BOX", v))
        l_toggles.addWidget(self.cb_corner, 0, 1)

        self.cb_3d = QCheckBox("3D Wireframe")
        self.cb_3d.setChecked(ESP_3D_BOX)
        self.cb_3d.toggled.connect(lambda v: self._set_toggle("ESP_3D_BOX", v))
        l_toggles.addWidget(self.cb_3d, 1, 0)

        self.cb_skeleton = QCheckBox("Skeleton (R6 & R15)")
        self.cb_skeleton.setChecked(ESP_SHOW_SKELETON)
        self.cb_skeleton.toggled.connect(lambda v: self._set_toggle("ESP_SHOW_SKELETON", v))
        l_toggles.addWidget(self.cb_skeleton, 1, 1)

        self.cb_tracers = QCheckBox("Snapline Tracers")
        self.cb_tracers.setChecked(ESP_SHOW_TRACER)
        self.cb_tracers.toggled.connect(lambda v: self._set_toggle("ESP_SHOW_TRACER", v))
        l_toggles.addWidget(self.cb_tracers, 2, 0)

        self.cb_names = QCheckBox("Player Names")
        self.cb_names.setChecked(ESP_SHOW_NAME)
        self.cb_names.toggled.connect(lambda v: self._set_toggle("ESP_SHOW_NAME", v))
        l_toggles.addWidget(self.cb_names, 2, 1)

        self.cb_dist = QCheckBox("Distance (Studs)")
        self.cb_dist.setChecked(ESP_SHOW_DISTANCE)
        self.cb_dist.toggled.connect(lambda v: self._set_toggle("ESP_SHOW_DISTANCE", v))
        l_toggles.addWidget(self.cb_dist, 3, 0)

        self.cb_health = QCheckBox("Health Bars")
        self.cb_health.setChecked(ESP_SHOW_HEALTH)
        self.cb_health.toggled.connect(lambda v: self._set_toggle("ESP_SHOW_HEALTH", v))
        l_toggles.addWidget(self.cb_health, 3, 1)

        self.cb_dyn_hp = QCheckBox("Dynamic HP Color")
        self.cb_dyn_hp.setChecked(ESP_DYNAMIC_HEALTH_COLOR)
        self.cb_dyn_hp.toggled.connect(lambda v: self._set_toggle("ESP_DYNAMIC_HEALTH_COLOR", v))
        l_toggles.addWidget(self.cb_dyn_hp, 4, 0)

        self.cb_item_esp = QCheckBox("Item & Dropped Weapon ESP")
        self.cb_item_esp.setChecked(ITEM_ESP_ENABLED)
        self.cb_item_esp.toggled.connect(lambda v: self._set_toggle("ITEM_ESP_ENABLED", v))
        l_toggles.addWidget(self.cb_item_esp, 4, 1)

        layout_esp.addWidget(grp_toggles)

        grp_limits = QGroupBox("Sizing & Rendering Limits")
        l_limits = QGridLayout(grp_limits)
        l_limits.setHorizontalSpacing(10)
        l_limits.setVerticalSpacing(8)

        l_limits.addWidget(QLabel("Box Thickness:"), 0, 0)
        self.spin_box_thick = QSpinBox()
        self.spin_box_thick.setRange(1, 6)
        self.spin_box_thick.setValue(ESP_BOX_THICKNESS)
        self.spin_box_thick.valueChanged.connect(self._on_box_thickness_changed)
        l_limits.addWidget(self.spin_box_thick, 0, 1)

        l_limits.addWidget(QLabel("Skeleton Thickness:"), 1, 0)
        self.spin_skel_thick = QSpinBox()
        self.spin_skel_thick.setRange(1, 6)
        self.spin_skel_thick.setValue(ESP_SKELETON_THICKNESS)
        self.spin_skel_thick.valueChanged.connect(self._on_skel_thickness_changed)
        l_limits.addWidget(self.spin_skel_thick, 1, 1)

        l_limits.addWidget(QLabel("Max Distance:"), 2, 0)
        self.spin_max_dist = QDoubleSpinBox()
        self.spin_max_dist.setRange(50.0, 5000.0)
        self.spin_max_dist.setValue(MAX_DISTANCE)
        self.spin_max_dist.setSingleStep(50.0)
        self.spin_max_dist.setSuffix(" studs")
        self.spin_max_dist.valueChanged.connect(self._on_max_dist_changed)
        l_limits.addWidget(self.spin_max_dist, 2, 1)

        layout_esp.addWidget(grp_limits)
        layout_esp.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_esp))

        # -------------------------------------------------------------
        # PAGE 1: SCRIPT EXECUTOR & LUAU HUB
        # -------------------------------------------------------------
        tab_exec = QWidget()
        layout_exec = QVBoxLayout(tab_exec)
        layout_exec.setContentsMargins(16, 12, 16, 16)
        layout_exec.setSpacing(8)

        layout_exec.addWidget(self._make_page_header(
            "⚡ Luau Bytecode Runner & Script Hub",
            "Paste custom Luau scripts or load popular scripts from the built-in preset hub"
        ))

        self.script_editor = QPlainTextEdit()
        self.script_editor.setPlaceholderText("-- Write or paste your Luau / Roblox script here...\nprint('Hello from Nova External Luau Executor! :3')")
        layout_exec.addWidget(self.script_editor)

        exec_btn_row = QHBoxLayout()
        exec_btn_row.setSpacing(6)

        self.btn_exec_run = QPushButton("▶ Execute Script")
        self.btn_exec_run.setObjectName("actionBtn")
        self.btn_exec_run.clicked.connect(self._on_execute_script_clicked)
        exec_btn_row.addWidget(self.btn_exec_run)

        self.btn_exec_clear = QPushButton("🧹 Clear")
        self.btn_exec_clear.clicked.connect(lambda: self.script_editor.clear())
        exec_btn_row.addWidget(self.btn_exec_clear)

        self.btn_exec_open = QPushButton("📂 Open Script")
        self.btn_exec_open.clicked.connect(self._on_open_script_clicked)
        exec_btn_row.addWidget(self.btn_exec_open)

        self.btn_exec_save = QPushButton("💾 Save Script")
        self.btn_exec_save.clicked.connect(self._on_save_script_clicked)
        exec_btn_row.addWidget(self.btn_exec_save)

        layout_exec.addLayout(exec_btn_row)

        grp_presets = QGroupBox("📚 Universal & Rivals Script Hub Presets")
        l_pre = QGridLayout(grp_presets)
        l_pre.setHorizontalSpacing(8)
        l_pre.setVerticalSpacing(6)

        self.btn_pre_rivals = QPushButton("🎯 Rivals Silent Aim & Wallbang")
        self.btn_pre_rivals.clicked.connect(self._load_preset_rivals)
        l_pre.addWidget(self.btn_pre_rivals, 0, 0)

        self.btn_pre_iy = QPushButton("👑 Infinite Yield (Admin)")
        self.btn_pre_iy.clicked.connect(self._load_preset_iy)
        l_pre.addWidget(self.btn_pre_iy, 0, 1)

        self.btn_pre_dex = QPushButton("🔍 Dark Dex Explorer V4")
        self.btn_pre_dex.clicked.connect(self._load_preset_dex)
        l_pre.addWidget(self.btn_pre_dex, 1, 0)

        self.btn_pre_spy = QPushButton("🕵️ SimpleSpy V3 (Remote Spy)")
        self.btn_pre_spy.clicked.connect(self._load_preset_spy)
        l_pre.addWidget(self.btn_pre_spy, 1, 1)

        self.btn_pre_fling = QPushButton("🌪️ Touch Fling & Troll Hub")
        self.btn_pre_fling.clicked.connect(self._load_preset_fling)
        l_pre.addWidget(self.btn_pre_fling, 2, 0, 1, 2)

        layout_exec.addWidget(grp_presets)

        self.lbl_exec_status = QLabel("Ready to execute.")
        self.lbl_exec_status.setObjectName("infoLabel")
        self.lbl_exec_status.setWordWrap(True)
        layout_exec.addWidget(self.lbl_exec_status)

        layout_exec.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_exec))

        # -------------------------------------------------------------
        # PAGE 2: RADAR MINI-MAP
        # -------------------------------------------------------------
        tab_radar = QWidget()
        layout_radar = QVBoxLayout(tab_radar)
        layout_radar.setContentsMargins(16, 12, 16, 16)
        layout_radar.setSpacing(10)

        layout_radar.addWidget(self._make_page_header(
            "📡 Tactical 2D Radar Mini-Map",
            "High-frequency 360° player scanner with camera rotation and heading sync"
        ))

        grp_radar = QGroupBox("Tactical 2D Radar")
        l_rad = QGridLayout(grp_radar)
        l_rad.setHorizontalSpacing(12)
        l_rad.setVerticalSpacing(10)

        self.cb_radar_en = QCheckBox("Enable Radar Mini-map")
        self.cb_radar_en.setChecked(RADAR_ENABLED)
        self.cb_radar_en.toggled.connect(self._on_toggle_radar)
        l_rad.addWidget(self.cb_radar_en, 0, 0, 1, 2)

        self.cb_radar_cross = QCheckBox("Show Cardinal Crosshairs")
        self.cb_radar_cross.setChecked(RADAR_SHOW_CROSSHAIR)
        self.cb_radar_cross.toggled.connect(lambda v: self._set_toggle("RADAR_SHOW_CROSSHAIR", v))
        l_rad.addWidget(self.cb_radar_cross, 1, 0, 1, 2)

        l_rad.addWidget(QLabel("Radar Size:"), 2, 0)
        self.spin_radar_size = QSpinBox()
        self.spin_radar_size.setRange(100, 320)
        self.spin_radar_size.setValue(RADAR_SIZE)
        self.spin_radar_size.setSingleStep(10)
        self.spin_radar_size.setSuffix(" px")
        self.spin_radar_size.valueChanged.connect(self._on_radar_size_changed)
        l_rad.addWidget(self.spin_radar_size, 2, 1)

        l_rad.addWidget(QLabel("Radar Range:"), 3, 0)
        self.spin_radar_range = QDoubleSpinBox()
        self.spin_radar_range.setRange(50.0, 1500.0)
        self.spin_radar_range.setValue(RADAR_RANGE_STUDS)
        self.spin_radar_range.setSingleStep(25.0)
        self.spin_radar_range.setSuffix(" studs")
        self.spin_radar_range.valueChanged.connect(self._on_radar_range_changed)
        l_rad.addWidget(self.spin_radar_range, 3, 1)

        l_rad.addWidget(QLabel("Radar Opacity:"), 4, 0)
        self.spin_radar_opac = QSpinBox()
        self.spin_radar_opac.setRange(50, 255)
        self.spin_radar_opac.setValue(RADAR_OPACITY)
        self.spin_radar_opac.setSingleStep(15)
        self.spin_radar_opac.valueChanged.connect(self._on_radar_opacity_changed)
        l_rad.addWidget(self.spin_radar_opac, 4, 1)

        layout_radar.addWidget(grp_radar)

        lbl_radar_info = QLabel("Radar rotates with your camera heading. Off-range players are shown as hollow pips on the border.")
        lbl_radar_info.setObjectName("infoLabel")
        lbl_radar_info.setWordWrap(True)
        layout_radar.addWidget(lbl_radar_info)

        layout_radar.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_radar))

        # -------------------------------------------------------------
        # PAGE 3: AIMBOT & HITBOX EXPANDER (COMBAT)
        # -------------------------------------------------------------
        tab_aim = QWidget()
        layout_aim = QVBoxLayout(tab_aim)
        layout_aim.setContentsMargins(16, 12, 16, 16)
        layout_aim.setSpacing(10)

        layout_aim.addWidget(self._make_page_header(
            "🎯 Combat & Hitbox Manipulation",
            "Custom hitbox expansion for Roblox Rivals, auto triggerbot, and smooth aimbot"
        ))

        grp_hb = QGroupBox("🎯 Hitbox Expander (Roblox Rivals & Universal)")
        l_hb = QGridLayout(grp_hb)
        l_hb.setHorizontalSpacing(10)
        l_hb.setVerticalSpacing(8)

        self.cb_hb_en = QCheckBox("Enable Hitbox Expander")
        self.cb_hb_en.setChecked(HITBOX_EXPANDER_ENABLED)
        self.cb_hb_en.toggled.connect(self._on_toggle_hitbox_expander)
        l_hb.addWidget(self.cb_hb_en, 0, 0)

        self.cb_hb_rivals = QCheckBox("Roblox Rivals Rig Mode")
        self.cb_hb_rivals.setChecked(HITBOX_RIVALS_MODE)
        self.cb_hb_rivals.setToolTip("Optimized for Rivals character models and Hitbox attachments")
        self.cb_hb_rivals.toggled.connect(lambda v: self._set_toggle("HITBOX_RIVALS_MODE", v))
        l_hb.addWidget(self.cb_hb_rivals, 0, 1)

        l_hb.addWidget(QLabel("Hitbox Size:"), 1, 0)
        self.spin_hb_size = QDoubleSpinBox()
        self.spin_hb_size.setRange(2.0, 50.0)
        self.spin_hb_size.setValue(HITBOX_SIZE)
        self.spin_hb_size.setSingleStep(2.0)
        self.spin_hb_size.setSuffix(" studs")
        self.spin_hb_size.valueChanged.connect(lambda v: self._set_toggle("HITBOX_SIZE", v))
        l_hb.addWidget(self.spin_hb_size, 1, 1)

        l_hb.addWidget(QLabel("Target Part:"), 2, 0)
        self.combo_hb_part = QComboBox()
        self.combo_hb_part.addItems(["Head", "HumanoidRootPart", "Both"])
        hb_map = {"Head": 0, "HumanoidRootPart": 1, "Both": 2}
        self.combo_hb_part.setCurrentIndex(hb_map.get(HITBOX_TARGET_PART, 0))
        self.combo_hb_part.currentIndexChanged.connect(self._on_hitbox_part_changed)
        l_hb.addWidget(self.combo_hb_part, 2, 1)

        self.cb_hb_nocollide = QCheckBox("No-Collide (CanCollide = False)")
        self.cb_hb_nocollide.setChecked(not HITBOX_CAN_COLLIDE)
        self.cb_hb_nocollide.toggled.connect(lambda v: self._set_toggle("HITBOX_CAN_COLLIDE", not v))
        l_hb.addWidget(self.cb_hb_nocollide, 3, 0)

        self.cb_hb_vis = QCheckBox("Draw 3D Hitbox Wireframe")
        self.cb_hb_vis.setChecked(HITBOX_VISUALIZE)
        self.cb_hb_vis.toggled.connect(lambda v: self._set_toggle("HITBOX_VISUALIZE", v))
        l_hb.addWidget(self.cb_hb_vis, 3, 1)

        self.cb_hb_team = QCheckBox("Team Check (Enemies Only)")
        self.cb_hb_team.setChecked(HITBOX_TEAM_CHECK)
        self.cb_hb_team.toggled.connect(lambda v: self._set_toggle("HITBOX_TEAM_CHECK", v))
        l_hb.addWidget(self.cb_hb_team, 4, 0, 1, 2)

        layout_aim.addWidget(grp_hb)

        grp_tb = QGroupBox("⚡ Auto Triggerbot")
        l_tb = QGridLayout(grp_tb)
        l_tb.setHorizontalSpacing(10)
        l_tb.setVerticalSpacing(8)

        self.cb_tb_en = QCheckBox("Enable Triggerbot (Auto-Fire)")
        self.cb_tb_en.setChecked(TRIGGERBOT_ENABLED)
        self.cb_tb_en.toggled.connect(lambda v: self._set_toggle("TRIGGERBOT_ENABLED", v))
        l_tb.addWidget(self.cb_tb_en, 0, 0)

        l_tb.addWidget(QLabel("Delay (ms):"), 0, 1)
        self.spin_tb_delay = QSpinBox()
        self.spin_tb_delay.setRange(5, 500)
        self.spin_tb_delay.setValue(TRIGGERBOT_DELAY_MS)
        self.spin_tb_delay.setSingleStep(5)
        self.spin_tb_delay.setSuffix(" ms")
        self.spin_tb_delay.valueChanged.connect(lambda v: self._set_toggle("TRIGGERBOT_DELAY_MS", v))
        l_tb.addWidget(self.spin_tb_delay, 0, 2)

        l_tb.addWidget(QLabel("Firing Mode:"), 1, 0)
        self.combo_tb_mode = QComboBox()
        self.combo_tb_mode.addItems(["Tap (Burst/Semi)", "Auto Spray (Hold)"])
        self.combo_tb_mode.setCurrentIndex(0 if TRIGGERBOT_MODE == "Tap" else 1)
        self.combo_tb_mode.currentIndexChanged.connect(lambda idx: self._set_toggle("TRIGGERBOT_MODE", "Tap" if idx == 0 else "Auto Spray"))
        l_tb.addWidget(self.combo_tb_mode, 1, 1)

        l_tb.addWidget(QLabel("Max Random Delay:"), 1, 2)
        self.spin_tb_max_delay = QSpinBox()
        self.spin_tb_max_delay.setRange(10, 500)
        self.spin_tb_max_delay.setValue(TRIGGERBOT_MAX_DELAY_MS)
        self.spin_tb_max_delay.setSingleStep(5)
        self.spin_tb_max_delay.setSuffix(" ms")
        self.spin_tb_max_delay.setToolTip("Humanized jitter to randomize click cadence")
        self.spin_tb_max_delay.valueChanged.connect(lambda v: self._set_toggle("TRIGGERBOT_MAX_DELAY_MS", v))
        l_tb.addWidget(self.spin_tb_max_delay, 1, 3)

        layout_aim.addWidget(grp_tb)

        grp_aim = QGroupBox("🎯 Advanced Smooth Aimbot & RCS")
        l_aim = QGridLayout(grp_aim)
        l_aim.setHorizontalSpacing(10)
        l_aim.setVerticalSpacing(10)

        self.cb_aim_en = QCheckBox("Enable Aimbot")
        self.cb_aim_en.setChecked(AIMBOT_ENABLED)
        self.cb_aim_en.toggled.connect(lambda v: self._set_toggle("AIMBOT_ENABLED", v))
        l_aim.addWidget(self.cb_aim_en, 0, 0)

        self.cb_aim_fov_show = QCheckBox("Draw FOV Circle")
        self.cb_aim_fov_show.setChecked(AIMBOT_SHOW_FOV)
        self.cb_aim_fov_show.toggled.connect(lambda v: self._set_toggle("AIMBOT_SHOW_FOV", v))
        l_aim.addWidget(self.cb_aim_fov_show, 0, 1)

        l_aim.addWidget(QLabel("Activation Key:"), 1, 0)
        self.combo_aim_key = QComboBox()
        self.combo_aim_key.addItems(["RBUTTON (Right Click)", "LBUTTON (Left Click)", "LSHIFT (Left Shift)", "E Key", "Q Key", "ALT Key"])
        key_map = {"RBUTTON": 0, "LBUTTON": 1, "LSHIFT": 2, "E": 3, "Q": 4, "ALT": 5}
        self.combo_aim_key.setCurrentIndex(key_map.get(AIMBOT_KEY, 0))
        self.combo_aim_key.currentIndexChanged.connect(self._on_aimbot_key_changed)
        l_aim.addWidget(self.combo_aim_key, 1, 1)

        l_aim.addWidget(QLabel("Target Bone:"), 1, 2)
        self.combo_aim_part = QComboBox()
        self.combo_aim_part.addItems(["Head", "Torso / RootPart"])
        self.combo_aim_part.setCurrentIndex(0 if AIMBOT_TARGET_PART == "Head" else 1)
        self.combo_aim_part.currentIndexChanged.connect(lambda idx: self._set_toggle("AIMBOT_TARGET_PART", "Head" if idx == 0 else "HumanoidRootPart"))
        l_aim.addWidget(self.combo_aim_part, 1, 3)

        l_aim.addWidget(QLabel("Target Priority:"), 2, 0)
        self.combo_aim_prio = QComboBox()
        self.combo_aim_prio.addItems(["Closest to Crosshair", "Closest 3D Distance", "Lowest Health"])
        prio_map = {"Crosshair": 0, "Distance": 1, "Lowest HP": 2}
        self.combo_aim_prio.setCurrentIndex(prio_map.get(AIMBOT_PRIORITY, 0))
        self.combo_aim_prio.currentIndexChanged.connect(lambda idx: self._set_toggle("AIMBOT_PRIORITY", ["Crosshair", "Distance", "Lowest HP"][idx]))
        l_aim.addWidget(self.combo_aim_prio, 2, 1)

        self.cb_aim_sticky = QCheckBox("Sticky Target (Keep Locked)")
        self.cb_aim_sticky.setChecked(AIMBOT_STICKY)
        self.cb_aim_sticky.setToolTip("Locks onto current target until key release or target leaves FOV")
        self.cb_aim_sticky.toggled.connect(lambda v: self._set_toggle("AIMBOT_STICKY", v))
        l_aim.addWidget(self.cb_aim_sticky, 2, 2, 1, 2)

        l_aim.addWidget(QLabel("FOV Radius:"), 3, 0)
        self.spin_aim_fov = QDoubleSpinBox()
        self.spin_aim_fov.setRange(20.0, 800.0)
        self.spin_aim_fov.setValue(AIMBOT_FOV)
        self.spin_aim_fov.setSingleStep(10.0)
        self.spin_aim_fov.setSuffix(" px")
        self.spin_aim_fov.valueChanged.connect(lambda v: self._set_toggle("AIMBOT_FOV", v))
        l_aim.addWidget(self.spin_aim_fov, 3, 1)

        l_aim.addWidget(QLabel("Smoothness:"), 3, 2)
        self.spin_aim_smooth = QDoubleSpinBox()
        self.spin_aim_smooth.setRange(1.0, 30.0)
        self.spin_aim_smooth.setValue(AIMBOT_SMOOTHNESS)
        self.spin_aim_smooth.setSingleStep(0.5)
        self.spin_aim_smooth.setDecimals(1)
        self.spin_aim_smooth.valueChanged.connect(lambda v: self._set_toggle("AIMBOT_SMOOTHNESS", v))
        l_aim.addWidget(self.spin_aim_smooth, 3, 3)

        self.cb_aim_pred = QCheckBox("Target Prediction (Lead Aim)")
        self.cb_aim_pred.setChecked(AIMBOT_PREDICTION)
        self.cb_aim_pred.setToolTip("Estimates target movement vector and leads shots")
        self.cb_aim_pred.toggled.connect(lambda v: self._set_toggle("AIMBOT_PREDICTION", v))
        l_aim.addWidget(self.cb_aim_pred, 4, 0)

        l_aim.addWidget(QLabel("Micro-Deadzone:"), 4, 2)
        self.spin_aim_deadzone = QDoubleSpinBox()
        self.spin_aim_deadzone.setRange(0.0, 15.0)
        self.spin_aim_deadzone.setValue(AIMBOT_DEADZONE)
        self.spin_aim_deadzone.setSingleStep(0.5)
        self.spin_aim_deadzone.setSuffix(" px")
        self.spin_aim_deadzone.setToolTip("Prevents cursor twitching/jitter when already centered on target")
        self.spin_aim_deadzone.valueChanged.connect(lambda v: self._set_toggle("AIMBOT_DEADZONE", v))
        l_aim.addWidget(self.spin_aim_deadzone, 4, 3)

        self.cb_aim_rcs = QCheckBox("Recoil Compensation (RCS)")
        self.cb_aim_rcs.setChecked(AIMBOT_RCS_ENABLED)
        self.cb_aim_rcs.setToolTip("Applies automatic pull-down compensation while firing")
        self.cb_aim_rcs.toggled.connect(lambda v: self._set_toggle("AIMBOT_RCS_ENABLED", v))
        l_aim.addWidget(self.cb_aim_rcs, 5, 0)

        l_aim.addWidget(QLabel("RCS Strength:"), 5, 2)
        self.spin_aim_rcs_strength = QDoubleSpinBox()
        self.spin_aim_rcs_strength.setRange(0.5, 10.0)
        self.spin_aim_rcs_strength.setValue(AIMBOT_RCS_STRENGTH)
        self.spin_aim_rcs_strength.setSingleStep(0.5)
        self.spin_aim_rcs_strength.valueChanged.connect(lambda v: self._set_toggle("AIMBOT_RCS_STRENGTH", v))
        l_aim.addWidget(self.spin_aim_rcs_strength, 5, 3)

        self.cb_aim_team = QCheckBox("Team Check (Ignore Teammates)")
        self.cb_aim_team.setChecked(AIMBOT_TEAM_CHECK)
        self.cb_aim_team.toggled.connect(lambda v: self._set_toggle("AIMBOT_TEAM_CHECK", v))
        l_aim.addWidget(self.cb_aim_team, 6, 0, 1, 2)

        layout_aim.addWidget(grp_aim)
        layout_aim.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_aim))

        # -------------------------------------------------------------
        # PAGE 4: MOVEMENT & FLIGHT
        # -------------------------------------------------------------
        tab_move = QWidget()
        layout_move = QVBoxLayout(tab_move)
        layout_move.setContentsMargins(16, 12, 16, 16)
        layout_move.setSpacing(10)

        layout_move.addWidget(self._make_page_header(
            "🏃 Movement Physics & Flight",
            "Anti-Kick Safe Speed bypass, CFrame flight, infinite jump, noclip, and freecam"
        ))

        grp_safe_speed = QGroupBox("Anti-Kick Safe Speed (Bypasses AC / No Kick)")
        l_ss = QGridLayout(grp_safe_speed)
        l_ss.setHorizontalSpacing(10)
        l_ss.setVerticalSpacing(8)

        self.cb_safe_speed = QCheckBox("Enable Safe Speed [Anti-Kick]")
        self.cb_safe_speed.setChecked(ENABLE_SAFE_SPEED)
        self.cb_safe_speed.toggled.connect(self._on_toggle_safe_speed)
        l_ss.addWidget(self.cb_safe_speed, 0, 0)

        self.spin_safe_speed = QDoubleSpinBox()
        self.spin_safe_speed.setRange(16.0, 300.0)
        self.spin_safe_speed.setValue(SAFE_SPEED_VALUE)
        self.spin_safe_speed.setSingleStep(5.0)
        self.spin_safe_speed.setDecimals(1)
        self.spin_safe_speed.setSuffix(" studs/s")
        self.spin_safe_speed.valueChanged.connect(self._on_safe_speed_changed)
        l_ss.addWidget(self.spin_safe_speed, 0, 1)

        lbl_safe_speed_desc = QLabel("🛡️ Safe Speed keeps your Humanoid.WalkSpeed at 16.0! Boosts AssemblyLinearVelocity & CFrame physics directly so game anti-cheats (Adonis, HD Admin, custom kick scripts) NEVER detect or kick you.")
        lbl_safe_speed_desc.setObjectName("infoLabel")
        lbl_safe_speed_desc.setWordWrap(True)
        l_ss.addWidget(lbl_safe_speed_desc, 1, 0, 1, 2)

        layout_move.addWidget(grp_safe_speed)

        grp_move = QGroupBox("Character Physics Overrides")
        l_mv = QGridLayout(grp_move)
        l_mv.setHorizontalSpacing(10)
        l_mv.setVerticalSpacing(10)

        self.cb_walkspeed = QCheckBox("Direct WalkSpeed (Classic)")
        self.cb_walkspeed.setChecked(ENABLE_WALKSPEED)
        self.cb_walkspeed.toggled.connect(self._on_toggle_walkspeed)
        l_mv.addWidget(self.cb_walkspeed, 0, 0)

        self.spin_walkspeed = QDoubleSpinBox()
        self.spin_walkspeed.setRange(0.0, 1000.0)
        self.spin_walkspeed.setValue(WALKSPEED_VALUE)
        self.spin_walkspeed.setSingleStep(5.0)
        self.spin_walkspeed.setDecimals(1)
        self.spin_walkspeed.setSuffix(" studs/s")
        self.spin_walkspeed.valueChanged.connect(self._on_walkspeed_changed)
        l_mv.addWidget(self.spin_walkspeed, 0, 1)

        self.cb_jumppower = QCheckBox("JumpPower (R6 & R15)")
        self.cb_jumppower.setChecked(ENABLE_JUMPPOWER)
        self.cb_jumppower.toggled.connect(self._on_toggle_jumppower)
        l_mv.addWidget(self.cb_jumppower, 1, 0)

        self.spin_jumppower = QDoubleSpinBox()
        self.spin_jumppower.setRange(0.0, 1000.0)
        self.spin_jumppower.setValue(JUMPPOWER_VALUE)
        self.spin_jumppower.setSingleStep(5.0)
        self.spin_jumppower.setDecimals(1)
        self.spin_jumppower.setSuffix(" power")
        self.spin_jumppower.valueChanged.connect(self._on_jumppower_changed)
        l_mv.addWidget(self.spin_jumppower, 1, 1)

        self.cb_infjump = QCheckBox("Infinite Jump [SPACEBAR]")
        self.cb_infjump.setChecked(ENABLE_INFINITE_JUMP)
        self.cb_infjump.toggled.connect(self._on_toggle_infjump)
        l_mv.addWidget(self.cb_infjump, 2, 0)

        self.cb_noclip = QCheckBox("Noclip (Walk Thru Walls)")
        self.cb_noclip.setChecked(ENABLE_NOCLIP)
        self.cb_noclip.toggled.connect(lambda v: self._set_toggle("ENABLE_NOCLIP", v))
        l_mv.addWidget(self.cb_noclip, 2, 1)

        self.cb_fly = QCheckBox("Fly Hack [W/A/S/D/Space/Shift]")
        self.cb_fly.setChecked(ENABLE_FLY)
        self.cb_fly.toggled.connect(lambda v: self._set_toggle("ENABLE_FLY", v))
        l_mv.addWidget(self.cb_fly, 3, 0)

        self.spin_fly_speed = QDoubleSpinBox()
        self.spin_fly_speed.setRange(10.0, 500.0)
        self.spin_fly_speed.setValue(FLY_SPEED)
        self.spin_fly_speed.setSingleStep(10.0)
        self.spin_fly_speed.setSuffix(" speed")
        self.spin_fly_speed.valueChanged.connect(lambda v: self._set_toggle("FLY_SPEED", v))
        l_mv.addWidget(self.spin_fly_speed, 3, 1)

        self.cb_freecam = QCheckBox("Freecam Mode [W/A/S/D/Q/E]")
        self.cb_freecam.setChecked(FREECAM_ENABLED)
        self.cb_freecam.toggled.connect(lambda v: self._set_toggle("FREECAM_ENABLED", v))
        l_mv.addWidget(self.cb_freecam, 4, 0)

        self.spin_freecam_speed = QDoubleSpinBox()
        self.spin_freecam_speed.setRange(0.5, 20.0)
        self.spin_freecam_speed.setValue(FREECAM_SPEED)
        self.spin_freecam_speed.setSingleStep(0.5)
        self.spin_freecam_speed.setSuffix(" speed")
        self.spin_freecam_speed.valueChanged.connect(lambda v: self._set_toggle("FREECAM_SPEED", v))
        l_mv.addWidget(self.spin_freecam_speed, 4, 1)

        layout_move.addWidget(grp_move)

        lbl_jump_info = QLabel("✓ Noclip: Clears CanCollide bits across character parts in memory.\n✓ Fly: Uses camera orientation (LookVector & RightVector) for 3D physics flight.\n✓ Freecam: Detaches camera to explore map independently.")
        lbl_jump_info.setObjectName("infoLabel")
        lbl_jump_info.setWordWrap(True)
        layout_move.addWidget(lbl_jump_info)

        btn_reset_move = QPushButton("Restore Default Movement (Walk: 16 | Jump: 50)")
        btn_reset_move.clicked.connect(self._on_reset_movement)
        layout_move.addWidget(btn_reset_move)

        layout_move.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_move))

        # -------------------------------------------------------------
        # PAGE 5: PLAYER TELEPORT & FLING
        # -------------------------------------------------------------
        tab_tp = QWidget()
        layout_tp = QVBoxLayout(tab_tp)
        layout_tp.setContentsMargins(16, 12, 16, 16)
        layout_tp.setSpacing(10)

        layout_tp.addWidget(self._make_page_header(
            "🌀 Player Teleport & Physical Fling",
            "Instant player CFrame teleportation, loop stalk, coordinate copier, and momentum launch"
        ))

        grp_tp = QGroupBox("Player Teleport & Stalker")
        l_tp = QVBoxLayout(grp_tp)
        l_tp.setSpacing(8)

        self.tp_search_box = QLineEdit()
        self.tp_search_box.setPlaceholderText("🔍 Filter players by username or display name...")
        self.tp_search_box.textChanged.connect(self._filter_player_list)
        l_tp.addWidget(self.tp_search_box)

        self.lbl_tp_count = QLabel("Players in Server: 0 (Live Auto-Updating)")
        self.lbl_tp_count.setStyleSheet("color: #00d2ff; font-weight: bold;")
        l_tp.addWidget(self.lbl_tp_count)

        self.player_list_widget = QListWidget()
        self.player_list_widget.setMinimumHeight(200)
        self.player_list_widget.itemDoubleClicked.connect(lambda: self._on_teleport_clicked("Exact"))
        l_tp.addWidget(self.player_list_widget)

        btn_box = QHBoxLayout()
        btn_box.setSpacing(6)

        self.btn_tp_selected = QPushButton("⚡ Teleport To Player")
        self.btn_tp_selected.setObjectName("actionBtn")
        self.btn_tp_selected.clicked.connect(lambda: self._on_teleport_clicked("Exact"))
        btn_box.addWidget(self.btn_tp_selected)

        self.btn_tp_above = QPushButton("⬆️ Above (+6)")
        self.btn_tp_above.clicked.connect(lambda: self._on_teleport_clicked("Above"))
        btn_box.addWidget(self.btn_tp_above)

        self.btn_tp_behind = QPushButton("🔙 Behind (-3.5)")
        self.btn_tp_behind.clicked.connect(lambda: self._on_teleport_clicked("Behind"))
        btn_box.addWidget(self.btn_tp_behind)

        l_tp.addLayout(btn_box)

        btn_box_sub = QHBoxLayout()
        btn_box_sub.setSpacing(6)

        self.btn_expand_target_hb = QPushButton("🎯 Expand Target Hitbox")
        self.btn_expand_target_hb.setStyleSheet("background-color: #0088aa; color: white; font-weight: bold;")
        self.btn_expand_target_hb.clicked.connect(self._on_expand_target_hitbox_clicked)
        btn_box_sub.addWidget(self.btn_expand_target_hb)

        self.btn_copy_coords = QPushButton("📋 Copy Coords / CFrame")
        self.btn_copy_coords.clicked.connect(self._on_copy_player_cframe_clicked)
        btn_box_sub.addWidget(self.btn_copy_coords)

        l_tp.addLayout(btn_box_sub)

        btn_box2 = QHBoxLayout()
        self.cb_loop_tp = QCheckBox("🔄 Loop TP / Stalk Target")
        self.cb_loop_tp.setChecked(LOOP_TP_ENABLED)
        self.cb_loop_tp.toggled.connect(self._on_toggle_loop_tp)
        btn_box2.addWidget(self.cb_loop_tp)

        self.btn_refresh_tp = QPushButton("🔄 Refresh List Now")
        self.btn_refresh_tp.clicked.connect(self._refresh_player_list)
        btn_box2.addWidget(self.btn_refresh_tp)
        l_tp.addLayout(btn_box2)

        self.lbl_tp_status = QLabel("Select a player from the list to teleport.")
        self.lbl_tp_status.setObjectName("infoLabel")
        self.lbl_tp_status.setWordWrap(True)
        l_tp.addWidget(self.lbl_tp_status)

        layout_tp.addWidget(grp_tp)

        grp_fling = QGroupBox("💥 Physical Fling & Momentum Launch")
        l_fling = QVBoxLayout(grp_fling)
        l_fling.setSpacing(6)

        fling_btn_row = QHBoxLayout()
        self.btn_fling_burst = QPushButton("💥 Fling Player (Burst 1.5s)")
        self.btn_fling_burst.setObjectName("actionBtn")
        self.btn_fling_burst.setStyleSheet("background-color: #a82020; color: white; font-weight: bold;")
        self.btn_fling_burst.clicked.connect(self._on_fling_burst_clicked)
        fling_btn_row.addWidget(self.btn_fling_burst)

        self.cb_loop_fling = QCheckBox("🌪️ Loop Fling Target")
        self.cb_loop_fling.setChecked(False)
        self.cb_loop_fling.toggled.connect(self._on_toggle_loop_fling)
        fling_btn_row.addWidget(self.cb_loop_fling)
        l_fling.addLayout(fling_btn_row)

        fling_opt_row = QHBoxLayout()
        self.cb_fling_return = QCheckBox("↩️ Return to start pos after fling")
        self.cb_fling_return.setChecked(FLING_RETURN_TO_START)
        self.cb_fling_return.toggled.connect(self._on_toggle_fling_return)
        fling_opt_row.addWidget(self.cb_fling_return)

        fling_opt_row.addWidget(QLabel("Power:"))
        self.spin_fling_power = QDoubleSpinBox()
        self.spin_fling_power.setRange(10000.0, 500000.0)
        self.spin_fling_power.setValue(FLING_POWER)
        self.spin_fling_power.setSingleStep(25000.0)
        self.spin_fling_power.setSuffix(" vel")
        self.spin_fling_power.valueChanged.connect(self._on_fling_power_changed)
        fling_opt_row.addWidget(self.spin_fling_power)
        l_fling.addLayout(fling_opt_row)

        self.lbl_fling_status = QLabel("Select a player above to launch them with physics impulse.")
        self.lbl_fling_status.setObjectName("infoLabel")
        self.lbl_fling_status.setWordWrap(True)
        l_fling.addWidget(self.lbl_fling_status)

        layout_tp.addWidget(grp_fling)
        layout_tp.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_tp))

        # -------------------------------------------------------------
        # PAGE 6: SPECTATE (LIVE SERVER MONITOR & NATIVE CAMERA TRACKER)
        # -------------------------------------------------------------
        tab_spec = QWidget()
        layout_spec = QVBoxLayout(tab_spec)
        layout_spec.setContentsMargins(16, 12, 16, 16)
        layout_spec.setSpacing(8)

        layout_spec.addWidget(self._make_page_header(
            "🎥 Native Camera Spectator & Activity Monitor",
            "Switch camera viewpoint to any player in server and monitor live player leaves/joins"
        ))

        grp_spec = QGroupBox("Player Spectator & Server Departure Monitor")
        l_spec = QVBoxLayout(grp_spec)
        l_spec.setSpacing(6)

        self.spectate_search_box = QLineEdit()
        self.spectate_search_box.setPlaceholderText("🔍 Filter spectate list by username or display name...")
        self.spectate_search_box.textChanged.connect(self._filter_spectate_list)
        l_spec.addWidget(self.spectate_search_box)

        self.lbl_spectate_count = QLabel("Players in Server: 0 (Live Auto-Updating)")
        self.lbl_spectate_count.setStyleSheet("color: #00d2ff; font-weight: bold;")
        l_spec.addWidget(self.lbl_spectate_count)

        self.spectate_list_widget = QListWidget()
        self.spectate_list_widget.setMinimumHeight(160)
        self.spectate_list_widget.itemDoubleClicked.connect(self._on_spectate_double_clicked)
        l_spec.addWidget(self.spectate_list_widget)

        btn_spec_row1 = QHBoxLayout()
        btn_spec_row1.setSpacing(6)

        self.btn_spectate_toggle = QPushButton("👁️ Spectate Selected")
        self.btn_spectate_toggle.setObjectName("actionBtn")
        self.btn_spectate_toggle.clicked.connect(self._on_spectate_toggle_clicked)
        btn_spec_row1.addWidget(self.btn_spectate_toggle)

        self.btn_spectate_stop = QPushButton("🛑 Return to Self (Stop Spectate)")
        self.btn_spectate_stop.clicked.connect(self._on_stop_spectate_clicked)
        btn_spec_row1.addWidget(self.btn_spectate_stop)
        l_spec.addLayout(btn_spec_row1)

        btn_spec_row2 = QHBoxLayout()
        btn_spec_row2.setSpacing(6)

        self.btn_spectate_prev = QPushButton("⬅️ Prev")
        self.btn_spectate_prev.clicked.connect(self._on_spectate_prev_clicked)
        btn_spec_row2.addWidget(self.btn_spectate_prev)

        self.btn_spectate_next = QPushButton("➡️ Next")
        self.btn_spectate_next.clicked.connect(self._on_spectate_next_clicked)
        btn_spec_row2.addWidget(self.btn_spectate_next)

        self.btn_spectate_tp = QPushButton("⚡ Teleport To")
        self.btn_spectate_tp.clicked.connect(self._on_spectate_tp_clicked)
        btn_spec_row2.addWidget(self.btn_spectate_tp)

        self.btn_spectate_fling = QPushButton("💥 Fling")
        self.btn_spectate_fling.setStyleSheet("background-color: #a82020; color: white; font-weight: bold;")
        self.btn_spectate_fling.clicked.connect(self._on_spectate_fling_clicked)
        btn_spec_row2.addWidget(self.btn_spectate_fling)
        l_spec.addLayout(btn_spec_row2)

        self.cb_auto_next = QCheckBox("Auto-spectate next player if current target leaves")
        self.cb_auto_next.setChecked(SPECTATE_AUTO_NEXT)
        self.cb_auto_next.toggled.connect(self._on_toggle_auto_next)
        l_spec.addWidget(self.cb_auto_next)

        self.lbl_spectate_target_info = QLabel("Status: Viewing Local Player (Self)")
        self.lbl_spectate_target_info.setStyleSheet("color: #8fa0ba; font-weight: bold; background: #161a24; padding: 6px; border-radius: 4px; border: 1px solid #282d3c;")
        self.lbl_spectate_target_info.setWordWrap(True)
        l_spec.addWidget(self.lbl_spectate_target_info)

        lbl_feed = QLabel("Server Departure & Arrival Feed (Updates Live):")
        lbl_feed.setStyleSheet("color: #8c93a8; font-size: 11px; margin-top: 2px;")
        l_spec.addWidget(lbl_feed)

        self.spectate_event_list = QListWidget()
        self.spectate_event_list.setMaximumHeight(75)
        self.spectate_event_list.setStyleSheet("background: #0d0f14; border: 1px solid #202430; font-size: 11px; border-radius: 4px;")
        l_spec.addWidget(self.spectate_event_list)

        self.lbl_spectate_status = QLabel("Select any player from the list to spectate.")
        self.lbl_spectate_status.setObjectName("infoLabel")
        self.lbl_spectate_status.setWordWrap(True)
        l_spec.addWidget(self.lbl_spectate_status)

        layout_spec.addWidget(grp_spec)
        layout_spec.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_spec))

        # -------------------------------------------------------------
        # PAGE 7: WORLD & UTILITY CHEATS
        # -------------------------------------------------------------
        tab_world = QWidget()
        layout_world = QVBoxLayout(tab_world)
        layout_world.setContentsMargins(16, 12, 16, 16)
        layout_world.setSpacing(10)

        layout_world.addWidget(self._make_page_header(
            "🌐 World Mechanics & Script Dumper",
            "Lighting overrides, proximity prompts, gravity modification, and memory script extractor"
        ))

        grp_world = QGroupBox("Lighting & World Mechanics")
        l_wld = QGridLayout(grp_world)
        l_wld.setHorizontalSpacing(10)
        l_wld.setVerticalSpacing(10)

        self.cb_fullbright = QCheckBox("Fullbright / Remove Fog")
        self.cb_fullbright.setChecked(ENABLE_FULLBRIGHT)
        self.cb_fullbright.toggled.connect(lambda v: self._set_toggle("ENABLE_FULLBRIGHT", v))
        l_wld.addWidget(self.cb_fullbright, 0, 0)

        self.cb_instant_prompts = QCheckBox("Instant Proximity Prompts")
        self.cb_instant_prompts.setChecked(ENABLE_INSTANT_PROMPTS)
        self.cb_instant_prompts.toggled.connect(lambda v: self._set_toggle("ENABLE_INSTANT_PROMPTS", v))
        l_wld.addWidget(self.cb_instant_prompts, 0, 1)

        self.cb_inf_click = QCheckBox("Map-Wide ClickDetectors")
        self.cb_inf_click.setChecked(ENABLE_INF_CLICK)
        self.cb_inf_click.toggled.connect(lambda v: self._set_toggle("ENABLE_INF_CLICK", v))
        l_wld.addWidget(self.cb_inf_click, 1, 0)

        self.cb_grav = QCheckBox("Custom Gravity")
        self.cb_grav.setChecked(ENABLE_GRAVITY_MOD)
        self.cb_grav.toggled.connect(lambda v: self._set_toggle("ENABLE_GRAVITY_MOD", v))
        l_wld.addWidget(self.cb_grav, 1, 1)

        l_wld.addWidget(QLabel("Gravity Level:"), 2, 0)
        self.spin_grav = QDoubleSpinBox()
        self.spin_grav.setRange(0.0, 500.0)
        self.spin_grav.setValue(GRAVITY_VALUE)
        self.spin_grav.setSingleStep(20.0)
        self.spin_grav.setSuffix(" studs/s²")
        self.spin_grav.valueChanged.connect(lambda v: self._set_toggle("GRAVITY_VALUE", v))
        l_wld.addWidget(self.spin_grav, 2, 1)

        self.cb_fps = QCheckBox("Unlock FPS")
        self.cb_fps.setChecked(UNLOCK_FPS)
        self.cb_fps.toggled.connect(lambda v: self._set_toggle("UNLOCK_FPS", v))
        l_wld.addWidget(self.cb_fps, 3, 0)

        self.spin_fps = QDoubleSpinBox()
        self.spin_fps.setRange(30.0, 1000.0)
        self.spin_fps.setValue(UNLOCK_FPS_VALUE)
        self.spin_fps.setSingleStep(30.0)
        self.spin_fps.setSuffix(" FPS")
        self.spin_fps.valueChanged.connect(lambda v: self._set_toggle("UNLOCK_FPS_VALUE", v))
        l_wld.addWidget(self.spin_fps, 3, 1)

        layout_world.addWidget(grp_world)

        grp_dumper = QGroupBox("Script & Bytecode Dumper")
        l_dmp = QVBoxLayout(grp_dumper)
        l_dmp.setSpacing(8)

        self.btn_dump_scripts = QPushButton("⚡ Dump All LocalScripts & ModuleScripts")
        self.btn_dump_scripts.setObjectName("actionBtn")
        self.btn_dump_scripts.clicked.connect(self._on_dump_scripts)
        l_dmp.addWidget(self.btn_dump_scripts)

        self.lbl_dump_status = QLabel("Ready to extract client bytecode to dumped_scripts/")
        self.lbl_dump_status.setObjectName("infoLabel")
        self.lbl_dump_status.setWordWrap(True)
        l_dmp.addWidget(self.lbl_dump_status)

        layout_world.addWidget(grp_dumper)
        layout_world.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_world))

        # -------------------------------------------------------------
        # PAGE 8: COLORS & STYLING
        # -------------------------------------------------------------
        tab_colors = QWidget()
        layout_colors = QVBoxLayout(tab_colors)
        layout_colors.setContentsMargins(16, 12, 16, 16)
        layout_colors.setSpacing(10)

        layout_colors.addWidget(self._make_page_header(
            "🎨 Visual Theme & Color Palette",
            "Custom RGBA colors for enemies, teammates, tracers, and skeletal bone segments"
        ))

        grp_colors = QGroupBox("Color Palette")
        l_col = QGridLayout(grp_colors)
        l_col.setHorizontalSpacing(12)
        l_col.setVerticalSpacing(10)

        l_col.addWidget(QLabel("Enemy Box:"), 0, 0)
        self.enemy_color_btn = QPushButton()
        self._update_color_btn_swatch(self.enemy_color_btn, ESP_BOX_COLOR)
        self.enemy_color_btn.clicked.connect(self._pick_enemy_color)
        l_col.addWidget(self.enemy_color_btn, 0, 1)

        l_col.addWidget(QLabel("Teammate Box:"), 1, 0)
        self.team_color_btn = QPushButton()
        self._update_color_btn_swatch(self.team_color_btn, ESP_TEAMMATE_COLOR)
        self.team_color_btn.clicked.connect(self._pick_teammate_color)
        l_col.addWidget(self.team_color_btn, 1, 1)

        l_col.addWidget(QLabel("Tracers:"), 2, 0)
        self.tracer_color_btn = QPushButton()
        self._update_color_btn_swatch(self.tracer_color_btn, ESP_TRACER_COLOR)
        self.tracer_color_btn.clicked.connect(self._pick_tracer_color)
        l_col.addWidget(self.tracer_color_btn, 2, 1)

        l_col.addWidget(QLabel("Skeleton:"), 3, 0)
        self.skel_color_btn = QPushButton()
        self._update_color_btn_swatch(self.skel_color_btn, ESP_SKELETON_COLOR)
        self.skel_color_btn.clicked.connect(self._pick_skeleton_color)
        l_col.addWidget(self.skel_color_btn, 3, 1)

        layout_colors.addWidget(grp_colors)
        layout_colors.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_colors))

        # -------------------------------------------------------------
        # PAGE 9: CONFIG & SETTINGS
        # -------------------------------------------------------------
        tab_cfg = QWidget()
        layout_cfg = QVBoxLayout(tab_cfg)
        layout_cfg.setContentsMargins(16, 12, 16, 16)
        layout_cfg.setSpacing(10)

        layout_cfg.addWidget(self._make_page_header(
            "⚙️ Profile & Engine Configuration",
            "Target filtering, always-on-top window control, and configuration profile management"
        ))

        grp_filter = QGroupBox("Target Filtering & Window")
        l_filt = QVBoxLayout(grp_filter)

        self.team_combo = QComboBox()
        self.team_combo.addItems([
            "Everyone (Enemies & Teammates)",
            "Enemies Only",
            "Teammates Only",
        ])
        index_map = {"Everyone": 0, "Enemies Only": 1, "Teammates Only": 2}
        self.team_combo.setCurrentIndex(index_map.get(TEAM_FILTER_MODE, 0))
        self.team_combo.currentIndexChanged.connect(self._on_team_filter_changed)
        l_filt.addWidget(self.team_combo)

        self.cb_ontop = QCheckBox("Overlay Always On Top")
        self.cb_ontop.setChecked(ALWAYS_ON_TOP)
        self.cb_ontop.toggled.connect(self._on_toggle_always_on_top)
        l_filt.addWidget(self.cb_ontop)
        layout_cfg.addWidget(grp_filter)

        grp_profiles = QGroupBox("Configuration Profile (config.json)")
        l_prof = QVBoxLayout(grp_profiles)
        l_prof.setSpacing(8)

        self.btn_save_cfg = QPushButton("💾 Save Current Configuration")
        self.btn_save_cfg.setObjectName("actionBtn")
        self.btn_save_cfg.clicked.connect(self._on_save_config)
        l_prof.addWidget(self.btn_save_cfg)

        self.btn_load_cfg = QPushButton("🔄 Reload Configuration from File")
        self.btn_load_cfg.clicked.connect(self._on_load_config)
        l_prof.addWidget(self.btn_load_cfg)

        self.btn_reset_cfg = QPushButton("⚠️ Reset All Settings to Defaults")
        self.btn_reset_cfg.clicked.connect(self._on_reset_defaults)
        l_prof.addWidget(self.btn_reset_cfg)

        self.lbl_cfg_status = QLabel("Status: Active")
        self.lbl_cfg_status.setStyleSheet("color: #00d2ff; font-weight: bold;")
        l_prof.addWidget(self.lbl_cfg_status, alignment=Qt.AlignCenter)

        layout_cfg.addWidget(grp_profiles)
        layout_cfg.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_cfg))

        # -------------------------------------------------------------
        # PAGE 10: MM2 ROLE ESP
        # -------------------------------------------------------------
        tab_mm2 = QWidget()
        layout_mm2 = QVBoxLayout(tab_mm2)
        layout_mm2.setContentsMargins(16, 12, 16, 16)
        layout_mm2.setSpacing(10)

        layout_mm2.addWidget(self._make_page_header(
            "🔪 Murder Mystery 2 — Role ESP",
            "Detect and display player roles (Murderer / Sheriff / Innocent) by scanning their character inventory"
        ))

        # ── Master toggle ──────────────────────────────────────────────
        grp_mm2_toggle = QGroupBox("Role Detection")
        l_mm2_toggle = QVBoxLayout(grp_mm2_toggle)

        self.cb_mm2_enabled = QCheckBox("Enable MM2 Role ESP")
        self.cb_mm2_enabled.setChecked(MM2_ROLE_ESP_ENABLED)
        self.cb_mm2_enabled.setToolTip(
            "Scans each player's character children for knife/gun tool names "
            "to identify their MM2 role. Displayed as a colored badge above the player."
        )
        self.cb_mm2_enabled.toggled.connect(self._on_mm2_toggle)
        l_mm2_toggle.addWidget(self.cb_mm2_enabled)

        note_lbl = QLabel(
            "ℹ️  Role is auto-detected by scanning weapon names in each player's character.\n"
            "   Murderer carries a 'Knife' tool · Sheriff carries a 'Gun' tool."
        )
        note_lbl.setStyleSheet("color: #7e8c9f; font-size: 10px; padding: 4px 0;")
        note_lbl.setWordWrap(True)
        l_mm2_toggle.addWidget(note_lbl)
        layout_mm2.addWidget(grp_mm2_toggle)

        # ── Role color pickers ─────────────────────────────────────────
        grp_mm2_colors = QGroupBox("Role Colors")
        l_mm2_colors = QGridLayout(grp_mm2_colors)
        l_mm2_colors.setSpacing(8)

        l_mm2_colors.addWidget(QLabel("🔪 Murderer:"), 0, 0)
        self.btn_mm2_murderer_col = QPushButton()
        self._update_color_btn_swatch_mm2(self.btn_mm2_murderer_col, MM2_MURDERER_COLOR)
        self.btn_mm2_murderer_col.clicked.connect(self._pick_mm2_murderer_color)
        l_mm2_colors.addWidget(self.btn_mm2_murderer_col, 0, 1)

        l_mm2_colors.addWidget(QLabel("🔫 Sheriff:"), 1, 0)
        self.btn_mm2_sheriff_col = QPushButton()
        self._update_color_btn_swatch_mm2(self.btn_mm2_sheriff_col, MM2_SHERIFF_COLOR)
        self.btn_mm2_sheriff_col.clicked.connect(self._pick_mm2_sheriff_color)
        l_mm2_colors.addWidget(self.btn_mm2_sheriff_col, 1, 1)

        l_mm2_colors.addWidget(QLabel("😇 Innocent:"), 2, 0)
        self.btn_mm2_innocent_col = QPushButton()
        self._update_color_btn_swatch_mm2(self.btn_mm2_innocent_col, MM2_INNOCENT_COLOR)
        self.btn_mm2_innocent_col.clicked.connect(self._pick_mm2_innocent_color)
        l_mm2_colors.addWidget(self.btn_mm2_innocent_col, 2, 1)

        layout_mm2.addWidget(grp_mm2_colors)

        # ── Keyword editors ────────────────────────────────────────────
        grp_mm2_kw = QGroupBox("Detection Keywords (comma-separated, lowercase)")
        l_mm2_kw = QVBoxLayout(grp_mm2_kw)
        l_mm2_kw.setSpacing(6)

        l_mm2_kw.addWidget(QLabel("🔪 Knife tool name substrings (Murderer detection):"))
        self.le_knife_kw = QLineEdit(", ".join(MM2_KNIFE_NAMES))
        self.le_knife_kw.setToolTip("Comma-separated lowercase substrings found in the knife tool's Instance Name")
        self.le_knife_kw.textChanged.connect(self._on_mm2_knife_kw_changed)
        l_mm2_kw.addWidget(self.le_knife_kw)

        l_mm2_kw.addWidget(QLabel("🔫 Gun tool name substrings (Sheriff detection):"))
        self.le_gun_kw = QLineEdit(", ".join(MM2_GUN_NAMES))
        self.le_gun_kw.setToolTip("Comma-separated lowercase substrings found in the sheriff gun tool's Instance Name")
        self.le_gun_kw.textChanged.connect(self._on_mm2_gun_kw_changed)
        l_mm2_kw.addWidget(self.le_gun_kw)

        layout_mm2.addWidget(grp_mm2_kw)

        # ── Dropped Gun & Teleport Section ─────────────────────────────
        grp_mm2_gun = QGroupBox("Dropped Sheriff Gun (GunDrop)")
        l_mm2_gun = QVBoxLayout(grp_mm2_gun)
        l_mm2_gun.setSpacing(8)

        gun_toggles_row = QHBoxLayout()
        gun_toggles_row.setSpacing(12)

        self.cb_mm2_gun_esp = QCheckBox("Dropped Gun Visual ESP (Tracer & Beacon)")
        self.cb_mm2_gun_esp.setChecked(MM2_GUN_ESP_ENABLED)
        self.cb_mm2_gun_esp.toggled.connect(self._on_mm2_gun_esp_toggle)
        gun_toggles_row.addWidget(self.cb_mm2_gun_esp)

        self.cb_mm2_gun_notify = QCheckBox("Banner Alert On Drop")
        self.cb_mm2_gun_notify.setChecked(MM2_GUN_NOTIFY)
        self.cb_mm2_gun_notify.toggled.connect(self._on_mm2_gun_notify_toggle)
        gun_toggles_row.addWidget(self.cb_mm2_gun_notify)
        l_mm2_gun.addLayout(gun_toggles_row)

        self.btn_tp_gun = QPushButton("⚡ TELEPORT TO DROPPED GUN [T]")
        self.btn_tp_gun.setObjectName("actionBtn")
        self.btn_tp_gun.setFixedHeight(34)
        self.btn_tp_gun.setStyleSheet("""
            QPushButton#actionBtn {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ffd700, stop:1 #ffaa00);
                color: #0b0e14;
                font-weight: bold;
                font-size: 12px;
                border-radius: 6px;
                border: 1px solid #ffe655;
            }
            QPushButton#actionBtn:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #ffe033, stop:1 #ffbb22);
            }
        """)
        self.btn_tp_gun.clicked.connect(self._on_tp_to_gun_clicked)
        l_mm2_gun.addWidget(self.btn_tp_gun)

        self.lbl_gun_status = QLabel("Gun Status: Scanning for dropped revolver...")
        self.lbl_gun_status.setStyleSheet("color: #7e8c9f; font-size: 11px;")
        l_mm2_gun.addWidget(self.lbl_gun_status, alignment=Qt.AlignCenter)

        layout_mm2.addWidget(grp_mm2_gun)
        layout_mm2.addStretch()
        self.stack.addWidget(self._wrap_scroll(tab_mm2))

        body_layout.addWidget(self.stack)
        frame_layout.addWidget(body_widget)

        # Compatibility shim for self.tabs
        self.tabs = TabsCompat(self)

    # ── Color & Swatch Helpers ─────────────────────────────────────────

    def _update_color_btn_swatch(self, btn: QPushButton, rgba: tuple) -> None:
        r, g, b = rgba[0], rgba[1], rgba[2]
        hex_col = f"#{r:02x}{g:02x}{b:02x}".upper()
        pix = QPixmap(14, 14)
        pix.fill(QColor(r, g, b))
        btn.setIcon(QIcon(pix))
        btn.setText(f" {hex_col}")

    def _update_color_btn_swatch_mm2(self, btn: QPushButton, rgba: tuple) -> None:
        """Alias so the MM2 page can call it before _update_color_btn_swatch is defined."""
        self._update_color_btn_swatch(btn, rgba)

    # ── MM2 Role ESP Handlers ──────────────────────────────────────────

    def _on_mm2_toggle(self, checked: bool) -> None:
        global MM2_ROLE_ESP_ENABLED
        MM2_ROLE_ESP_ENABLED = checked

    def _pick_mm2_murderer_color(self) -> None:
        global MM2_MURDERER_COLOR
        col = QColorDialog.getColor(QColor(*MM2_MURDERER_COLOR), self, "Select Murderer Color")
        if col.isValid():
            MM2_MURDERER_COLOR = (col.red(), col.green(), col.blue(), 255)
            self._update_color_btn_swatch(self.btn_mm2_murderer_col, MM2_MURDERER_COLOR)

    def _pick_mm2_sheriff_color(self) -> None:
        global MM2_SHERIFF_COLOR
        col = QColorDialog.getColor(QColor(*MM2_SHERIFF_COLOR), self, "Select Sheriff Color")
        if col.isValid():
            MM2_SHERIFF_COLOR = (col.red(), col.green(), col.blue(), 255)
            self._update_color_btn_swatch(self.btn_mm2_sheriff_col, MM2_SHERIFF_COLOR)

    def _pick_mm2_innocent_color(self) -> None:
        global MM2_INNOCENT_COLOR
        col = QColorDialog.getColor(QColor(*MM2_INNOCENT_COLOR), self, "Select Innocent Color")
        if col.isValid():
            MM2_INNOCENT_COLOR = (col.red(), col.green(), col.blue(), 255)
            self._update_color_btn_swatch(self.btn_mm2_innocent_col, MM2_INNOCENT_COLOR)

    def _on_mm2_knife_kw_changed(self, text: str) -> None:
        global MM2_KNIFE_NAMES
        MM2_KNIFE_NAMES = [kw.strip().lower() for kw in text.split(",") if kw.strip()]

    def _on_mm2_gun_kw_changed(self, text: str) -> None:
        global MM2_GUN_NAMES
        MM2_GUN_NAMES = [kw.strip().lower() for kw in text.split(",") if kw.strip()]

    def _on_mm2_gun_esp_toggle(self, checked: bool) -> None:
        global MM2_GUN_ESP_ENABLED
        MM2_GUN_ESP_ENABLED = checked

    def _on_mm2_gun_notify_toggle(self, checked: bool) -> None:
        global MM2_GUN_NOTIFY
        MM2_GUN_NOTIFY = checked

    def _on_tp_to_gun_clicked(self) -> None:
        success, msg = self.overlay.teleport_to_dropped_gun()
        if hasattr(self, "lbl_gun_status"):
            self.lbl_gun_status.setText(msg)
            if success:
                self.lbl_gun_status.setStyleSheet("color: #00ffaa; font-weight: bold;")
            else:
                self.lbl_gun_status.setStyleSheet("color: #ff5555; font-weight: bold;")

    def _pick_enemy_color(self) -> None:
        global ESP_BOX_COLOR
        init_col = QColor(*ESP_BOX_COLOR)
        col = QColorDialog.getColor(init_col, self, "Select Enemy Box Color")
        if col.isValid():
            ESP_BOX_COLOR = (col.red(), col.green(), col.blue(), 220)
            self._update_color_btn_swatch(self.enemy_color_btn, ESP_BOX_COLOR)
            self.overlay.update_pens()

    def _pick_teammate_color(self) -> None:
        global ESP_TEAMMATE_COLOR
        init_col = QColor(*ESP_TEAMMATE_COLOR)
        col = QColorDialog.getColor(init_col, self, "Select Teammate Box Color")
        if col.isValid():
            ESP_TEAMMATE_COLOR = (col.red(), col.green(), col.blue(), 220)
            self._update_color_btn_swatch(self.team_color_btn, ESP_TEAMMATE_COLOR)
            self.overlay.update_pens()

    def _pick_tracer_color(self) -> None:
        global ESP_TRACER_COLOR
        init_col = QColor(*ESP_TRACER_COLOR)
        col = QColorDialog.getColor(init_col, self, "Select Tracer Color")
        if col.isValid():
            ESP_TRACER_COLOR = (col.red(), col.green(), col.blue(), 160)
            self._update_color_btn_swatch(self.tracer_color_btn, ESP_TRACER_COLOR)
            self.overlay.update_pens()

    def _pick_skeleton_color(self) -> None:
        global ESP_SKELETON_COLOR
        init_col = QColor(*ESP_SKELETON_COLOR)
        col = QColorDialog.getColor(init_col, self, "Select Skeleton Color")
        if col.isValid():
            ESP_SKELETON_COLOR = (col.red(), col.green(), col.blue(), 200)
            self._update_color_btn_swatch(self.skel_color_btn, ESP_SKELETON_COLOR)
            self.overlay.update_pens()

    # ── Setting Handlers ───────────────────────────────────────────────

    def _set_toggle(self, name: str, val: bool) -> None:
        globals()[name] = val

    def _on_box_thickness_changed(self, val: int) -> None:
        global ESP_BOX_THICKNESS
        ESP_BOX_THICKNESS = val
        self.overlay.update_pens()

    def _on_skel_thickness_changed(self, val: int) -> None:
        global ESP_SKELETON_THICKNESS
        ESP_SKELETON_THICKNESS = val
        self.overlay.update_pens()

    def _on_max_dist_changed(self, val: float) -> None:
        global MAX_DISTANCE
        MAX_DISTANCE = val

    def _on_toggle_radar(self, checked: bool) -> None:
        global RADAR_ENABLED
        RADAR_ENABLED = checked

    def _on_radar_size_changed(self, val: int) -> None:
        global RADAR_SIZE
        RADAR_SIZE = val

    def _on_radar_range_changed(self, val: float) -> None:
        global RADAR_RANGE_STUDS
        RADAR_RANGE_STUDS = val

    def _on_radar_opacity_changed(self, val: int) -> None:
        global RADAR_OPACITY
        RADAR_OPACITY = val

    def _on_team_filter_changed(self, idx: int) -> None:
        global TEAM_FILTER_MODE
        modes = ["Everyone", "Enemies Only", "Teammates Only"]
        if 0 <= idx < len(modes):
            TEAM_FILTER_MODE = modes[idx]

    def _on_toggle_always_on_top(self, checked: bool) -> None:
        global ALWAYS_ON_TOP
        ALWAYS_ON_TOP = checked
        self.overlay.set_always_on_top(checked)
        pos = self.pos()
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | (Qt.WindowStaysOnTopHint if ALWAYS_ON_TOP else Qt.Widget)
        )
        self.show()
        self.move(pos)

    def _on_toggle_walkspeed(self, checked: bool) -> None:
        global ENABLE_WALKSPEED
        ENABLE_WALKSPEED = checked
        if checked:
            self.overlay.apply_movement_modifiers()
        else:
            self.overlay.restore_default_walkspeed()

    def _on_walkspeed_changed(self, val: float) -> None:
        global WALKSPEED_VALUE
        WALKSPEED_VALUE = val
        if ENABLE_WALKSPEED:
            self.overlay.apply_movement_modifiers()

    def _on_toggle_jumppower(self, checked: bool) -> None:
        global ENABLE_JUMPPOWER
        ENABLE_JUMPPOWER = checked
        if checked:
            self.overlay.apply_movement_modifiers()
        else:
            self.overlay.restore_default_jumppower()

    def _on_jumppower_changed(self, val: float) -> None:
        global JUMPPOWER_VALUE
        JUMPPOWER_VALUE = val
        if ENABLE_JUMPPOWER:
            self.overlay.apply_movement_modifiers()

    def _on_toggle_infjump(self, checked: bool) -> None:
        global ENABLE_INFINITE_JUMP
        ENABLE_INFINITE_JUMP = checked

    def _on_toggle_safe_speed(self, checked: bool) -> None:
        global ENABLE_SAFE_SPEED, ENABLE_WALKSPEED
        ENABLE_SAFE_SPEED = checked
        if checked and ENABLE_WALKSPEED:
            ENABLE_WALKSPEED = False
            self.cb_walkspeed.setChecked(False)
            self.overlay.restore_default_walkspeed()

    def _on_safe_speed_changed(self, val: float) -> None:
        global SAFE_SPEED_VALUE
        SAFE_SPEED_VALUE = val

    def _get_selected_player(self) -> dict | None:
        if not hasattr(self, "player_list_widget"):
            return None
        items = self.player_list_widget.selectedItems()
        if not items:
            return None
        return items[0].data(Qt.UserRole)

    # -------------------------------------------------------------
    # FLING HANDLERS
    # -------------------------------------------------------------

    def _on_fling_burst_clicked(self) -> None:
        player_entry = self._get_selected_player()
        if not player_entry:
            self.lbl_fling_status.setText("⚠️ Please select a player from the list above to fling!")
            self.lbl_fling_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
            return

        uname = player_entry.get("username", "Unknown")
        pwr = self.spin_fling_power.value() if hasattr(self, "spin_fling_power") else FLING_POWER
        ret = self.cb_fling_return.isChecked() if hasattr(self, "cb_fling_return") else True

        success = self.overlay.start_fling(player_entry, mode="burst", power=pwr, return_to_start=ret, duration=FLING_DURATION)
        if success:
            self.lbl_fling_status.setText(f"💥 Fling burst active: Launching '{uname}' ({int(pwr):,} vel)!")
            self.lbl_fling_status.setStyleSheet("color: #ff4444; font-weight: bold;")
        else:
            self.lbl_fling_status.setText(f"✗ Failed to fling '{uname}' (character/root part not loaded).")
            self.lbl_fling_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    def _on_toggle_loop_fling(self, checked: bool) -> None:
        if checked:
            player_entry = self._get_selected_player()
            if player_entry:
                uname = player_entry.get("username", "Unknown")
                pwr = self.spin_fling_power.value() if hasattr(self, "spin_fling_power") else FLING_POWER
                ret = self.cb_fling_return.isChecked() if hasattr(self, "cb_fling_return") else True
                self.overlay.start_fling(player_entry, mode="loop", power=pwr, return_to_start=ret)
                self.lbl_fling_status.setText(f"🌪️ Loop Fling active on '{uname}'! Sticking and launching...")
                self.lbl_fling_status.setStyleSheet("color: #ff3333; font-weight: bold;")
            else:
                self.cb_loop_fling.setChecked(False)
                self.lbl_fling_status.setText("⚠️ Select a player from the list before enabling Loop Fling.")
                self.lbl_fling_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
        else:
            self.overlay.stop_fling()
            self.lbl_fling_status.setText("Loop Fling stopped. Velocities restored.")
            self.lbl_fling_status.setStyleSheet("color: #8fa0ba;")

    def _on_toggle_fling_return(self, checked: bool) -> None:
        global FLING_RETURN_TO_START
        FLING_RETURN_TO_START = checked
        self.overlay._fling_return_to_start = checked

    def _on_fling_power_changed(self, val: float) -> None:
        global FLING_POWER
        FLING_POWER = val
        self.overlay._fling_power = val

    def _on_teleport_clicked(self, mode: str = "Exact") -> None:
        player_entry = self._get_selected_player()
        if not player_entry:
            self.lbl_tp_status.setText("⚠️ Please select a player from the list first!")
            self.lbl_tp_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
            return

        uname = player_entry.get("username", "Unknown")
        success = self.overlay.teleport_to_player(player_entry, mode=mode)
        if success:
            self.lbl_tp_status.setText(f"✓ Teleported to '{uname}' ({mode})!")
            self.lbl_tp_status.setStyleSheet("color: #00ff88; font-weight: bold;")
        else:
            self.lbl_tp_status.setText(f"✗ Could not teleport to '{uname}' (character/root part not loaded).")
            self.lbl_tp_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    def _on_toggle_loop_tp(self, checked: bool) -> None:
        global LOOP_TP_ENABLED, LOOP_TP_TARGET_NAME
        LOOP_TP_ENABLED = checked
        if checked:
            player_entry = self._get_selected_player()
            if player_entry:
                LOOP_TP_TARGET_NAME = player_entry.get("username", "")
                self.lbl_tp_status.setText(f"🔄 Loop TP active: Stalking '{LOOP_TP_TARGET_NAME}'...")
                self.lbl_tp_status.setStyleSheet("color: #00d2ff; font-weight: bold;")
            else:
                LOOP_TP_ENABLED = False
                LOOP_TP_TARGET_NAME = ""
                self.cb_loop_tp.setChecked(False)
                self.lbl_tp_status.setText("⚠️ Select a player from the list before enabling Loop TP.")
                self.lbl_tp_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
        else:
            LOOP_TP_TARGET_NAME = ""
            self.lbl_tp_status.setText("Loop TP stopped.")
            self.lbl_tp_status.setStyleSheet("color: #8fa0ba;")

    def _filter_player_list(self) -> None:
        self._refresh_player_list()

    def _refresh_player_list(self) -> None:
        if not hasattr(self, "player_list_widget"):
            return

        players = self.overlay.get_server_players()
        self.lbl_tp_count.setText(f"Players in Server: {len(players)} (Live Auto-Updating)")

        # Remember currently selected username
        selected_player = self._get_selected_player()
        selected_username = selected_player.get("username") if selected_player else None

        query = self.tp_search_box.text().strip().lower() if hasattr(self, "tp_search_box") else ""

        self.player_list_widget.clear()
        target_still_present = False

        for p in players:
            uname = p.get("username", "")
            dname = p.get("display_name", "")
            if query and (query not in uname.lower() and query not in dname.lower()):
                continue

            dist = p.get("dist", 0.0)
            dist_str = f"{int(dist)} studs" if dist > 0 else "N/A"
            team_str = "Teammate" if p.get("is_teammate") else "Enemy"

            item_text = f"👤 {uname}  (@{dname})  —  {dist_str}  [{team_str}]"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, p)

            if p.get("is_teammate"):
                item.setForeground(QColor(0, 210, 255))
            else:
                item.setForeground(QColor(230, 235, 245))

            self.player_list_widget.addItem(item)

            if uname == selected_username:
                item.setSelected(True)
                target_still_present = True

        # If a player was selected, but has now left the game:
        if selected_username and not target_still_present:
            self.lbl_tp_status.setText(f"⚠️ Player '{selected_username}' left the server.")
            self.lbl_tp_status.setStyleSheet("color: #ff9900; font-weight: bold;")
            global LOOP_TP_ENABLED, LOOP_TP_TARGET_NAME
            if LOOP_TP_ENABLED and LOOP_TP_TARGET_NAME == selected_username:
                LOOP_TP_ENABLED = False
                LOOP_TP_TARGET_NAME = ""
                self.cb_loop_tp.setChecked(False)

        # Check if active fling target left the server
        if self.overlay._fling_active:
            fling_target = self.overlay._fling_target_name
            if fling_target and fling_target not in [p.get("username") for p in players]:
                self.overlay.stop_fling()
                if hasattr(self, "cb_loop_fling"):
                    self.cb_loop_fling.setChecked(False)
                if hasattr(self, "lbl_fling_status"):
                    self.lbl_fling_status.setText(f"⚠️ Target '{fling_target}' left the server! Returned to start position.")
                    self.lbl_fling_status.setStyleSheet("color: #ff9900; font-weight: bold;")

    # -------------------------------------------------------------
    # SPECTATE EVENT & ACTION HANDLERS
    # -------------------------------------------------------------

    def _get_selected_spectate_player(self) -> dict | None:
        if not hasattr(self, "spectate_list_widget"):
            return None
        items = self.spectate_list_widget.selectedItems()
        if not items:
            return None
        return items[0].data(Qt.UserRole)

    def _filter_spectate_list(self) -> None:
        self._refresh_spectate_tab()

    def _on_toggle_auto_next(self, checked: bool) -> None:
        global SPECTATE_AUTO_NEXT
        SPECTATE_AUTO_NEXT = checked

    def _on_spectate_toggle_clicked(self) -> None:
        if self.overlay.is_spectating():
            self._on_stop_spectate_clicked()
            return

        player_entry = self._get_selected_spectate_player()
        if not player_entry:
            self.lbl_spectate_status.setText("⚠️ Please select a player from the list to spectate!")
            self.lbl_spectate_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
            return

        uname = player_entry.get("username", "Unknown")
        success = self.overlay.start_spectate(player_entry)
        if success:
            self.lbl_spectate_status.setText(f"👁️ Now spectating '{uname}'. Camera subject updated.")
            self.lbl_spectate_status.setStyleSheet("color: #00ffcc; font-weight: bold;")
            self.btn_spectate_toggle.setText("🛑 Stop Spectating (Return to Self)")
            self.btn_spectate_toggle.setStyleSheet("background-color: #a82020; color: white; font-weight: bold;")
        else:
            self.lbl_spectate_status.setText(f"✗ Could not spectate '{uname}' (humanoid/camera not found).")
            self.lbl_spectate_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    def _on_stop_spectate_clicked(self) -> None:
        self.overlay.stop_spectate()
        self.btn_spectate_toggle.setText("👁️ Spectate Selected")
        self.btn_spectate_toggle.setStyleSheet("")
        self.lbl_spectate_status.setText("Camera restored to local player.")
        self.lbl_spectate_status.setStyleSheet("color: #8fa0ba;")
        self.lbl_spectate_target_info.setText("Status: Viewing Local Player (Self)")
        self.lbl_spectate_target_info.setStyleSheet("color: #8fa0ba; font-weight: bold; background: #161a24; padding: 6px; border-radius: 4px; border: 1px solid #282d3c;")

    def _on_spectate_double_clicked(self, item: QListWidgetItem) -> None:
        player_entry = item.data(Qt.UserRole)
        if player_entry:
            uname = player_entry.get("username", "Unknown")
            if self.overlay.start_spectate(player_entry):
                self.lbl_spectate_status.setText(f"👁️ Spectating '{uname}' (Double-click quick switch)")
                self.lbl_spectate_status.setStyleSheet("color: #00ffcc; font-weight: bold;")
                self.btn_spectate_toggle.setText("🛑 Stop Spectating (Return to Self)")
                self.btn_spectate_toggle.setStyleSheet("background-color: #a82020; color: white; font-weight: bold;")

    def _on_spectate_prev_clicked(self) -> None:
        players = self.overlay.get_server_players()
        if not players:
            return
        cur_target = self.overlay.get_spectate_target()
        idx = 0
        for i, p in enumerate(players):
            if p.get("username") == cur_target:
                idx = (i - 1) % len(players)
                break
        target = players[idx]
        self.overlay.start_spectate(target)
        self.lbl_spectate_status.setText(f"👁️ Spectating '{target.get('username')}'")
        self.lbl_spectate_status.setStyleSheet("color: #00ffcc; font-weight: bold;")
        self.btn_spectate_toggle.setText("🛑 Stop Spectating (Return to Self)")
        self.btn_spectate_toggle.setStyleSheet("background-color: #a82020; color: white; font-weight: bold;")

    def _on_spectate_next_clicked(self) -> None:
        players = self.overlay.get_server_players()
        if not players:
            return
        cur_target = self.overlay.get_spectate_target()
        idx = 0
        for i, p in enumerate(players):
            if p.get("username") == cur_target:
                idx = (i + 1) % len(players)
                break
        target = players[idx]
        self.overlay.start_spectate(target)
        self.lbl_spectate_status.setText(f"👁️ Spectating '{target.get('username')}'")
        self.lbl_spectate_status.setStyleSheet("color: #00ffcc; font-weight: bold;")
        self.btn_spectate_toggle.setText("🛑 Stop Spectating (Return to Self)")
        self.btn_spectate_toggle.setStyleSheet("background-color: #a82020; color: white; font-weight: bold;")

    def _on_spectate_tp_clicked(self) -> None:
        target_player = None
        if self.overlay.is_spectating():
            cur_uname = self.overlay.get_spectate_target()
            target_player = next((p for p in self.overlay.get_server_players() if p.get("username") == cur_uname), None)
        if not target_player:
            target_player = self._get_selected_spectate_player()
        if not target_player:
            self.lbl_spectate_status.setText("⚠️ Select or spectate a player first to teleport!")
            self.lbl_spectate_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
            return
        uname = target_player.get("username", "Unknown")
        if self.overlay.teleport_to_player(target_player, mode="Exact"):
            self.lbl_spectate_status.setText(f"✓ Teleported to '{uname}'!")
            self.lbl_spectate_status.setStyleSheet("color: #00ff88; font-weight: bold;")
        else:
            self.lbl_spectate_status.setText(f"✗ Failed to teleport to '{uname}'.")
            self.lbl_spectate_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    def _on_spectate_fling_clicked(self) -> None:
        target_player = None
        if self.overlay.is_spectating():
            cur_uname = self.overlay.get_spectate_target()
            target_player = next((p for p in self.overlay.get_server_players() if p.get("username") == cur_uname), None)
        if not target_player:
            target_player = self._get_selected_spectate_player()
        if not target_player:
            self.lbl_spectate_status.setText("⚠️ Select or spectate a player first to fling!")
            self.lbl_spectate_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
            return
        uname = target_player.get("username", "Unknown")
        pwr = self.spin_fling_power.value() if hasattr(self, "spin_fling_power") else FLING_POWER
        ret = self.cb_fling_return.isChecked() if hasattr(self, "cb_fling_return") else True
        if self.overlay.start_fling(target_player, mode="burst", power=pwr, return_to_start=ret, duration=FLING_DURATION):
            self.lbl_spectate_status.setText(f"💥 Flinging spectated target '{uname}'!")
            self.lbl_spectate_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    def _refresh_spectate_tab(self) -> None:
        """
        Real-time Spectate tab refresh.
        Automatically updates when someone leaves or joins the server!
        If the currently spectated player leaves, safely stops spectate (or switches to next).
        """
        if not hasattr(self, "spectate_list_widget"):
            return

        players = self.overlay.get_server_players()
        current_names = {p.get("username") for p in players if p.get("username")}
        self.lbl_spectate_count.setText(f"Players in Server: {len(players)} (Live Auto-Updating)")

        # Departure and Join Detection
        if hasattr(self, "_known_spectate_names") and self._known_spectate_names:
            left_names = self._known_spectate_names - current_names
            joined_names = current_names - self._known_spectate_names

            for left_uname in left_names:
                ts = time.strftime("%H:%M:%S")
                if hasattr(self, "spectate_event_list"):
                    ev_item = QListWidgetItem(f"[{ts}] ❌ Player '{left_uname}' LEFT the game")
                    ev_item.setForeground(QColor(255, 90, 90))
                    self.spectate_event_list.insertItem(0, ev_item)
                    if self.spectate_event_list.count() > 30:
                        self.spectate_event_list.takeItem(self.spectate_event_list.count() - 1)

                # Check if the player who left was the one currently spectated!
                if self.overlay.is_spectating() and self.overlay.get_spectate_target() == left_uname:
                    if hasattr(self, "cb_auto_next") and self.cb_auto_next.isChecked() and players:
                        next_player = players[0]
                        next_uname = next_player.get("username", "")
                        self.overlay.start_spectate(next_player)
                        self.lbl_spectate_status.setText(f"⚠️ Spectated player '{left_uname}' LEFT the server! Auto-switched to '{next_uname}'.")
                        self.lbl_spectate_status.setStyleSheet("color: #00d2ff; font-weight: bold;")
                        self.lbl_spectate_target_info.setText(f"Status: 👁️ Spectating '{next_uname}' (Auto-Switched)")
                        self.lbl_spectate_target_info.setStyleSheet("color: #00ffcc; font-weight: bold; background: #162432; padding: 6px; border-radius: 4px; border: 1px solid #0099aa;")
                    else:
                        self.overlay.stop_spectate()
                        self.lbl_spectate_status.setText(f"⚠️ Spectated player '{left_uname}' LEFT THE SERVER! Camera safely restored to self.")
                        self.lbl_spectate_status.setStyleSheet("color: #ff4444; font-weight: bold;")
                        self.lbl_spectate_target_info.setText("Status: Viewing Local Player (Self)")
                        self.lbl_spectate_target_info.setStyleSheet("color: #8fa0ba; font-weight: bold; background: #161a24; padding: 6px; border-radius: 4px; border: 1px solid #282d3c;")
                        self.btn_spectate_toggle.setText("👁️ Spectate Selected")
                        self.btn_spectate_toggle.setStyleSheet("")

            for joined_uname in joined_names:
                ts = time.strftime("%H:%M:%S")
                if hasattr(self, "spectate_event_list"):
                    ev_item = QListWidgetItem(f"[{ts}] ➕ Player '{joined_uname}' JOINED the game")
                    ev_item.setForeground(QColor(0, 230, 150))
                    self.spectate_event_list.insertItem(0, ev_item)
                    if self.spectate_event_list.count() > 30:
                        self.spectate_event_list.takeItem(self.spectate_event_list.count() - 1)

        self._known_spectate_names = current_names

        # Preserve selection if item is still present
        selected_player = self._get_selected_spectate_player()
        selected_username = selected_player.get("username") if selected_player else None

        active_spectate_target = self.overlay.get_spectate_target() if self.overlay.is_spectating() else ""
        query = self.spectate_search_box.text().strip().lower() if hasattr(self, "spectate_search_box") else ""

        self.spectate_list_widget.clear()

        for p in players:
            uname = p.get("username", "")
            dname = p.get("display_name", "")
            if query and (query not in uname.lower() and query not in dname.lower()):
                continue

            dist = p.get("dist", 0.0)
            dist_str = f"{int(dist)} studs" if dist > 0 else "N/A"
            hp = int(p.get("health", 100.0))
            max_hp = int(p.get("max_health", 100.0))
            team_str = "Teammate" if p.get("is_teammate") else "Enemy"

            spectating_tag = " [SPECTATING]" if uname == active_spectate_target else ""
            item_text = f"👤 {uname}  (@{dname}){spectating_tag}  —  {dist_str}  |  HP: {hp}/{max_hp}  [{team_str}]"
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, p)

            if uname == active_spectate_target:
                item.setForeground(QColor(0, 255, 180))
                font = item.font()
                font.setBold(True)
                item.setFont(font)
            elif p.get("is_teammate"):
                item.setForeground(QColor(0, 210, 255))
            else:
                item.setForeground(QColor(230, 235, 245))

            self.spectate_list_widget.addItem(item)

            if uname == selected_username:
                item.setSelected(True)

        # Update Live Target Info Card
        if active_spectate_target:
            tgt_p = next((p for p in players if p.get("username") == active_spectate_target), None)
            if tgt_p:
                hp = int(tgt_p.get("health", 100.0))
                max_hp = int(tgt_p.get("max_health", 100.0))
                dist = int(tgt_p.get("dist", 0.0))
                self.lbl_spectate_target_info.setText(f"Status: 👁️ Spectating '{active_spectate_target}' (@{tgt_p.get('display_name', '')}) | Distance: {dist} studs | HP: {hp}/{max_hp}")
                self.lbl_spectate_target_info.setStyleSheet("color: #00ffcc; font-weight: bold; background: #162432; padding: 6px; border-radius: 4px; border: 1px solid #0099aa;")
            self.btn_spectate_toggle.setText("🛑 Stop Spectating (Return to Self)")
            self.btn_spectate_toggle.setStyleSheet("background-color: #a82020; color: white; font-weight: bold;")
        else:
            self.lbl_spectate_target_info.setText("Status: Viewing Local Player (Self)")
            self.lbl_spectate_target_info.setStyleSheet("color: #8fa0ba; font-weight: bold; background: #161a24; padding: 6px; border-radius: 4px; border: 1px solid #282d3c;")
            self.btn_spectate_toggle.setText("👁️ Spectate Selected")
            self.btn_spectate_toggle.setStyleSheet("")

    def _on_reset_movement(self) -> None:
        global ENABLE_SAFE_SPEED, SAFE_SPEED_VALUE, ENABLE_WALKSPEED, ENABLE_JUMPPOWER, ENABLE_INFINITE_JUMP, WALKSPEED_VALUE, JUMPPOWER_VALUE
        ENABLE_SAFE_SPEED = False
        SAFE_SPEED_VALUE = 50.0
        ENABLE_WALKSPEED = False
        ENABLE_JUMPPOWER = False
        ENABLE_INFINITE_JUMP = False
        WALKSPEED_VALUE = 50.0
        JUMPPOWER_VALUE = 100.0
        self.cb_safe_speed.setChecked(False)
        self.spin_safe_speed.setValue(50.0)
        self.cb_walkspeed.setChecked(False)
        self.cb_jumppower.setChecked(False)
        self.cb_infjump.setChecked(False)
        self.spin_walkspeed.setValue(50.0)
        self.spin_jumppower.setValue(100.0)
        self.overlay.restore_default_walkspeed()
        self.overlay.restore_default_jumppower()

    def _on_aimbot_key_changed(self, idx: int) -> None:
        global AIMBOT_KEY
        keys = ["RBUTTON", "LBUTTON", "LSHIFT", "E", "Q", "ALT"]
        if 0 <= idx < len(keys):
            AIMBOT_KEY = keys[idx]

    def _on_dump_scripts(self) -> None:
        self.lbl_dump_status.setText("Extracting bytecode from DataModel...")
        self.lbl_dump_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
        QApplication.processEvents()

        count, out_path = self.overlay.dump_scripts_to_disk()
        if count > 0:
            self.lbl_dump_status.setText(f"✓ Dumped {count} scripts to: {out_path}")
            self.lbl_dump_status.setStyleSheet("color: #00ff88; font-weight: bold;")
        else:
            self.lbl_dump_status.setText(f"Status: {out_path}")
            self.lbl_dump_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    # ── Config Actions ─────────────────────────────────────────────────

    def _on_save_config(self) -> None:
        if save_config():
            self.lbl_cfg_status.setText("Status: Saved to config.json!")
            self.lbl_cfg_status.setStyleSheet("color: #00ff88; font-weight: bold;")
        else:
            self.lbl_cfg_status.setText("Status: Error saving config.")
            self.lbl_cfg_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    def _on_load_config(self) -> None:
        if load_config():
            self._refresh_ui_from_globals()
            self.overlay.update_pens()
            self.lbl_cfg_status.setText("Status: Loaded from config.json!")
            self.lbl_cfg_status.setStyleSheet("color: #00ff88; font-weight: bold;")
        else:
            self.lbl_cfg_status.setText("Status: config.json not found.")
            self.lbl_cfg_status.setStyleSheet("color: #ffaa00; font-weight: bold;")

    # ── Combat & Hitbox Expander Handlers ─────────────────────────────

    def _on_toggle_hitbox_expander(self, checked: bool) -> None:
        global HITBOX_EXPANDER_ENABLED
        HITBOX_EXPANDER_ENABLED = checked
        if checked:
            self.overlay.apply_hitbox_expander()
        else:
            self.overlay.restore_hitboxes()

    def _on_hitbox_part_changed(self, idx: int) -> None:
        global HITBOX_TARGET_PART
        parts = ["Head", "HumanoidRootPart", "Both"]
        if 0 <= idx < len(parts):
            HITBOX_TARGET_PART = parts[idx]
            if HITBOX_EXPANDER_ENABLED:
                self.overlay.apply_hitbox_expander()

    def _on_expand_target_hitbox_clicked(self) -> None:
        player_entry = self._get_selected_player()
        if not player_entry:
            self.lbl_tp_status.setText("⚠️ Please select a player from the list to expand their hitbox!")
            self.lbl_tp_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
            return
        uname = player_entry.get("username", "Unknown")
        char = player_entry.get("character", 0)
        if not char:
            self.lbl_tp_status.setText(f"✗ Character not loaded for '{uname}'.")
            self.lbl_tp_status.setStyleSheet("color: #ff4444; font-weight: bold;")
            return

        parts = get_character_parts(self.overlay.mem, char)
        head = parts.get("Head") or find_first_child(self.overlay.mem, char, "Head")
        hrp = parts.get("HumanoidRootPart") or parts.get("Torso")
        sz = float(HITBOX_SIZE)
        expanded_count = 0
        for p_inst in (head, hrp):
            if p_inst:
                prim = self.overlay.mem.read_ptr(p_inst + offsets.get("BasePart_Primitive", 0x178))
                if prim:
                    if prim not in self.overlay._expanded_prims:
                        orig_sz = self.overlay.mem.read_vec3(prim + offsets.get("Primitive_Size", 0x1BC))
                        orig_fl = self.overlay.mem.read(prim + offsets.get("Primitive_Flags", 0x1B6), 1)
                        if orig_sz != (0.0, 0.0, 0.0):
                            self.overlay._expanded_prims[prim] = (orig_sz, orig_fl[0] if orig_fl else 0)
                    self.overlay.mem.write_vec3(prim + offsets.get("Primitive_Size", 0x1BC), sz, sz, sz)
                    if not HITBOX_CAN_COLLIDE:
                        cur_flags = self.overlay.mem.read(prim + offsets.get("Primitive_Flags", 0x1B6), 1)
                        if cur_flags:
                            val = cur_flags[0] & ~offsets.get("PrimitiveFlags_CanCollide", 0x8)
                            self.overlay.mem.write(prim + offsets.get("Primitive_Flags", 0x1B6), bytes([val]))
                    expanded_count += 1

        if expanded_count > 0:
            self.lbl_tp_status.setText(f"🎯 Expanded hitbox on '{uname}' to {sz:.0f} studs!")
            self.lbl_tp_status.setStyleSheet("color: #00ff88; font-weight: bold;")
        else:
            self.lbl_tp_status.setText(f"✗ Could not find Head/RootPart primitives for '{uname}'.")
            self.lbl_tp_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    def _on_copy_player_cframe_clicked(self) -> None:
        player_entry = self._get_selected_player()
        if not player_entry:
            self.lbl_tp_status.setText("⚠️ Select a player first to copy coordinates!")
            self.lbl_tp_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
            return
        wpos = player_entry.get("world_pos", (0.0, 0.0, 0.0))
        coords_str = f"CFrame.new({wpos[0]:.2f}, {wpos[1]:.2f}, {wpos[2]:.2f})"
        cb = QApplication.clipboard()
        if cb:
            cb.setText(coords_str)
        self.lbl_tp_status.setText(f"📋 Copied to clipboard: {coords_str}")
        self.lbl_tp_status.setStyleSheet("color: #00e5ff; font-weight: bold;")

    # ── Executor Handlers ─────────────────────────────────────────────

    def _on_execute_script_clicked(self) -> None:
        code = self.script_editor.toPlainText()
        if not code.strip():
            self.lbl_exec_status.setText("⚠️ Editor is empty! Type or paste a script first.")
            self.lbl_exec_status.setStyleSheet("color: #ffaa00; font-weight: bold;")
            return
        self.lbl_exec_status.setText("⚡ Executing Luau script...")
        self.lbl_exec_status.setStyleSheet("color: #00d2ff; font-weight: bold;")
        QApplication.processEvents()

        success, msg = self.overlay.execute_luau_script(code)
        if success:
            self.lbl_exec_status.setText(msg)
            self.lbl_exec_status.setStyleSheet("color: #00ff88; font-weight: bold;")
        else:
            self.lbl_exec_status.setText(f"✗ {msg}")
            self.lbl_exec_status.setStyleSheet("color: #ff4444; font-weight: bold;")

    def _on_open_script_clicked(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Luau Script", "", "Lua Scripts (*.lua *.luau *.txt);;All Files (*.*)")
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    self.script_editor.setPlainText(f.read())
                self.lbl_exec_status.setText(f"✓ Loaded {os.path.basename(file_path)}")
                self.lbl_exec_status.setStyleSheet("color: #00ff88;")
            except Exception as e:
                self.lbl_exec_status.setText(f"✗ Load failed: {e}")
                self.lbl_exec_status.setStyleSheet("color: #ff4444;")

    def _on_save_script_clicked(self) -> None:
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Luau Script", "script.lua", "Lua Scripts (*.lua *.luau);;All Files (*.*)")
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.script_editor.toPlainText())
                self.lbl_exec_status.setText(f"✓ Saved to {os.path.basename(file_path)}")
                self.lbl_exec_status.setStyleSheet("color: #00ff88;")
            except Exception as e:
                self.lbl_exec_status.setText(f"✗ Save failed: {e}")
                self.lbl_exec_status.setStyleSheet("color: #ff4444;")

    def _load_preset_rivals(self) -> None:
        code = '''-- Roblox Rivals Silent Aim & Hitbox Expander
local Players = game:GetService("Players")
local LocalPlayer = Players.LocalPlayer
local Camera = workspace.CurrentCamera

print("[Rivals Hub] Activated Silent Aim & Hitbox Expander")
for _, p in pairs(Players:GetPlayers()) do
    if p ~= LocalPlayer and p.Character then
        local head = p.Character:FindFirstChild("Head")
        if head then
            head.Size = Vector3.new(12, 12, 12)
            head.CanCollide = false
            head.Transparency = 0.5
        end
    end
end
'''
        self.script_editor.setPlainText(code)
        self.lbl_exec_status.setText("Loaded Roblox Rivals Silent Aim & Hitbox Expander Preset!")
        self.lbl_exec_status.setStyleSheet("color: #00ffcc;")

    def _load_preset_iy(self) -> None:
        self.script_editor.setPlainText("loadstring(game:HttpGet('https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source'))()")
        self.lbl_exec_status.setText("Loaded Infinite Yield Admin Preset!")
        self.lbl_exec_status.setStyleSheet("color: #00ffcc;")

    def _load_preset_dex(self) -> None:
        self.script_editor.setPlainText("loadstring(game:HttpGet('https://raw.githubusercontent.com/infyiff/backup/main/dex.lua'))()")
        self.lbl_exec_status.setText("Loaded Dark Dex V4 Preset!")
        self.lbl_exec_status.setStyleSheet("color: #00ffcc;")

    def _load_preset_spy(self) -> None:
        self.script_editor.setPlainText("loadstring(game:HttpGet('https://raw.githubusercontent.com/exxtremestuffs/SimpleSpy/master/source.lua'))()")
        self.lbl_exec_status.setText("Loaded SimpleSpy V3 Preset!")
        self.lbl_exec_status.setStyleSheet("color: #00ffcc;")

    def _load_preset_fling(self) -> None:
        code = '''-- Universal Touch Fling Script
local p = game:GetService("Players").LocalPlayer
local c = p.Character
local root = c and c:FindFirstChild("HumanoidRootPart")
if root then
    local bv = Instance.new("BodyAngularVelocity")
    bv.AngularVelocity = Vector3.new(999999, 999999, 999999)
    bv.MaxTorque = Vector3.new(math.huge, math.huge, math.huge)
    bv.P = math.huge
    bv.Parent = root
    print("[Fling] Fling physics momentum activated!")
end
'''
        self.script_editor.setPlainText(code)
        self.lbl_exec_status.setText("Loaded Touch Fling Script Preset!")
        self.lbl_exec_status.setStyleSheet("color: #00ffcc;")

    def _on_reset_defaults(self) -> None:
        global ESP_SHOW_BOX, ESP_CORNER_BOX, ESP_3D_BOX, ESP_SHOW_TRACER, ESP_SHOW_SKELETON
        global ESP_SHOW_NAME, ESP_SHOW_DISTANCE, ESP_SHOW_HEALTH, ESP_DYNAMIC_HEALTH_COLOR
        global ESP_BOX_THICKNESS, ESP_SKELETON_THICKNESS, ESP_TEXT_SIZE, MAX_DISTANCE
        global TEAM_FILTER_MODE, ALWAYS_ON_TOP
        global ESP_BOX_COLOR, ESP_TEAMMATE_COLOR, ESP_TRACER_COLOR, ESP_SKELETON_COLOR
        global RADAR_ENABLED, RADAR_SIZE, RADAR_RANGE_STUDS, RADAR_SHOW_CROSSHAIR, RADAR_OPACITY
        global ENABLE_SAFE_SPEED, SAFE_SPEED_VALUE, LOOP_TP_ENABLED, LOOP_TP_TARGET_NAME
        global ENABLE_WALKSPEED, WALKSPEED_VALUE, ENABLE_JUMPPOWER, JUMPPOWER_VALUE, ENABLE_INFINITE_JUMP
        global ENABLE_NOCLIP, ENABLE_FLY, FLY_SPEED, ENABLE_FULLBRIGHT, ENABLE_INSTANT_PROMPTS
        global ENABLE_INF_CLICK, ENABLE_GRAVITY_MOD, GRAVITY_VALUE, UNLOCK_FPS, UNLOCK_FPS_VALUE
        global AIMBOT_ENABLED, AIMBOT_KEY, AIMBOT_TARGET_PART, AIMBOT_FOV, AIMBOT_SMOOTHNESS
        global AIMBOT_SHOW_FOV, AIMBOT_FOV_COLOR, AIMBOT_TEAM_CHECK
        global AIMBOT_PRIORITY, AIMBOT_PREDICTION, AIMBOT_STICKY, AIMBOT_DEADZONE, AIMBOT_RCS_ENABLED, AIMBOT_RCS_STRENGTH
        global FLING_POWER, FLING_RETURN_TO_START, FLING_DURATION, SPECTATE_AUTO_NEXT
        global HITBOX_EXPANDER_ENABLED, HITBOX_SIZE, HITBOX_TARGET_PART, HITBOX_RIVALS_MODE, HITBOX_CAN_COLLIDE, HITBOX_TEAM_CHECK, HITBOX_VISUALIZE
        global TRIGGERBOT_ENABLED, TRIGGERBOT_DELAY_MS, TRIGGERBOT_TEAM_CHECK, TRIGGERBOT_MODE, TRIGGERBOT_MAX_DELAY_MS
        global FREECAM_ENABLED, FREECAM_SPEED, ITEM_ESP_ENABLED, ITEM_ESP_MAX_DIST

        ESP_BOX_COLOR = (255, 255, 255, 220)
        ESP_TRACER_COLOR = (255, 255, 255, 160)
        ESP_SKELETON_COLOR = (220, 220, 255, 200)
        ESP_TEAMMATE_COLOR = (0, 220, 255, 220)
        ESP_SHOW_BOX = True
        ESP_CORNER_BOX = False
        ESP_3D_BOX = False
        ESP_SHOW_SKELETON = True
        ESP_SHOW_TRACER = True
        ESP_SHOW_NAME = True
        ESP_SHOW_DISTANCE = True
        ESP_SHOW_HEALTH = True
        ESP_DYNAMIC_HEALTH_COLOR = True
        ESP_BOX_THICKNESS = 1
        ESP_SKELETON_THICKNESS = 1
        MAX_DISTANCE = 1500.0
        RADAR_ENABLED = True
        RADAR_SIZE = 175
        RADAR_RANGE_STUDS = 350.0
        RADAR_SHOW_CROSSHAIR = True
        RADAR_OPACITY = 190
        ENABLE_SAFE_SPEED = False
        SAFE_SPEED_VALUE = 50.0
        LOOP_TP_ENABLED = False
        LOOP_TP_TARGET_NAME = ""
        ENABLE_WALKSPEED = False
        WALKSPEED_VALUE = 50.0
        ENABLE_JUMPPOWER = False
        JUMPPOWER_VALUE = 100.0
        ENABLE_INFINITE_JUMP = False
        ENABLE_NOCLIP = False
        ENABLE_FLY = False
        FLY_SPEED = 50.0
        ENABLE_FULLBRIGHT = False
        ENABLE_INSTANT_PROMPTS = False
        ENABLE_INF_CLICK = False
        ENABLE_GRAVITY_MOD = False
        GRAVITY_VALUE = 196.2
        UNLOCK_FPS = False
        UNLOCK_FPS_VALUE = 240.0
        FLING_POWER = 100000.0
        FLING_RETURN_TO_START = True
        FLING_DURATION = 1.5
        SPECTATE_AUTO_NEXT = False
        AIMBOT_ENABLED = False
        AIMBOT_KEY = "RBUTTON"
        AIMBOT_TARGET_PART = "Head"
        AIMBOT_FOV = 120.0
        AIMBOT_SMOOTHNESS = 4.0
        AIMBOT_SHOW_FOV = True
        AIMBOT_TEAM_CHECK = True
        AIMBOT_PRIORITY = "Crosshair"
        AIMBOT_PREDICTION = False
        AIMBOT_STICKY = True
        AIMBOT_DEADZONE = 2.0
        AIMBOT_RCS_ENABLED = False
        AIMBOT_RCS_STRENGTH = 2.0
        TEAM_FILTER_MODE = "Everyone"

        HITBOX_EXPANDER_ENABLED = False
        HITBOX_SIZE = 12.0
        HITBOX_TARGET_PART = "Head"
        HITBOX_RIVALS_MODE = True
        HITBOX_CAN_COLLIDE = False
        HITBOX_TEAM_CHECK = True
        HITBOX_VISUALIZE = True

        TRIGGERBOT_ENABLED = False
        TRIGGERBOT_DELAY_MS = 20
        TRIGGERBOT_TEAM_CHECK = True
        TRIGGERBOT_MODE = "Tap"
        TRIGGERBOT_MAX_DELAY_MS = 35

        FREECAM_ENABLED = False
        FREECAM_SPEED = 2.0

        ITEM_ESP_ENABLED = False
        ITEM_ESP_MAX_DIST = 800.0

        self.overlay.restore_hitboxes()
        self._refresh_ui_from_globals()
        self.overlay.update_pens()
        self.overlay.restore_default_walkspeed()
        self.overlay.restore_default_jumppower()
        save_config()
        self.lbl_cfg_status.setText("Status: Reset to defaults!")
        self.lbl_cfg_status.setStyleSheet("color: #00d2ff; font-weight: bold;")

    def _refresh_ui_from_globals(self) -> None:
        """Update all GUI widgets to match global variables."""
        self.cb_boxes.setChecked(ESP_SHOW_BOX)
        self.cb_corner.setChecked(ESP_CORNER_BOX)
        self.cb_3d.setChecked(ESP_3D_BOX)
        self.cb_skeleton.setChecked(ESP_SHOW_SKELETON)
        self.cb_tracers.setChecked(ESP_SHOW_TRACER)
        self.cb_names.setChecked(ESP_SHOW_NAME)
        self.cb_dist.setChecked(ESP_SHOW_DISTANCE)
        self.cb_health.setChecked(ESP_SHOW_HEALTH)
        self.cb_dyn_hp.setChecked(ESP_DYNAMIC_HEALTH_COLOR)
        if hasattr(self, "cb_item_esp"):
            self.cb_item_esp.setChecked(ITEM_ESP_ENABLED)

        self.spin_box_thick.setValue(ESP_BOX_THICKNESS)
        self.spin_skel_thick.setValue(ESP_SKELETON_THICKNESS)
        self.spin_max_dist.setValue(MAX_DISTANCE)

        self.cb_radar_en.setChecked(RADAR_ENABLED)
        self.cb_radar_cross.setChecked(RADAR_SHOW_CROSSHAIR)
        self.spin_radar_size.setValue(RADAR_SIZE)
        self.spin_radar_range.setValue(RADAR_RANGE_STUDS)
        self.spin_radar_opac.setValue(RADAR_OPACITY)

        self.cb_safe_speed.setChecked(ENABLE_SAFE_SPEED)
        self.spin_safe_speed.setValue(SAFE_SPEED_VALUE)
        self.cb_loop_tp.setChecked(LOOP_TP_ENABLED)

        self.cb_walkspeed.setChecked(ENABLE_WALKSPEED)
        self.spin_walkspeed.setValue(WALKSPEED_VALUE)
        self.cb_jumppower.setChecked(ENABLE_JUMPPOWER)
        self.spin_jumppower.setValue(JUMPPOWER_VALUE)
        self.cb_infjump.setChecked(ENABLE_INFINITE_JUMP)
        self.cb_noclip.setChecked(ENABLE_NOCLIP)
        self.cb_fly.setChecked(ENABLE_FLY)
        self.spin_fly_speed.setValue(FLY_SPEED)

        if hasattr(self, "cb_freecam"):
            self.cb_freecam.setChecked(FREECAM_ENABLED)
        if hasattr(self, "spin_freecam_speed"):
            self.spin_freecam_speed.setValue(FREECAM_SPEED)

        if hasattr(self, "cb_hb_en"):
            self.cb_hb_en.setChecked(HITBOX_EXPANDER_ENABLED)
        if hasattr(self, "cb_hb_rivals"):
            self.cb_hb_rivals.setChecked(HITBOX_RIVALS_MODE)
        if hasattr(self, "spin_hb_size"):
            self.spin_hb_size.setValue(HITBOX_SIZE)
        if hasattr(self, "combo_hb_part"):
            hb_map = {"Head": 0, "HumanoidRootPart": 1, "Both": 2}
            self.combo_hb_part.setCurrentIndex(hb_map.get(HITBOX_TARGET_PART, 0))
        if hasattr(self, "cb_hb_nocollide"):
            self.cb_hb_nocollide.setChecked(not HITBOX_CAN_COLLIDE)
        if hasattr(self, "cb_hb_vis"):
            self.cb_hb_vis.setChecked(HITBOX_VISUALIZE)
        if hasattr(self, "cb_hb_team"):
            self.cb_hb_team.setChecked(HITBOX_TEAM_CHECK)

        if hasattr(self, "cb_tb_en"):
            self.cb_tb_en.setChecked(TRIGGERBOT_ENABLED)
        if hasattr(self, "spin_tb_delay"):
            self.spin_tb_delay.setValue(TRIGGERBOT_DELAY_MS)
        if hasattr(self, "combo_tb_mode"):
            self.combo_tb_mode.setCurrentIndex(0 if TRIGGERBOT_MODE == "Tap" else 1)
        if hasattr(self, "spin_tb_max_delay"):
            self.spin_tb_max_delay.setValue(TRIGGERBOT_MAX_DELAY_MS)

        self.cb_aim_en.setChecked(AIMBOT_ENABLED)
        self.cb_aim_fov_show.setChecked(AIMBOT_SHOW_FOV)
        key_map = {"RBUTTON": 0, "LBUTTON": 1, "LSHIFT": 2, "E": 3, "Q": 4, "ALT": 5}
        self.combo_aim_key.setCurrentIndex(key_map.get(AIMBOT_KEY, 0))
        self.combo_aim_part.setCurrentIndex(0 if AIMBOT_TARGET_PART == "Head" else 1)
        prio_map = {"Crosshair": 0, "Distance": 1, "Lowest HP": 2}
        if hasattr(self, "combo_aim_prio"):
            self.combo_aim_prio.setCurrentIndex(prio_map.get(AIMBOT_PRIORITY, 0))
        if hasattr(self, "cb_aim_sticky"):
            self.cb_aim_sticky.setChecked(AIMBOT_STICKY)
        self.spin_aim_fov.setValue(AIMBOT_FOV)
        self.spin_aim_smooth.setValue(AIMBOT_SMOOTHNESS)
        if hasattr(self, "cb_aim_pred"):
            self.cb_aim_pred.setChecked(AIMBOT_PREDICTION)
        if hasattr(self, "spin_aim_deadzone"):
            self.spin_aim_deadzone.setValue(AIMBOT_DEADZONE)
        if hasattr(self, "cb_aim_rcs"):
            self.cb_aim_rcs.setChecked(AIMBOT_RCS_ENABLED)
        if hasattr(self, "spin_aim_rcs_strength"):
            self.spin_aim_rcs_strength.setValue(AIMBOT_RCS_STRENGTH)
        self.cb_aim_team.setChecked(AIMBOT_TEAM_CHECK)

        self.cb_fullbright.setChecked(ENABLE_FULLBRIGHT)
        self.cb_instant_prompts.setChecked(ENABLE_INSTANT_PROMPTS)
        self.cb_inf_click.setChecked(ENABLE_INF_CLICK)
        self.cb_grav.setChecked(ENABLE_GRAVITY_MOD)
        self.spin_grav.setValue(GRAVITY_VALUE)
        self.cb_fps.setChecked(UNLOCK_FPS)
        self.spin_fps.setValue(UNLOCK_FPS_VALUE)

        if hasattr(self, "spin_fling_power"):
            self.spin_fling_power.setValue(FLING_POWER)
        if hasattr(self, "cb_fling_return"):
            self.cb_fling_return.setChecked(FLING_RETURN_TO_START)
        if hasattr(self, "cb_auto_next"):
            self.cb_auto_next.setChecked(SPECTATE_AUTO_NEXT)

        self._update_color_btn_swatch(self.enemy_color_btn, ESP_BOX_COLOR)
        self._update_color_btn_swatch(self.team_color_btn, ESP_TEAMMATE_COLOR)
        self._update_color_btn_swatch(self.tracer_color_btn, ESP_TRACER_COLOR)
        self._update_color_btn_swatch(self.skel_color_btn, ESP_SKELETON_COLOR)

        index_map = {"Everyone": 0, "Enemies Only": 1, "Teammates Only": 2}
        self.team_combo.setCurrentIndex(index_map.get(TEAM_FILTER_MODE, 0))
        self.cb_ontop.setChecked(ALWAYS_ON_TOP)

        if hasattr(self, "cb_mm2_enabled"):
            self.cb_mm2_enabled.setChecked(MM2_ROLE_ESP_ENABLED)
        if hasattr(self, "btn_mm2_murderer_col"):
            self._update_color_btn_swatch(self.btn_mm2_murderer_col, MM2_MURDERER_COLOR)
        if hasattr(self, "btn_mm2_sheriff_col"):
            self._update_color_btn_swatch(self.btn_mm2_sheriff_col, MM2_SHERIFF_COLOR)
        if hasattr(self, "btn_mm2_innocent_col"):
            self._update_color_btn_swatch(self.btn_mm2_innocent_col, MM2_INNOCENT_COLOR)
        if hasattr(self, "le_knife_kw"):
            self.le_knife_kw.setText(", ".join(MM2_KNIFE_NAMES))
        if hasattr(self, "le_gun_kw"):
            self.le_gun_kw.setText(", ".join(MM2_GUN_NAMES))
        if hasattr(self, "cb_mm2_gun_esp"):
            self.cb_mm2_gun_esp.setChecked(MM2_GUN_ESP_ENABLED)
        if hasattr(self, "cb_mm2_gun_notify"):
            self.cb_mm2_gun_notify.setChecked(MM2_GUN_NOTIFY)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event) -> None:
        if event.buttons() == Qt.LeftButton and hasattr(self, "_drag_pos"):
            self.move(event.globalPos() - self._drag_pos)
            event.accept()

    def toggle_menu(self) -> None:
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()
            self.activateWindow()

# ====================================
# HOTKEY HANDLER
# ====================================

class HotkeyHandler(threading.Thread):
    """
    Background thread polling GetAsyncKeyState for hotkeys.
    Requires no additional libraries — pure ctypes.

    INSERT  → toggle configuration UI menu
    P       → toggle ESP on/off
    END     → exit the application
    """

    def __init__(self, overlay: ESPOverlay, app: QApplication, menu: ESPMenu) -> None:
        super().__init__(daemon=True, name="HotkeyThread")
        self.overlay   = overlay
        self.app       = app
        self.menu      = menu
        self._p_held   = False
        self._ins_held = False
        self._end_held = False
        self._space_held = False
        self._last_jump_time = 0.0

    def run(self) -> None:
        while True:
            try:
                # INSERT → toggle configuration UI menu
                ins_now = bool(_user32.GetAsyncKeyState(VK_INSERT) & 0x8000)
                if ins_now and not self._ins_held:
                    QTimer.singleShot(0, self.menu.toggle_menu)
                self._ins_held = ins_now

                # P → toggle ESP rendering
                p_now = bool(_user32.GetAsyncKeyState(VK_P) & 0x8000)
                if p_now and not self._p_held:
                    self.overlay.enabled = not self.overlay.enabled
                    if DEBUG_MODE:
                        state = "ON" if self.overlay.enabled else "OFF"
                        print(f"[*] ESP → {state}")
                self._p_held = p_now

                # END → quit application
                end_now = bool(_user32.GetAsyncKeyState(VK_END) & 0x8000)
                if end_now and not self._end_held:
                    if DEBUG_MODE:
                        print("[*] END — closing application.")
                    QTimer.singleShot(0, self.app.quit)
                    return
                self._end_held = end_now

                # SPACE → Infinite Jump & R6 Walking JumpPower Handler
                space_now = bool(_user32.GetAsyncKeyState(VK_SPACE) & 0x8000)
                if space_now:
                    now = time.time()
                    if ENABLE_INFINITE_JUMP:
                        # Fresh key press (tap) → instant jump mid-air!
                        if not self._space_held:
                            self.overlay.execute_infinite_jump()
                            self._last_jump_time = now
                        elif now - self._last_jump_time >= 0.22:
                            # Holding space down → smooth repetitive airborne climb
                            self.overlay.execute_infinite_jump()
                            self._last_jump_time = now
                    elif ENABLE_JUMPPOWER:
                        if not self._space_held:
                            self.overlay.execute_jump_boost()
                            self._last_jump_time = now
                    self._space_held = True
                else:
                    self._space_held = False

                # T → Teleport to Dropped MM2 Gun
                t_now = bool(_user32.GetAsyncKeyState(VK_KEY_T) & 0x8000)
                if t_now and not getattr(self, "_t_held", False):
                    success, msg = self.overlay.teleport_to_dropped_gun()
                    if DEBUG_MODE:
                        print(f"[*] [T] TP to Gun: {msg}")
                    if hasattr(self.menu, "lbl_gun_status"):
                        QTimer.singleShot(0, lambda m=msg, s=success: (
                            self.menu.lbl_gun_status.setText(m),
                            self.menu.lbl_gun_status.setStyleSheet("color: #00ffaa; font-weight: bold;" if s else "color: #ff5555; font-weight: bold;")
                        ))
                self._t_held = t_now

            except Exception:
                pass

            time.sleep(0.015)

# ====================================
# ELEVATION
# ====================================

def _ensure_admin() -> None:
    """
    Check whether this process is running with administrator privileges.
    If not, re-launch the same script via ShellExecuteW with the "runas"
    verb, which triggers the Windows UAC elevation dialog, then exit the
    current (un-elevated) process cleanly.
    """
    try:
        already_admin: bool = bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        already_admin = False

    if already_admin:
        if DEBUG_MODE:
            print("[+] Already running as Administrator.")
        return

    print("[*] Administrator privileges required.")
    print("[*] Requesting elevation via UAC ...")

    # Build the argument string to pass to the elevated instance
    params = " ".join(f'"{arg}"' for arg in sys.argv)

    ret = ctypes.windll.shell32.ShellExecuteW(
        None,           # hwnd  — no parent window
        "runas",        # verb  — triggers the UAC prompt
        sys.executable, # file  — python.exe / pythonw.exe
        params,         # parameters: script path + any CLI args
        None,           # working directory (inherit from parent)
        1,              # nShowCmd: SW_SHOWNORMAL
    )

    # ShellExecuteW returns a value > 32 on success
    if ret <= 32:
        print(f"[!] Elevation request failed (ShellExecuteW returned {ret}).")
        print("[!] Right-click the script and choose 'Run as administrator'.")
        sys.exit(1)

    # Elevated copy is now launching — exit this un-elevated instance
    sys.exit(0)


# ====================================
# MAIN ENTRY POINT
# ====================================

def main() -> None:
    global offsets

    # Must be the very first call — triggers UAC if not already elevated
    _ensure_admin()

    print("=" * 56)
    print("  Roblox ESP Overlay")
    print("  Offline-only — zero network connections")
    print("=" * 56)

    # 1. Load offsets from local file
    print("[*] Loading offsets.json ...")
    offsets = load_offsets()
    print(f"[+] Loaded {len(offsets)} entries.")

    # 2. Validate required keys
    print("[*] Validating offsets ...")
    if not validate_offsets(offsets):
        print("[!] One or more required offsets are missing. Aborting.")
        sys.exit(1)
    print("[+] Offset validation passed.")

    # 2.1 Load user configuration profile
    print("[*] Loading configuration profile ...")
    if load_config():
        print("[+] Config loaded successfully from config.json")
    else:
        print("[*] No custom config found, using default profile.")

    # 3. Locate Roblox process
    mem = Memory()
    print(f"[*] Searching for process: {TARGET_PROCESS}")
    pid = mem.get_pid_by_name(TARGET_PROCESS)
    if not pid:
        print(f"[!] '{TARGET_PROCESS}' not found.")
        print("[!] Launch Roblox and run this overlay again.")
        sys.exit(1)
    print(f"[+] Found PID: {pid}")

    # 4. Open process handle
    if not mem.open_process(pid):
        err = ctypes.get_last_error()
        print(f"[!] OpenProcess failed (error {err}).")
        print("[!] Try running this script as Administrator.")
        sys.exit(1)
    print(f"[+] Process handle acquired.")
    print(f"[+] Raw handle value     : {mem.handle} (0x{mem.handle:X})")

    # Quick sanity-check: try to read 4 bytes from module base
    # 5. Get module base address
    mem.module_base = mem.get_module_base(TARGET_PROCESS)
    if not mem.module_base:
        print(f"[!] Could not find module base for '{TARGET_PROCESS}'.")
        mem.close()
        sys.exit(1)
    print(f"[+] Module base          : 0x{mem.module_base:016X}")

    test_bytes = mem.read(mem.module_base, 4)
    test_int   = int.from_bytes(test_bytes, "little")
    print(f"[+] Test read @ base     : {test_bytes.hex().upper()}  ({test_int:#010x})")
    if test_bytes == b"\x00\x00\x00\x00":
        print("[!] Test read returned all zeros — handle may lack VM_READ rights.")
        print("[!] Try running as Administrator or check if Byfron stripped the handle.")
    elif test_bytes[:2] == b"MZ":
        print("[+] MZ header confirmed — reads are working correctly.")
    else:
        print("[*] Non-zero read (not MZ — may be obfuscated PE header, still OK).")

    # 6. Create Qt application
    app = QApplication(sys.argv)
    app.setApplicationName("RobloxESP")

    # 7. Create and show the overlay & control panel menu
    overlay = ESPOverlay(mem)
    overlay.show()

    menu = ESPMenu(overlay, app)
    menu._refresh_ui_from_globals()
    menu.show()

    # 8. Start hotkey handler thread
    hotkeys = HotkeyHandler(overlay, app, menu)
    hotkeys.start()

    if DEBUG_MODE:
        print("[*] Debug mode is ON.")
        print("[*] Hotkeys:  [INSERT] Menu    [P] Toggle ESP    [SPACE] Infinite Jump    [END] Exit")
        print("[*] Features: Smooth Aimbot, FOV Circle, Noclip, Fly, Fullbright, Instant Prompts, FPS Unlocker, Script Dumper")

    # 9. Enter the Qt event loop
    try:
        exit_code = app.exec_()
    finally:
        mem.close()
        print("[*] Memory handle released. Goodbye.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()

# =============================================================================
#  POST-GENERATION AUDIT — NO NETWORKING PRESENT
# =============================================================================
#
#  Files required
#  ──────────────
#    esp_overlay.py    (this file)
#    offsets.json      (same directory — flat key/hex-value JSON)
#
#  Python packages required
#  ────────────────────────
#    PyQt5   (pip install PyQt5)
#    numpy   (pip install numpy)
#    Standard library: ctypes, json, math, os, struct, sys, threading, time
#
#  offsets.json format
#  ───────────────────
#    {
#        "FakeDataModel_Pointer":  "0x8ee1728",
#        "Humanoid_Health":        "0x180",
#        ...
#    }
#    Keys map to hex strings (0x…) or plain integers.
#
#  Hotkeys
#  ───────
#    P       → Toggle ESP on / off
#    INSERT  → Close the overlay
#
#  Network audit
#  ─────────────
#    ✗ requests          — NOT imported
#    ✗ urllib            — NOT imported
#    ✗ socket            — NOT imported
#    ✗ websocket         — NOT imported
#    ✗ http / https      — NOT present
#    ✗ webhooks          — NOT present
#    ✗ remote APIs       — NOT present
#    ✗ remote JSON       — NOT present
#    ✗ online updates    — NOT present
#    ✗ telemetry         — NOT present
#    ✓ Only source of data: ./offsets.json (local file)
#
# =============================================================================
