#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.1),
    on 四月 19, 2026, at 21:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.1'
expName = 'midterm_project'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\irene_python\\week8_midterm_project\\midterm_project_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0, 0, 0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "start" ---
    open_text = visual.TextStim(win=win, name='open_text',
        text='歡迎參加本次視覺認知與注意力實驗\n\n【實驗任務說明】\n在接下來的畫面中，\n會出現許多不同顏色與形狀的圖案。\n您的目標是尋找：「紅色正方形」。\n\n【按鍵操作指引】\n● 看到紅色正方形：請按 方向鍵右鍵 (→)\n● 沒有紅色正方形：請按 方向鍵左鍵 (←)\n\n\n按下空白鍵進入下一頁',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    start_key = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instr_practice" ---
    prac_text = visual.TextStim(win=win, name='prac_text',
        text='【練習階段】\n\n為了讓您熟悉操作，我們準備了幾題練習題。\n\n此階段會顯示「正確」或是「錯誤」。\n\n請在確保正確的前提下，盡可能快地做出反應。\n\n\n\n準備好後，請按下「空白鍵」開始練習。',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    prac_key = keyboard.Keyboard(deviceName='defaultKeyboard')
    # Run 'Begin Experiment' code from prac_code
    # 初始化計數器（全域變數）
    total_correct = 0
    total_trials = 0
    
    # --- Initialize components for Routine "reset_prac_acc" ---
    
    # --- Initialize components for Routine "fixation" ---
    fix_text = visual.TextStim(win=win, name='fix_text',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "trial_prac" ---
    prac_key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "feedback" ---
    fb_text = visual.TextStim(win=win, name='fb_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "ITI" ---
    ITI_text = visual.TextStim(win=win, name='ITI_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "prac_feedback" ---
    # Run 'Begin Experiment' code from prac_fb_code
    prac_threshold = 0.8  # 設定達標門檻 (例如 80%)
    prac_fb_text = visual.TextStim(win=win, name='prac_fb_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "instr_formal" ---
    formal_text = visual.TextStim(win=win, name='formal_text',
        text='練習結束，即將進入正式實驗\n\n規則維持不變：\n目標是尋找 「紅色正方形」\n● 有目標：按 右鍵 (→)\n● 無目標：按 左鍵 (←)\n\n注意：\n1. 正式實驗將不再提供對錯回饋。\n2. 螢幕會自動跳轉，請保持注意力集中。\n3. 請盡可能兼顧速度與正確率。\n\n準備好後，請按「空白鍵」開始正式實驗。',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    formal_key = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "fixation" ---
    fix_text = visual.TextStim(win=win, name='fix_text',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "trial" ---
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "ITI" ---
    ITI_text = visual.TextStim(win=win, name='ITI_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "rest_routine" ---
    rest_text = visual.TextStim(win=win, name='rest_text',
        text='休息時間。\n準備好後請按【空白鍵】繼續實驗。',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_rest = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "thanks" ---
    thanks_text = visual.TextStim(win=win, name='thanks_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "start" ---
    # create an object to store info about Routine start
    start = data.Routine(
        name='start',
        components=[open_text, start_key],
    )
    start.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for start_key
    start_key.keys = []
    start_key.rt = []
    _start_key_allKeys = []
    # store start times for start
    start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start.tStart = globalClock.getTime(format='float')
    start.status = STARTED
    thisExp.addData('start.started', start.tStart)
    start.maxDuration = None
    # keep track of which components have finished
    startComponents = start.components
    for thisComponent in start.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start" ---
    thisExp.currentRoutine = start
    start.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *open_text* updates
        
        # if open_text is starting this frame...
        if open_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            open_text.frameNStart = frameN  # exact frame index
            open_text.tStart = t  # local t and not account for scr refresh
            open_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(open_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'open_text.started')
            # update status
            open_text.status = STARTED
            open_text.setAutoDraw(True)
        
        # if open_text is active this frame...
        if open_text.status == STARTED:
            # update params
            pass
        
        # *start_key* updates
        waitOnFlip = False
        
        # if start_key is starting this frame...
        if start_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_key.frameNStart = frameN  # exact frame index
            start_key.tStart = t  # local t and not account for scr refresh
            start_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'start_key.started')
            # update status
            start_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(start_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if start_key.status == STARTED and not waitOnFlip:
            theseKeys = start_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _start_key_allKeys.extend(theseKeys)
            if len(_start_key_allKeys):
                start_key.keys = _start_key_allKeys[-1].name  # just the last key pressed
                start_key.rt = _start_key_allKeys[-1].rt
                start_key.duration = _start_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=start,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            start.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if start.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in start.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start" ---
    for thisComponent in start.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start
    start.tStop = globalClock.getTime(format='float')
    start.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start.stopped', start.tStop)
    # check responses
    if start_key.keys in ['', [], None]:  # No response was made
        start_key.keys = None
    thisExp.addData('start_key.keys',start_key.keys)
    if start_key.keys != None:  # we had a response
        thisExp.addData('start_key.rt', start_key.rt)
        thisExp.addData('start_key.duration', start_key.duration)
    thisExp.nextEntry()
    # the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr_practice" ---
    # create an object to store info about Routine instr_practice
    instr_practice = data.Routine(
        name='instr_practice',
        components=[prac_text, prac_key],
    )
    instr_practice.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for prac_key
    prac_key.keys = []
    prac_key.rt = []
    _prac_key_allKeys = []
    # store start times for instr_practice
    instr_practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr_practice.tStart = globalClock.getTime(format='float')
    instr_practice.status = STARTED
    thisExp.addData('instr_practice.started', instr_practice.tStart)
    instr_practice.maxDuration = None
    # keep track of which components have finished
    instr_practiceComponents = instr_practice.components
    for thisComponent in instr_practice.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr_practice" ---
    thisExp.currentRoutine = instr_practice
    instr_practice.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_text* updates
        
        # if prac_text is starting this frame...
        if prac_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_text.frameNStart = frameN  # exact frame index
            prac_text.tStart = t  # local t and not account for scr refresh
            prac_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_text.started')
            # update status
            prac_text.status = STARTED
            prac_text.setAutoDraw(True)
        
        # if prac_text is active this frame...
        if prac_text.status == STARTED:
            # update params
            pass
        
        # *prac_key* updates
        waitOnFlip = False
        
        # if prac_key is starting this frame...
        if prac_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_key.frameNStart = frameN  # exact frame index
            prac_key.tStart = t  # local t and not account for scr refresh
            prac_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_key.started')
            # update status
            prac_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_key.status == STARTED and not waitOnFlip:
            theseKeys = prac_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _prac_key_allKeys.extend(theseKeys)
            if len(_prac_key_allKeys):
                prac_key.keys = _prac_key_allKeys[-1].name  # just the last key pressed
                prac_key.rt = _prac_key_allKeys[-1].rt
                prac_key.duration = _prac_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr_practice,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instr_practice.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instr_practice.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instr_practice.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_practice" ---
    for thisComponent in instr_practice.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr_practice
    instr_practice.tStop = globalClock.getTime(format='float')
    instr_practice.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr_practice.stopped', instr_practice.tStop)
    # check responses
    if prac_key.keys in ['', [], None]:  # No response was made
        prac_key.keys = None
    thisExp.addData('prac_key.keys',prac_key.keys)
    if prac_key.keys != None:  # we had a response
        thisExp.addData('prac_key.rt', prac_key.rt)
        thisExp.addData('prac_key.duration', prac_key.duration)
    thisExp.nextEntry()
    # the Routine "instr_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_repeat_loop = data.TrialHandler2(
        name='practice_repeat_loop',
        nReps=99, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(practice_repeat_loop)  # add the loop to the experiment
    thisPractice_repeat_loop = practice_repeat_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_repeat_loop.rgb)
    if thisPractice_repeat_loop != None:
        for paramName in thisPractice_repeat_loop:
            globals()[paramName] = thisPractice_repeat_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_repeat_loop in practice_repeat_loop:
        practice_repeat_loop.status = STARTED
        if hasattr(thisPractice_repeat_loop, 'status'):
            thisPractice_repeat_loop.status = STARTED
        currentLoop = practice_repeat_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_repeat_loop.rgb)
        if thisPractice_repeat_loop != None:
            for paramName in thisPractice_repeat_loop:
                globals()[paramName] = thisPractice_repeat_loop[paramName]
        
        # --- Prepare to start Routine "reset_prac_acc" ---
        # create an object to store info about Routine reset_prac_acc
        reset_prac_acc = data.Routine(
            name='reset_prac_acc',
            components=[],
        )
        reset_prac_acc.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_reset
        # 這裡只會在一輪練習開始前跑一次
        prac_correct_count = 0
        prac_total_count = 0
        continueRoutine = False # 確保不顯示畫面
        # store start times for reset_prac_acc
        reset_prac_acc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reset_prac_acc.tStart = globalClock.getTime(format='float')
        reset_prac_acc.status = STARTED
        thisExp.addData('reset_prac_acc.started', reset_prac_acc.tStart)
        reset_prac_acc.maxDuration = None
        # keep track of which components have finished
        reset_prac_accComponents = reset_prac_acc.components
        for thisComponent in reset_prac_acc.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reset_prac_acc" ---
        thisExp.currentRoutine = reset_prac_acc
        reset_prac_acc.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_repeat_loop, 'status') and thisPractice_repeat_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=reset_prac_acc,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                reset_prac_acc.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if reset_prac_acc.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in reset_prac_acc.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reset_prac_acc" ---
        for thisComponent in reset_prac_acc.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reset_prac_acc
        reset_prac_acc.tStop = globalClock.getTime(format='float')
        reset_prac_acc.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reset_prac_acc.stopped', reset_prac_acc.tStop)
        # the Routine "reset_prac_acc" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practice_loop = data.TrialHandler2(
            name='practice_loop',
            nReps=1, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('practice_cond.xlsx'), 
            seed=None, 
            isTrials=True, 
        )
        thisExp.addLoop(practice_loop)  # add the loop to the experiment
        thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
        if thisPractice_loop != None:
            for paramName in thisPractice_loop:
                globals()[paramName] = thisPractice_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPractice_loop in practice_loop:
            practice_loop.status = STARTED
            if hasattr(thisPractice_loop, 'status'):
                thisPractice_loop.status = STARTED
            currentLoop = practice_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
            if thisPractice_loop != None:
                for paramName in thisPractice_loop:
                    globals()[paramName] = thisPractice_loop[paramName]
            
            # --- Prepare to start Routine "fixation" ---
            # create an object to store info about Routine fixation
            fixation = data.Routine(
                name='fixation',
                components=[fix_text],
            )
            fixation.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for fixation
            fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation.tStart = globalClock.getTime(format='float')
            fixation.status = STARTED
            thisExp.addData('fixation.started', fixation.tStart)
            fixation.maxDuration = None
            # keep track of which components have finished
            fixationComponents = fixation.components
            for thisComponent in fixation.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation" ---
            thisExp.currentRoutine = fixation
            fixation.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # if trial has changed, end Routine now
                if hasattr(thisPractice_loop, 'status') and thisPractice_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fix_text* updates
                
                # if fix_text is starting this frame...
                if fix_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix_text.frameNStart = frameN  # exact frame index
                    fix_text.tStart = t  # local t and not account for scr refresh
                    fix_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_text.started')
                    # update status
                    fix_text.status = STARTED
                    fix_text.setAutoDraw(True)
                
                # if fix_text is active this frame...
                if fix_text.status == STARTED:
                    # update params
                    pass
                
                # if fix_text is stopping this frame...
                if fix_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix_text.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fix_text.tStop = t  # not accounting for scr refresh
                        fix_text.tStopRefresh = tThisFlipGlobal  # on global time
                        fix_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix_text.stopped')
                        # update status
                        fix_text.status = FINISHED
                        fix_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=fixation,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    fixation.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if fixation.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in fixation.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation" ---
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation
            fixation.tStop = globalClock.getTime(format='float')
            fixation.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation.stopped', fixation.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if fixation.maxDurationReached:
                routineTimer.addTime(-fixation.maxDuration)
            elif fixation.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            
            # --- Prepare to start Routine "trial_prac" ---
            # create an object to store info about Routine trial_prac
            trial_prac = data.Routine(
                name='trial_prac',
                components=[prac_key_resp],
            )
            trial_prac.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from prac_trial_code
            import random
            
            # 1. 建立網格座標 (避免物件重疊)
            locations = []
            
            # 增加間隔 (從 80 改成 120-150) 
            grid_spacing = 130 # 每個點的間隔增加，讓分布更廣
            
            for x in range(-5, 6): # 橫向的 11 個點
                for y in range(-3, 4): # 縱向的 7 個點
                    #加入一點點隨機偏移 (Jitter)，讓網格看起來不那麼死板
                   x_jitter = random.randint(-15, 15)
                   y_jitter = random.randint(-15, 15)
                   locations.append([(x * grid_spacing) + x_jitter, (y * grid_spacing) + y_jitter]) 
                   
            # 2. 隨機打亂位置
            random.shuffle(locations)
            # 取出本次需要的物件數量
            pos_list = locations[0:int(set_size)]
            
            # 3. 建立物件儲存清單
            stims = []
            
            # 4. 生成物件邏輯
            for i in range(int(set_size)):
                # 決定顏色和形狀
                if i == 0 and target_present == 1:
                    # 這是目標物: 紅色正方形
                    curr_color = 'red'
                    curr_shape = 'rectangle'
                else: 
                    # 根據實驗條件決定干擾項
                    if condition_type == 'feature':
                        # 特徵搜尋: 干擾項全是藍色正方形 (只差顏色)
                        curr_color = 'blue'
                        curr_shape = 'rectangle'
                    else:
                        # 聯結搜尋: 一半紅圓，一半藍方 (顏色形狀都干擾)
                        if i % 2 == 0:
                            curr_color = 'red'
                            curr_shape = 'circle'
                        else:
                            curr_color = 'blue'
                            curr_shape = 'rectangle'
                # 5. 建立物件 (如果是圓形就用 Polygon 設定) 
                obj_size = 60 # 將原本的 40 提高到 60 或更高
                
                if curr_shape == 'rectangle':
                    el = visual.Rect(win=win, width=obj_size, height=obj_size, fillColor=curr_color, lineColor=curr_color, pos=pos_list[i], units='pix')
                else:
                    el = visual.Polygon(win=win, edges=32, radius=obj_size/2, fillColor=curr_color, lineColor=curr_color, pos=pos_list[i], units='pix')
                stims.append(el)
            # create starting attributes for prac_key_resp
            prac_key_resp.keys = []
            prac_key_resp.rt = []
            _prac_key_resp_allKeys = []
            # store start times for trial_prac
            trial_prac.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_prac.tStart = globalClock.getTime(format='float')
            trial_prac.status = STARTED
            thisExp.addData('trial_prac.started', trial_prac.tStart)
            trial_prac.maxDuration = None
            # keep track of which components have finished
            trial_pracComponents = trial_prac.components
            for thisComponent in trial_prac.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_prac" ---
            thisExp.currentRoutine = trial_prac
            trial_prac.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # if trial has changed, end Routine now
                if hasattr(thisPractice_loop, 'status') and thisPractice_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from prac_trial_code
                # 每一幀都把清單裡的物件畫出來
                for stim in stims:
                    stim.draw()
                
                # *prac_key_resp* updates
                waitOnFlip = False
                
                # if prac_key_resp is starting this frame...
                if prac_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    prac_key_resp.frameNStart = frameN  # exact frame index
                    prac_key_resp.tStart = t  # local t and not account for scr refresh
                    prac_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(prac_key_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_key_resp.started')
                    # update status
                    prac_key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(prac_key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(prac_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if prac_key_resp is stopping this frame...
                if prac_key_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > prac_key_resp.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        prac_key_resp.tStop = t  # not accounting for scr refresh
                        prac_key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                        prac_key_resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'prac_key_resp.stopped')
                        # update status
                        prac_key_resp.status = FINISHED
                        prac_key_resp.status = FINISHED
                if prac_key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = prac_key_resp.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                    _prac_key_resp_allKeys.extend(theseKeys)
                    if len(_prac_key_resp_allKeys):
                        prac_key_resp.keys = _prac_key_resp_allKeys[0].name  # just the first key pressed
                        prac_key_resp.rt = _prac_key_resp_allKeys[0].rt
                        prac_key_resp.duration = _prac_key_resp_allKeys[0].duration
                        # was this correct?
                        if (prac_key_resp.keys == str(corr_resp)) or (prac_key_resp.keys == corr_resp):
                            prac_key_resp.corr = 1
                        else:
                            prac_key_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=trial_prac,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    trial_prac.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if trial_prac.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in trial_prac.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_prac" ---
            for thisComponent in trial_prac.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_prac
            trial_prac.tStop = globalClock.getTime(format='float')
            trial_prac.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_prac.stopped', trial_prac.tStop)
            # Run 'End Routine' code from prac_trial_code
            # 累計練習正確率
            if hasattr(prac_key_resp, 'corr') and prac_key_resp.corr:
                prac_correct_count += 1
            
            prac_total_count += 1
            
            # check responses
            if prac_key_resp.keys in ['', [], None]:  # No response was made
                prac_key_resp.keys = None
                # was no response the correct answer?!
                if str(corr_resp).lower() == 'none':
                   prac_key_resp.corr = 1;  # correct non-response
                else:
                   prac_key_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for practice_loop (TrialHandler)
            practice_loop.addData('prac_key_resp.keys',prac_key_resp.keys)
            practice_loop.addData('prac_key_resp.corr', prac_key_resp.corr)
            if prac_key_resp.keys != None:  # we had a response
                practice_loop.addData('prac_key_resp.rt', prac_key_resp.rt)
                practice_loop.addData('prac_key_resp.duration', prac_key_resp.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_prac.maxDurationReached:
                routineTimer.addTime(-trial_prac.maxDuration)
            elif trial_prac.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[fb_text],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from fb_code
            # 判斷對錯
            if prac_key_resp.corr:
                msg = "正確!"
                msg_color = "green"
            else:
                msg = "錯誤!"
                msg_color = "red"
            
            # 顯示反應時間
            if prac_key_resp.rt:
                rt_ms = round(prac_key_resp.rt * 1000)
                msg += f"\n{rt_ms} ms"
            else:
                msg += "\n太慢了!"
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback" ---
            thisExp.currentRoutine = feedback
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.5:
                # if trial has changed, end Routine now
                if hasattr(thisPractice_loop, 'status') and thisPractice_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fb_text* updates
                
                # if fb_text is starting this frame...
                if fb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fb_text.frameNStart = frameN  # exact frame index
                    fb_text.tStart = t  # local t and not account for scr refresh
                    fb_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fb_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fb_text.started')
                    # update status
                    fb_text.status = STARTED
                    fb_text.setAutoDraw(True)
                
                # if fb_text is active this frame...
                if fb_text.status == STARTED:
                    # update params
                    fb_text.setColor(msg_color, colorSpace='rgb', log=False)
                    fb_text.setText(msg, log=False)
                
                # if fb_text is stopping this frame...
                if fb_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fb_text.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fb_text.tStop = t  # not accounting for scr refresh
                        fb_text.tStopRefresh = tThisFlipGlobal  # on global time
                        fb_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fb_text.stopped')
                        # update status
                        fb_text.status = FINISHED
                        fb_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=feedback,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    feedback.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if feedback.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.500000)
            
            # --- Prepare to start Routine "ITI" ---
            # create an object to store info about Routine ITI
            ITI = data.Routine(
                name='ITI',
                components=[ITI_text],
            )
            ITI.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ITI
            ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ITI.tStart = globalClock.getTime(format='float')
            ITI.status = STARTED
            thisExp.addData('ITI.started', ITI.tStart)
            ITI.maxDuration = None
            # keep track of which components have finished
            ITIComponents = ITI.components
            for thisComponent in ITI.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ITI" ---
            thisExp.currentRoutine = ITI
            ITI.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # if trial has changed, end Routine now
                if hasattr(thisPractice_loop, 'status') and thisPractice_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ITI_text* updates
                
                # if ITI_text is starting this frame...
                if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI_text.frameNStart = frameN  # exact frame index
                    ITI_text.tStart = t  # local t and not account for scr refresh
                    ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_text.started')
                    # update status
                    ITI_text.status = STARTED
                    ITI_text.setAutoDraw(True)
                
                # if ITI_text is active this frame...
                if ITI_text.status == STARTED:
                    # update params
                    pass
                
                # if ITI_text is stopping this frame...
                if ITI_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ITI_text.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        ITI_text.tStop = t  # not accounting for scr refresh
                        ITI_text.tStopRefresh = tThisFlipGlobal  # on global time
                        ITI_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                        # update status
                        ITI_text.status = FINISHED
                        ITI_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=ITI,
                    )
                    # skip the frame we paused on
                    continue
                
                # has a Component requested the Routine to end?
                if not continueRoutine:
                    ITI.forceEnded = routineForceEnded = True
                # has the Routine been forcibly ended?
                if ITI.forceEnded or routineForceEnded:
                    break
                # has every Component finished?
                continueRoutine = False
                for thisComponent in ITI.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ITI
            ITI.tStop = globalClock.getTime(format='float')
            ITI.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ITI.stopped', ITI.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if ITI.maxDurationReached:
                routineTimer.addTime(-ITI.maxDuration)
            elif ITI.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            # mark thisPractice_loop as finished
            if hasattr(thisPractice_loop, 'status'):
                thisPractice_loop.status = FINISHED
            # if awaiting a pause, pause now
            if practice_loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                practice_loop.status = STARTED
            thisExp.nextEntry()
            
        # completed 1 repeats of 'practice_loop'
        practice_loop.status = FINISHED
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "prac_feedback" ---
        # create an object to store info about Routine prac_feedback
        prac_feedback = data.Routine(
            name='prac_feedback',
            components=[prac_fb_text],
        )
        prac_feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_fb_code
        if prac_total_count > 0:
            # 強制轉換成浮點數 (float) 確保算出 0.85 這種數字
            current_acc = float(prac_correct_count) / float(prac_total_count)
        else:
            current_acc = 0
        
        # 設定門檻
        threshold = 0.8
        
        if current_acc >= threshold:
            msg = f"練習完成！\n您的正確率為 {current_acc*100:.1f}%\n即將開始正式實驗。"
            practice_repeat_loop.finished = True
        else:
            msg = f"正確率僅 {current_acc*100:.1f}%\n未達標 ({threshold*100:.0f}%)\n請再練習一次。"
        # store start times for prac_feedback
        prac_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prac_feedback.tStart = globalClock.getTime(format='float')
        prac_feedback.status = STARTED
        thisExp.addData('prac_feedback.started', prac_feedback.tStart)
        prac_feedback.maxDuration = None
        # keep track of which components have finished
        prac_feedbackComponents = prac_feedback.components
        for thisComponent in prac_feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_feedback" ---
        thisExp.currentRoutine = prac_feedback
        prac_feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_repeat_loop, 'status') and thisPractice_repeat_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_fb_text* updates
            
            # if prac_fb_text is starting this frame...
            if prac_fb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_fb_text.frameNStart = frameN  # exact frame index
                prac_fb_text.tStart = t  # local t and not account for scr refresh
                prac_fb_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_fb_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_fb_text.started')
                # update status
                prac_fb_text.status = STARTED
                prac_fb_text.setAutoDraw(True)
            
            # if prac_fb_text is active this frame...
            if prac_fb_text.status == STARTED:
                # update params
                prac_fb_text.setText(msg, log=False)
            
            # if prac_fb_text is stopping this frame...
            if prac_fb_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_fb_text.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_fb_text.tStop = t  # not accounting for scr refresh
                    prac_fb_text.tStopRefresh = tThisFlipGlobal  # on global time
                    prac_fb_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_fb_text.stopped')
                    # update status
                    prac_fb_text.status = FINISHED
                    prac_fb_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=prac_feedback,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                prac_feedback.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if prac_feedback.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in prac_feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_feedback" ---
        for thisComponent in prac_feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prac_feedback
        prac_feedback.tStop = globalClock.getTime(format='float')
        prac_feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prac_feedback.stopped', prac_feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if prac_feedback.maxDurationReached:
            routineTimer.addTime(-prac_feedback.maxDuration)
        elif prac_feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPractice_repeat_loop as finished
        if hasattr(thisPractice_repeat_loop, 'status'):
            thisPractice_repeat_loop.status = FINISHED
        # if awaiting a pause, pause now
        if practice_repeat_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practice_repeat_loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 99 repeats of 'practice_repeat_loop'
    practice_repeat_loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instr_formal" ---
    # create an object to store info about Routine instr_formal
    instr_formal = data.Routine(
        name='instr_formal',
        components=[formal_text, formal_key],
    )
    instr_formal.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    # 在正式實驗開始前，將計數器歸零
    total_correct = 0
    total_trials = 0
    # create starting attributes for formal_key
    formal_key.keys = []
    formal_key.rt = []
    _formal_key_allKeys = []
    # store start times for instr_formal
    instr_formal.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr_formal.tStart = globalClock.getTime(format='float')
    instr_formal.status = STARTED
    thisExp.addData('instr_formal.started', instr_formal.tStart)
    instr_formal.maxDuration = None
    # keep track of which components have finished
    instr_formalComponents = instr_formal.components
    for thisComponent in instr_formal.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr_formal" ---
    thisExp.currentRoutine = instr_formal
    instr_formal.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *formal_text* updates
        
        # if formal_text is starting this frame...
        if formal_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            formal_text.frameNStart = frameN  # exact frame index
            formal_text.tStart = t  # local t and not account for scr refresh
            formal_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_text.started')
            # update status
            formal_text.status = STARTED
            formal_text.setAutoDraw(True)
        
        # if formal_text is active this frame...
        if formal_text.status == STARTED:
            # update params
            pass
        
        # *formal_key* updates
        waitOnFlip = False
        
        # if formal_key is starting this frame...
        if formal_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            formal_key.frameNStart = frameN  # exact frame index
            formal_key.tStart = t  # local t and not account for scr refresh
            formal_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(formal_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'formal_key.started')
            # update status
            formal_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(formal_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(formal_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if formal_key.status == STARTED and not waitOnFlip:
            theseKeys = formal_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _formal_key_allKeys.extend(theseKeys)
            if len(_formal_key_allKeys):
                formal_key.keys = _formal_key_allKeys[-1].name  # just the last key pressed
                formal_key.rt = _formal_key_allKeys[-1].rt
                formal_key.duration = _formal_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr_formal,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instr_formal.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instr_formal.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instr_formal.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_formal" ---
    for thisComponent in instr_formal.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr_formal
    instr_formal.tStop = globalClock.getTime(format='float')
    instr_formal.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr_formal.stopped', instr_formal.tStop)
    # check responses
    if formal_key.keys in ['', [], None]:  # No response was made
        formal_key.keys = None
    thisExp.addData('formal_key.keys',formal_key.keys)
    if formal_key.keys != None:  # we had a response
        thisExp.addData('formal_key.rt', formal_key.rt)
        thisExp.addData('formal_key.duration', formal_key.duration)
    thisExp.nextEntry()
    # the Routine "instr_formal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    formal_loop = data.TrialHandler2(
        name='formal_loop',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('formal_cond.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(formal_loop)  # add the loop to the experiment
    thisFormal_loop = formal_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFormal_loop.rgb)
    if thisFormal_loop != None:
        for paramName in thisFormal_loop:
            globals()[paramName] = thisFormal_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisFormal_loop in formal_loop:
        formal_loop.status = STARTED
        if hasattr(thisFormal_loop, 'status'):
            thisFormal_loop.status = STARTED
        currentLoop = formal_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisFormal_loop.rgb)
        if thisFormal_loop != None:
            for paramName in thisFormal_loop:
                globals()[paramName] = thisFormal_loop[paramName]
        
        # --- Prepare to start Routine "fixation" ---
        # create an object to store info about Routine fixation
        fixation = data.Routine(
            name='fixation',
            components=[fix_text],
        )
        fixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation
        fixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation.tStart = globalClock.getTime(format='float')
        fixation.status = STARTED
        thisExp.addData('fixation.started', fixation.tStart)
        fixation.maxDuration = None
        # keep track of which components have finished
        fixationComponents = fixation.components
        for thisComponent in fixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        thisExp.currentRoutine = fixation
        fixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisFormal_loop, 'status') and thisFormal_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_text* updates
            
            # if fix_text is starting this frame...
            if fix_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_text.frameNStart = frameN  # exact frame index
                fix_text.tStart = t  # local t and not account for scr refresh
                fix_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_text.started')
                # update status
                fix_text.status = STARTED
                fix_text.setAutoDraw(True)
            
            # if fix_text is active this frame...
            if fix_text.status == STARTED:
                # update params
                pass
            
            # if fix_text is stopping this frame...
            if fix_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_text.tStop = t  # not accounting for scr refresh
                    fix_text.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_text.stopped')
                    # update status
                    fix_text.status = FINISHED
                    fix_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fixation,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                fixation.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if fixation.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in fixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation
        fixation.tStop = globalClock.getTime(format='float')
        fixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation.stopped', fixation.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation.maxDurationReached:
            routineTimer.addTime(-fixation.maxDuration)
        elif fixation.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[key_resp],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from trial_code
        import random
        
        # 1. 建立網格座標 (避免物件重疊)
        locations = []
        
        # 增加間隔 (從 80 改成 120-150) 
        grid_spacing = 130 # 每個點的間隔增加，讓分布更廣
        
        for x in range(-5, 6): # 橫向的 11 個點
            for y in range(-3, 4): # 縱向的 7 個點
                #加入一點點隨機偏移 (Jitter)，讓網格看起來不那麼死板
               x_jitter = random.randint(-15, 15)
               y_jitter = random.randint(-15, 15)
               locations.append([(x * grid_spacing) + x_jitter, (y * grid_spacing) + y_jitter]) 
               
        # 2. 隨機打亂位置
        random.shuffle(locations)
        # 取出本次需要的物件數量
        pos_list = locations[0:int(set_size)]
        
        # 3. 建立物件儲存清單
        stims = []
        
        # 4. 生成物件邏輯
        for i in range(int(set_size)):
            # 決定顏色和形狀
            if i == 0 and target_present == 1:
                # 這是目標物: 紅色正方形
                curr_color = 'red'
                curr_shape = 'rectangle'
            else: 
                # 根據實驗條件決定干擾項
                if condition_type == 'feature':
                    # 特徵搜尋: 干擾項全是藍色正方形 (只差顏色)
                    curr_color = 'blue'
                    curr_shape = 'rectangle'
                else:
                    # 聯結搜尋: 一半紅圓，一半藍方 (顏色形狀都干擾)
                    if i % 2 == 0:
                        curr_color = 'red'
                        curr_shape = 'circle'
                    else:
                        curr_color = 'blue'
                        curr_shape = 'rectangle'
            # 5. 建立物件 (如果是圓形就用 Polygon 設定) 
            obj_size = 60 # 將原本的 40 提高到 60 或更高
            
            if curr_shape == 'rectangle':
                el = visual.Rect(win=win, width=obj_size, height=obj_size, fillColor=curr_color, lineColor=curr_color, pos=pos_list[i], units='pix')
            else:
                el = visual.Polygon(win=win, edges=32, radius=obj_size/2, fillColor=curr_color, lineColor=curr_color, pos=pos_list[i], units='pix')
            stims.append(el)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        thisExp.currentRoutine = trial
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisFormal_loop, 'status') and thisFormal_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from trial_code
            # 每一幀都把清單裡的物件畫出來
            for stim in stims:
                stim.draw()
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # was this correct?
                    if (key_resp.keys == str(corr_resp)) or (key_resp.keys == corr_resp):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        # Run 'End Routine' code from trial_code
        if key_resp.corr:
            total_correct += 1
        total_trials += 1
        
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for formal_loop (TrialHandler)
        formal_loop.addData('key_resp.keys',key_resp.keys)
        formal_loop.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            formal_loop.addData('key_resp.rt', key_resp.rt)
            formal_loop.addData('key_resp.duration', key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if trial.maxDurationReached:
            routineTimer.addTime(-trial.maxDuration)
        elif trial.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[ITI_text],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = None
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        thisExp.currentRoutine = ITI
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisFormal_loop, 'status') and thisFormal_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_text* updates
            
            # if ITI_text is starting this frame...
            if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_text.frameNStart = frameN  # exact frame index
                ITI_text.tStart = t  # local t and not account for scr refresh
                ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_text.started')
                # update status
                ITI_text.status = STARTED
                ITI_text.setAutoDraw(True)
            
            # if ITI_text is active this frame...
            if ITI_text.status == STARTED:
                # update params
                pass
            
            # if ITI_text is stopping this frame...
            if ITI_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_text.tStop = t  # not accounting for scr refresh
                    ITI_text.tStopRefresh = tThisFlipGlobal  # on global time
                    ITI_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                    # update status
                    ITI_text.status = FINISHED
                    ITI_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                ITI.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if ITI.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if ITI.maxDurationReached:
            routineTimer.addTime(-ITI.maxDuration)
        elif ITI.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "rest_routine" ---
        # create an object to store info about Routine rest_routine
        rest_routine = data.Routine(
            name='rest_routine',
            components=[rest_text, key_rest],
        )
        rest_routine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from rest_code
        # 設定每 10 題休息一次 
        if (formal_loop.thisN > 0) and (formal_loop.thisN % 10 == 0):
            continueRoutine = True  # 顯示休息畫面
        else:
            continueRoutine = False # 不到題數，直接跳過此 Routine
        # create starting attributes for key_rest
        key_rest.keys = []
        key_rest.rt = []
        _key_rest_allKeys = []
        # store start times for rest_routine
        rest_routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        rest_routine.tStart = globalClock.getTime(format='float')
        rest_routine.status = STARTED
        thisExp.addData('rest_routine.started', rest_routine.tStart)
        rest_routine.maxDuration = None
        # keep track of which components have finished
        rest_routineComponents = rest_routine.components
        for thisComponent in rest_routine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "rest_routine" ---
        thisExp.currentRoutine = rest_routine
        rest_routine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisFormal_loop, 'status') and thisFormal_loop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rest_text* updates
            
            # if rest_text is starting this frame...
            if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest_text.frameNStart = frameN  # exact frame index
                rest_text.tStart = t  # local t and not account for scr refresh
                rest_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_text.started')
                # update status
                rest_text.status = STARTED
                rest_text.setAutoDraw(True)
            
            # if rest_text is active this frame...
            if rest_text.status == STARTED:
                # update params
                pass
            
            # *key_rest* updates
            waitOnFlip = False
            
            # if key_rest is starting this frame...
            if key_rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_rest.frameNStart = frameN  # exact frame index
                key_rest.tStart = t  # local t and not account for scr refresh
                key_rest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_rest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_rest.started')
                # update status
                key_rest.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_rest.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_rest.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_rest.status == STARTED and not waitOnFlip:
                theseKeys = key_rest.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_rest_allKeys.extend(theseKeys)
                if len(_key_rest_allKeys):
                    key_rest.keys = _key_rest_allKeys[-1].name  # just the last key pressed
                    key_rest.rt = _key_rest_allKeys[-1].rt
                    key_rest.duration = _key_rest_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=rest_routine,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                rest_routine.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if rest_routine.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in rest_routine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "rest_routine" ---
        for thisComponent in rest_routine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for rest_routine
        rest_routine.tStop = globalClock.getTime(format='float')
        rest_routine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('rest_routine.stopped', rest_routine.tStop)
        # check responses
        if key_rest.keys in ['', [], None]:  # No response was made
            key_rest.keys = None
        formal_loop.addData('key_rest.keys',key_rest.keys)
        if key_rest.keys != None:  # we had a response
            formal_loop.addData('key_rest.rt', key_rest.rt)
            formal_loop.addData('key_rest.duration', key_rest.duration)
        # the Routine "rest_routine" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisFormal_loop as finished
        if hasattr(thisFormal_loop, 'status'):
            thisFormal_loop.status = FINISHED
        # if awaiting a pause, pause now
        if formal_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            formal_loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'formal_loop'
    formal_loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "thanks" ---
    # create an object to store info about Routine thanks
    thanks = data.Routine(
        name='thanks',
        components=[thanks_text],
    )
    thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from thanks_code
    # 確保沒有除以零 (如果實驗中途結束)
    if total_trials > 0:
        acc_percent = round((total_correct / total_trials) * 100)
        final_msg = f"實驗結束！\n您的正確率為: {acc_percent}%\n\n感謝參與。"
    else:
        final_msg = "實驗結束，謝謝參與。"
    # store start times for thanks
    thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thanks.tStart = globalClock.getTime(format='float')
    thanks.status = STARTED
    thisExp.addData('thanks.started', thanks.tStart)
    thanks.maxDuration = None
    # keep track of which components have finished
    thanksComponents = thanks.components
    for thisComponent in thanks.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thanks" ---
    thisExp.currentRoutine = thanks
    thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thanks_text* updates
        
        # if thanks_text is starting this frame...
        if thanks_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thanks_text.frameNStart = frameN  # exact frame index
            thanks_text.tStart = t  # local t and not account for scr refresh
            thanks_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks_text.started')
            # update status
            thanks_text.status = STARTED
            thanks_text.setAutoDraw(True)
        
        # if thanks_text is active this frame...
        if thanks_text.status == STARTED:
            # update params
            thanks_text.setText(final_msg, log=False)
        
        # if thanks_text is stopping this frame...
        if thanks_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thanks_text.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                thanks_text.tStop = t  # not accounting for scr refresh
                thanks_text.tStopRefresh = tThisFlipGlobal  # on global time
                thanks_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'thanks_text.stopped')
                # update status
                thanks_text.status = FINISHED
                thanks_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thanks,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            thanks.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if thanks.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thanks
    thanks.tStop = globalClock.getTime(format='float')
    thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thanks.stopped', thanks.tStop)
    # Run 'End Routine' code from thanks_code
    if key_resp.corr:
        total_correct += 1
    total_trials += 1
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if thanks.maxDurationReached:
        routineTimer.addTime(-thanks.maxDuration)
    elif thanks.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
