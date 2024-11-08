import { useState, useEffect } from 'react';
import { Outlet } from 'react-router-dom';
import ChatRoom from './ChatRoom';

function App() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5555/messages')
    .then(resp => resp.json())
    .then(data => {
      console.log(data);
      setMessages(data);
    });
  }, []);

  return (
    <div>
      <header>
        <h1>Header</h1>
      </header>
      <main>
        <Outlet context={messages} />
      </main>
    </div>
  );
}

export default App;
