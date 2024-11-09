import { useState, useEffect } from 'react';
import { Outlet } from 'react-router-dom';
import ChatRoom from './ChatRoom';

function App() {
  const [msgs, setMsgs] = useState([]);
  console.log('In App, msgs: ', msgs);

  useEffect(() => {
    fetch('http://localhost:5555/messages')
    .then(resp => resp.json())
    .then(data => {
      setMsgs(data);
    });
  }, []);

  return (
    <div>
      <header>
        <h1>Header</h1>
      </header>
      <main>
        <Outlet context={{
          msgs: msgs,
          onSetMsgs: setMsgs,
        }} />
      </main>
    </div>
  );
}

export default App;
