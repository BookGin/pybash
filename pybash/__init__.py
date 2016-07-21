#!/usr/bin/env python3
import subprocess

class ChildProcess:
    def __init__(self, proc, get_return_code):
        self.process = proc
        self.get_return_code = get_return_code

    def wait(self, timeout = None):
        self.process.wait(timeout)
        stdout = self.process.communicate()[0].decode("utf-8").rstrip("\n")
        return_code = self.process.returncode
        return return_code if self.get_return_code else stdout

    def isFinished(self):
        return self.process.poll() != None


SHELL = '/bin/bash'

def setShell(path):
    global SHELL
    SHELL = path

def run(cmd, get_return_code = False, asynchronous = False):
    subproc = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, executable = SHELL)
    if asynchronous:
        return ChildProcess(subproc, get_return_code)

    stdout = subproc.communicate()[0].decode("utf-8").rstrip("\n")
    return_code = subproc.returncode
    return return_code if get_return_code else stdout
