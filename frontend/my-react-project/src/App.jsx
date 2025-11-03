import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { Routes, Route } from 'react-router-dom'; // 1. Import
import Navbar from './components/Navbar/Navbar';
import HomePage from './pages/HomePage'; // 2. Import your new page
import './App.css'
// A simple component for your root/index page
function RootPage() {
    return <h1>......This is the ROOT page (at /)</h1>;
}

// 5. This is your *entire* App component
function App() {
    return (
        <div className="App">
            <Navbar /> {/* <-- Self-closing, it has no children */}
            <Routes>
                <Route path="/" element={<RootPage />} />
                <Route path="/home" element={<HomePage />} />
            </Routes>
            
        </div>
    );
}



export default App
