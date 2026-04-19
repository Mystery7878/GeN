import os

arch = os.uname().machine

if arch == "armv7l":
    import gen32 as mymodule
elif arch == "aarch64":
    import gen64 as mymodule
else:
    print("Unsupported Device:", arch)