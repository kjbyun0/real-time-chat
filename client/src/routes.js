import App from './pages/App';
import ChatRoom from './pages/ChatRoom';

const routes = [
    {
        path: '/',
        element: <App />,
        // errorElement: ,
        children: [
            {
                path: '/',
                element: <ChatRoom />,

            },
        ],
    },
];

export default routes;