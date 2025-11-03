import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'; // 1. Import
import './index.css'
import App from './App.jsx'
const rootElement = document.getElementById('root');

// 2. Create the root using the function you imported
const root = createRoot(rootElement);
root.render(
    <StrictMode>
        <BrowserRouter>
            <App />
        </BrowserRouter>
    </StrictMode>
);
