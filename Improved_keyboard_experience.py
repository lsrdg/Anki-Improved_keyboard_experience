# jkl; will show answer or answer cards
# creds to faster-keys, handy keys, left hand reps because i either use them or scavenged code from them.
# (i don't actually know what i'm doing)

from aqt import mw
from aqt.reviewer import Reviewer

def leftHandKeys(self, evt):
    key = unicode(evt.text())
    
    if key == "u":
        try:# throws an error on undo -> do -> undo pattern,  otherwise works fine
            mw.onUndo()
        except:
            pass

    if key == "i":
        try:
            mw.onEditCurrent()
        except:
            pass

    if key == "h":
        if self.state == "question":
            self._showAnswerHack()
        elif self.state == "answer":
            self._answerCard(1)
    elif key == "j":
        if self.state == "question":
            self._showAnswerHack()
        elif self.state == "answer":
            self._answerCard(2)
    elif key == "k":
        if self.state == "question":
            self._showAnswerHack()
        elif self.state == "answer":
            self._answerCard(3)
    elif key == "l":
        if self.state == "question":
            self._showAnswerHack()
        elif self.state == "answer":
            self._answerCard(4)
    else:
        origKeyHandler(self, evt)    


origKeyHandler= Reviewer._keyHandler
Reviewer._keyHandler = leftHandKeys
