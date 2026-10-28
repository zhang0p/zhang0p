 * Nokia N86音量调节
 */
#include "N86MediaVolume.h"
#include <w32std.h>
#include <e32keys.h>

// ConstructL 中创建视图
CN86MediaVolumeAppUi::CN86MediaVolumeAppUi()
: iView(NULL)
    {
    }

// 建立界面视图
void CN86MediaVolumeAppUi::ConstructL()
    {
    BaseConstructL();
    iView = CN86MediaVolumeView::NewL(ClientRect(), *this);
    AddToStackL(iView);
    }

// 退出时把视图从栈中移除
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

    TInt keyCode = 0;
    if (aCommand == EN86VolumeUp)
        keyCode = EKeyIncVolume;       // 塞班定义的音量增加按键码
    else if (aCommand == EN86VolumeDown)
        keyCode = EKeyDecVolume;       // 塞班定义的音量降低按键码
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
