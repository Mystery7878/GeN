import os
import sys

def load_module():
    arch = os.uname().machine.lower()
    
    # Add current directory to Python's search path
    sys.path.insert(0, os.getcwd())
    
    try:
        if 'aarch64' in arch:
            import mystery as mod
            print("Loaded 64-bit module")
        elif 'armv7' in arch or 'armv8l' in arch or ('arm' in arch and '64' not in arch):
            import mystery32 as mod
            print("Loaded 32-bit module")
        else:
            print("Unsupported Device:", arch)
            sys.exit()
        return mod
    except ImportError as e:
        print(f"Module load failed: {e}")
        print(f"Files in current directory: {os.listdir('.')}")
        sys.exit()

mymodule = load_module()
