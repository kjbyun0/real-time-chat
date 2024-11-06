import App from './pages/App';
import DirectMsg from './pages/DirectMsg';

const routes = [
    {
        path: '/',
        element: <App />,
        // errorElement: ,
        children: [
            {
                path: '/',
                element: <DirectMsg />,

            },
        ],
    },
];

export default routes;