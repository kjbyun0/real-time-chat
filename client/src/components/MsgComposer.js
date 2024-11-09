import { useState, } from 'react';
import { useOutletContext } from 'react-router-dom';


function MsgComposer() {
    const { msgs, onSetMsgs } = useOutletContext();
    const [newMsg, setNewMsg] = useState('');


    function handleMsgInputChange(e) {
        // console.log('In MsgComposser, handleMsgInputChange value: ', e.target.value);
        setNewMsg(e.target.value);
    }

    function handleNewMsgSubmit(e) {
        e.preventDefault();
        
        fetch("http://localhost:5555/messages", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                body: newMsg,
                // it is hard coded temporarily
                user_id: 1,
            }),
        })
        .then(r => r.json())
        .then(data => {
            // console.log(data);
            onSetMsgs([
                ...msgs,
                data,
            ]);
            
        })
        .catch(error => console.log(error));

        setNewMsg('');
    }

    return (
        <div>
            <form onSubmit={handleNewMsgSubmit}>
                <input type='text' name='msg' value={newMsg} 
                    onChange={handleMsgInputChange} />
                <input type='submit' value='Send' />
            </form>
        </div>
    );
}

export default MsgComposer;