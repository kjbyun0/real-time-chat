import { useOutletContext } from 'react-router-dom';
import Msg from './Msg';

function PrevMsgs() {
    const {msgs} = useOutletContext();

    const dispMsgs = msgs.map(msg => 
        <Msg key={msg.id} msg={msg} />
    );

    return (
        <div>
            {dispMsgs}
        </div>
    );
}

export default PrevMsgs;