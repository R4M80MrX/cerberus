import win32serviceutil
import win32service
import win32timezone
import win32event
import winerror
import servicemanager
import time
import sys
import os
import ctypes
import admin
import inspect

from core.MyLog.log import getLogger


class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'cerberus'
    _svc_display_name_ = 'cerberus'
    _svc_description_ = 'python windows monitor'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True
        self.interval = 10

        self.logger = self._getLogger()

    def _getLogger(self):
        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        log_path = os.path.join(dirpath, 'log.txt')

        LOGGER = getLogger('Daemon Service', log_path)

        return LOGGER

    def SvcDoRun(self):
        self.logger.info('daemon service start running...')
        while self.running:
            self.logger.info('test')
            time.sleep(self.interval)

    def SvcStop(self):
        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)

        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.running = False


if __name__ == '__main__':
    if not admin.isUserAdmin():
        LOGGER = getLogger('Register Service', 'log.txt')
        LOGGER.warning('you are not an admin')
        admin.runAsAdmin()

    else:
        if len(sys.argv) == 1:
            try:
                evtsrc_dll = os.path.abspath(servicemanager.__file__)
                servicemanager.PrepareToHostSingle(PythonService)
                servicemanager.Initialize('PythonService', evtsrc_dll)
                servicemanager.StartServiceCtrlDispatcher()

            except win32service.error as details:
                if details == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                    win32serviceutil.usage()

        elif sys.argv[1] in ['start', 'stop', 'install', 'remove', '--startup=auto']):
            try:
                win32serviceutil.HandleCommandLine(PythonService)
            except Exception as e:
                LOGGER.error(e)
            finally:
                input('press any key to continue')
