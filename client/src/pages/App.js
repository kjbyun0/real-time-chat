import {Outlet} from 'react-router-dom';
import DirectMsg from './DirectMsg';

function App() {
  return (
    <div>
      <header>
        <h1>Header</h1>
      </header>
      <main>
        <Outlet />
      </main>
    </div>
  );
}

export default App;
