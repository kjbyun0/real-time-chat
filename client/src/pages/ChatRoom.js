import PrevMsgs from '../components/PrevMsgs';
import MsgComposer from '../components/MsgComposer';

function ChatRoom() {
    return (
        <div>
            <h1>Chat Room</h1>
            <PrevMsgs />
            <MsgComposer />
        </div>
    );
}

export default ChatRoom;