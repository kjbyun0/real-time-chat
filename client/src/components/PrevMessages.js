import { useOutletContext } from 'react-router-dom';
import Message from './Message';

function PrevMessages() {
    const messages = useOutletContext();

    const dispMessages = messages.map(message => 
        <Message message={message} />
    );

    return (
        <div>
            {dispMessages}
        </div>
    );
}

export default PrevMessages;