from twisted.application.service import ServiceMaker


DreamSSHService = ServiceMaker(
    "DreamSSH Server",
    "dreamssh.app.service",
    ("A highly flexible pure-Python, Twisted-based SSH Server with custom "
     "account shells"),
    "dreamssh")
