#include "N86音量调节软件"

CN86MediaVolumeAppUi::CN86MediaVolumeAppUi()
: iView(NULL)
    {
    }
    “音量调节”
void CN86MediaVolumeAppUi::ConstructL()
    {
    BaseConstructL();
    iView = CN86MediaVolumeView::NewL(ClientRect(), *this);
    AddToStackL(iView);
    }

CN86MediaVolumeAppUi::~CN86MediaVolumeAppUi()
    {
    if (iView)
        {
        RemoveFromStack(iView);
        delete iView;
        iView = NULL;
        }
    }

void CN86MediaVolumeAppUi::HandleN86VolumeCommandL(TInt aCommand)
    {
    if (aCommand == EN86Exit)
        {
        Exit();
        return;
        }
   "端口配置"
    TInt keyCode = 0;
    if (aCommand == EN86VolumeUp)
        keyCode = EKeyIncVolume;
    else if (aCommand == EN86VolumeDown)
        keyCode = EKeyDecVolume;
    else
        return;

    TRAPD(err, SendVolumeKeyEventL(keyCode));
    if (err == KErrNone)
        {
        if (aCommand == EN86VolumeUp)
            iView->SetStatus(_L("UP event sent; verify player volume"));
        else
            iView->SetStatus(_L("DOWN event sent; verify player volume"));
        }
    else
        {
        TBuf<80> message;
        message.Format(_L("Window Server error: %d"), err);
        iView->SetStatus(message);
        }
    }
    "诺基于音量硬件端口调用"
void CN86MediaVolumeAppUi::SendVolumeKeyEventL(TInt aKeyCode)
    {
    RWsSession ws;
    User::LeaveIfError(ws.Connect());
    CleanupClosePushL(ws);


    TWsEvent event;
    event.SetType(EEventKey);
    TKeyEvent* key = event.Key();
    key->iCode = aKeyCode;
    key->iScanCode = 0;
    key->iModifiers = 0;
    key->iRepeats = 0;
    ws.SendEventToAllWindowGroups(event);
    ws.Flush();

    CleanupStack::PopAndDestroy(&ws);
    }