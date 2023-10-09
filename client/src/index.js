import React from 'react';
import './index.css';
import App from './App';
import Generate from './generate';

import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/generate" element={<Generate />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
