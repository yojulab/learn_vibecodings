import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import PostListPage from './pages/PostListPage';
import PostDetailPage from './pages/PostDetailPage';
import PostFormPage from './pages/PostFormPage';
import './App.css';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50">
        <div className="container mx-auto p-4">
          <nav className="bg-gray-800 text-white p-4 rounded-md mb-6 shadow-md">
            <ul className="flex space-x-4">
              <li>
                <Link to="/" className="hover:text-gray-300 font-semibold">Home</Link>
              </li>
              <li>
                <Link to="/new-post" className="hover:text-gray-300 font-semibold">New Post</Link>
              </li>
            </ul>
          </nav>
          <Routes>
            <Route path="/" element={<PostListPage />} />
            <Route path="/posts/:id" element={<PostDetailPage />} />
            <Route path="/new-post" element={<PostFormPage />} />
            <Route path="/edit-post/:id" element={<PostFormPage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
