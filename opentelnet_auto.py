# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:56:05 2018
be careful to open with administrive priviledge
@author: Abigial
"""
import win32gui
import win32con
import time
import win32api

WM_CHAR = 0x0102
WM_SETTEXT    =                  0x000C

#shell = win32com.client.Dispatch("WScript.Shell")
#shell.Run('cmd /K (cd "F:\\download\\C3L\\tools\\OpenTelnetV3.exe)')
def runApp():
    
    # 最后一个参数表示是窗口属性，0表示不显示，1表示正常显示，2表示最小化，3表示最大化
    return win32api.ShellExecute(0, 'open', 'F:\\download\\C3L\\tools\\OpenTelnetV3.exe', '', '', 1)
def findAppHandle():
    appName = "OpenTelnetV2"
    hwnd = win32gui.FindWindow(None, appName)

    return hwnd
def closeSoft(hwnd):
    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default='192.168.1.9')
    args = parser.parse_args()
    win = runApp()
    time.sleep (1)
    hwnd =    findAppHandle()
    if hwnd > 0:
        child1 = win32gui.FindWindowEx(hwnd, 0, "Edit", None);
        child2 = win32gui.FindWindowEx(hwnd, child1, "Edit", None)
        child3 = win32gui.FindWindowEx(hwnd, 0, "Button", None)
    time.sleep (0.5)
    buf, fakepwd= args.ip,'135791'
    
    win32api.SendMessage(child1,win32con.WM_SETTEXT,None,buf)
    win32api.SendMessage(child2,win32con.WM_SETTEXT,None,fakepwd)
      
    win32gui.PostMessage(child3, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
    win32gui.PostMessage(child3, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
    
    time.sleep (1)
    ans = win32gui.FindWindow( None,u"提示")  
    while  ans <= 0 :
        ans = win32gui.FindWindow( None,u"提示") 
    if ans > 0:
    
        win32gui.SendMessage(ans,win32con.WM_CLOSE,0,0)
    closeSoft(hwnd) 