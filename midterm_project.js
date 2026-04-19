/************************ 
 * Midterm_Project *
 ************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2026.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'midterm_project';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(startRoutineBegin());
flowScheduler.add(startRoutineEachFrame());
flowScheduler.add(startRoutineEnd());
flowScheduler.add(instr_practiceRoutineBegin());
flowScheduler.add(instr_practiceRoutineEachFrame());
flowScheduler.add(instr_practiceRoutineEnd());
const practice_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_loopLoopBegin(practice_loopLoopScheduler));
flowScheduler.add(practice_loopLoopScheduler);
flowScheduler.add(practice_loopLoopEnd);





flowScheduler.add(instr_formalRoutineBegin());
flowScheduler.add(instr_formalRoutineEachFrame());
flowScheduler.add(instr_formalRoutineEnd());
const formal_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(formal_loopLoopBegin(formal_loopLoopScheduler));
flowScheduler.add(formal_loopLoopScheduler);
flowScheduler.add(formal_loopLoopEnd);




flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'practice_cond.xlsx', 'path': 'practice_cond.xlsx'},
    {'name': 'formal_cond.xlsx', 'path': 'formal_cond.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "start"
  startClock = new util.Clock();
  open_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'open_text',
    text: '歡迎參加本次視覺認知與注意力實驗\n\n【實驗任務說明】\n在接下來的畫面中，\n會出現許多不同顏色與形狀的圖案。\n您的目標是尋找：「紅色正方形」。\n\n【按鍵操作指引】\n● 看到紅色正方形：請按 方向鍵右鍵 (→)\n● 沒有紅色正方形：請按 方向鍵左鍵 (←)\n\n\n按下空白鍵進入下一頁',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  start_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr_practice"
  instr_practiceClock = new util.Clock();
  prac_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_text',
    text: '【練習階段】\n\n為了讓您熟悉操作，我們準備了幾題練習題。\n\n此階段會顯示「正確」或是「錯誤」。\n\n請在確保正確的前提下，盡可能快地做出反應。\n\n\n\n準備好後，請按下「空白鍵」開始練習。',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  prac_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from prac_code
  total_correct = 0;
  total_trials = 0;
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  fix_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_text',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  fb_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'fb_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  ITI_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ITI_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instr_formal"
  instr_formalClock = new util.Clock();
  formal_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'formal_text',
    text: '練習結束，即將進入正式實驗\n\n規則維持不變：\n目標是尋找 「紅色正方形」\n● 有目標：按 右鍵 (→)\n● 無目標：按 左鍵 (←)\n\n注意：\n1. 正式實驗將不再提供對錯回饋。\n2. 螢幕會自動跳轉，請保持注意力集中。\n3. 請盡可能兼顧速度與正確率。\n\n準備好後，請按「空白鍵」開始正式實驗。',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  formal_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  thanks_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    startClock.reset();
    routineTimer.reset();
    startMaxDurationReached = false;
    // update component parameters for each repeat
    start_key.keys = undefined;
    start_key.rt = undefined;
    _start_key_allKeys = [];
    psychoJS.experiment.addData('start.started', globalClock.getTime());
    startMaxDuration = null
    // keep track of which components have finished
    startComponents = [];
    startComponents.push(open_text);
    startComponents.push(start_key);
    
    for (const thisComponent of startComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function startRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start' ---
    // get current time
    t = startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *open_text* updates
    if (t >= 0.0 && open_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      open_text.tStart = t;  // (not accounting for frame time here)
      open_text.frameNStart = frameN;  // exact frame index
      
      open_text.setAutoDraw(true);
    }
    
    
    // if open_text is active this frame...
    if (open_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *start_key* updates
    if (t >= 0.0 && start_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_key.tStart = t;  // (not accounting for frame time here)
      start_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start_key.clearEvents(); });
    }
    
    // if start_key is active this frame...
    if (start_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_key.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _start_key_allKeys = _start_key_allKeys.concat(theseKeys);
      if (_start_key_allKeys.length > 0) {
        start_key.keys = _start_key_allKeys[_start_key_allKeys.length - 1].name;  // just the last key pressed
        start_key.rt = _start_key_allKeys[_start_key_allKeys.length - 1].rt;
        start_key.duration = _start_key_allKeys[_start_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function startRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start' ---
    for (const thisComponent of startComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('start.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(start_key.corr, level);
    }
    psychoJS.experiment.addData('start_key.keys', start_key.keys);
    if (typeof start_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start_key.rt', start_key.rt);
        psychoJS.experiment.addData('start_key.duration', start_key.duration);
        routineTimer.reset();
        }
    
    start_key.stop();
    // the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instr_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr_practice' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instr_practiceClock.reset();
    routineTimer.reset();
    instr_practiceMaxDurationReached = false;
    // update component parameters for each repeat
    prac_key.keys = undefined;
    prac_key.rt = undefined;
    _prac_key_allKeys = [];
    psychoJS.experiment.addData('instr_practice.started', globalClock.getTime());
    instr_practiceMaxDuration = null
    // keep track of which components have finished
    instr_practiceComponents = [];
    instr_practiceComponents.push(prac_text);
    instr_practiceComponents.push(prac_key);
    
    for (const thisComponent of instr_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instr_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr_practice' ---
    // get current time
    t = instr_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_text* updates
    if (t >= 0.0 && prac_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_text.tStart = t;  // (not accounting for frame time here)
      prac_text.frameNStart = frameN;  // exact frame index
      
      prac_text.setAutoDraw(true);
    }
    
    
    // if prac_text is active this frame...
    if (prac_text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *prac_key* updates
    if (t >= 0.0 && prac_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_key.tStart = t;  // (not accounting for frame time here)
      prac_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_key.clearEvents(); });
    }
    
    // if prac_key is active this frame...
    if (prac_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_key.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _prac_key_allKeys = _prac_key_allKeys.concat(theseKeys);
      if (_prac_key_allKeys.length > 0) {
        prac_key.keys = _prac_key_allKeys[_prac_key_allKeys.length - 1].name;  // just the last key pressed
        prac_key.rt = _prac_key_allKeys[_prac_key_allKeys.length - 1].rt;
        prac_key.duration = _prac_key_allKeys[_prac_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instr_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instr_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr_practice' ---
    for (const thisComponent of instr_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr_practice.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(prac_key.corr, level);
    }
    psychoJS.experiment.addData('prac_key.keys', prac_key.keys);
    if (typeof prac_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_key.rt', prac_key.rt);
        psychoJS.experiment.addData('prac_key.duration', prac_key.duration);
        routineTimer.reset();
        }
    
    prac_key.stop();
    // the Routine "instr_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practice_loopLoopBegin(practice_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'practice_cond.xlsx',
      seed: undefined, name: 'practice_loop'
    });
    psychoJS.experiment.addLoop(practice_loop); // add the loop to the experiment
    currentLoop = practice_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice_loop of practice_loop) {
      snapshot = practice_loop.getSnapshot();
      practice_loopLoopScheduler.add(importConditions(snapshot));
      practice_loopLoopScheduler.add(fixationRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(fixationRoutineEachFrame());
      practice_loopLoopScheduler.add(fixationRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(trialRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(trialRoutineEachFrame());
      practice_loopLoopScheduler.add(trialRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(feedbackRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(feedbackRoutineEachFrame());
      practice_loopLoopScheduler.add(feedbackRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(ITIRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(ITIRoutineEachFrame());
      practice_loopLoopScheduler.add(ITIRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(practice_loopLoopEndIteration(practice_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function practice_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function practice_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function formal_loopLoopBegin(formal_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    formal_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'formal_cond.xlsx',
      seed: undefined, name: 'formal_loop'
    });
    psychoJS.experiment.addLoop(formal_loop); // add the loop to the experiment
    currentLoop = formal_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisFormal_loop of formal_loop) {
      snapshot = formal_loop.getSnapshot();
      formal_loopLoopScheduler.add(importConditions(snapshot));
      formal_loopLoopScheduler.add(fixationRoutineBegin(snapshot));
      formal_loopLoopScheduler.add(fixationRoutineEachFrame());
      formal_loopLoopScheduler.add(fixationRoutineEnd(snapshot));
      formal_loopLoopScheduler.add(trialRoutineBegin(snapshot));
      formal_loopLoopScheduler.add(trialRoutineEachFrame());
      formal_loopLoopScheduler.add(trialRoutineEnd(snapshot));
      formal_loopLoopScheduler.add(ITIRoutineBegin(snapshot));
      formal_loopLoopScheduler.add(ITIRoutineEachFrame());
      formal_loopLoopScheduler.add(ITIRoutineEnd(snapshot));
      formal_loopLoopScheduler.add(formal_loopLoopEndIteration(formal_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function formal_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(formal_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function formal_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fixationClock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    fixationMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation.started', globalClock.getTime());
    fixationMaxDuration = null
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(fix_text);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_text* updates
    if (t >= 0.0 && fix_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_text.tStart = t;  // (not accounting for frame time here)
      fix_text.frameNStart = frameN;  // exact frame index
      
      fix_text.setAutoDraw(true);
    }
    
    
    // if fix_text is active this frame...
    if (fix_text.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fix_text.tStop = t;  // not accounting for scr refresh
      fix_text.frameNStop = frameN;  // exact frame index
      // update status
      fix_text.status = PsychoJS.Status.FINISHED;
      fix_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixation.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (fixationMaxDurationReached) {
        fixationClock.add(fixationMaxDuration);
    } else {
        fixationClock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from trial_code
    import * as random from 'random';
    locations = [];
    for (var x, _pj_c = 0, _pj_a = util.range((- 4), 5), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        x = _pj_a[_pj_c];
        for (var y, _pj_f = 0, _pj_d = util.range((- 3), 4), _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
            y = _pj_d[_pj_f];
            locations.push([(x * 80), (y * 80)]);
        }
    }
    Math.random.shuffle(locations);
    pos_list = locations.slice(0, Number.parseInt(set_size));
    stims = [];
    for (var i, _pj_c = 0, _pj_a = util.range(Number.parseInt(set_size)), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if (((i === 0) && (target_present === 1))) {
            curr_color = "red";
            curr_shape = "rectangle";
        } else {
            if ((condition_type === "feature")) {
                curr_color = "blue";
                curr_shape = "rectangle";
            } else {
                if (((i % 2) === 0)) {
                    curr_color = "red";
                    curr_shape = "circle";
                } else {
                    curr_color = "blue";
                    curr_shape = "rectangle";
                }
            }
        }
        if ((curr_shape === "rectangle")) {
            el = new visual.Rect({"win": psychoJS.window, "width": 40, "height": 40, "fillColor": curr_color, "lineColor": curr_color, "pos": pos_list[i], "units": "pix"});
        } else {
            el = new visual.Polygon({"win": psychoJS.window, "edges": 32, "radius": 20, "fillColor": curr_color, "lineColor": curr_color, "pos": pos_list[i], "units": "pix"});
        }
        stims.push(el);
    }
    
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(key_resp);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from trial_code
    for (var stim, _pj_c = 0, _pj_a = stims, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        stim = _pj_a[_pj_c];
        stim.draw();
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      key_resp.tStop = t;  // not accounting for scr refresh
      key_resp.frameNStop = frameN;  // exact frame index
      // update status
      key_resp.status = PsychoJS.Status.FINISHED;
      frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        key_resp.tStop = t;  // not accounting for scr refresh
        key_resp.frameNStop = frameN;  // exact frame index
        // update status
        key_resp.status = PsychoJS.Status.FINISHED;
        key_resp.status = PsychoJS.Status.FINISHED;
          }
        
      }
      
      // if key_resp is active this frame...
      if (key_resp.status === PsychoJS.Status.STARTED) {
        let theseKeys = key_resp.getKeys({
          keyList: typeof ['left','right'] === 'string' ? [['left','right']] : ['left','right'], 
          waitRelease: false
        });
        _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
        if (_key_resp_allKeys.length > 0) {
          key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
          key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
          key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
          // was this correct?
          if (key_resp.keys == corr_resp) {
              key_resp.corr = 1;
          } else {
              key_resp.corr = 0;
          }
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of trialComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function trialRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'trial' ---
      for (const thisComponent of trialComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
      // Run 'End Routine' code from trial_code
      if (key_resp.corr) {
          total_correct += 1;
      }
      total_trials += 1;
      
      // was no response the correct answer?!
      if (key_resp.keys === undefined) {
        if (['None','none',undefined].includes(corr_resp)) {
           key_resp.corr = 1;  // correct non-response
        } else {
           key_resp.corr = 0;  // failed to respond (incorrectly)
        }
      }
      // store data for current loop
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(key_resp.corr, level);
      }
      psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
      psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
      if (typeof key_resp.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
          psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
          routineTimer.reset();
          }
      
      key_resp.stop();
      if (routineForceEnded) {
          routineTimer.reset();} else if (trialMaxDurationReached) {
          trialClock.add(trialMaxDuration);
      } else {
          trialClock.add(2.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function feedbackRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'feedback' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      feedbackClock.reset(routineTimer.getTime());
      routineTimer.add(1.500000);
      feedbackMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from fb_code
      if (key_resp.corr) {
          msg = "\u6b63\u78ba!";
          msg_color = "green";
      } else {
          msg = "\u932f\u8aa4!";
          msg_color = "red";
      }
      if (key_resp.rt) {
          rt_ms = util.round((key_resp.rt * 1000));
          msg += `
      ${rt_ms} ms`
      ;
      } else {
          msg += "\n\u592a\u6162\u4e86!";
      }
      
      psychoJS.experiment.addData('feedback.started', globalClock.getTime());
      feedbackMaxDuration = null
      // keep track of which components have finished
      feedbackComponents = [];
      feedbackComponents.push(fb_text);
      
      for (const thisComponent of feedbackComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function feedbackRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'feedback' ---
      // get current time
      t = feedbackClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *fb_text* updates
      if (t >= 0.0 && fb_text.status === PsychoJS.Status.NOT_STARTED) {
        // update params
        fb_text.setColor(new util.Color(msg_color), false);
        fb_text.setText(msg, false);
        // keep track of start time/frame for later
        fb_text.tStart = t;  // (not accounting for frame time here)
        fb_text.frameNStart = frameN;  // exact frame index
        
        fb_text.setAutoDraw(true);
      }
      
      
      // if fb_text is active this frame...
      if (fb_text.status === PsychoJS.Status.STARTED) {
        // update params
        fb_text.setColor(new util.Color(msg_color), false);
        fb_text.setText(msg, false);
      }
      
      frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (fb_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        fb_text.tStop = t;  // not accounting for scr refresh
        fb_text.frameNStop = frameN;  // exact frame index
        // update status
        fb_text.status = PsychoJS.Status.FINISHED;
        fb_text.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of feedbackComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function feedbackRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'feedback' ---
      for (const thisComponent of feedbackComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (feedbackMaxDurationReached) {
          feedbackClock.add(feedbackMaxDuration);
      } else {
          feedbackClock.add(1.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function ITIRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'ITI' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      ITIClock.reset(routineTimer.getTime());
      routineTimer.add(0.500000);
      ITIMaxDurationReached = false;
      // update component parameters for each repeat
      psychoJS.experiment.addData('ITI.started', globalClock.getTime());
      ITIMaxDuration = null
      // keep track of which components have finished
      ITIComponents = [];
      ITIComponents.push(ITI_text);
      
      for (const thisComponent of ITIComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function ITIRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'ITI' ---
      // get current time
      t = ITIClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *ITI_text* updates
      if (t >= 0.0 && ITI_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        ITI_text.tStart = t;  // (not accounting for frame time here)
        ITI_text.frameNStart = frameN;  // exact frame index
        
        ITI_text.setAutoDraw(true);
      }
      
      
      // if ITI_text is active this frame...
      if (ITI_text.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (ITI_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        ITI_text.tStop = t;  // not accounting for scr refresh
        ITI_text.frameNStop = frameN;  // exact frame index
        // update status
        ITI_text.status = PsychoJS.Status.FINISHED;
        ITI_text.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of ITIComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function ITIRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'ITI' ---
      for (const thisComponent of ITIComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('ITI.stopped', globalClock.getTime());
      if (routineForceEnded) {
          routineTimer.reset();} else if (ITIMaxDurationReached) {
          ITIClock.add(ITIMaxDuration);
      } else {
          ITIClock.add(0.500000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function instr_formalRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'instr_formal' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      instr_formalClock.reset();
      routineTimer.reset();
      instr_formalMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from code
      total_correct = 0;
      total_trials = 0;
      
      formal_key.keys = undefined;
      formal_key.rt = undefined;
      _formal_key_allKeys = [];
      psychoJS.experiment.addData('instr_formal.started', globalClock.getTime());
      instr_formalMaxDuration = null
      // keep track of which components have finished
      instr_formalComponents = [];
      instr_formalComponents.push(formal_text);
      instr_formalComponents.push(formal_key);
      
      for (const thisComponent of instr_formalComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function instr_formalRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'instr_formal' ---
      // get current time
      t = instr_formalClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *formal_text* updates
      if (t >= 0.0 && formal_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        formal_text.tStart = t;  // (not accounting for frame time here)
        formal_text.frameNStart = frameN;  // exact frame index
        
        formal_text.setAutoDraw(true);
      }
      
      
      // if formal_text is active this frame...
      if (formal_text.status === PsychoJS.Status.STARTED) {
      }
      
      
      // *formal_key* updates
      if (t >= 0.0 && formal_key.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        formal_key.tStart = t;  // (not accounting for frame time here)
        formal_key.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { formal_key.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { formal_key.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { formal_key.clearEvents(); });
      }
      
      // if formal_key is active this frame...
      if (formal_key.status === PsychoJS.Status.STARTED) {
        let theseKeys = formal_key.getKeys({
          keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
          waitRelease: false
        });
        _formal_key_allKeys = _formal_key_allKeys.concat(theseKeys);
        if (_formal_key_allKeys.length > 0) {
          formal_key.keys = _formal_key_allKeys[_formal_key_allKeys.length - 1].name;  // just the last key pressed
          formal_key.rt = _formal_key_allKeys[_formal_key_allKeys.length - 1].rt;
          formal_key.duration = _formal_key_allKeys[_formal_key_allKeys.length - 1].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of instr_formalComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function instr_formalRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'instr_formal' ---
      for (const thisComponent of instr_formalComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('instr_formal.stopped', globalClock.getTime());
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(formal_key.corr, level);
      }
      psychoJS.experiment.addData('formal_key.keys', formal_key.keys);
      if (typeof formal_key.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('formal_key.rt', formal_key.rt);
          psychoJS.experiment.addData('formal_key.duration', formal_key.duration);
          routineTimer.reset();
          }
      
      formal_key.stop();
      // the Routine "instr_formal" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function thanksRoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'thanks' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      thanksClock.reset(routineTimer.getTime());
      routineTimer.add(3.000000);
      thanksMaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from thanks_code
      if ((total_trials > 0)) {
          acc_percent = util.round(((total_correct / total_trials) * 100));
          final_msg = `實驗結束！
      您的正確率為: ${acc_percent}%
      
      感謝參與。`
      ;
      } else {
          final_msg = "\u5be6\u9a57\u7d50\u675f\uff0c\u8b1d\u8b1d\u53c3\u8207\u3002";
      }
      
      psychoJS.experiment.addData('thanks.started', globalClock.getTime());
      thanksMaxDuration = null
      // keep track of which components have finished
      thanksComponents = [];
      thanksComponents.push(thanks_text);
      
      for (const thisComponent of thanksComponents)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function thanksRoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'thanks' ---
      // get current time
      t = thanksClock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *thanks_text* updates
      if (t >= 0.0 && thanks_text.status === PsychoJS.Status.NOT_STARTED) {
        // update params
        thanks_text.setText(final_msg, false);
        // keep track of start time/frame for later
        thanks_text.tStart = t;  // (not accounting for frame time here)
        thanks_text.frameNStart = frameN;  // exact frame index
        
        thanks_text.setAutoDraw(true);
      }
      
      
      // if thanks_text is active this frame...
      if (thanks_text.status === PsychoJS.Status.STARTED) {
        // update params
        thanks_text.setText(final_msg, false);
      }
      
      frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (thanks_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        thanks_text.tStop = t;  // not accounting for scr refresh
        thanks_text.frameNStop = frameN;  // exact frame index
        // update status
        thanks_text.status = PsychoJS.Status.FINISHED;
        thanks_text.setAutoDraw(false);
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of thanksComponents)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine && routineTimer.getTime() > 0) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function thanksRoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'thanks' ---
      for (const thisComponent of thanksComponents) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('thanks.stopped', globalClock.getTime());
      // Run 'End Routine' code from thanks_code
      if (key_resp.corr) {
          total_correct += 1;
      }
      total_trials += 1;
      
      if (routineForceEnded) {
          routineTimer.reset();} else if (thanksMaxDurationReached) {
          thanksClock.add(thanksMaxDuration);
      } else {
          thanksClock.add(3.000000);
      }
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function importConditions(currentLoop) {
    return async function () {
      psychoJS.importAttributes(currentLoop.getCurrentTrial());
      return Scheduler.Event.NEXT;
      };
  }
  
  async function quitPsychoJS(message, isCompleted) {
    // Check for and save orphaned data
    if (psychoJS.experiment.isEntryEmpty()) {
      psychoJS.experiment.nextEntry();
    }
    psychoJS.window.close();
    psychoJS.quit({message: message, isCompleted: isCompleted});
    
    return Scheduler.Event.QUIT;
  }
